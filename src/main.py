from src.extract import fetch_top_stories
from src.transform import transform_data
from src.load import load_data
from src.logger import get_logger

logger = get_logger(__name__)

def run_etl():
    """Main execution block for the ETL pipeline."""
    logger.info("Starting ETL Pipeline...")
    
    raw_data = fetch_top_stories(limit=50)
    if not raw_data:
        logger.error("Extraction failed. Aborting pipeline.")
        return
        
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data)
    
    logger.info("ETL Pipeline completed successfully.")

if __name__ == "__main__":
    run_etl()
