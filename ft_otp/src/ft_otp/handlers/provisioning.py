
import pathlib, qrcode
import base64

from email.utils import quote
from logging import getLogger
from ft_otp.config import TIMESTEP

# ===============================================================================
#  Generate an OTP authentication URL using the provided secret key,
#  account, issuer, and TOTP configuration parameters.
#
#  @param key: The secret key used to generate the OTP URL.
#  @param account: The account identifier associated with the OTP.
#  @param issuer: The name of the service or issuer associated with the OTP.
#  @return: The generated OTP authentication URL.
# ===============================================================================
def generate_otp_url(key: bytes, account: str ="None" , issuer: str = "None") -> str:
    logger      = getLogger(__name__)
    secret_b32  = base64.b32encode(key).decode()
    issuer      = quote(issuer)
    account     = quote(account)
    logger.info("OTP URL generated successfully.")
    return (
        f"otpauth://totp/{issuer}:{account}"
        f"?secret={secret_b32}"
        f"&issuer={issuer}"
        f"&algorithm=SHA1"
        f"&digits=6"
        f"&period={TIMESTEP}"
    )


# ===============================================================================
#  Generate a QR code image from an OTP authentication URL
#  and save it to the specified path.
#
#  @param otp_url: The OTP authentication URL to encode in the QR code.
#  @param save_path: The path where the QR code image will be saved.
#  @return: None.
# ===============================================================================
def generate_qr_code(otp_url: str, save_path: str) -> None:
    logger  = getLogger(__name__)
    img     = qrcode.make(otp_url)
    path    = pathlib.Path.cwd().joinpath(save_path)
    logger.info(f"QR code generated successfully and saved as {path}.")
    img.save(path)
