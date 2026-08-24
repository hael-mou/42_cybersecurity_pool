
import time
import uuid
from urllib.parse import unquote

# ===============================================================================
#  Generate a unique identifier based on the current timestamp
#  and a short random UUID segment.
#
#  @return: An identifier in the format: "<timestamp>_<random_hex>"
# ===============================================================================
def unique_id() -> str:
    return f"{int(time.time() * 1000)}_{uuid.uuid4().hex[:6]}"


# ===============================================================================
#  Decode a URL-encoded string.
#
#  @param str: URL-encoded string.
#  @retrun: The decoded string
# ===============================================================================
def auto_decode(s: str) -> str:
    if "%25" in s.lower():
        return unquote(unquote(s))
    else:
        return unquote(s)
