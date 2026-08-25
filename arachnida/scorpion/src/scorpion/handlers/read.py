
import piexif

from pathlib import Path
from humanize import naturalsize
from time import ctime
from stat import filemode
from PIL import ImageFile
from scorpion.utils.constant import SECTIONS
from scorpion.utils.decode import decode_exif_value

# ===============================================================================
#  Read file information from an image path.
#
#  @param path: Image file path.
#  @return: File information.
# ===============================================================================
def file_info_reader(path: Path) -> dict[str, str]:
    data = {}
    data["File Name"] = path.name
    data["Directory"] = str(path.parent.resolve())
    data["File Size"] = naturalsize(path.stat().st_size, binary=True)
    data["Creation Date"] = ctime(path.stat().st_ctime)
    data["Modification Date"] = ctime(path.stat().st_mtime)
    data["Permissions"] = filemode(path.stat().st_mode)
    return data


# ===============================================================================
#  Read image information.
#
#  @param image: Opened image.
#  @return: Image information.
# ===============================================================================
def image_info_reader(image: ImageFile) -> dict[str, str]:
    data = {}
    data["Format"] = image.format
    data["Mode"]   = image.mode
    data["Width"]  = image.width
    data["Height"] = image.height
    return data


# ===============================================================================
#  Read EXIF metadata from an image.
#
#  @param image: Opened image.
#  @return: EXIF metadata grouped by section.
# ===============================================================================
def exif_reader(image: ImageFile) -> dict[str, dict[str, str]]:
    data = {}
    exif_bytes = image.info.get("exif")
    
    if not exif_bytes: return {}

    exif_dict  = piexif.load(exif_bytes)
    for ifd_name, ifd_data in exif_dict.items():
        if not ifd_data or not isinstance(ifd_data, dict) :
            continue
        tmp = {}
        for tag_id, value in ifd_data.items():
            tag_name = piexif.TAGS[ifd_name][tag_id]["name"]
            tag_type = piexif.TAGS[ifd_name][tag_id]["type"]
            value    = decode_exif_value(value, tag_type)
            tmp[tag_name] = value
        data[SECTIONS.get(ifd_name, ifd_name)] = tmp
    return data
