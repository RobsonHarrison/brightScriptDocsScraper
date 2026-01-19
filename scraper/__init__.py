"""
BrightScript Documentation Scraper

A tool for scraping Roku/BrightScript documentation to markdown files.
"""

from scraper.scraper import (
    ScraperConfig,
    ScrapeStats,
    run_scraper,
)

__version__ = "1.0.0"
__all__ = ["ScraperConfig", "ScrapeStats", "run_scraper", "__version__"]

