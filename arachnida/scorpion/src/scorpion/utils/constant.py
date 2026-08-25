
# ===============================================================================
#  Map EXIF sections to readable names.
# ===============================================================================
SECTIONS : dict = {
    "0th"  : "Main image metadata",
    "Exif" : "Exif metadata",
    "GPS"  : "GPS metadata",
    "Interop" : "Interop metadata",
    "1st"  : "Thumbnail image metadata",
    "thumbnail" : "Thumbnail image metadata"
}

# ===============================================================================
#  Map EXIF type IDs to readable names.
# ===============================================================================
TYPES = {
    1: "BYTE",
    2: "ASCII",
    3: "SHORT",
    4: "LONG",
    5: "RATIONAL",
    6: "SBYTE",
    7: "UNDEFINED",
    8: "SSHORT",
    9: "SLONG",
    10: "SRATIONAL",
    11: "FLOAT",
    12: "DOUBLE",
}
