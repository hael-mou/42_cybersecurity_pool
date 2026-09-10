
from pathlib import Path
from cryptography.fernet import Fernet

# ===============================================================================
#  decrypt a file using its encryption key.
#
#  @param file_path: File to decrypt.
#  @param file_key: Decryption key.
#  @return: Path to the decrypted file.
# ===============================================================================
def decrypt_file(file_path: Path, file_key: bytes) -> str:
    with file_path.open("rb") as file_handle:
        encrypted_data = file_handle.read()

    decrypted_data = decrypt_data(file_key, encrypted_data)

    output_path = file_path.with_name(
        f"{file_path.stem}"
    )

    with output_path.open("wb") as file_handle:
        file_handle.write(decrypted_data)

    return output_path


# ===============================================================================
#  Decrypt data using Fernet.
#
#  @param key: Decryption key.
#  @param data: Data to decrypt.
#  @return: Decrypted data.
# ===============================================================================
def decrypt_data(key: bytes, data: bytes) -> bytes:
    return Fernet(key).decrypt(data)