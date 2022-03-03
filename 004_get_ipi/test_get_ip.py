from unittest import mock
import pytest
from get_ip import get_ip

@mock.patch("get_ip.requests.get")
def test_get_ip(mock_requests_get):
  mock_requests_get.return_value = mock.Mock(name='Mocke requests.get',
                                             **{'status_code': 200,
                                                'json.return_value': {'origin': '0.0.0.0'},
                                             })
  # Another way
  # mock_requests_get.return_value = mock.Mock()
  # mock_requests_get.return_value.status_code = 200
  # mock_requests_get.return_value.json.return_value = {'origin': '0.0.0.0'}
  assert get_ip() == '0.0.0.0'
