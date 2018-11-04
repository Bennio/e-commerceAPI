import os

from flask_restful import Api
from flask import Flask, Blueprint
from flask_mail import Mail
from api.database import db
import logging


app = Flask(__name__)
api = Api()
app.config.from_object('api.config.Config')
mail = Mail()
# api.database.init(app)

# config.configure_logging_relative('logging.ini')

logging.basicConfig(filename="ecommerce.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

logger.info("Registering resources")


def configure_app(flask_app):
    flask_app.config.from_object(os.environ['APP_SETTINGS'])


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)
    mail.init_app(flask_app)
    return flask_app


def main():
    initialize_app(app)
    logger.info('>>>>> Starting development server at http://{}/api/v1/ <<<<<'.format(
        app.config['FLASK_SERVER_NAME']))
    app.run(debug=app.config['DEBUG'])


# api.add_resource(Sellers, '/sellers')
# api.add_resource(Products, '/products')
# api.add_resource(Tokens, '/token')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
