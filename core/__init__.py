from flask import Flask

from .extensions import db, owm
from .routes import api


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py", silent=True)

    register_blueprints(app)
    register_extesions(app)

    return app


def register_extesions(app: Flask):
    db.init_app(app)
    owm.init_app(app)


def register_blueprints(app: Flask):
    app.register_blueprint(api, url_prefix="/api")
