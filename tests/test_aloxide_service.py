from os import path
from aloxidesdk.aloxide_service import AloxideService

def test_deploy_icon_contract():
  # __file__ = tests/test_aloxide_service.py
  current_dir_path = path.abspath(path.dirname(__file__))
  score_path_standard_token = path.join(current_dir_path, 'data/standard_token.zip')
  service = AloxideService({
    'endpoint': 'https://bicon.net.solidwallet.io',
    'network_id': 3
  })

  params = {
    'initialSupply': 1000
  }

  tx_result = service.deploy_contract(score_path_standard_token, '9c47f32534309f67e88cf71aeb2e0269c7a84501341cae1f122b0195263be601', params)

  print('scoreAddress:', tx_result['scoreAddress'])
  assert 42 == len(tx_result['scoreAddress'])
