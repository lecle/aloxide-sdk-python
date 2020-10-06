from eospy.cleos import Cleos

class EosNetwork:
  def __init__(self, endpoint):
    self.endpoint = endpoint
    self.cleos = Cleos(url = endpoint)

  def deploy_contract(self, contract_info, account_info):
    return None
