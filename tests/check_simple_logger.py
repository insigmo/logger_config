import logging

from logger_config import configure_logging

logger_name = 'root_logger'
configure_logging(logger_name, log_dir='logs')
logger = logging.getLogger(logger_name)


logger.info('text')
