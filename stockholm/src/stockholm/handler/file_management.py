
from pathlib import Path

# ===============================================================================
#  Find files with matching extensions recursively.
#
#  @param directory: Directory to search.
#  @param exts: File extensions to match.
#  @param recurse: Whether to search subdirectories.
#  @return: Matching files and warnings.
# ===============================================================================
def find_files( directory: Path, exts: list[str], recurse: bool = True,
        )-> tuple[list[Path], list[str]]:

    if not directory.is_dir():
        raise NotADirectoryError(f"Directory does not exist: {directory}")

    files    : list[Path] = []
    warnings : list[str]  = []

    try:
        entries = directory.iterdir()

    except PermissionError as exc:
        warnings.append(f"Permission denied, skipping: {directory}")
        return files, warnings
    except OSError as exc:
        warnings.append(f"Unable to read '{directory}': {exc}")
        return files, warnings
    
    for entry in entries:
        try:
            if entry.is_file() and entry.suffix in exts:
                files.append(entry)
            elif recurse and entry.is_dir():
                child_files, child_warnings = find_files(entry, exts, recurse) or []
                files.extend(child_files)
                warnings.extend(child_warnings)

        except OSError as exc:
            warnings.append(f"Unable to access '{entry}': {exc}")

    return files, warnings
