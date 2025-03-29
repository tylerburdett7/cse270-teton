import pytest
import requests

@pytest.fixture
def url():
    return "https://127.0.0.1:8000/users"

def test_unauthorized_access(url, mocker):
    # Mock the response for unauthorized access
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ''
    mocker.patch('requests.get', return_value=mock_response)

    # Parameters for authentication
    params = {
        'username': 'admin',
        'password': 'admin'
    }

    # Send GET request
    response = requests.get(url, params=params, verify=False)

    # Assert the response status code is 401
    assert response.status_code == 401

    # Assert the response body is empty (plain text)
    assert response.text == ''

def test_authorized_access(url, mocker):
    # Mock the response for authorized access
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ''
    mocker.patch('requests.get', return_value=mock_response)

    # Parameters for authentication
    params = {
        'username': 'admin',
        'password': 'qwerty'
    }

    # Send GET request
    response = requests.get(url, params=params, verify=False)

    # Assert the response status code is 200
    assert response.status_code == 200

    # Assert the response body is empty (plain text)
    assert response.text == ''
