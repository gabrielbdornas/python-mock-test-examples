import requests

def get_github_user_name(username):
  url = f"https://api.github.com/users/{username}"
  # make the request and return the json
  response = requests.get(url)
  if response.status_code == 200:
    user_data = response.json()
    return user_data['name']
  else:
    return None

# print(get_github_user_name('gabrielbdornas'))
