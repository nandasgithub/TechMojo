import logging.handlers

# Logger formatter
log_level = "ERROR"
log_format = "%(asctime)s %(name)s %(levelname)s %(module)s %(funcName)s %(lineno)4d %(message)s"
max_bytes_kb = 1024
backup_count = 50
log_handler = logging.handlers.RotatingFileHandler('LOG_FILE.log', 'a', max_bytes_kb * 1024, backup_count)

# Logger Settings
log_handler.setLevel(log_level)
log_formatter = logging.Formatter(log_format)
log_handler.setFormatter(log_formatter)
logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(log_level)
