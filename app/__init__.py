from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_options[config_name])
    Bootstrap(app)
    return app