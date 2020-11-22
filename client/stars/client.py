
import requests
from .config import (
    DevelopmentConfig,
    QAConfig,
    ProductionConfig  
)
class Client():
    """
    Represents a shared state class specific to each client (using the Borg design pattern) to
    which all other classes can have access by declaring an instance of it. It is further customized based on the env.

    Parameters
    ----------
    host: str, optional
        which host the job will run on
    port: str, otional
        which port will be used for the jobs
    env: str, optional
        which env the jobs will run in

    Attributes
    ----------
    http_client: Object
        uses the python request package 
    url: str
        the url where all requests will be submitted to

    Notes
    -----
    As mentioned above, this class acts as a singleton
    """

    def __init__ (self, host=None, port=None, env=None):
        env = env or 'dev'

        if env == 'dev':
            config = DevelopmentConfig
        elif env == 'qa':
            config = QAConfig
        elif env == 'prod':
            config == ProductionConfig
        else:
            raise ValueError(f'Invalid FLASK_ENV {env}; must be dev/qa/prod')

        _host = host or config.FLASK_HOST
        _port = port or config.FLASK_PORT
        self.url = f'http://{_host}:{_port}'
    
        # If we wanted to extend this to include authentication, http_client would use the the requests-oauthlib OAuth2Session library
        self.http_client = requests
