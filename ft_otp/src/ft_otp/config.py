
# ===============================
### scorpion: Configuration file
# ===============================

from typing_extensions import Literal

### terminal colors :
TERMINAL_COLORS : dict[str, str] = {
    "INFO"      : "\033[0;36m",      # sky blue
    "WARNING"   : "\033[0;33m",      # Yellow
    "ERROR"     : "\033[0;31m",      # Red
    "RESET"     : "\033[0m"          # Reset
}

### Logging configuration :
LOG_DISABLED        : bool = False   # Disable logging
LOG_LEVEL           : Literal["INFO", "WARNING", "ERROR"] = "INFO"
LOG_FORMAT          : str = "%(asctime)s: [%(levelname)-7s] - %(message)s"
LOG_DATE_FORMAT     : str = "%Y-%m-%d %H:%M:%S"
LOG_ENABLE_STDOUT   : bool = True           # Enable logging to stdout
LOG_FILE            : str | None = None     # Path of log file if None not used

### Default Value :
DEFAULT_HEX_KEY_FILE    : str = "./hex_key.txt"
DEFAULT_KEY_FILE        : str = "./ft_otp.key"
DEFAULT_KEY_OUTPUT      : str = "./ft_otp.key"
DEFAULT_ISSUER          : str = "ft_otp"
DEFAULT_ACCOUNT         : str = "user@ft_otp.app"
DEFAULT_QR_OUTPUT       : str = "./ft_otp.png"

DEFAULT_OTP_DIGITS      : int = 6
TIMESTEP                : int = 30  # Time step in seconds for OTP generation