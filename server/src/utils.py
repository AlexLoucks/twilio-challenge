import requests
from flask import jsonify
from functools import wraps
from loguru import logger 

def construct_response(invoke_endpoint):
    """
    Helper method constucting the response for the http call
    """
    @wraps(invoke_endpoint)
    def wrapper (*args, **kwargs):
        response, status_code = invoke_endpoint(*args, **kwargs)
        return jsonify(response), status_code
    return wrapper


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
        
    error_msg = f'Error calling the github API, status: {response.status_code}, body: {res_body}'
    logger.error(error_msg)
    raise RuntimeError(error_msg)
