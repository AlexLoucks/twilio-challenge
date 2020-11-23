import pytest
import requests
from stars.stars import StarsClient
from unittest.mock import patch

def test_init():
    client = StarsClient(host = '127.0.0.1', port = '8080', env = 'dev')
    assert client.url == "http://127.0.0.1:8080"
    assert client.headers == {"Accept":"application.json", "Content-Type":"application/json"}

    client = StarsClient()
    assert client.url == "http://0.0.0.0:5000"
    assert client.headers == {"Accept":"application.json", "Content-Type":"application/json"}


def test_submit_API_call_null_list():
    client = StarsClient()
    actual_result = client.submit_API_call()
    assert actual_result == "Repo list cannot be null. Please add a list of repos to your command."


def test_submit_API_call():
    client = StarsClient()
    test_response = requests.Response()
    test_response.status_code = 200
    test_response._content = b'{ "success" : "success" }'
    
    with patch ('stars.stars.requests.post', return_value = test_response ):
        actual_result = client.submit_API_call(["test/test"])
        assert actual_result == {'success' : 'success'}


def test_validate_http_response_random_error():
    client = StarsClient()
    test_response = requests.Response()
    test_response.status_code = 400
    test_response.error_type = "Random"
    test_response._content = b'{ "test" : "test" }'

    actual_response = client.validate_response (test_response)
    assert {'Error calling the stars API for the given repo list, status': 400, 'body': {'test': 'test'}}


def test_validate_http_response_value_error():
    client = StarsClient()
    test_response = requests.Response()
    test_response.status_code = 400
    test_response.error_type = "Random"
    test_response._content = b'test'

    actual_response = client.validate_response (test_response)
    assert {'Error calling the stars API for the given repo list, status': 400, 'body': {'test': 'test'}}


   




