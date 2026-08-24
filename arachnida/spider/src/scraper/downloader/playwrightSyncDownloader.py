
from playwright._impl._errors import TimeoutError
from .downloaderFactory import DownloaderFactory
from playwright.sync_api import sync_playwright
from .downloader import Downloader
from logging import getLogger
from scraper import config

# ===============================================================================
# Downloader implementation using Playwright's synchronous API.
#
# Handles page loading, element selection, and browser resource management.
# ===============================================================================
@DownloaderFactory.register("playwrightSync")
class PlaywrightSyncDownloader(Downloader):
    def __init__(self):
        self.logger = getLogger(__name__)
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.page = self.browser.new_page()


    def load(self, url: str) -> bool:
        """
        - Load the page from the given URL.
        @param url: URL of the page to load.
        @return: True if the page loaded successfully, otherwise False.
        """
        try:
            self.page.goto(url)
            self.page.wait_for_load_state("networkidle", timeout=config.LOAD_STATE_TIMEOUT)
        except TimeoutError:
            self.logger.warning(f"Timeout loading page not complete [ {url} ] 'add more timeout to LOAD_STATE_TIMEOUT in config.py'")
            return True
        except Exception as e:
            self.logger.error(f"Error loading page: {e}")
            return False
        return True


    def query_selector_all(self, selector: str) -> list:
        """
        - Return all elements matching the selector.
        @param selector: CSS selector used to find elements.
        @return: List of matching page elements.
        """
        return self.page.query_selector_all(selector)


    def close(self):
        """Close the page, browser, and Playwright resources."""
        try:
            self.page.close()
            self.browser.close()
            self.playwright.stop()
        except:
            pass


    def __del__(self):
        """Ensure resources are closed when the object is destroyed."""
        try:
            self.close()
        except:
            pass
