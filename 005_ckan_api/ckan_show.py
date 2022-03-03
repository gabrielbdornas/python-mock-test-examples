from ckanapi import RemoteCKAN

def ckan_show(ckan_host, dataset_id):
  # import ipdb; ipdb.set_trace(context=10)
  # ckan_instance = RemoteCKAN('https://homologa.cge.mg.gov.br/') #, apikey = ckan_key)
  # result = ckan_instance.action.package_show(id = 'letters-vowel')
  return RemoteCKAN(ckan_host).action.package_show(id = dataset_id)['state']
  # return RemoteCKAN(ckan_host).action.package_show(id = dataset_id)

# print(ckan_show('https://homologa.cge.mg.gov.br/', 'letters-vowel'))
