
from pathlib import Path

# ===============================
### Scraper Configuration file
# ===============================

DOWNLOADER          : str  = "playwrightSync"   # downloader use to obtain page content
DOWNLOAD_FOLDER     : str  = str(Path.cwd() / "data")   # folder where downloaded images will be saved
LOAD_STATE_TIMEOUT  : int = 1000 # ms   # Timeout for waiting page load state

DEFAULT_DEPTH       : int = 5
IMG_EXTENSIONS      : list[str] = [".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico", ".bmp"]
