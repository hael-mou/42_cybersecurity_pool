
import pathlib

from argparse import Namespace as Args
from argparse import ArgumentParser as Parser
from rich_argparse import RichHelpFormatter
from importlib.metadata import version

# ===============================================================================
#  Parse command-line arguments.
#
#  @return: Parsed command-line arguments.
# ===============================================================================
def parse_args() -> Args:
    parser: Parser = Parser(
        description="Scorpion — View and modify image EXIF metadata.",
        formatter_class=RichHelpFormatter
    )
    parser.add_argument(
        "images",
        type = pathlib.Path,
        nargs = '+',
        help = "Path to the image file."
    )

    parser.add_argument(
        "-d",
        "--delete",
        action="store_true",
        default=False,
        help="Delete all EXIF metadata"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {version("scorpion")}"
    )
    
    args = parser.parse_args()
    args.images = list(dict.fromkeys(args.images))

    return args
