import os

class Config(object):
    # Paths.
    APP_DIR = os.path.abspath(os.path.dirname(__file__))

    # Database.
    DB_NAME = os.environ['DB_NAME']
    DB_SERVER = os.environ['DB_SERVER']
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']

class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True

class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    TESTING = True