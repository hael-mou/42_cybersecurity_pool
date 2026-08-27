
import pathlib, sys
import time

from logging import getLogger
from ft_otp.cli.formatter import print_otp
from ft_otp.config import DEFAULT_OTP_DIGITS, TIMESTEP
from ft_otp.handlers import key
from ft_otp.handlers.hotp import hotp
from ft_otp.handlers.provisioning import generate_otp_url, generate_qr_code

# ===============================================================================
#  Generate an encrypted key from a hexadecimal key stored in a file
#  and save the resulting encrypted data to the specified path.
#
#  @param file_path: Path to the file containing the hexadecimal key.
#  @param save_path: Path where the generated encrypted key will be saved.
#  @return: The generated encrypted key.
# ===============================================================================
def generate_key_from_file(file_path: str, save_path: str) -> str:
    logger = getLogger(__name__)
    
    try:
        with open(file_path, "r") as file:
            hex_key = file.read().strip()

        encrypted_data = key.generate_key(hex_key)
        save_path = pathlib.Path(save_path).resolve()
        with open(save_path, "wb") as file:
            file.write(encrypted_data)

        logger.info(f"Key was successfully saved in {save_path}.")


    except FileNotFoundError:
        logger.error(f"[generate_key_from_file] - File not found: {file_path}")
        sys.exit(1)

    except Exception as e:
        logger.error(f"[generate_key_from_file] - {e}")
        sys.exit(1)


# ===============================================================================
#  Load an encrypted key from a file, decrypt it, and return
#  the resulting secret key.
#
#  @param key_path: Path to the encrypted key file.
#  @return: The decrypted secret key as bytes.
# ===============================================================================
def get_key(key_path: str) -> bytes:
    logger = getLogger(__name__)

    try:
        logger.info(f"Loading key: {key_path}")

        path = pathlib.Path.cwd().joinpath(key_path)
        with open(path, "rb") as f:
            data = f.read()
        
        logger.info("Key loaded successfully.")
        secret = key.decrypt_key(data)

    except Exception as e:
        logger.error(f"Failed to load key file: {e}")
        sys.exit(1)
    
    return secret


# ===============================================================================
#  Continuously generate a digit OTP based on the current time
#  and display the remaining validity time until the OTP expires.
#
#  @param key_path: Path to the encrypted key file used to generate the OTP.
#  @return: None. The generated OTP is continuously displayed in the terminal.
# ===============================================================================
def generate_totp_digits(
    key_path: str,
    digits: int = DEFAULT_OTP_DIGITS
) -> None:
    secret = get_key(key_path)
    while True:
        counter = int(time.time()) // TIMESTEP
        remaining = TIMESTEP - (int(time.time()) % TIMESTEP)
        otp = hotp(secret, counter, digits)
        print_otp(otp, remaining)
        time.sleep(1)


# ===============================================================================
#  Generate a QR code image containing the OTP authentication URL
#  for the specified account and issuer.
#
#  @param key_path: Path to the encrypted key file.
#  @param save_path: Path where the generated QR code image will be saved.
#  @param account: Account identifier associated with the OTP.
#  @param issuer: Name of the service or issuer associated with the OTP.
#  @return: None. The generated QR code is saved to the specified path.
# ===============================================================================
def generate_qrcode_image(key_path: str, save_path: str,  account: str , issuer: str) -> None:
    logger = getLogger(__name__)
    secret = get_key(key_path)

    try:
        url = generate_otp_url(secret, account, issuer)
        generate_qr_code(url, save_path)

    except Exception as e:
        logger.error(f"Failed to generate qrcode: {e}")
