import os

class Config(object):
    FLASK_HOST = os.getenv('FLASK_HOST') or '127.0.0.1'
    FLASK_PORT = os.getenv('FLASK_PORT') or '5000'
    GITHUB_URL = "https://api.github.com"

class DevelopmentConfig(Config):
    DEBUG = True

class QAConfig(Config):
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False