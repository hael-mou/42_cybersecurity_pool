
from argparse import Namespace as Args
from argparse import ArgumentParser as Parser
from rich_argparse import RichHelpFormatter
from importlib.metadata import version
from spider.config import DEFAULT_DEPTH, DOWNLOAD_FOLDER

# ===============================================================================
#  Parse command-line arguments.
#
#  @return: Parsed command-line arguments.
# ===============================================================================
def parse_args() -> Args:
    parser: Parser = Parser(
        description="Spider - A tool to scrape data from a website.",
        formatter_class=RichHelpFormatter
    )

    parser.add_argument(
        "url",
        type=str,
        help="The URL of the website to crawl and extract images from."
    )

    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Enable recursive crawling of the website (same domain only)."
    )

    parser.add_argument(
        "-l",
        "--level",
        type=int,
        default=DEFAULT_DEPTH,
        help=f"Maximum depth level for recursive crawling (default: {DEFAULT_DEPTH})."
            "Only effective with -r."
    )

    parser.add_argument(
        "-p",
        "--path",
        type=str,
        default=DOWNLOAD_FOLDER,
        help=f"Path where downloaded images will be saved (default: {DOWNLOAD_FOLDER})."
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {version("spider")}"
    )

    return parser.parse_args()
