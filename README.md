# brightScriptDocsScraper

A Python scraper that recursively downloads Roku/BrightScript documentation from [developer.roku.com](https://developer.roku.com) and stores it as clean markdown files. Updated automatically every week via GitHub Actions.

## 🤖 Use with AI Assistants (MCP)

The documentation in this repository is available as an MCP (Model Context Protocol) server via [Context7](https://context7.com):

```
https://context7.com/robsonharrison/brightscriptdocsscraper
```

This allows AI coding assistants that support MCP (like Cursor, Windsurf, Claude Desktop, etc.) to access up-to-date Roku/BrightScript documentation directly.

### Setup for MCP-compatible tools

Add to your MCP configuration:
```json
{
  "mcpServers": {
    "brightscript-docs": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-client", "https://context7.com/robsonharrison/brightscriptdocsscraper"]
    }
  }
}
```

## 📁 Project Structure

```
brightScriptDocsScraper/
├── .github/workflows/      # GitHub Actions (weekly auto-scrape)
├── scraper/                # Scraper source code
│   └── WebScraper.py
├── roku_docs/              # 📚 Scraped documentation
│   ├── docs/               #    Developer guides & API references
│   ├── trc-docs/           #    TRC documentation
│   └── results.json        #    Scrape results summary
├── .gitignore
├── requirements.txt
└── README.md
```

## ✨ Features

- **Weekly automated updates** via GitHub Actions
- **MCP-compatible** for AI assistant integration
- Deep crawls the Roku developer documentation
- Converts pages to clean markdown files
- Compares content to detect actual changes (not just file existence)
- Tracks broken links and their source pages
- Handles malformed URLs with automatic retry

## 🚀 Running Locally

```bash
# Install dependencies
pip install -r requirements.txt
crawl4ai-setup

# Run the scraper
python scraper/WebScraper.py

# Custom options
python scraper/WebScraper.py --output-dir ./roku_docs --max-depth 5 --max-pages 500 --verbose
```

### Options

| Option | Default | Description |
|--------|---------|-------------|
| `--output-dir` | `./roku_docs` | Directory to save markdown files |
| `--max-depth` | `10` | Maximum link depth to crawl |
| `--max-pages` | `2000` | Maximum number of pages to crawl |
| `--verbose`, `-v` | `false` | Show detailed crawl4ai logging |

## 🔄 GitHub Actions

The scraper runs automatically every **Sunday at 2:00 AM UTC**.

- New and updated documentation is committed directly to the repository
- Commit messages include a summary of what changed
- Manual trigger available: **Actions** → **Scrape Roku Documentation** → **Run workflow**

## 📄 Output

The `roku_docs/` folder contains:
- Markdown files preserving the original URL path structure
- `results.json` with scrape summary:
  - `new` - Newly added pages
  - `updated` - Pages with content changes
  - `unchanged` - Pages with no changes
  - `failed` - Failed pages with error reasons

## 📜 License

This project scrapes publicly available documentation from [developer.roku.com](https://developer.roku.com). The scraped content remains the property of Roku, Inc. This tool is provided for convenience and offline access.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

