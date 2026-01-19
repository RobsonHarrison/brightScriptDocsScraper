# brightScriptDocsScraper

A Python scraper that recursively downloads Roku/BrightScript documentation from [developer.roku.com](https://developer.roku.com) and stores it as clean markdown files. Runs automatically via GitHub Actions on a weekly schedule.

## 📁 Project Structure

```
brightScriptDocsScraper/
├── .github/workflows/      # GitHub Actions (weekly auto-scrape)
├── scraper/                # Scraper source code
│   └── WebScraper.py
├── roku_docs/              # 📚 Scraped documentation
│   ├── docs/               #    Developer guides & API references
│   ├── trc-docs/           #    TRC documentation
│   └── results.json        #    Scrape results & broken link report
├── .gitignore
├── requirements.txt
└── README.md
```

## ✨ Features

- **Automated weekly updates** via GitHub Actions
- Deep crawls the Roku developer documentation
- Converts pages to clean markdown files
- Tracks broken links and their source pages
- Handles malformed URLs and retries with corrections
- Duplicate protection (skips already-saved files)

## 🚀 Quick Start

### Local Usage

```bash
# Install dependencies
pip install -r requirements.txt
crawl4ai-setup

# Run the scraper
python scraper/WebScraper.py

# Custom options
python scraper/WebScraper.py --output-dir ./roku_docs --max-depth 5 --max-pages 500

# Verbose mode
python scraper/WebScraper.py --verbose
```

### Options

| Option | Default | Description |
|--------|---------|-------------|
| `--output-dir` | `./roku_docs` | Directory to save markdown files |
| `--max-depth` | `10` | Maximum link depth to crawl |
| `--max-pages` | `2000` | Maximum number of pages to crawl |
| `--verbose`, `-v` | `false` | Show detailed crawl4ai logging |

## 🤖 GitHub Actions

The scraper runs automatically every **Sunday at 2:00 AM UTC**. New/updated documentation is committed directly to the repository.

To run manually: **Actions** → **Scrape Roku Documentation** → **Run workflow**

## 📄 Output

The `roku_docs/` folder contains:
- Markdown files preserving the original URL path structure
- `results.json` with scrape summary:
  - `saved` - Successfully saved pages with source URLs
  - `skipped` - Count of already-existing files
  - `failed` - Failed pages with error reasons (useful for finding broken links on Roku's site)

