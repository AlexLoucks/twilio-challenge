import os

from flask import Flask

from . import stars
from .config import (
    DevelopmentConfig,
    QAConfig,
    ProductionConfig  
)

def create_app():
    # set the config corresponding to the current environment
    env = os.getenv('FLASK_ENV', 'dev').lower()
    if env == 'dev':
        config = DevelopmentConfig
    elif env == 'qa':
        config = QAConfig
    elif env == 'prod':
        config = ProductionConfig
    else:
        raise ValueError(f'Invalid FLASK_ENV {env}; must be dev/qa/prod')


    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(stars.blueprint)

    return app
        
