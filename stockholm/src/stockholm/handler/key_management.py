
import xattr

from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from stockholm.config import ENCRYPTED_KEY_ATTRIBUTE


# ===============================================================================
#  Load an wapping public key from a  file.
#
#  @param path: Path to the public key.
#  @return: public key.
# ===============================================================================
def load_wrapping_public_key(path: str) -> rsa.RSAPublicKey:
    key_path = Path(path)

    if not key_path.is_file():
        raise FileNotFoundError(f"RSA public key not found in: {key_path}")

    try:
        with key_path.open("rb") as file:
            key = serialization.load_pem_public_key(file.read())

    except (ValueError, TypeError) as exc:
        raise ValueError(f"Invalid RSA public key: {key_path}") from exc

    if not isinstance(key, rsa.RSAPublicKey):
        raise TypeError(f"The key is not an RSA public key: {key_path}")

    return key


# ===============================================================================
# Load an wapping private key from a  file.
#
#  @param path: Path to the private key.
#  @return: private key.
# ===============================================================================
def load_wrapping_private_key(path: str) -> rsa.RSAPrivateKey:
    key_path = Path(path)

    if not key_path.is_file():
        raise FileNotFoundError(f"RSA private key not found in: {key_path}")

    try:
        with key_path.open("rb") as file:
            key = serialization.load_pem_private_key(file.read(), password=None)

    except (ValueError, TypeError) as exc:
        raise ValueError(f"Invalid RSA private key: {key_path}") from exc

    if not isinstance(key, rsa.RSAPrivateKey):
        raise TypeError(f"The key is not an RSA private key: {key_path}")

    return key



# ===============================================================================
#  Generate a file encryption key.
#
#  @return: Generated encryption key.
# ===============================================================================
def create_file_encryption_key() -> bytes:
    return Fernet.generate_key()


# ===============================================================================
#  Encrypt an encryption key with an RSA public key.
#
#  @param public_key: RSA public key.
#  @param encryption_key: Key to encrypt.
#  @return: Encrypted encryption key.
# ===============================================================================
def encrypt_key(public_key: rsa.RSAPublicKey, encryption_key: bytes) -> bytes:
    return public_key.encrypt(
        encryption_key,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


# ===============================================================================
# Decrypt an encrypted key with an RSA private key.
#
#  @param private_key: RSA private key.
#  @param encrypted_key: Key to decrypt.
#  @return: Decrypted encryption key.
# ===============================================================================
def decrypt_key(private_key: rsa.RSAPrivateKey, encrypted_key: bytes) -> bytes:
    return private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


# ===============================================================================
#  Store an encrypted key as a file extended attribute.
#
#  @param file_path: File to store the key on.
#  @param encrypted_key: Encrypted key to store.
#  @return: None.
# ===============================================================================
def store_encrypted_key(file_path: Path, encrypted_key: bytes) -> None:
    xattr.setxattr(
        str(file_path),
        ENCRYPTED_KEY_ATTRIBUTE,
        encrypted_key,
    )


# ===============================================================================
#  Retrieve an encrypted key from a file extended attribute.
#
#  @param file_path: File containing the key.
#  @return: Encrypted key.
# ===============================================================================
def retrieve_encrypted_key(file_path: Path) -> bytes:
    return xattr.getxattr(
        str(file_path),
        ENCRYPTED_KEY_ATTRIBUTE,
    )
