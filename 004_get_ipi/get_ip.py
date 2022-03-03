import requests

def get_ip():
  response = requests.get("https://httpbin.org/ip")
  if response.status_code == 200:
    return response.json()['origin']
