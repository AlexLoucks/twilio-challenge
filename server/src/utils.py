from flask import jsonify
from functools import wraps

def construct_response(invoke_endpoint):
    @wraps(invoke_endpoint)
    def wrapper (*args, **kwargs):
        response, status_code = invoke_endpoint(*args, **kwargs)
        return jsonify(response), status_code
    return wrapper