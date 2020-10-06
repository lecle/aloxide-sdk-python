from os import path
from aloxidesdk.aloxide_service import AloxideService, ICON_NETWORK, EOS_NETWORK

def deploy_icon_contract():
  # __file__ = tests/test_aloxide_service.py
  current_dir_path = path.abspath(path.dirname(__file__))
  score_path_standard_token = path.join(current_dir_path, '../tests/data/standard_token.zip')
  service = AloxideService({
    'type': ICON_NETWORK,
    'endpoint': 'https://bicon.net.solidwallet.io',
    'network_id': 3
  })

  params = {
    'initialSupply': 1000
  }

  tx_result = service.deploy_contract({
    'contract_file': score_path_standard_token,
    'params': params
  }, {
    'wallet_key': '00f9417a4b915d39df04f195efc95ae7d4139728cb0f60b5eb418be666b70018'
  })
  print(tx_result)

# deployed contract at cx75ebc9841a5b7f84fa12729a251ff54e6572f66a
# deploy_icon_contract()
