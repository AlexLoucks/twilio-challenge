

from .client import Client
class StarsClient:
    """
    Represents a Client of Counting Stars API.
    It allows users to make queries to our endpoint.

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
    client: Client object
        based on the environment, the client object's attributes are set to diff values, in 
        order to allow us to make http calls to the correct host. 
    http_client: Object
        uses the python request package 
    url: str
        the url where all requests will be submitted to
    """

    def __init__(self, host=None, port=None, env='dev'):
        self.client = Client(host, port, env)
        self.http_client = self.client.http_client
        self.url = self.client.url


    def submit_API_call(repoList=None):
        if repoList is not None:
            payload = {'repositoryList' : repoList}
            response = self.http_client.post(url=f'{self.url}/stars/count', json=payload)
        else 
            response = None
        return self.validate_response(response)


    def validate_http_response(response):
    """
    Helper method validating the github API call response 
    """
    try:
        response.raise_for_status()
        return response.json()
    except (requests.HTTPError, ValueError):
        try:
            res_body = response.json()
        except ValueError:
            res_body = response.text
    # Pass along meaningful errors from github api
    error_msg = f'Error calling the github API for one or more repos, status: {response.status_code}, body: {res_body}'
    logger.error(error_msg)
    raise RuntimeError(error_msg)
