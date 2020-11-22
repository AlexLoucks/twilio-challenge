import pytest
from src.schemas import StarCountRequestSchema
from marshmallow import ValidationError

def test_request_schema_valid():
    payload = {"repositoryList":["AlexLoucks/test-repo-2", "AlexLoucks/test-repo-1"]}
    request_input = StarCountRequestSchema().load(payload)
    assert payload == request_input


def test_request_schema_missing_repo_list():
    payload = {}
    with pytest.raises(ValidationError) as e:
        request_input = StarCountRequestSchema().load(payload)
    assert "'repositoryList': ['Missing data for required field.']" in str(e.value)


def test_request_schema_diff_name_for_list():
    payload = {"repoList":["AlexLoucks/test-repo-2", "AlexLoucks/test-repo-1"]}
    with pytest.raises(ValidationError) as e:
        request_input = StarCountRequestSchema().load(payload)
    assert "'repositoryList': ['Missing data for required field.']" in str(e.value)
    assert "'repoList': ['Unknown field.']" in str(e.value)


def test_request_schema_null_repo_list():
    payload = {"repositoryList": None}
    with pytest.raises(ValidationError) as e:
        request_input = StarCountRequestSchema().load(payload)
    assert "'repositoryList': ['Field may not be null.']" in str(e.value)


def test_request_schema_empty_repo_list():
    payload = {"repositoryList": []}
    with pytest.raises(ValidationError) as e:
        request_input = StarCountRequestSchema().load(payload)
    assert "Repository list must have at least one item" in str(e.value)


def test_request_schema_malformed_repo_string():
    # only org specified
    payload = {"repositoryList":["AlexLoucks/", "AlexLoucks/test-repo-1"]}
    with pytest.raises(ValidationError) as e:
        request_input = StarCountRequestSchema().load(payload)
    assert "The repo named AlexLoucks/ does not match the expected pattern ogranziation/repository from chars [A-Za-z0-9_.-]" in str(e.value)


    # only repo name specified
    payload = {"repositoryList":["AlexLoucks", "AlexLoucks/test-repo-1"]}
    with pytest.raises(ValidationError) as e:
        request_input = StarCountRequestSchema().load(payload)
    assert "The repo named AlexLoucks does not match the expected pattern ogranziation/repository from chars [A-Za-z0-9_.-]" in str(e.value)


    # unallowed char in org name
    payload = {"repositoryList":["Alex*Loucks/test-repo-2", "AlexLoucks/test-repo-1"]}
    with pytest.raises(ValidationError) as e:
        request_input = StarCountRequestSchema().load(payload)
    assert "The repo named Alex*Loucks/test-repo-2 does not match the expected pattern ogranziation/repository from chars [A-Za-z0-9_.-]" in str(e.value)