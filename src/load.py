import sqlite3
from src.logger import get_logger

logger = get_logger(__name__)

def load_data(stories, db_path="data.db"):
    """Insert or update stories into SQLite database."""
    if not stories:
        logger.warning("No stories to insert. Skipping DB operation.")
        return
        
    logger.info(f"Connecting to database at {db_path}...")
    conn = None
    try:
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
        logger.info("Successfully loaded data into database.")
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
