import os


class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY", "my_precious")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
