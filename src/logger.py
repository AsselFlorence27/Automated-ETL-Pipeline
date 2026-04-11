import logging
import sys

def get_logger(name):
    """Return a properly configured logger."""
    logger = logging.getLogger(name)
    
    # Avoid duplicate logs if get_logger is called multiple times
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Create console handler
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        
        # Create formatting
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
    return logger
