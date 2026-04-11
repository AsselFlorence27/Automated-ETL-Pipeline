# HackerNews ETL Pipeline

An automated data pipeline that extracts trending stories from HackerNews and persists them into a local SQLite database for downstream analytics.

## Overview
This project serves as a reliable data feed, removing the need for manual CSV handling. It automatically fetches the top stories, cleans the raw JSON payloads, and implements an upsert mechanism to track engagement metrics over time.

## Architecture
- **Source**: HackerNews API (topstories)
- **Pipeline**: Python (`requests`)
- **Storage**: SQLite (`data.db`)
- **Automation**: GitHub Actions (Scheduled daily cron job)

## Setup and Usage

1. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the pipeline manually:
   ```bash
   python etl_pipeline.py
   ```
3. Query the results:
   ```bash
   sqlite3 data.db "SELECT * FROM top_stories LIMIT 5;"
   ```

## Workflow
The pipeline runs autonomously via GitHub Actions every day at 08:00 UTC. The database file (`data.db`) is tracked and automatically updated via git commits when new data is fetched, ensuring a historical record of trending stories is maintained.
