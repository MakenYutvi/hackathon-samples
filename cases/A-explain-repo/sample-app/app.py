"""Feature Board API entry point."""
from flask import Flask

from config import Config
from routes import features_bp, users_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(users_bp)
    app.register_blueprint(features_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
