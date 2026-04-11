import requests
import datetime
import sqlite3

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL_TEMPLATE = "https://hacker-news.firebaseio.com/v0/item/{}.json"

def fetch_top_stories(limit=50):
    """Fetch top stories from HackerNews API."""
    response = requests.get(TOP_STORIES_URL)
    response.raise_for_status()
    story_ids = response.json()[:limit]
    
    processed_stories = []
    
    for story_id in story_ids:
        item_response = requests.get(ITEM_URL_TEMPLATE.format(story_id))
        if item_response.status_code == 200:
            item_data = item_response.json()
            
            clean_story = {
                "id": item_data.get("id"),
                "title": item_data.get("title", "No Title"),
                "url": item_data.get("url", ""),
                "score": item_data.get("score", 0),
                "author": item_data.get("by", "Unknown"),
                "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
            }
            processed_stories.append(clean_story)
            
    return processed_stories

def load_data(stories, db_path="data.db"):
    """Insert or update stories into SQLite database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS top_stories (
            id INTEGER PRIMARY KEY,
            title TEXT,
            url TEXT,
            score INTEGER,
            author TEXT,
            retrieved_at TEXT
        )
    ''')
    
    for story in stories:
        cursor.execute('''
            INSERT OR REPLACE INTO top_stories (id, title, url, score, author, retrieved_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (story['id'], story['title'], story['url'], story['score'], story['author'], story['retrieved_at']))
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    stories = fetch_top_stories(limit=50)
    load_data(stories)
