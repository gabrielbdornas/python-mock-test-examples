import requests

def get_ckan_dataset_id(ckan_host, dataset_name):
  url = f"{ckan_host}/api/3/action/package_show?id={dataset_name}"
  # make the request and return the json
  response = requests.get(url)
  if response.status_code == 200:
    dataset = response.json()
    return dataset['result']['id']
  else:
    return None


# print(get_ckan_dataset_id('https://homologa.cge.mg.gov.br', 'letters-vowel'))
