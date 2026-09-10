
from pathlib import Path
from cryptography.fernet import Fernet
from stockholm.config import ENCRYPTED_EXTENSION

# ===============================================================================
#  Encrypt a file and store its encrypted key.
#
#  @param file_path: File to encrypt.
#  @param file_key: Encryption key.
#  @return: Path to the encrypted file.
# ===============================================================================
def encrypt_file(file_path: Path, file_key: bytes) -> str:

    with file_path.open("rb") as file_handle:
        file_data = file_handle.read()

    encrypted_data = encrypt_data(file_key, file_data)

    output_path = file_path.with_name(
        f"{file_path.name}{ENCRYPTED_EXTENSION}"
    )

    with output_path.open("wb") as file_handle:
        file_handle.write(encrypted_data)

    return output_path


# ===============================================================================
#  Encrypt data using Fernet.
#
#  @param key: Encryption key.
#  @param data: Data to encrypt.
#  @return: Encrypted data.
# ===============================================================================
def encrypt_data(key: bytes, data: bytes) -> bytes:
    return Fernet(key).encrypt(data)
