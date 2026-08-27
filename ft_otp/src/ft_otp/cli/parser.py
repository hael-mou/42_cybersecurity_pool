
import sys

from argparse import Namespace as Args
from argparse import ArgumentParser as Parser
from rich_argparse import RichHelpFormatter
from importlib.metadata import version
from ft_otp import config as C


# ===============================================================================
#  Parse command-line arguments.
#
#  @return: Parsed command-line arguments.
# ===============================================================================
def parse_args() -> Args:
    parser: Parser = Parser(
        description="A one-time password (OTP) generator",
        formatter_class=RichHelpFormatter
    )

    parser.add_argument(
        "-g",
        "--generate",
        nargs="?",
        const=C.DEFAULT_HEX_KEY_FILE,
        default=None,
        metavar="HEX_KEY",
        help=f"Generate an encrypted key from a hex key file. Default: {C.DEFAULT_HEX_KEY_FILE}"
    )

    parser.add_argument(
        "--key-output",
        default=C.DEFAULT_KEY_OUTPUT,
        dest="key_output",
        metavar="KEY_FILE",
        help=f"Output encrypted key file. Default: {C.DEFAULT_KEY_OUTPUT}"
    )

    parser.add_argument(
        "-q",
        "--qrcode",
        nargs="?",
        const=C.DEFAULT_KEY_FILE,
        default=None,
        metavar="KEY_FILE",
        help=f"Generate a QR code from a key file. Default: {C.DEFAULT_KEY_FILE}"
    )

    parser.add_argument(
        "--issuer",
        default=C.DEFAULT_ISSUER,
        metavar="NAME",
        help=f"Service or application name. Default: {C.DEFAULT_ISSUER}"
    )

    parser.add_argument(
        "--account",
        default=C.DEFAULT_ACCOUNT,
        metavar="ACCOUNT",
        help=f"Account name. Default: {C.DEFAULT_ACCOUNT}"
    )

    parser.add_argument(
        "--qr-output",
        default=C.DEFAULT_QR_OUTPUT,
        dest="qr_output",
        metavar="IMAGE",
        help=f"Output QR code image. Default: {C.DEFAULT_QR_OUTPUT}"
    )

    parser.add_argument(
        "-k",
        "--key",
        nargs="?",
        const=C.DEFAULT_KEY_FILE,
        default=None,
        metavar="KEY_FILE",
        help=f"Generate a 6-digit OTP from a key file. Default: {C.DEFAULT_KEY_FILE}"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {version('ft_otp')}"
    )

    if len(sys.argv) == 1:
        parser.print_help()
        parser.exit(1)

    return parser.parse_args()
