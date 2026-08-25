
import binascii
from .constant import TYPES

# ===============================================================================
#  Decode an EXIF value into a readable string.
#
#  @param value: EXIF value.
#  @param type_id: EXIF type ID.
#  @return: Decoded EXIF value.
# ===============================================================================
def decode_exif_value(value, type_id) -> str:
    type_name = TYPES.get(type_id, "UNKNOWN")
    try:
        if type_name == "ASCII" and isinstance(value, bytes):
            return value.decode("utf-8", errors="replace")
        elif type_name in ("RATIONAL", "SRATIONAL") and isinstance(value, tuple) and len(value) == 2:
            num, denom = value
            return str(round(num / denom, 6)) if denom != 0 else "0"
        elif isinstance(value, bytes):
            preview = binascii.hexlify(value[:8]).decode("ascii") 
            return f"{preview}... (total {len(value)} bytes)"
        else:
            return str(value)
    except Exception:
        return str(value)
