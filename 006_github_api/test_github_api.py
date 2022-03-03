from unittest import mock
from github_api import get_github_user_name

@mock.patch("github_api.requests.get")
def test_github_api(mock_requests):
  mock_requests.return_value = mock.Mock(name='Mocke requests.get',
                                             **{'status_code': 200,
                                                'json.return_value': {'avatar_url': 'https://avatars.githubusercontent.com/u/49699290?v=4',
                                               'bio': "I've been working in public offices for 10 years in Brazil, my "
                                                      "country, but recently I'm just crazy about programming and code. Ruby "
                                                      'on Rails is my focus now!',
                                               'login': 'gabrielbdornas',
                                               'name': 'Gabriel Braico Dornas',
                                               },
                                              })
  assert get_github_user_name('gabrielbdornas') == 'Gabriel Braico Dornas'
