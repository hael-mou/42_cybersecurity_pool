
from urllib.parse import quote, urljoin, urlparse, urlunparse

# ===============================================================================
#  Normalize a URL by cleaning whitespace, encoding its components, and ensuring
#  a valid scheme and network location.
#
#  @param str: URL to normalize.
#  @return: The normalized URL.
# ===============================================================================
def normalize_url(url: str) -> str:

    url = url.strip()

    if url.startswith("data:"):
        return url

    parsed   = urlparse(url)
    scheme   = parsed.scheme or "http"
    netloc   = parsed.netloc or parsed.path
    path     = quote(parsed.path if parsed.netloc else "", safe="/:@&?=#,+-_.!~*'()")
    query    = quote(parsed.query, safe="=&")
    fragment = quote(parsed.fragment, safe="")

    return urlunparse((scheme, netloc, path, "", query, fragment))


# ===============================================================================
#  Check whether a URL contains a valid scheme and network location.
#
#  @param str: URL to validate.
#  @return: True if the URL is valid, otherwise False.
# ===============================================================================
def is_valid_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
        return bool(parsed.scheme and parsed.netloc)
    except:
        return False


# ===============================================================================
#  Build a complete URL from a base URL and a relative or absolute path.
#
#  @param str: Base URL.
#  @param str: Relative or absolute path.
#  @return: The complete URL.
# ===============================================================================
def full_url(base_url: str, path: str = "") -> str:
    base_url = normalize_url(base_url)
    path = quote(path, safe="/:@&?=#,+-_.!~*'()")

    if path.startswith("data:"):
        return path

    if urlparse(path).scheme:
        return path

    if not urlparse(base_url).path.endswith('/'):
        base_url += '/'

    return urljoin(base_url, path)


# ===============================================================================
#  Check whether two URLs belong to the same domain.
#
#  The "www." prefix is ignored when comparing domains.
#
#  @param str: First URL.
#  @param str: Second URL.
#  @return: True if both URLs belong to the same domain, otherwise False.
# ===============================================================================
def is_same_domain(first_url: str, second_url: str) -> bool: 
    first_url  = urlparse(normalize_url(first_url)).netloc
    second_url = urlparse(normalize_url(second_url)).netloc

    first_url  = first_url.replace("www.", "")
    second_url = second_url.replace("www.", "")

    return first_url == second_url
