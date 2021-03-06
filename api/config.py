import os
import logging.config
from sqlalchemy.databases import postgres

basedir = os.path.abspath(os.path.dirname(__file__))


# default config
class Config(object):
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_SERVER_NAME = 'localhost:8000'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('APP_MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('APP_MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = 'from@example.com'
    DATABASE_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=postgres, pw=postgres,
                                                                                    url='jdbc:postgresql://localhost:5432/postgres',
                                                                                    db=postgres)


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    TEST_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=postgres, pw=postgres,
                                                                                    url='jdbc:postgresql"//localhost:5432/postgres',
                                                                                    db=postgres)
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    BCRYPT_LOG_ROUNDS = 4
    PAYLOAD_EXPIRATION_TIME = 5
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/ecommerce_db'


def configure_logging(logging_ini):
    """Configure logging from a file."""

    logging.config.fileConfig(logging_ini)
    logging.info("logging configured using '{0}'.".format(logging_ini))


def configure_logging_relative(logging_ini):
    """Configure logging from a relative file."""

    base_dir = os.path.dirname(__file__)
    logging_ini = os.path.join(base_dir, logging_ini)
    configure_logging(logging_ini)


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    PAYLOAD_EXPIRATION_TIME = 3000


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    PAYLOAD_EXPIRATION_TIME = 3000


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
