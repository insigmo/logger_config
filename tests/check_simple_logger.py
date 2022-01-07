import logging

from logger_config import configure_logging

logger_name = 'root_logger'
configure_logging(logger_name, log_dir='logs')
logger = logging.getLogger(logger_name)

logger.warning('This is warning')
logger.error('This is exception')
logger.info('This is info message')
logger.debug('This is debug message')
