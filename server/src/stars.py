import json
import requests
import sys
import traceback
from flask import request, Blueprint, current_app
from marshmallow import ValidationError
from loguru import logger 
from .schemas import StarCountRequestSchema
from .utils import construct_response, validate_http_response


blueprint = Blueprint('stars', __name__, url_prefix='/stars') 

@blueprint.route('/count', methods=['POST'])
@construct_response
def count():
    """
    ---
    get:
        summary: Determine how many stars any given list of github repositories has received.
        description: Given a list of gigithub repositories in the form organization/repository, 
        the method will return the number of stars each repo has received, as well as a 
        cumulative value for all repos.
        requestBody:
            content:
                application/json:
                    schema: StarCountRequestSchema
        responses:
            200: 
                description: a successfull star count was returned
                content:
                    application/json:
                        starsCount: A map containing the number of stars for each repo.
                        totalStars: An integer representing the sum of stars on all repos.
            400:
                description: invalid input provided to the api endpoint
            500: 
                description: unspecified server error
    """

    payload = request.get_json()
    logger.info(f'The stars/count endpoint has been called with the following payload: {payload}')
    request_input = StarCountRequestSchema().load(payload)
    return count_stars_github(payload)


def count_stars_github(payload):
    star_count_map = {}
    response = {}
    sum = 0
    for repo in payload.get('repositoryList'):
        number_stars = invoke_github_api_for_repo(repo)
        star_count_map[repo] = number_stars
        sum += number_stars
    response['starsCount'] = star_count_map
    response['totalStars'] = sum
    return response, 200


def invoke_github_api_for_repo(repo):
    github_url = f"{current_app.config['GITHUB_URL']}/repos/{repo}"
    repo_data = requests.get(url=github_url)
    return validate_http_response(repo_data).get('stargazers_count')


@blueprint.errorhandler(Exception)
@construct_response
def handle_api_errors(exception):
    if isinstance(exception, ValidationError):
        exception.error_type = "Input Error"
        exception.description = exception.messages
        exception.code = 400
    if isinstance(exception, RuntimeError):
        exception.error_type = "Internal Server Error"
        exception.description = f'{exception}'
        exception.code = 500
    elif not getattr(exception, 'code', None):
        exception.error_type = "Internal Server Error"
        exception.description = ''
        exception.code = 500

    exc_type, value, tb = sys.exc_info()
    logger.error (f'{exc_type} : {value}')
    traceback.print_tb(tb) 
    error_type = getattr(exception, 'error_type', None) or exception.__class__.__name__

    if not getattr(exception, 'description', None):
        exception.description = ''

    logger.error(f'{error_type}: {exception.description} with code: {exception.code}')
    return {error_type: exception.description}, exception.code




