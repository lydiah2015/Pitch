from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_options[config_name])
    Bootstrap(app)
    # register blueprints
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    return app