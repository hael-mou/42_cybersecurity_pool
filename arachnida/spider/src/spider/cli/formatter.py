
from spider.config import TERMINAL_COLORS as C
from importlib.metadata import version

# ===============================================================================
# CONSTENT :
# ===============================================================================
HEADER = f'''
███████ ██████  ██ ██████  ███████ ██████
██      ██   ██ ██ ██   ██ ██      ██   ██
███████ ██████  ██ ██   ██ █████   ██████
     ██ ██      ██ ██   ██ ██      ██   ██
███████ ██      ██ ██████  ███████ ██   ██
===================================================
By: @hael-mou / v: {version("spider")}
Warning: just for Education purposes only !!
===================================================
'''


# ===============================================================================
#  Display the Spider application banner.
#
#  @return: None.
# ===============================================================================
def print_Flag() -> None:
    print(f"{ C['INFO'] + HEADER + C['RESET'] }")


# ===============================================================================
#  Display the scraping results in the terminal.
#
#  @param total_imgs: Total number of images downloaded.
#  @param directory: Directory where the downloaded images were saved.
#  @return: None.
# ===============================================================================
def print_Results(total_imgs: int, directory: str) -> None:
    print(
        f"{C['INFO']}images downloaded: "
        f"{C['WARNING']}{total_imgs} "
        f"{C['INFO']}images{C['RESET']}\n"
        f"{C['INFO']}images saved in: "
        f"{C['WARNING']}{directory}"
        f"{C['RESET']}"
    )
