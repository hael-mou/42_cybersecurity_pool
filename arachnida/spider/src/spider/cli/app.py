
from .formatter import print_Flag
from .parser import Args, parse_args
from .commands import scrape_images
from spider.logger import Logger, setup_logger

# ===============================================================================
#  Main Function :
# ===============================================================================
def main() -> None :
    try:
        print_Flag()
        logger : Logger  = setup_logger()
        args   : Args    = parse_args()
        depth  : int     = args.level if args.recursive else 0
        scrape_images(args.url, args.path,logger, depth)
        
    except KeyboardInterrupt:
        logger.warning("Program interrupted by user. Bye !\n")
    except Exception as e:
        logger.error(f"- {e}")