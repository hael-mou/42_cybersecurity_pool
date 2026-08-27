
from ft_otp.config import TERMINAL_COLORS as C
from importlib.metadata import version

# ===============================================================================
# CONSTENT :
# ===============================================================================
HEADER = f'''
                                                           
███████╗████████╗      █████╗ ████████╗██████╗
██╔════╝╚══██╔══╝     ██╔══██╗╚══██╔══╝██╔══██╗
█████╗     ██║        ██║  ██║   ██║   ██████╔╝
██╔══╝     ██║        ██║  ██║   ██║   ██╔═══╝
██║        ██║ ██████╗ █████╔╝   ██║   ██║
╚═╝        ╚═╝ ╚═════╝ ╚════╝    ╚═╝   ╚═╝
=====================================================
By: @hael-mou / v: {version("ft_otp")}
=====================================================
'''

# ===============================================================================
#  Display the Spider application banner.
#
#  @return: None.
# ===============================================================================
def print_Flag() -> None:
    print(f"{ C['INFO'] + HEADER + C['RESET'] }")


# ===============================================================================
#  Display the generated OTP and the remaining time before it expires
#  on the same line in the terminal.
#
#  @param otp: The one-time password to display.
#  @param remaining: The number of seconds remaining before the OTP expires.
#  @return: None.
# ===============================================================================
def print_otp(otp: str, remaining) -> None:
    print(f"\rOTP: {otp} | Expires in: {remaining:02d}s", end="", flush=True)