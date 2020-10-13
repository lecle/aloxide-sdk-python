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
      self.eos_client = self.eos_network.cleos
    else:
      raise KeyError('Unsupported network type')

  def deploy_contract(self, contract_info, account_info):
    if ICON_NETWORK == self.config['type']:
      return self.icon_network.deploy_contract(contract_info, account_info)
    elif EOS_NETWORK == self.config['type']:
      return self.eos_network.deploy_contract(contract_info, account_info)
    else:
      return None

  def read_data(self, contract_info, account_info = None, params = None):
    if ICON_NETWORK == self.config['type']:
      return self.icon_network.read_data(contract_info['contract_address'], contract_info['table_name'], account_info['wallet_key'], params)
    elif EOS_NETWORK == self.config['type']:
      return self.eos_network.read_data(contract_info['code'], contract_info['scope'], contract_info['table_name'])
    else:
      return None

  def write_data(self, contract_info, account_info, params):
    if ICON_NETWORK == self.config['type']:
      return self.icon_network.write_data(contract_info['contract_address'], contract_info['action_name'], account_info['wallet_key'], params)
    elif EOS_NETWORK == self.config['type']:
      return self.eos_network.write_data(contract_info['contract_name'], contract_info['action_name'], account_info['name'], account_info['private_key'], params)
    else:
      return None

  def create_data(self, contract_name, table_name, private_key, data):
    if ICON_NETWORK == self.config['type']:
      return self.icon_network.create_data(contract_name, table_name, private_key, data)
    elif EOS_NETWORK == self.config['type']:
      return self.eos_network.create_data(contract_name, table_name, private_key, data)
    else:
      return None

  def update_data(self, contract_name, table_name, private_key, data):
    if ICON_NETWORK == self.config['type']:
      return self.icon_network.update_data(contract_name, table_name, private_key, data)
    elif EOS_NETWORK == self.config['type']:
      return self.eos_network.update_data(contract_name, table_name, private_key, data)
    else:
      return None

  def delete_data(self, contract_name, table_name, private_key, data):
    if ICON_NETWORK == self.config['type']:
      return self.icon_network.delete_data(contract_name, table_name, private_key, data)
    elif EOS_NETWORK == self.config['type']:
      return self.eos_network.delete_data(contract_name, table_name, private_key, data)
    else:
      return None
