#!/usr/bin/env python3
"""
Roku Developer Documentation Scraper

Recursively scrapes markdown documentation from developer.roku.com using crawl4ai.
Converts HTML pages to clean markdown files for offline access and AI integration.

Requirements:
    pip install crawl4ai
    crawl4ai-setup

Usage:
    python scraper.py [--output-dir DIR] [--max-depth N] [--max-pages N] [--verbose]

Author: Robson Harrison
License: MIT
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.deep_crawling.filters import FilterChain, URLPatternFilter

if TYPE_CHECKING:
    from crawl4ai.async_crawler_strategy import CrawlResult

# =============================================================================
# Configuration
# =============================================================================

@dataclass
class ScraperConfig:
    """Configuration for the documentation scraper."""

    start_url: str = "https://developer.roku.com/en-gb/docs/developer-program/getting-started/roku-dev-prog.md"
    doc_pattern: str = "*docs*.md"
    content_selector: str = ".markdown-body.developer-content-body"
    locale_prefix: str = "/en-gb/"
    wait_timeout_ms: int = 15000
    page_timeout_ms: int = 30000


@dataclass
class ScrapeStats:
    """Statistics from a scrape run."""

    new: list[dict] = field(default_factory=list)
    updated: list[dict] = field(default_factory=list)
    unchanged: int = 0
    failed: list[dict] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Convert stats to dictionary for JSON serialization."""
        return {
            "new": self.new,
            "updated": self.updated,
            "unchanged": self.unchanged,
            "failed": self.failed,
        }


# Default configuration
CONFIG = ScraperConfig()

# =============================================================================
# Logging Setup
# =============================================================================

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    """Configure logging for the scraper.

    Args:
        verbose: If True, set DEBUG level; otherwise INFO level.
    """
    level = logging.DEBUG if verbose else logging.INFO

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%H:%M:%S"
    ))

    logger.setLevel(level)
    logger.addHandler(handler)

    # Suppress noisy third-party loggers
    logging.getLogger("crawl4ai").setLevel(logging.WARNING)
    logging.getLogger("playwright").setLevel(logging.WARNING)


# =============================================================================
# URL and Content Processing
# =============================================================================

def url_to_path(url: str, output_dir: Path, locale_prefix: str = "/en-gb/") -> Path:
    """Convert a documentation URL to a local file path.

    Args:
        url: The full URL to convert.
        output_dir: Base directory for output files.
        locale_prefix: Locale prefix to strip from paths (e.g., "/en-gb/").

    Returns:
        Path object for the local file location.
    """
    path = urlparse(url).path
    if path.startswith(locale_prefix):
        path = path[len(locale_prefix):]
    return output_dir / path.lstrip("/")


def correct_malformed_url(url: str) -> str | None:
    """Correct malformed URLs with duplicate /docs/ segments.

    Some pages have broken links that result in URLs like:
    .../docs/developer-program/.../docs/references/...

    This function extracts the last valid /docs/ segment.

    Args:
        url: The potentially malformed URL.

    Returns:
        Corrected URL if malformed, None if URL is valid.
    """
    parsed = urlparse(url)
    path = parsed.path

    if path.count("/docs/") > 1:
        last_docs_idx = path.rfind("/docs/")
        corrected_path = path[last_docs_idx:]
        return f"{parsed.scheme}://{parsed.netloc}{corrected_path}"

    return None


def clean_markdown(text: str) -> str:
    """Clean up markdown content by normalizing whitespace.

    Removes consecutive blank lines and trailing whitespace.

    Args:
        text: Raw markdown text.

    Returns:
        Cleaned markdown text.
    """
    if not text:
        return ""

    lines: list[str] = []
    prev_empty = False

    for line in text.split("\n"):
        is_empty = not line.strip()
        if not (is_empty and prev_empty):
            lines.append(line.rstrip())
        prev_empty = is_empty

    return "\n".join(lines).strip()


def extract_markdown(result: CrawlResult) -> str:
    """Extract and clean markdown content from a crawl result.

    Args:
        result: The crawl result from crawl4ai.

    Returns:
        Cleaned markdown content.
    """
    md_content = (
        result.markdown.raw_markdown
        if hasattr(result.markdown, 'raw_markdown')
        else str(result.markdown)
    )
    return clean_markdown(md_content)


def is_empty_or_error_page(content: str) -> bool:
    """Check if content represents an empty or error page.

    Args:
        content: The page content to check.

    Returns:
        True if the page appears to be empty or an error page.
    """
    if not content:
        return True
    normalized = content.strip().lower()
    return normalized in ("document not found.", "document not found")


# =============================================================================
# Page Processing
# =============================================================================

def save_page(
    output_path: Path,
    content: str,
    url: str,
    parent_url: str | None,
    stats: ScrapeStats,
    depth: int = 0,
) -> None:
    """Save a page to disk, tracking whether it's new or updated.

    Args:
        output_path: Where to save the file.
        content: The markdown content to save.
        url: Source URL of the page.
        parent_url: URL of the page that linked to this one.
        stats: Statistics object to update.
        depth: Crawl depth for logging.
    """
    if output_path.exists():
        existing_content = output_path.read_text(encoding="utf-8")
        if existing_content == content:
            stats.unchanged += 1
            logger.debug("[%d] Unchanged: %s", depth, output_path)
            return

        # Content changed - update the file
        output_path.write_text(content, encoding="utf-8")
        stats.updated.append({"path": str(output_path), "url": url, "found_on": parent_url})
        logger.info("✏ [%d] Updated: %s", depth, output_path)
    else:
        # New file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
        stats.new.append({"path": str(output_path), "url": url, "found_on": parent_url})
        logger.info("✓ [%d] New: %s", depth, output_path)


# =============================================================================
# Main Scraper
# =============================================================================

async def run_scraper(
    output_dir: Path,
    max_depth: int,
    max_pages: int,
    verbose: bool,
    config: ScraperConfig | None = None,
) -> ScrapeStats:
    """Run the deep crawl scraper.

    Args:
        output_dir: Directory to save scraped documentation.
        max_depth: Maximum link depth to crawl.
        max_pages: Maximum number of pages to crawl.
        verbose: Enable verbose logging.
        config: Optional custom scraper configuration.

    Returns:
        ScrapeStats object with results.
    """
    if config is None:
        config = CONFIG

    output_dir.mkdir(parents=True, exist_ok=True)
    stats = ScrapeStats()

    logger.info("=" * 50)
    logger.info("Roku Documentation Scraper (crawl4ai)")
    logger.info("Output: %s | Max Depth: %d | Max Pages: %d", output_dir, max_depth, max_pages)
    logger.info("=" * 50)

    # Configure browser
    browser_config = BrowserConfig(headless=True, verbose=verbose)

    # Configure deep crawl with URL filtering
    filter_chain = FilterChain([
        URLPatternFilter(patterns=[config.doc_pattern]),
    ])

    crawl_config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=max_depth,
            max_pages=max_pages,
            include_external=False,
            filter_chain=filter_chain,
        ),
        wait_until="domcontentloaded",
        wait_for="css:.markdown-body",
        wait_for_timeout=config.wait_timeout_ms,
        page_timeout=config.page_timeout_ms,
        target_elements=[config.content_selector, ".markdown-body"],
        cache_mode=CacheMode.BYPASS,
        stream=True,
        verbose=verbose,
    )

    # Track corrected URLs to retry
    corrected_urls: set[str] = set()

    async with AsyncWebCrawler(config=browser_config) as crawler:
        async for result in await crawler.arun(config.start_url, config=crawl_config):
            parent_url = result.metadata.get("parent_url") if result.metadata else None
            depth = result.metadata.get("depth", 0) if result.metadata else 0

            if not result.success:
                corrected = correct_malformed_url(result.url)
                if corrected:
                    corrected_urls.add(corrected)
                    logger.warning("⚠ Malformed URL, will retry: %s", corrected)
                else:
                    stats.failed.append({
                        "url": result.url,
                        "reason": result.error_message,
                        "found_on": parent_url,
                    })
                    logger.error("✗ Failed: %s", result.url)
                continue

            output_path = url_to_path(result.url, output_dir, config.locale_prefix)
            content = extract_markdown(result)

            if is_empty_or_error_page(content):
                stats.failed.append({
                    "url": result.url,
                    "reason": "Document not found - likely broken link",
                    "found_on": parent_url,
                })
                logger.warning("✗ Document not found: %s", result.url)
                continue

            save_page(output_path, content, result.url, parent_url, stats, depth)

        # Retry corrected URLs
        if corrected_urls:
            logger.info("Retrying %d corrected URLs...", len(corrected_urls))
            retry_config = CrawlerRunConfig(
                wait_until="domcontentloaded",
                wait_for="css:.markdown-body",
                wait_for_timeout=config.wait_timeout_ms,
                page_timeout=config.page_timeout_ms,
                target_elements=[config.content_selector, ".markdown-body"],
                cache_mode=CacheMode.BYPASS,
                verbose=verbose,
            )

            for url in corrected_urls:
                output_path = url_to_path(url, output_dir, config.locale_prefix)
                result = await crawler.arun(url, config=retry_config)

                if not result.success:
                    stats.failed.append({
                        "url": url,
                        "reason": result.error_message,
                        "found_on": "retry",
                    })
                    logger.error("✗ Retry failed: %s", url)
                    continue

                content = extract_markdown(result)

                if is_empty_or_error_page(content):
                    stats.failed.append({
                        "url": url,
                        "reason": "Document not found - likely broken link",
                        "found_on": "retry",
                    })
                    logger.warning("✗ [retry] Document not found: %s", url)
                    continue

                save_page(output_path, content, url, "retry", stats, depth=0)

    return stats


def format_duration(seconds: float) -> str:
    """Format a duration in seconds to a human-readable string.

    Args:
        seconds: Duration in seconds.

    Returns:
        Formatted string like "1h 23m 45s" or "5m 30s" or "45s".
    """
    minutes, secs = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)

    if hours:
        return f"{hours}h {minutes}m {secs}s"
    elif minutes:
        return f"{minutes}m {secs}s"
    return f"{secs}s"


def main() -> int:
    """Main entry point for the Roku documentation scraper.

    Returns:
        Exit code: 0 for success, 1 for errors.
    """
    parser = argparse.ArgumentParser(
        description="Scrape Roku Developer Documentation to markdown files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--output-dir",
        default="./docs",
        help="Directory to save scraped documentation",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=10,
        help="Maximum link depth to crawl",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=2000,
        help="Maximum number of pages to crawl",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose/debug logging",
    )
    args = parser.parse_args()

    # Set up logging
    setup_logging(verbose=args.verbose)

    try:
        start_time = time.time()
        stats = asyncio.run(
            run_scraper(
                Path(args.output_dir),
                args.max_depth,
                args.max_pages,
                args.verbose,
            )
        )
        duration = time.time() - start_time

        # Log summary
        logger.info("=" * 50)
        logger.info("COMPLETE")
        logger.info(
            "New: %d | Updated: %d | Unchanged: %d | Failed: %d",
            len(stats.new),
            len(stats.updated),
            stats.unchanged,
            len(stats.failed),
        )
        logger.info("Duration: %s", format_duration(duration))
        logger.info("=" * 50)

        # Save results
        results_path = Path(args.output_dir) / "results.json"
        results_path.write_text(json.dumps(stats.to_dict(), indent=2))
        logger.info("Results saved to: %s", results_path)

        return 0 if not stats.failed else 1

    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        return 1
    except Exception as e:
        logger.exception("Fatal error: %s", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())