import os

DB_TYPE = os.getenv('DATABASE_TYPE')
DB_USERNAME = os.getenv('MYSQL_USER')
DB_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
DB_SERVER = os.getenv('DATABASE_SERVER')
DB_NAME = os.getenv('MYSQL_DATABASE')


class Config(object):
    """Base config, uses staging database server."""
    SQLALCHEMY_DATABASE_URI = DB_TYPE + DB_USERNAME + ":" + DB_ROOT_PASSWORD + "@" + DB_SERVER + "/" + DB_NAME
    # TODO: DELETE mysql://username:password@server/db


# This classes heredate from Config
class ProductionConfig(Config):
    """Uses production database server."""


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
