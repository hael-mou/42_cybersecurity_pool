
import logging

from stockholm.utils.logger import Logger, setup_logger
from .parser import Args, parse_args
from .formatter import print_Flag
from . import commands as cmd
from stockholm import config

# ===============================================================================
#  Main Function :
# ===============================================================================
def main() -> None :
    logger : Logger = logging.getLogger(__name__)

    try:
        args: Args = parse_args()

        if not args.silent:
            print_Flag()

        if args.silent:
            config.LOG_ENABLE_STDOUT = False

        setup_logger(config)

        if args.reverse:
            cmd.run_reverse(args.reverse)
        else:        
            cmd.run_infection()

    except KeyboardInterrupt:
        print("", flush=True)
        logger.warning("Program interrupted by user. Bye !\n")

    except Exception as e:
        logger.error(f"- {e}")
