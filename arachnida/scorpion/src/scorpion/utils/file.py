
from pathlib import Path

# ===============================================================================
#  Generate a unique path for a cleaned image.
#
#  @param file: Original image path.
#  @return: Unique cleaned image path.
# ===============================================================================
def get_clean_path(file: Path) -> Path:
    path = file.with_stem(f"{file.stem}_clean")

    counter = 1
    while path.exists():
        path = file.with_stem(f"{file.stem}_clean_{counter}")
        counter += 1

    return path