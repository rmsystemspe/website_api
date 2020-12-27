from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from app.db import db
from app.api.v1.prospects.resources import api_prospect_v1
from app.ext import ma, migrate, mail


def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)
    CORS(app)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    Api(app, catch_all_404s=True)

    app.url_map.strict_slashes = False
    app.register_blueprint(api_prospect_v1)

    return app
