import os
import pytest
from unittest.mock import patch
from src.app import create_app

@patch.dict(os.environ, {"FLASK_ENV" : "dev"})
def test_app_dev():
    my_app = create_app()

    assert my_app.config['FLASK_HOST'] == '0.0.0.0'
    assert my_app.config['FLASK_PORT'] == '5000'
    assert my_app.config['GITHUB_URL'] == 'https://api.github.com' 
    assert my_app.config['DEBUG'] == True 


@patch.dict(os.environ, {"FLASK_ENV" : "qa"})
def test_app_qa():
    my_app = create_app()

    assert my_app.config['FLASK_HOST'] == '0.0.0.0'
    assert my_app.config['FLASK_PORT'] == '5000'
    assert my_app.config['GITHUB_URL'] == 'https://api.github.com' 
    assert my_app.config['DEBUG'] == False 


@patch.dict(os.environ, {"FLASK_ENV" : "prod"})
def test_app_prod():
    my_app = create_app()

    assert my_app.config['FLASK_HOST'] == '0.0.0.0'
    assert my_app.config['FLASK_PORT'] == '5000'
    assert my_app.config['GITHUB_URL'] == 'https://api.github.com' 
    assert my_app.config['DEBUG'] == False 


@patch.dict(os.environ, {"FLASK_ENV" : "test"})
def test_app_invalid_env():
    with pytest.raises(ValueError) as e:
        my_app = create_app()
    assert 'Invalid FLASK_ENV fail; must be dev/qa/prod' in str(e.value)

  