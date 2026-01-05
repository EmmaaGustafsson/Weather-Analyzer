import logging
from config.paths import LOG_FILE



def get_logger(name: str):
    """
    Creates and returns a logger that writes logs to a file.
    """
    logger = logging.getLogger(name) # Hämtar en logger med ett namn
    logger.setLevel(logging.INFO)    # Sätter loggnivå (INFO = normal information)
    
    if not logger.handlers:          # Förhindrar att flera handlers läggs till av misstag
        handler = logging.FileHandler(LOG_FILE)  # Skapar en fil där loggar kommer sparas
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")  # Bestämmer hur loggarna ska se ut
        handler.setFormatter(formatter) 
        logger.addHandler(handler)
        
    return logger