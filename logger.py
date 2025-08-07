import logging


LOGGER_FORMAT = "[%(asctime)s] [%(levelname)s] [%(filename)s -> %(funcName)s()] [%(lineno)s] %(message)s"


def setup_custom_logger() -> logging.Logger:
    logger = logging.getLogger("learn celery")
    logger.setLevel(level=logging.DEBUG)
    if not logger.handlers:
        formatter = logging.Formatter(LOGGER_FORMAT)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    logger.propagate = False

    return logger


log = setup_custom_logger()
