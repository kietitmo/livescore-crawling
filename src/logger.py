import logging
import os

# Create a single logger instance
logger = None

def setup_logger(log_file_name='app.log'):
    """Sets up a single logger to write logs to a specified file."""
    global logger 
    
    if logger is not None:
        return logger  

    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)  
    log_file_path = os.path.join(log_dir, log_file_name)

    logger = logging.getLogger('ApplicationLogger')
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger