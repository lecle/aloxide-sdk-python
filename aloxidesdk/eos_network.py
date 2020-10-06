import datetime
import json
import pytz
from eospy.cleos import Cleos
from eospy.types import Abi
from eospy.keys import EOSKey
from binascii import hexlify

class EosNetwork:
  def __init__(self, endpoint):
    self.endpoint = endpoint
    self.cleos = Cleos(url = endpoint)

  def deploy_contract(self, contract_info, account_info):
    setcode_action = self.create_setcode_action(contract_info['code_file'], account_info['name'])
    setabi_action = self.create_setcode_action(contract_info['abi_file'], account_info['name'])
    transaction = {
      'actions': [setcode_action, setabi_action],
      'expiration': str((datetime.datetime.utcnow() + datetime.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))
    }

    key = EOSKey(account_info['private_key'])
    tx_result = self.cleos.push_transaction(transaction, key)
    return tx_result

  def create_setcode_action(self, code_file, account_name):
    file_handle = open(code_file, 'rb')
    file_data = file_handle.read()
    hex_data = hexlify(file_data)

    arguments = {
      'account': account_name,
      'code': hex_data.decode('utf-8'),
      'vmtype': 0,
      'vmversion': 0
    }

    payload = {
      'account': 'eosio',
      'name': 'setcode',
      'authorization': [{
        'actor': account_name,
        'permission': 'active'
      }]
    }

    # Converting payload to binary data.
    data = self.cleos.abi_json_to_bin(payload['account'], payload['name'], arguments)
    # Inserting payload binary form as 'data' field in original payload.
    payload['data'] = data['binargs']
    return payload

  def create_setabi_action(self, abi_file, account_name):
    file_handle = open(abi_file)
    file_data = json.load(file_handle)
    abi_data = Abi(file_data)

    arguments = {
      'account': account_name,
      'abi': abi_data.get_raw()
    }

    payload = {
      'account': 'eosio',
      'name': 'setabi',
      'authorization': [{
        'actor': account_name,
        'permission': 'active'
      }]
    }

    # Converting payload to binary data.
    data = self.cleos.abi_json_to_bin(payload['account'], payload['name'], arguments)
    # Inserting payload binary form as 'data' field in original payload.
    payload['data'] = data['binargs']
    return payload
