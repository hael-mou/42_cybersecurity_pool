
from flask import Flask

from scorpion.config import HOST, PORT
from .routes import web_bp

# ===============================================================================
#  Create and configure the Flask application.
#
#  @return: Configured Flask application.
# ===============================================================================
def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )
    app.register_blueprint(web_bp)
    return app


# ===============================================================================
#  Start the Flask application.
#
#  @return: None.
# ===============================================================================
def main() -> None:
    app = create_app()
    app.run(
        host=HOST,
        port=PORT,
        debug=True,
    )
    