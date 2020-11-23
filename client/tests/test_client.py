import pytest
from stars.client import Client

def test_init():
    dev_client = Client(host = '127.0.0.1', port = '8080', env = 'dev')
    assert dev_client.url == "http://127.0.0.1:8080"

    qa_client = Client(env = 'qa')
    assert qa_client.url == "http://0.0.0.0:5000"

    prod_client = Client(env = 'prod')
    assert prod_client.url == "http://0.0.0.0:5000"

def test_init_value_error():
    with pytest.raises(ValueError) as e:
        client = Client(env = 'fail')
    assert 'Invalid FLASK_ENV fail; must be dev/qa/prod' in str(e.value)


