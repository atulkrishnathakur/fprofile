import logging
from datetime import datetime

def setup_logger():
    """Set up logging configuration."""
    current_date = datetime.now().strftime('%Y-%m-%d')
    log_directory = 'logs'
    log_file = f'{log_directory}/fprofile_{current_date}.log'
    logging.basicConfig(
        level=logging.DEBUG,  # Set the logging level to INFO
        format='%(asctime)s - %(levelname)s - %(message)s',  # Define the format of log messages
        filename=log_file,  # Specify the log file name
        filemode='a'  # Append to the log file
    )

    return logging.getLogger(__name__)

# Create a logger instance
logger = setup_logger()
