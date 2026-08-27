
from string import hexdigits
from cryptography.fernet import Fernet
from ft_otp.utils.constant import INVALID_KEY, KEY_GENERATION_SUCCESS
from logging import Logger, getLogger

# ===============================================================================
#  Generate an encrypted key from a hexadecimal key.
#  The hexadecimal key is validated, converted to bytes, and encrypted
#  using a newly generated Fernet key.
#
#  @param hex_key: The hexadecimal key to validate and encrypt.
#  @return: The encrypted key containing the Fernet key and encrypted data.
# ===============================================================================
def generate_key(hex_key: str) -> str:
    logger: Logger = getLogger(__name__)

    if len(hex_key) < 64 or not all(c in hexdigits for c in hex_key):
        raise ValueError(INVALID_KEY)

    bytes_key = bytes.fromhex(hex_key)
    encrypted_key = encrypt_key(bytes_key)
    logger.info(KEY_GENERATION_SUCCESS)
    return encrypted_key


# ===============================================================================
#  Encrypt a byte sequence using a newly generated Fernet key.
#  The Fernet key is stored together with the encrypted data.
#
#  @param bytes_key: The key data to encrypt.
#  @return: The Fernet key combined with the encrypted key data.
# ===============================================================================
def encrypt_key(bytes_key: bytes) -> bytes:
    logger: Logger = getLogger(__name__)
    fernet_key = Fernet.generate_key()
    encrypted_key = Fernet(fernet_key).encrypt(bytes_key)
    logger.info("Key encrypted successfully.")
    return fernet_key + encrypted_key


# ===============================================================================
#  Decrypt an encrypted key using the Fernet key stored in the encrypted data.
#
#  @param encrypted_data: The encrypted key data containing the Fernet key.
#  @return: The decrypted key as bytes.
# ===============================================================================
def decrypt_key(encrypted_data: bytes) -> bytes:
    logger: Logger = getLogger(__name__)
    fernet_key = encrypted_data[:44]
    encrypted_key = encrypted_data[44:]
    decrypted_key = Fernet(fernet_key).decrypt(encrypted_key)
    logger.info("Key decrypted successfully.")
    return decrypted_key
