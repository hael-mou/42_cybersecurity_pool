
import sys, logging
from logging import Logger
from stockholm.config import TERMINAL_COLORS as C

# ===============================================================================
#  Configure the application logger.
#
#  @return: Configured root logger. 
# ===============================================================================
def setup_logger(config) -> Logger:
    logger = logging.getLogger()

    # Remove handlers created previously, including default handlers.
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()

    logger.disabled = False
    logger.setLevel(getattr(logging, config.LOG_LEVEL, logging.INFO))

    # Prevent logging.lastResort .
    if (
        config.LOG_DISABLED
        or (
            not config.LOG_ENABLE_STDOUT
            and not config.LOG_FILE
        )
    ):
        logger.addHandler(logging.NullHandler())
        return logger

    if config.LOG_ENABLE_STDOUT:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(
            ColoredFormatter(
                fmt=config.LOG_FORMAT,
                datefmt=config.LOG_DATE_FORMAT,
            )
        )
        logger.addHandler(stdout_handler)

    if config.LOG_FILE:
        file_handler = logging.FileHandler(config.LOG_FILE)
        file_handler.setFormatter(
            logging.Formatter(
                fmt=config.LOG_FORMAT,
                datefmt=config.LOG_DATE_FORMAT,
            )
        )
        logger.addHandler(file_handler)

    return logger


# ===============================================================================
#  Formatter that adds terminal colors based on the log level.
#
#  @return: Colored formatted log message.
# ===============================================================================
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        level_color = C.get(record.levelname, "")
        message = super().format(record)
        return f"{level_color}{message}{C['RESET']}"
