# 📰 Content Aggregator

A Python-based news aggregation tool that fetches technology news from The New York Times RSS feed, formats it into a daily digest, and can convert it to PDF format for easy reading.

## 🚀 Features

- **News Fetching**: Automatically retrieves the latest technology news from NYT's RSS feed
- **Daily Digest**: Generates a formatted markdown file with today's date
- **PDF Conversion**: Converts the markdown digest to a professional PDF format
- **Clean Formatting**: Well-structured output with titles, summaries, and links
- **Date-based Naming**: Files are automatically named with the current date

## 📋 Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## 🛠️ Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install feedparser markdown2 weasyprint
```

### Dependencies Explained

- **feedparser**: Parses RSS feeds to extract news articles
- **markdown2**: Converts markdown to HTML for PDF generation
- **weasyprint**: Generates PDF files from HTML content

## 📖 Usage

### 1. Fetch News and Save to Markdown

Run the main script to fetch today's technology news and save it as a markdown file:

```bash
python save_to_markdown.py
```

This will:

- Fetch the latest technology news from NYT
- Create a file named `digest-YYYY-MM-DD.md` (e.g., `digest-2025-07-26.md`)
- Format the news with titles, publication dates, summaries, and links

### 2. Convert Markdown to PDF

Convert the generated markdown file to PDF:

```bash
python convert_to_pdf.py
```

This will:

- Look for today's markdown digest file
- Convert it to a professional PDF format
- Save it as `digest-YYYY-MM-DD.pdf`

### 3. Individual Components

You can also run the components separately:

```bash
# Just fetch and display news (for testing)
python news_fetcher.py

# Convert a specific markdown file to PDF
python convert_to_pdf.py
```

## 📁 Project Structure

```
content_aggree/
├── news_fetcher.py          # Fetches news from NYT RSS feed
├── save_to_markdown.py      # Saves news to formatted markdown
├── convert_to_pdf.py        # Converts markdown to PDF
├── digest-2025-07-26.md     # Example output file
└── README.md               # This file
```

## 📰 Sample Output

The generated markdown file includes:

- Daily header with date
- Formatted news articles with:
  - Article titles
  - Publication dates
  - Summaries
  - Direct links to full articles
- Clean separators between articles

Example structure:

```markdown
# 🗞️ Daily Tech Digest – 2025-07-26

## 📰 Technology News

### Article Title

_Published: Date_

Article summary...
[Read more](link)

---
```

## 🔧 Customization

### Change News Source

To fetch news from a different RSS feed, modify the `feed_url` in `news_fetcher.py`:

```python
feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
```

### Modify Output Format

Edit `save_to_markdown.py` to change the markdown formatting or add additional sections.

### PDF Styling

The PDF conversion uses basic HTML styling. You can enhance it by modifying the HTML generation in `convert_to_pdf.py`.

## 🐛 Troubleshooting

### Common Issues

1. **Missing dependencies**: Ensure all required packages are installed
2. **PDF generation fails**: WeasyPrint may require additional system dependencies on some platforms
3. **RSS feed unavailable**: Check if the NYT RSS feed is accessible

### Error Messages

- `❌ Markdown file not found`: Run `save_to_markdown.py` first to generate the markdown file
- `✅ Markdown file saved`: Successfully created the digest file
- `✅ PDF file saved`: Successfully converted to PDF

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- The New York Times for providing the RSS feed
- The Python community for the excellent libraries used in this project

---

**Happy reading! 📚**
