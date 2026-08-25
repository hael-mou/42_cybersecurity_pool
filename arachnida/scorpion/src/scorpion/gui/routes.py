
from flask import Blueprint, render_template, request
from .services import read_image_metadata

# ===============================================================================
#  blue print :
# ===============================================================================
web_bp = Blueprint("gui", __name__)


# ===============================================================================
#  the main page :
# ===============================================================================
@web_bp.route("/", methods=["GET", "POST"])
def index():
    metadata = None
    filename = None
    error = None

    if request.method == "POST":
        image = request.files.get("image")

        if image is None or image.filename == "":
            error = "Please select an image."
        else:
            try:
                filename = image.filename
                metadata = read_image_metadata(image)

            except Exception as exc:
                error = str(exc)

    return render_template(
        "index.html",
        metadata=metadata,
        filename=filename,
        error=error,
    )
