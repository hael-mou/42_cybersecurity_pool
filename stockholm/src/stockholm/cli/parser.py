
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
        description="A secure file encryption and decryption tool",
        formatter_class=RichHelpFormatter
    ) 

    parser.add_argument(
        "-r",
        "--reverse",
        metavar="KEY",
        help="Reverse the operation using the specified key"
    )

    parser.add_argument(
        "-s",
        "--silent",
        action="store_true",
        help="Do not produce any output"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {version('stockholm')}"
    )

    return parser.parse_args()
