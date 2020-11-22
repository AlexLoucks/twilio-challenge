import requests
from loguru import logger 


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
    headers: List
        list of headers for http request

    Attributes
    ----------
    client: Client object
        based on the environment, the client object's attributes are set to diff values, in 
        order to allow us to make http calls to the correct host. 
    http_client: Object
        uses the python request package 
    url: str
        the url where all requests will be submitted to
    headers: List
        list of headers to send on the http call
    """

    def __init__(self, host=None, port=None, env='dev'):
        self.client = Client(host, port, env)
        self.http_client = self.client.http_client
        self.url = self.client.url
        self.headers = {"Accept":"application.json", "Content-Type":"application/json"}
       

    def submit_API_call(self, repoList=None):
        if repoList is not None:
            payload = {'repositoryList' : repoList}
            response = self.http_client.post(url=f'{self.url}/stars/count', json=payload, headers=self.headers)
            return self.validate_response(response)
        else:      
            return "Repo list cannot be null. Please add a list of repos to your command."


    def validate_response(self, response):
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
        error_msg = {'Error calling the stars API for the given repo list, status': response.status_code, 'body': res_body}
        return (error_msg)
