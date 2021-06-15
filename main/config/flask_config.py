import os


class Config(object):
    """Base config, uses staging database server."""
    SQLALCHEMY_DATABASE_URI = f"{os.getenv('DATABASE_TYPE')}{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('DATABASE_SERVICE')}/{os.getenv('MYSQL_DATABASE')}"


# This classes heredate from Config
class ProductionConfig(Config):
    """Uses production database server."""


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
