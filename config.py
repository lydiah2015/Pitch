import os

class Config:
    SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI","postgres+psycopg2://postgres:p@127.0.0.1:5432/pitches")

class DevConfig(Config):
    pass

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

config_options={
    "development":DevConfig,
    "production":ProdConfig,
    "test":TestConfig,
}