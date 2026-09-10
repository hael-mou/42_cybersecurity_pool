
# ===============================
### stockholm: Configuration file
# ===============================

from typing_extensions import Literal
from pathlib import Path

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

### src dir :
BASE_DIR = Path(__file__).resolve().parent

### Default Value :
PUBLIC_KEY_PATH         : str  = BASE_DIR / "utils" / "stockholm.pub"
INFECTED_PATH           : Path = Path.home() / "infection"
ENCRYPTED_EXTENSION     : str  = ".ft"
ENCRYPTED_KEY_ATTRIBUTE : str  = "user.encrypted_key"
INFECTED_EXTENSIONS     : list = [
            ".der", ".pfx", ".key", ".crt", ".csr", ".p12", ".pem", ".odt", ".ott", ".sxw", ".stw", ".uot",
            ".3ds", ".max", ".3dm", ".ods", ".ots", ".sxc", ".stc", ".dif", ".slk", ".wb2", ".odp", ".otp",
            ".sxd", ".std", ".uop", ".odg", ".otg", ".sxm", ".mml", ".lay", ".lay6", ".asc", ".sqlite3",
            ".sqlitedb", ".sql", ".accdb", ".mdb", ".db", ".dbf", ".odb", ".frm", ".myd", ".myi", ".ibd",
            ".mdf", ".ldf", ".sln", ".suo", ".cs", ".c", ".cpp", ".pas", ".h", ".asm", ".js", ".cmd",
            ".bat", ".ps1", ".vbs", ".vb", ".pl", ".jsp", ".php", ".asp", ".rb", ".java", ".jar", ".class",
            ".sh", ".mp3", ".wav", ".swf", ".fla", ".wmv", ".mpg", ".vob", ".mpeg", ".asf", ".avi", ".mov",
            ".mp4", ".3gp", ".mkv", ".3g2", ".flv", ".wma", ".mid", ".m3u", ".m4u", ".djvu", ".svg", ".ai",
            ".psd", ".nef", ".tiff", ".tif", ".cgm", ".raw", ".gif", ".png", ".bmp", ".jpg", ".jpeg", ".vcd",
            ".iso", ".backup", ".zip", ".rar", ".7z", ".gz", ".tgz", ".tar", ".bak", ".tbk", ".bz2", ".paq",
            ".arc", ".aes", ".gpg", ".vmx", ".vmdk", ".vdi", ".sldm", ".sldx", ".sti", ".sxi", ".602", ".hwp",
            ".snt", ".onetoc2", ".dwg", ".pdf", ".wk1", ".wks", ".123", ".rtf", ".csv", ".txt", ".vsdx",
            ".vsd", ".edb", ".eml", ".msg", ".ost", ".pst", ".potm", ".potx", ".ppam", ".ppsx", ".ppsm",
            ".pp", ".ppt", ".xlt", ".xl", ".xlw", ".xlsb", ".xlsm", ".xlsx", ".xls", ".dotx", ".dotm",
            ".dot", ".docm", ".docb", ".docx", ".doc"
        ]