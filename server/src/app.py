import os

from flask import Flask

from . import stars
from .config import (
    DevelopmentConfig,
    QAConfig,
    ProductionConfig  
)

def create_app():
    """
    Creates a Flask app with the configuration defined based on the current environment.

    Returns
    -------
    app: 
        A new Flask application configured accoridng to environment

    Raises:
    -------
    ValueError:
        Raised when an incorrect environment name is set as an env variable
    """
    # choose the config based on the current environment
    env = os.getenv('FLASK_ENV', 'dev').lower()
    if env == 'dev':
        config = DevelopmentConfig
    elif env == 'qa':
        config = QAConfig
    elif env == 'prod':
        config = ProductionConfig
    else:
        raise ValueError(f'Invalid FLASK_ENV {env}; must be dev/qa/prod')

    # create new Flask app
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(stars.blueprint)

    return app
        
