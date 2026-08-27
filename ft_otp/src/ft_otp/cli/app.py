
from ft_otp.utils.logger import Logger, setup_logger
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

        if args.generate:
            cmd.generate_key_from_file(
                args.generate,
                args.key_output
            )
        
        if args.qrcode:
            cmd.generate_qrcode_image(
                args.qrcode,
                args.qr_output,
                args.account,
                args.issuer
            )

        if args.key:
            cmd.generate_totp_digits(args.key)


    except KeyboardInterrupt:
        print("", flush=True)
        logger.warning("Program interrupted by user. Bye !\n")

    except Exception as e:
        logger.error(f"- {e}")
