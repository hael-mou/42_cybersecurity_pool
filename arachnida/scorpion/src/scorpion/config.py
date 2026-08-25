
# ===============================
### scorpion: Configuration file
# ===============================

from typing_extensions import Literal

### terminal colors:
TERMINAL_COLORS : dict[str, str] = {
    "INFO"      : "\033[0;36m",      # sky blue
    "WARNING"   : "\033[0;33m",      # Yellow
    "ERROR"     : "\033[0;31m",      # Red
    "RESET"     : "\033[0m"          # Reset
}

### Logging configuration:
LOG_DISABLED        : bool = False   # Disable logging
LOG_LEVEL           : Literal["INFO", "WARNING", "ERROR"] = "INFO"
LOG_FORMAT          : str = "%(asctime)s: [%(levelname)-7s] - %(message)s"
LOG_DATE_FORMAT     : str = "%Y-%m-%d %H:%M:%S"
LOG_ENABLE_STDOUT   : bool = True           # Enable logging to stdout
LOG_FILE            : str | None = None     # Path of log file if None not used

## gui
HOST = "0.0.0.0"
PORT = 5000
