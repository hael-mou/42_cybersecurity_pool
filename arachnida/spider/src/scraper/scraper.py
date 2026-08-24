
import os

from logging import getLogger
from scraper.downloader import DownloaderFactory
from scraper.handlers.scrape_images import scrape_images
from scraper.handlers.scrape_links import scrape_links
from .utils import url as urlUtils
from .config import DOWNLOAD_FOLDER, DOWNLOADER, IMG_EXTENSIONS

## === Scraper Class : ==========================================================
class Scraper:
    # ==================================================================
    #  Constructor / Context Manager
    # ==================================================================
    def __init__(self, dir: str = DOWNLOAD_FOLDER, downloader: str = DOWNLOADER):
        self.logger       = getLogger(__name__)
        self._downloader  = None
        self.downloader   = downloader
        self._dir         = None
        self.dir          = dir

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __del__(self):
        self.close()
    

    # ==================================================================
    #  Resource Cleanup
    # ==================================================================
    def close(self):
        """Safely close downloader resources."""
        if self._downloader:
            try:
                self._downloader.close()
            except Exception as e:
                self.logger.error(f"Downloader close() failed: {e}")
            finally:
                self._downloader = None


    # ==================================================================
    #  Scraping Methods
    # ==================================================================
    def scrape_links(self, url: str, max_depth: int = 0) -> set[str]:
        """
        Scrape all links recursively from the given URL.
        @arg
        @return     
        """
        url = urlUtils.normalize_url(url)
        if not urlUtils.is_valid_url(url):
            self.logger.error(f"Invalid URL: {url}")
            return set()
        return scrape_links(self.downloader, url, max_depth)


    def scrape_images(self, url: str, extensions: list = IMG_EXTENSIONS) -> int:
        """ Scrape all images from the given URL. """
        return scrape_images(
                    url=url, 
                    downloader=self.downloader,
                    dir=self.dir, 
                    extensions=extensions
                )


    # ==================================================================
    # Properties: Directory
    # ==================================================================
    @property
    def dir(self) -> str:
        return self._dir


    @dir.setter
    def dir(self, path: str) -> None:
        """Validate directory path, create if needed, ensure permissions."""
        path = os.path.abspath(path)

        # Attempt to create directory
        try:
            os.makedirs(path, exist_ok=True)
        except PermissionError:
            self.logger.error(f"Permission denied to create directory: '{path}'")
            raise
        except Exception as e:
            self.logger.error(f"Failed to create directory '{path}': {e}")
            raise

        # Ensure directory exists
        if not os.path.isdir(path):
            msg = f"'{path}' exists but is not a directory."
            self.logger.error(msg)
            raise NotADirectoryError(msg)

        # Check permissions
        if not os.access(path, os.W_OK | os.X_OK):
            msg = f"Permission denied for directory '{path}'."
            self.logger.error(msg)
            raise PermissionError(msg)

        self._dir = path


    # ==============================================================================
    # Properties: Downloader
    # ==============================================================================
    @property
    def downloader(self):
        return self._downloader


    @downloader.setter
    def downloader(self, name: str):
        """Validate downloader name and create downloader instance."""
        instance = DownloaderFactory.create(name)

        if not instance:
            msg = f"No downloader found with name '{name}'."
            self.logger.error(msg)
            raise ValueError(msg)

        self._downloader = instance
