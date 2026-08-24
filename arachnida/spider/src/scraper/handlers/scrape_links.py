
import os

from scraper.downloader import Downloader
from scraper.utils import url as urlUtils
from scraper.utils.constant import FILE_EXTENSIONS
from logging import getLogger
from urllib.parse import urlparse

# ===============================================================================
#  Scrape internal links from a web page and recursively crawl them up to the
#  specified depth.
#
#  @param Downloader: Downloader used to load and query web pages.
#  @param str: URL of the page to start crawling from.
#  @param int: Maximum recursion depth.
#  @return: Set of discovered internal URLs.
# ===============================================================================
def scrape_links(downloader: Downloader, url: str, max_depth: int = 0) -> set[str]:
    visited    = set()
    logger     = getLogger(__name__)


    def _crawl(url: str, depth: int = 0) -> set[str]:
        if depth >= max_depth or  url in visited:
            return set()
        
        logger.info(f"Loading page: [SCRAP_LINK] [Depth: {depth}] [url: {url}]")
        if not downloader.load(url):
            return set()

        visited.add(url)
        links_found = set()
        try:
            anchors = downloader.query_selector_all("a")
            for a in  anchors:
                href = a.get_attribute("href")
                if not href or href[0] == '#':
                    continue
                
                href = urlUtils.full_url(url, href)
                if not urlUtils.is_same_domain(url, href):
                    continue

                if has_forbidden_extension(href):
                    continue
    
                if href not in visited:
                    links_found.add(href)
                
        except KeyboardInterrupt:
            raise
        except Exception as e:
            logger.error(f"[SCRAPE_LINKS] Error reading links from {url}: {e}")

    
        for link in list(links_found):
            links_found.update(_crawl(link, depth + 1))

        return links_found

    return _crawl(url, 0) | {url}


# ===============================================================================
#  Check whether a URL points to a resource with a forbidden file extension.
#
#  @param str: URL to check.
#  @return: True if the URL has a forbidden extension, otherwise False.
# ===============================================================================
def has_forbidden_extension(url: str) -> bool:
    path = urlparse(url).path
    ext  = os.path.splitext(path)[1].lower()
    return ext in FILE_EXTENSIONS
