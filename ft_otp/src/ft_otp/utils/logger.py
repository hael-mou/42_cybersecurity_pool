
import sys, logging
from logging import Logger
from ft_otp.config import LOG_DATE_FORMAT, LOG_ENABLE_STDOUT, LOG_FILE 
from ft_otp.config import LOG_DISABLED, LOG_LEVEL, LOG_FORMAT, TERMINAL_COLORS as C

# ===============================================================================
#  Configure the application logger.
#
#  @return: Configured root logger. 
# ===============================================================================
def setup_logger() -> Logger:
    logger = logging.getLogger()

    # Prevent duplicate handlers :
    if logger.handlers: return logger

    # Disable logging completely :
    if LOG_DISABLED: logger.disabled = True; return logger
    
    # Disable logging when no output destination is configured :
    if not LOG_ENABLE_STDOUT and not LOG_FILE: logger.disabled = True; return logger

    # Set logging level :
    level = getattr(logging, LOG_LEVEL, logging.INFO)
    logger.setLevel(level)

    # stdout handler :
    if LOG_ENABLE_STDOUT:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(ColoredFormatter(fmt=LOG_FORMAT, datefmt=LOG_DATE_FORMAT))
        logger.addHandler(stdout_handler)
    
    # file handler :
    if LOG_FILE is not None:
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(logging.Formatter(fmt=LOG_FORMAT, datefmt=LOG_DATE_FORMAT))
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
