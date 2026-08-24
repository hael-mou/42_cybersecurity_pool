
# ===============================
### Spider: Configuration file
# ===============================

from typing_extensions import Literal
from pathlib import Path

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

### Default  values :
DEFAULT_DEPTH       : int = 5
IMG_EXTENSIONS      : list[str] = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"]
DOWNLOAD_FOLDER     : str  = str(Path.cwd() / "data")   # folder where downloaded images will be saved
