from unittest import mock
from ckan_show import ckan_show

@mock.patch("ckan_show.package_show")
def test_ckan_show(mock_ckan_show):
  mock_ckan_show.return_value = mock.Mock(name='Mocke CKAN API',
                                             **{'json.return_value': {'license_title': 'CC0-1.0', 'maintainer': None, 'relationships_as_object': [], 'private': False, 'maintainer_email': None, 'num_tags': 2, 'id': 'a8580ed9-3b64-4a3f-9cee-c9587833278e', 'metadata_created': '2022-02-21T11:35:53.572487', 'metadata_modified': '2022-02-24T16:27:22.184409', 'author': None, 'author_email': None, 'state': 'active', 'version': '0.1.0', 'creator_user_id': '8b56d7f0-5f56-42f0-b422-c700683b7e93', 'type': 'dataset', 'resources': [{'mimetype': 'text/csv', 'cache_url': None, 'hash': '', 'description': 'This file contains the actual data', 'name': 'Vowels', 'format': 'CSV', 'url': 'https://homologa.cge.mg.gov.br/dataset/a8580ed9-3b64-4a3f-9cee-c9587833278e/resource/078c9abe-d53d-4e3c-8165-fabbe2d20e0c/download/letters-vowels.csv', 'datastore_active': True, 'cache_last_updated': None, 'package_id': 'a8580ed9-3b64-4a3f-9cee-c9587833278e', 'created': '2022-02-21T11:35:53.960961', 'state': 'active', 'mimetype_inner': None, 'last_modified': '2022-02-21T11:35:53.935518', 'position': 0, 'revision_id': 'fd4edc98-ae19-43ee-87d1-e9c5f0b134eb', 'url_type': 'upload', 'id': '078c9abe-d53d-4e3c-8165-fabbe2d20e0c', 'resource_type': None, 'size': 77}, {'mimetype': 'application/json', 'cache_url': None, 'hash': '', 'description': '', 'name': 'datapackage.json', 'format': 'JSON', 'url': 'https://homologa.cge.mg.gov.br/dataset/a8580ed9-3b64-4a3f-9cee-c9587833278e/resource/e92da77c-bcda-40e8-8a96-98a28a62720f/download/datapackage.json', 'datastore_active': False, 'cache_last_updated': None, 'package_id': 'a8580ed9-3b64-4a3f-9cee-c9587833278e', 'created': '2022-02-21T11:35:54.589495', 'state': 'active', 'mimetype_inner': None, 'last_modified': '2022-02-24T16:27:22.151679', 'position': 1, 'revision_id': 'f3dbbd76-b41f-4f48-b224-3223ab6beee7', 'url_type': 'upload', 'id': 'e92da77c-bcda-40e8-8a96-98a28a62720f', 'resource_type': None, 'size': 2773}, {'mimetype': 'text/csv', 'cache_url': None, 'hash': '', 'description': 'This file contains the actual data', 'name': 'Vowels Teste', 'format': 'CSV', 'url': 'https://homologa.cge.mg.gov.br/dataset/a8580ed9-3b64-4a3f-9cee-c9587833278e/resource/a0b443da-8241-4291-9479-ce2f0c8d1dc4/download/letters-vowels.csv', 'datastore_active': True, 'cache_last_updated': None, 'package_id': 'a8580ed9-3b64-4a3f-9cee-c9587833278e', 'created': '2022-02-21T11:36:45.944610', 'state': 'active', 'mimetype_inner': None, 'last_modified': '2022-02-24T16:27:21.320223', 'position': 2, 'revision_id': 'd415cdf0-df51-4fff-9b75-f96f865bcda1', 'url_type': 'upload', 'id': 'a0b443da-8241-4291-9479-ce2f0c8d1dc4', 'resource_type': None, 'size': 77}], 'num_resources': 3, 'tags': [{'vocabulary_id': None, 'state': 'active', 'display_name': 'english grammar', 'id': '0a96d04a-96dd-44f4-9eee-c82133e3ce7f', 'name': 'english grammar'}, {'vocabulary_id': None, 'state': 'active', 'display_name': 'letters', 'id': 'd9fcf340-7552-4511-a0d0-20fd0ce3f914', 'name': 'letters'}], 'groups': [], 'license_id': 'CC0-1.0', 'relationships_as_subject': [], 'organization': {'description': 'A Secretaria de Estado de Planejamento e Gestão - SEPLAG - tem como competência:\r\n\r\n- formular, propor, planejar e coordenar a ação governamental;\r\n\r\n- promover a gestão estratégica e o acompanhamento das metas e dos resultados das políticas públicas;\r\n\r\n- planejar e coordenar a formulação, a execução e a avaliação das políticas públicas de recursos humanos, de saúde ocupacional, de orçamento, de recursos logísticos e patrimônio, de tecnologia da informação e comunicação, de inovação e modernização da gestão e de atendimento ao usuário;\r\n\r\n- promover a orientação normativa, a supervisão técnica, a fiscalização, a execução e o controle das atividades de perícia médica, de administração e pagamento de pessoal e de compras governamentais;\r\n\r\n- promover a orientação normativa e a supervisão técnica relativas às parcerias entre o Poder Executivo, as Organizações Sociais e as Organizações da Sociedade Civil de Interesse Público;\r\n\r\n- planejar, coordenar, normatizar e executar atividades necessárias à gestão e à operação da Cidade Administrativa, bem como à gestão de seus bens e serviços;\r\n\r\n- formular, propor e coordenar a política de reforma do Estado.\r\n\r\n-- [Lei 23304, de 30/05/2019](https://www.almg.gov.br/consulte/legislacao/completa/completa.html?num=23304&ano=2019&tipo=LEI)', 'created': '2020-07-24T14:09:44.612088', 'title': 'Secretaria de Estado de Planejamento e Gestão - SEPLAG', 'name': 'secretaria-de-estado-de-planejamento-e-gestao-seplag', 'is_organization': True, 'state': 'active', 'image_url': '2020-07-24-144536.6480832020-07-17-013412.547577logo-seplag.png', 'revision_id': 'ec139210-2556-4fdc-875b-184799f8398e', 'type': 'organization', 'id': '20d85d1e-1bc6-43df-af39-2199f7ed04a8', 'approval_status': 'approved'}, 'name': 'letters-vowel', 'isopen': False, 'url': 'https://github.com/fjuniorr', 'notes': '\n# letters\n\n[![goodtables.io](https://goodtables.io/badge/github/dados-mg/letters-datapackage.svg)](https://goodtables.io/github/dados-mg/letters-datapackage)\n\n## Visão geral\n\nRepositório exemplo para testes do [dpkgckanmg](https://github.com/dados-mg/dpkgckanmg).\n\nPara instalar as dependências utilizadas no teste\n\n```bash\ngit checkout -b reprex1 reprex1\npip install -r requirements.txt\n```\n', 'owner_org': '20d85d1e-1bc6-43df-af39-2199f7ed04a8', 'extras': [{'key': 'contributors', 'value': '[{"title": "Francisco Alves", "role": "publisher", "organization": "gabinete-militar-do-governador-gmg"}]'}, {'key': 'profile', 'value': 'tabular-data-package'}, {'key': 'resources_ids', 'value': '{"letters-vowels": "a0b443da-8241-4291-9479-ce2f0c8d1dc4", "datapackage.json": "e92da77c-bcda-40e8-8a96-98a28a62720f"}'}, {'key': 'sources', 'value': '[{"name": "CBOE VIX Page", "path": "http://www.cboe.com/micro/vix/historical.aspx", "title": "CBOE VIX Page"}]'}], 'title': 'A vowel letters dataset', 'revision_id': '74882ab9-79b5-42a2-8cfd-29c486d613cb'},
                                             })
  # mock_requests_get.return_value = mock.Mock(name='Mocke requests.get',
  #                                            **{'status_code': 200,
  #                                               'json.return_value': {'origin': '0.0.0.0'},
  #                                            })
  print()
  # Another way
  # mock_requests_get.return_value = mock.Mock()
  # mock_requests_get.return_value.status_code = 200
  # mock_requests_get.return_value.json.return_value = {'origin': '0.0.0.0'}
  assert ckan_show('https://homologa.cge.mg.gov.br/', 'letters-vowel') == 'active'
