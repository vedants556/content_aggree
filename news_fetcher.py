import feedparser
from datetime import datetime

def fetch_news():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
    feed = feedparser.parse(feed_url)

    news_items = []

    for entry in feed.entries:
        news = {
            "title": entry.title,
            "summary": entry.summary,
            "link": entry.link,
            "published": entry.published
        }
        news_items.append(news)

    return news_items

if __name__ == "__main__":
    news = fetch_news()
    for item in news:
        print(f"Title: {item['title']}")
        print(f"Published: {item['published']}")
        print(f"Summary: {item['summary']}")
        print(f"Link: {item['link']}")
        print("-" * 80)
