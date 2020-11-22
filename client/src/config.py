import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    FLASK_ENV = os.getenv('FLASK_ENV') or 'dev'
    FLASK_HOST = os.getenv('FLASK_HOST') or '0.0.0.0'
    FLASK_PORT = os.getenv('FLASK_PORT') or '5000'

    # Assumed for the purpose of this small coding challenge, all repos will be public.
    # If we want to extend this app, we could include a github token for authentication 
    GITHUB_URL = os.getenv('GITHUB_URL') or 'https://api.github.com' 
    
class DevelopmentConfig(Config):
    DEBUG = True

class QAConfig(Config):
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False