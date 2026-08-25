
from PIL import Image
from scorpion.handlers import read as r

# ===============================================================================
#  Read metadata from an uploaded image.
#
#  @param upload: Uploaded image file.
#  @return: Image metadata grouped by section.
# ===============================================================================
def read_image_metadata(upload) -> dict[str, dict[str, str]]:
    with Image.open(upload.stream) as image:
        return  {
            "file_info": {
                "Filename": upload.filename,
                **r.image_info_reader(image),
            },
            "exif": r.exif_reader(image),
        }
