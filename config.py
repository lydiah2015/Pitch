class Config:
    pass

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