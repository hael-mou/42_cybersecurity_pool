
import os

from logging import Logger
from scraper import Scraper
from spider.config import IMG_EXTENSIONS
from .formatter import print_Results

# ===============================================================================
#  Scrape images from all links found at the given URL.
#
#  @param url: Starting URL to scrape.
#  @param save_path: Directory where images are saved.
#  @param logger: Logger used to report progress and errors.
#  @param depth: Link scraping depth.
#  @return: None
# ===============================================================================
def scrape_images(url: str, save_path: str, logger: Logger,  depth: int = 0) -> None :
    with Scraper(save_path) as scraper:
        logger.info(f"[scrape_Links] - Scraping links from {url}: ")
        links = scraper.scrape_links(url, depth)

        for link in links:
            logger.info(f"{'-' * 10}\n")
            logger.info(f"=== Scraping images from {link} :")
            try:
                scraper.scrape_images(link, IMG_EXTENSIONS)
            
            except KeyboardInterrupt:
                raise
            except Exception as e:
                logger.error(f"[scrape_images] - Failed to scrape {link}: {e}")

        path = os.path.abspath(save_path)
        total_images = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        print_Results(total_images, path)
