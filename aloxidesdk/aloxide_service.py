from aloxidesdk.icon_network import IconNetwork
from aloxidesdk.eos_network import EosNetwork

ICON_NETWORK = 'ICON Network'
EOS_NETWORK = 'EOS Network'

class AloxideService:
  def __init__(self, config):
    self.config = config

    if ICON_NETWORK == config['type']:
      self.icon_network = IconNetwork(config['endpoint'], config['network_id'])
      self.icon_service = self.icon_network.icon_service
    elif EOS_NETWORK == config['type']:
      self.eos_network = EosNetwork(config['endpoint'])
    else:
      raise KeyError('Unsupported network type')

  def deploy_contract(self, contract_info, account_info):
    if ICON_NETWORK == self.config['type']:
      return self.icon_network.deploy_contract(contract_info, account_info)
    elif EOS_NETWORK == self.config['type']:
      return self.eos_network.deploy_contract(contract_info, account_info)
    else:
      return None
