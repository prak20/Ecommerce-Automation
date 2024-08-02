# # logging_config.py
# import logging
# import os
#
#
# def get_logs(directory='../../Result/logs', log_file='logfile.log'):
#     """
#     Sets up logging to output messages to a file and the console.
#
#     :param directory: The directory where the log file will be saved.
#     :param log_file: The name of the log file.
#     """
#     # Create the directory if it does not exist
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#     # Define the full path for the log file
#     log_file_path = os.path.join(directory, log_file)
#
#     # Set up logging configuration
#     logging.basicConfig(
#         level=logging.DEBUG,
#         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#         handlers=[
#             logging.FileHandler(log_file_path),
#             logging.StreamHandler()
#         ]
#     )
#
#
#     return logging


import logging
import os
from backend.utils.params import log_dir


def get_logs(name, log_file, level=logging.INFO):
    """Function to setup a logger"""
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # Create the directory if it does not exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Define the full path for the log file
    log_file_path = os.path.join(log_dir, log_file)
    handler = logging.FileHandler(log_file_path)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

logger = get_logs('logger', 'logfile.log')
