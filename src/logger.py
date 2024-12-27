import logging

def setup_logging(log_file='devops_metrics.log'):
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def log_info(message):
    logging.info(message)