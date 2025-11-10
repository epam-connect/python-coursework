import pytest
from unittest import mock
from func.url_response import get_response


@mock.patch('func.url_response.requests.get')
def test_url_response(mock_request_get):
    mock_response = mock.Mock(status_code=200)
    mock_response.json.return_value = { 'slideshow' : {'author' : 'Yours Truely'}}

    #alternative syntax for the above code
    # mock_response = mock.Mock(**{ 'status_code' : 200, 'json.return_value' : {'slideshow' : { 'author' : 'Yours Truely'}} })

    mock_request_get.return_value = mock_response
    
    response = get_response()

    # mock_request_get.fun.return_value = 10
    # mock_request_get.fun() - > 10

    assert isinstance(response, dict) and response['author'] == 'Yours Truely'

