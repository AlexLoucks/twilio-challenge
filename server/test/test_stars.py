import pytest

from flask import Flask, jsonify
from loguru import logger 
from marshmallow import ValidationError
from unittest.mock import patch
from src.utils import construct_response
from src.config import DevelopmentConfig
from src.stars import count, count_stars_github, invoke_github_api_for_repo, handle_api_errors
from src.schemas import StarCountRequestSchema

class TestStars:
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    @patch('src.utils.construct_response')
    @patch('src.stars.count_stars_github')
    def test_count(self, count_stars_git_mock, construct_response_mock, caplog):
        construct_response_mock.return_value = {"test":"test"}, 200
        count_stars_git_mock.return_value = {"test":"test"}, 200
        with caplog.at_level("INFO"):
            with self.app.test_request_context():
                with patch ('flask.request.get_json', return_value = {"repositoryList":["AlexLoucks/test-repo-2", "AlexLoucks/test-repo-1"]}):
                    result = count()
                    assert result[1] == 200
                    assert result[0] is not None
        
            assert "The stars/count endpoint has been called with the following payload: {'repositoryList': ['AlexLoucks/test-repo-2', 'AlexLoucks/test-repo-1']" in caplog.text
                

    def test_count_stars_github(self):
        payload = {"repositoryList":["AlexLoucks/test-repo-2", "AlexLoucks/test-repo-1"]}
        with patch ('src.stars.invoke_github_api_for_repo', return_value=5):
            response, code = count_stars_github(payload)
        assert response == {'starsCount' : {'AlexLoucks/test-repo-1' : 5, 'AlexLoucks/test-repo-2' : 5}, 'totalStars' : 10}
        assert code == 200


    def test_invoke_github_api_for_repo(self):
        with self.app.test_request_context():
            with patch ('src.stars.validate_http_response', return_value = {'stargazers_count' : 7} ):
                with patch ('src.stars.requests.get', return_value = {'stargazers_count' : 7} ):
                    star_number = invoke_github_api_for_repo("AlexLoucks/test-repo-2")
        assert star_number == 7


    def test_handle_api_error_validationError(self, caplog):
        with caplog.at_level("ERROR"):
            with self.app.test_request_context():
                v_error = ValidationError("test validation error")
                dictionary, code = handle_api_errors(v_error)
                assert code == 400
                assert dictionary is not None
        assert "Input Error: ['test validation error'] with code: 400" in caplog.text
               

    def test_handle_api_error_runtimeError(self, caplog):
        with caplog.at_level("ERROR"):
            with self.app.test_request_context():
                v_error = RuntimeError("test validation error")
                dictionary, code = handle_api_errors(v_error)
                assert code == 500
                assert dictionary is not None
        assert "Internal Server Error: test validation error with code: 500" in caplog.text


    def test_handle_api_error_generic_no_code(self, caplog):
        with caplog.at_level("ERROR"):
            with self.app.test_request_context():
                v_error = Exception("test")
                dictionary, code = handle_api_errors(v_error)
                assert code == 500
                assert dictionary is not None
        assert "Internal Server Error:  with code: 500" in caplog.text
               
        

