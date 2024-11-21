import logging

def setup_logger(name: str, log_file: str, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

api_logger = setup_logger('api_logger', 'api_requests.log')
process_logger = setup_logger('process_logger', 'process.log')
