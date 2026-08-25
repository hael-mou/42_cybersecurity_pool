
from pathlib import Path
from logging import getLogger, Logger
from PIL import Image

from scorpion.handlers import read as r
from scorpion.handlers import write as w
from scorpion.utils import file as uf
from . import formatter as f

# ===============================================================================
#  Display image metadata.
#
#  @param images: List of image paths.
#  @return: None.
# ===============================================================================

def display_metadata(images: list[Path]) -> None :
    logger: Logger = getLogger(__name__)
    i = 0

    for imagePath in images:
        logger.info(f"[DISPLAY] - [{(i:=i+1)}/{len(images)}] : {imagePath}")
        logger.info(f"[DISPLAY] - Reading metadata: '{imagePath}'")
        try:
            with Image.open(imagePath) as image:
                f.print_header(f"Metadata for image: {imagePath.name}:")
                file_info = r.file_info_reader(imagePath)
                imag_info = r.image_info_reader(image)
                exif_info = r.exif_reader(image)
                f.print_metadata({
                    "File information": {**file_info, **imag_info },
                    **exif_info
                })
                if not exif_info:
                    print("* No EXIF data found.")

        except FileNotFoundError:
            logger.error(f"[DISPLAY] - [{imagePath}] : file not found")
        
        except Exception as e:
            logger.warning(f"[DISPLAY] - Error reading metadata: '{imagePath}': {e}")

        logger.info(f"[SHOW INFO] - Done !\n")


# ===============================================================================
#  Delete all image metadata.
#
#  @param images: List of image paths.
#  @return: None.
# ===============================================================================
def delete_all_metadata(images: list[Path]) -> None:
    logger: Logger = getLogger(__name__)
    i = 0

    for imagePath in images:
       logger.info(f"[DELETE_META] - [{(i:=i+1)}/{len(images)}] : {imagePath}")
       logger.info(f"[DELETE_META] - Removing all metadata: '{imagePath}'")
       try:
           with Image.open(imagePath) as image:
               f.print_header(f"Removing all metadata: {imagePath}")
               clean_image = w.remove_exif(image)
               newPath = uf.get_clean_path(imagePath)
               clean_image.save(newPath)
               print(f"All metadata removed → '{newPath}'\n")

       except FileNotFoundError:
           logger.error(f"[DELETE_META] - [{imagePath}] : file not found")
       except Exception as e:
           logger.warning(f"[DELETE_META] - Error reading metadata: '{imagePath}': {e}")

       logger.info(f"[DELETE_META] - Done !\n")
