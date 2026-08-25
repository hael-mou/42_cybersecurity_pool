
from scorpion.config import TERMINAL_COLORS as C
from importlib.metadata import version

# ===============================================================================
# CONSTENT :
# ===============================================================================
HEADER = f'''
███████  ██████  ██████  ██████  ██████  ██  ██████  ███    ██ 
██      ██      ██    ██ ██   ██ ██   ██ ██ ██    ██ ████   ██ 
███████ ██      ██    ██ ██████  ██████  ██ ██    ██ ██ ██  ██ 
     ██ ██      ██    ██ ██   ██ ██      ██ ██    ██ ██  ██ ██ 
███████  ██████  ██████  ██   ██ ██      ██  ██████  ██   ████               
=====================================================================
By: @hael-mou / v: {version("scorpion")}
Warning: just for Education purposes only !!
=====================================================================
'''

# ===============================================================================
#  Display the Spider application banner.
#
#  @return: None.
# ===============================================================================
def print_Flag() -> None:
    print(f"{ C['INFO'] + HEADER + C['RESET'] }")


# ===============================================================================
#  Display a formatted section header.
#
#  @param title: Header title.
#  @return: None.
# ===============================================================================
def print_header(title: str) -> None:
    print("=" * 3, title, "=" * 60)


# ===============================================================================
#  Display formatted image metadata.
#
#  @param data: Metadata grouped by section.
#  @return: None.
# ===============================================================================
def print_metadata(data: dict[str, dict[str, str]]) -> None:
    for section_name, section_data in data.items():
        print(f"* {section_name}:")
        for key, value in section_data.items():
            print(f"{' ' * 4}- {key:25}: {value}")
        print("")
