from news_fetcher import fetch_news
from datetime import datetime
import os

def save_news_to_markdown(news_items):
    today_str = datetime.today().strftime("%Y-%m-%d")
    filename = f"digest-{today_str}.md"

    lines = []
    lines.append(f"# 🗞️ Daily Tech Digest – {today_str}\n")
    lines.append("## 📰 Technology News\n")

    for item in news_items:
        lines.append(f"### {item['title']}")
        lines.append(f"*Published: {item['published']}*")
        lines.append("")
        lines.append(f"{item['summary']}")
        lines.append(f"[Read more]({item['link']})")
        lines.append("\n---\n")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"✅ Markdown file saved: {filename}")

if __name__ == "__main__":
    news = fetch_news()
    save_news_to_markdown(news)

