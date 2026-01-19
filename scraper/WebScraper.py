#!/usr/bin/env python3
"""
Roku Developer Documentation Scraper

Recursively scrapes markdown documentation from developer.roku.com using crawl4ai.

Requirements:
    pip install crawl4ai
    crawl4ai-setup

Usage:
    python WebScraper.py [--output-dir DIR] [--max-depth N] [--max-pages N] [--verbose]

Author: Robson Harrison
"""

import argparse
import asyncio
import json
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.deep_crawling.filters import FilterChain, URLPatternFilter

# Configuration
START_URL = "https://developer.roku.com/en-gb/docs/developer-program/getting-started/roku-dev-prog.md"
DOC_PATTERN = "*docs*.md"
CONTENT_SELECTOR = ".markdown-body.developer-content-body"


def url_to_path(url: str, output_dir: Path) -> Path:
    """Convert URL to local file path."""
    path = urlparse(url).path
    if path.startswith("/en-gb/"):
        path = path[7:]
    return output_dir / path.lstrip("/")


def correct_malformed_url(url: str) -> str | None:
    """Correct malformed URLs with duplicate /docs/ segments.

    Example: .../docs/developer-program/.../docs/references/...
    becomes: .../docs/references/...
    """
    parsed = urlparse(url)
    path = parsed.path

    # Check for duplicate /docs/ segments
    if path.count("/docs/") > 1:
        # Find the last /docs/ and keep from there
        last_docs_idx = path.rfind("/docs/")
        corrected_path = path[last_docs_idx:]
        return f"{parsed.scheme}://{parsed.netloc}{corrected_path}"

    return None  # URL is fine, no correction needed


def clean_markdown(text: str) -> str:
    """Clean up markdown whitespace."""
    if not text:
        return ""
    lines = []
    prev_empty = False
    for line in text.split("\n"):
        is_empty = not line.strip()
        if not (is_empty and prev_empty):
            lines.append(line.rstrip())
        prev_empty = is_empty
    return "\n".join(lines).strip()


async def run_scraper(output_dir: Path, max_depth: int, max_pages: int, verbose: bool) -> dict:
    """Run the deep crawl scraper."""
    output_dir.mkdir(parents=True, exist_ok=True)
    saved, skipped, failed = [], 0, []

    print("=" * 50)
    print("Roku Documentation Scraper (crawl4ai)")
    print(f"Output: {output_dir} | Max Depth: {max_depth} | Max Pages: {max_pages}")
    print("=" * 50)

    # Configure browser with stealth mode
    browser_config = BrowserConfig(headless=True, verbose=verbose)

    # Configure deep crawl with URL filtering
    filter_chain = FilterChain([
        URLPatternFilter(patterns=[DOC_PATTERN]),
    ])

    crawl_config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=max_depth,
            max_pages=max_pages,
            include_external=False,
            filter_chain=filter_chain,
        ),
        wait_until="domcontentloaded",
        wait_for="css:.markdown-body",  # Wait for JS to render content
        wait_for_timeout=15000,
        page_timeout=30000,
        target_elements=[CONTENT_SELECTOR, ".markdown-body"],
        cache_mode=CacheMode.BYPASS,
        stream=True,
        verbose=verbose,
    )

    # Track corrected URLs to retry
    corrected_urls = set()

    async with AsyncWebCrawler(config=browser_config) as crawler:
        async for result in await crawler.arun(START_URL, config=crawl_config):
            # Get parent URL for tracking
            parent_url = result.metadata.get("parent_url") if result.metadata else None

            if not result.success:
                # Check if this is a malformed URL we can correct
                corrected = correct_malformed_url(result.url)
                if corrected:
                    corrected_urls.add(corrected)
                    print(f"  ⚠ Malformed URL, will retry: {corrected}")
                    if parent_url:
                        print(f"      ↳ Found on: {parent_url}")
                else:
                    failed.append({"url": result.url, "reason": result.error_message, "found_on": parent_url})
                    print(f"  ✗ Failed: {result.url}")
                    if parent_url:
                        print(f"      ↳ Found on: {parent_url}")
                continue

            output_path = url_to_path(result.url, output_dir)

            # Duplicate protection
            if output_path.exists():
                skipped += 1
                print(f"  ⏭ Skipped (already exists): {output_path}")
                continue

            # Get markdown from crawl4ai (already focused on target_elements)
            md_content = result.markdown.raw_markdown if hasattr(result.markdown, 'raw_markdown') else str(result.markdown)
            content = clean_markdown(md_content)

            # Check for error pages that return 200 but have no real content
            if not content or content.strip().lower() in ["document not found.", "document not found"]:
                failed.append({"url": result.url, "reason": "Document not found - likely broken link", "found_on": parent_url})
                print(f"  ✗ Document not found (likely broken link on source page): {result.url}")
                if parent_url:
                    print(f"      ↳ Broken link found on: {parent_url}")
            else:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(content, encoding="utf-8")
                depth = result.metadata.get("depth", 0) if result.metadata else 0
                saved.append({"path": str(output_path), "url": result.url, "found_on": parent_url})
                print(f"  ✓ [{depth}] Saved: {output_path}")

        # Retry corrected URLs
        if corrected_urls:
            print(f"\n  Retrying {len(corrected_urls)} corrected URLs...")
            retry_config = CrawlerRunConfig(
                wait_until="domcontentloaded",
                wait_for="css:.markdown-body",
                wait_for_timeout=15000,
                page_timeout=30000,
                target_elements=[CONTENT_SELECTOR, ".markdown-body"],
                cache_mode=CacheMode.BYPASS,
                verbose=verbose,
            )
            for url in corrected_urls:
                output_path = url_to_path(url, output_dir)
                if output_path.exists():
                    skipped += 1
                    print(f"  ⏭ Skipped (already exists): {output_path}")
                    continue
                result = await crawler.arun(url, config=retry_config)
                if result.success:
                    md_content = result.markdown.raw_markdown if hasattr(result.markdown, 'raw_markdown') else str(result.markdown)
                    content = clean_markdown(md_content)
                    if not content or content.strip().lower() in ["document not found.", "document not found"]:
                        failed.append({"url": url, "reason": "Document not found - likely broken link", "found_on": "retry"})
                        print(f"  ✗ [retry] Document not found (likely broken link): {url}")
                    else:
                        output_path.parent.mkdir(parents=True, exist_ok=True)
                        output_path.write_text(content, encoding="utf-8")
                        saved.append({"path": str(output_path), "url": url, "found_on": "retry"})
                        print(f"  ✓ [retry] Saved: {output_path}")
                else:
                    failed.append({"url": url, "reason": result.error_message, "found_on": "retry"})
                    print(f"  ✗ Retry failed: {url}")

    return {"saved": saved, "skipped": skipped, "failed": failed}


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Scrape Roku Developer Documentation")
    parser.add_argument("--output-dir", default="./roku_docs", help="Output directory")
    parser.add_argument("--max-depth", type=int, default=10, help="Max crawl depth (default: 10)")
    parser.add_argument("--max-pages", type=int, default=2000, help="Max pages to crawl (default: 2000)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    try:
        start_time = time.time()
        stats = asyncio.run(run_scraper(Path(args.output_dir), args.max_depth, args.max_pages, args.verbose))
        duration = time.time() - start_time

        # Format duration
        minutes, seconds = divmod(int(duration), 60)
        hours, minutes = divmod(minutes, 60)
        if hours:
            duration_str = f"{hours}h {minutes}m {seconds}s"
        elif minutes:
            duration_str = f"{minutes}m {seconds}s"
        else:
            duration_str = f"{seconds}s"

        print("\n" + "=" * 50)
        print("COMPLETE")
        print(f"Saved: {len(stats['saved'])} | Skipped: {stats['skipped']} | Failed: {len(stats['failed'])}")
        print(f"Duration: {duration_str}")
        print("=" * 50)

        # Save results
        results_path = Path(args.output_dir) / "results.json"
        results_path.write_text(json.dumps(stats, indent=2))
        print(f"Results saved to: {results_path}")

        return 0 if not stats["failed"] else 1

    except KeyboardInterrupt:
        print("\nInterrupted by user")
        return 1
    except Exception as e:
        print(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())