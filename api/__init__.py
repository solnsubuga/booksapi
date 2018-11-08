"""module for initialising app"""

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config

from flask_restplus import Api


# create a database instance
db = SQLAlchemy()

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api/v1')

api = Api(api_blueprint)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    import api.views

    app.register_blueprint(api_blueprint)
    # initialise migrations
    Migrate(app, db)

    return app
