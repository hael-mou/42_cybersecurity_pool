import hashlib
import hmac

# ===============================================================================
#  Generate a time-independent One-Time Password (HOTP) using
#  the HMAC-based One-Time Password algorithm.
#
#  @param secret: The secret key used to generate the OTP.
#  @param counter: The counter value used for OTP generation.
#  @param digits: The number of digits in the generated OTP.
#  @return: The generated HOTP as a zero-padded string.
# ===============================================================================
def hotp(secret: bytes, counter: int, digits: int = 6) -> str:
    counter_bytes = counter.to_bytes(8, "big")
    hmac_hash = hmac.new(secret, counter_bytes, hashlib.sha1).digest()
    
    offset = hmac_hash[-1] & 0x0F
    truncated = (
        ((hmac_hash[offset] & 0x7f) << 24) |
        (hmac_hash[offset + 1] << 16) |
        (hmac_hash[offset + 2] << 8) |
        hmac_hash[offset + 3]
    )
    otp = truncated % (10 ** digits)
    return str(otp).zfill(digits)
