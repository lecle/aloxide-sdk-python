from aloxidesdk.icon_network import IconNetwork

class AloxideService:
  def __init__(self, config):
    self.config = config
    self.icon_network = IconNetwork(config['endpoint'], config['network_id'])
    self.icon_service = self.icon_network.icon_service

  def deploy_contract(self, contract_file, wallet_key, params):
    return self.icon_network.deploy_contract(contract_file, wallet_key, params)
