import logging
from config.paths import LOG_FILE



# Return a configured logger that writes to LOG_FILE
def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger