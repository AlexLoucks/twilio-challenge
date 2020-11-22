import pytest
import requests
from requests import Response 
from unittest.mock import patch
from src.utils import construct_response, validate_http_response


def test_validate_http_response_successful():
    test_response = Response()
    test_response.status_code = 200
    test_response._content = b'{ "test" : "test" }'

    actual_response = validate_http_response (test_response, "test_repo")
    assert actual_response == { "test" : "test" }


def test_validate_http_response_random_error():
    test_response = Response()
    test_response.status_code = 400
    test_response.error_type = "Random"
    test_response._content = b'{ "test" : "test" }'

    with pytest.raises(RuntimeError) as e:
        actual_response = validate_http_response (test_response, "test_repo")
   

def test_validate_http_response_value_error():
    test_response = Response()
    test_response.status_code = 200
    test_response._content = b'test'
    
    with pytest.raises(RuntimeError) as e:
        actual_response = validate_http_response (test_response, "test_repo")
       

