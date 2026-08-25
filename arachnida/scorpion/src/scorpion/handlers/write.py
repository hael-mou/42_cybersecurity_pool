
from PIL import Image, ImageFile

# ===============================================================================
#  Remove EXIF metadata from an image.
#
#  @param img: Opened image.
#  @return: Clean image without EXIF metadata.
# ===============================================================================
def remove_exif(img : ImageFile) -> ImageFile:
    clean = Image.new(img.mode, img.size)
    clean = Image.new(img.mode, img.size)
    clean.putdata(list(img.getdata()))  
    return clean