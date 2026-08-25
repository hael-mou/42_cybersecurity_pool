
from scorpion.utils.logger import Logger, setup_logger
from .parser import Args, parse_args
from .formatter import print_Flag
from . import commands as cmd

# ===============================================================================
#  Main Function :
# ===============================================================================
def main() -> None :
    try:
        print_Flag()
        logger : Logger  = setup_logger()
        args    : Args   = parse_args()
        
        if args.delete:
            cmd.delete_all_metadata(args.images)
            return
    
        cmd.display_metadata(args.images)

    except KeyboardInterrupt:
        logger.warning("Program interrupted by user. Bye !\n")

    except Exception as e:
        logger.error(f"- {e}")
