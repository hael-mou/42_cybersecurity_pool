
from logging import getLogger
from scraper.downloader import Downloader
from scraper.utils import url as urlUtils
from scraper.utils.other import auto_decode, unique_id
import base64, requests, os , re 

# ===============================================================================
#  HTML selectors and attributes used to locate image resources.
# ===============================================================================
selectors = {
    "img": ["src", "srcset", "data-src"],
    "source": ["src", "srcset"],
    "video[poster]": ["poster"],
    "svg": ["data-src", "src"],
    "input[type='image']": ["src"],
    "embed[src]": ["src"],
    "object[data]": ["data"],
    "link[rel~='icon']": ["href"],
    "meta[property='og:image']": ["content"],

    "[data-src], [data-original], [data-lazy], [data-url]":
        ["data-src", "data-original", "data-lazy", "data-url"],
}


# ===============================================================================
#  Scrape image resources from a web page and save them to the specified
#  directory.
#
#  @param Downloader: Downloader used to load and query the web page.
#  @param str: URL of the page to scrape.
#  @param str: Directory where images will be saved.
#  @param list: Allowed image file extensions.
#  @return: Number of successfully saved images.
# ===============================================================================
def scrape_images(downloader: Downloader, url: str, dir: str, extensions: list) -> int:
    """ Scrape all images from the given URL. """
    logger = getLogger(__name__)
    
    # normalize url :
    url = urlUtils.normalize_url(url)
    if not urlUtils.is_valid_url(url):
        logger.error(f"Invalid URL: {url}")
        return []
    
    # load page:
    logger.info(f"[SCRAP_IMAGES] Loading page:  {url}")
    if not downloader.load(url):
        return []

    # scrape images:
    image_save_count = 0
    found_urls = set()
    found_raw  = set()

    try:
        for selector, attrs in selectors.items():
            for el in downloader.query_selector_all(selector): 
                for attr in attrs:
                    val = el.get_attribute(attr)
                    if not val: continue
                    src = urlUtils.full_url(url, val)
                    
                    # base64 image
                    if src.startswith("data:image") and src not in found_raw:
                        found_raw.add(src)
                    
                    # external image
                    if urlUtils.is_valid_url(src) and src not in found_urls:
                        found_urls.add(src)
    except KeyboardInterrupt:
        raise
    except Exception as e:
        logger.error(f"[SCRAP_IMAGES] Error: {e}")

    # save base64 images:
    for img in found_raw:
        if save_raw_image(img, dir, extensions):
            image_save_count += 1
    
    # download and save external images:
    for url in found_urls:
        if save_external_image(url, dir, extensions):
            image_save_count += 1

    return image_save_count


# ===============================================================================
#  Decode and save a Base64 or URL-encoded image.
#
#  @param str: Data URI containing the encoded image.
#  @param str: Directory where the image will be saved.
#  @param list: Allowed image file extensions.
#  @return: True if the image was saved successfully, otherwise False.
# ===============================================================================
def save_raw_image(data: str, dir: str, extensions) -> bool:
    """ Save base64 image. """
    try:
        logger = getLogger(__name__)
        header, raw = data.split(",", 1)

        # get extension:
        header = header.lower().replace("%3b", ";")
        ext_part = header.split("image/")[1]
        ext = re.split(r"[;+\s]", ext_part)[0]
        
        # check extension:
        if not ext or f".{ext}" not in extensions:
            return False 
        
        # file name:
        filename = f"image_{unique_id()}.{ext}"
        filename = re.sub(r"[^a-zA-Z0-9._-]", "_", filename)
        filepath = os.path.join(dir, filename)

        # decode :
        if ";base64" in header:
            data = base64.b64decode(raw)
            mode = "wb"
        else:
            data = auto_decode(raw)
            mode = "w"
        
        # save image:
        with open(filepath, mode, encoding="utf-8" if mode == "w" else None) as f:
            f.write(data)
        logger.info(f"[SCRAP_IMAGES] image [{filename}] saved successfully")
        return True

    except:
        return False

    
# ===============================================================================
#  Download and save an external image from a URL.
#
#  @param str: URL of the image to download.
#  @param str: Directory where the image will be saved.
#  @param list: Allowed image file extensions.
#  @return: True if the image was saved successfully, otherwise False.
# ===============================================================================
def save_external_image(url: str, dir: str, extensions) -> bool:
    """ Download and Save external image. """
    logger = getLogger(__name__)

    # check extension:
    clean_url = clean_url = url.split("?")[0].split("#")[0]
    ext = os.path.splitext(clean_url)[1].lower()
    if not ext or ext not in extensions:
        return False

    # download image:
    try:
        logger.info(f"[SCRAP_IMAGES] Downloading: {url}")
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            logger.error(f"[SCRAP_IMAGES] Error downloading: {url}")
            return False
    except KeyboardInterrupt:
        raise
    except Exception:
        logger.error(f"[SCRAP_IMAGES] Error downloading: {url}")
        return False
    
    # safe name :
    raw_name = os.path.basename(clean_url)
    if not raw_name or "." not in raw_name:
        raw_name = f"file_{unique_id()}{ext}"
    filename = re.sub(r"[^a-zA-Z0-9._-]", "_", raw_name)
    filepath = os.path.join(dir, filename)

    # save image:
    try:
        with open(filepath, "wb") as f:
            f.write(resp.content)
        logger.info(f"[SCRAP_IMAGES] image [{filename}] saved successfully")
        return True
    except:
        return False
