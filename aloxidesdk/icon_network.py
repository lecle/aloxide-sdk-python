import sys
import time
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.wallet.wallet import KeyWallet
from iconsdk.builder.call_builder import CallBuilder
from iconsdk.builder.transaction_builder import TransactionBuilder
from iconsdk.builder.transaction_builder import DeployTransactionBuilder
from iconsdk.utils.convert_type import convert_hex_str_to_int
from iconsdk.libs.in_memory_zip import gen_deploy_data_content

GOVERNANCE_ADDRESS = 'cx0000000000000000000000000000000000000001'
SCORE_INSTALL_ADDRESS = 'cx0000000000000000000000000000000000000000'

class IconNetwork:
  def __init__(self, endpoint, network_id):
    self.endpoint = endpoint
    self.network_id = network_id
    self.icon_service = IconService(HTTPProvider(endpoint, network_id))

  def get_max_step_limit(self, wallet_address):
    params = {
      'contextType': 'invoke'
    }

    call_data = CallBuilder() \
      .from_(wallet_address) \
      .to(GOVERNANCE_ADDRESS) \
      .method('getMaxStepLimit') \
      .params(params) \
      .build()

    result = self.icon_service.call(call_data)
    return convert_hex_str_to_int(result)

  def deploy_contract(self, contract_file, wallet_key, params):
    wallet = KeyWallet.load(bytes.fromhex(wallet_key))
    contract_content_bytes = gen_deploy_data_content(contract_file)

    deploy_transaction = DeployTransactionBuilder() \
      .from_(wallet.get_address()) \
      .to(SCORE_INSTALL_ADDRESS) \
      .step_limit(self.get_max_step_limit(wallet.get_address())) \
      .nid(self.network_id) \
      .nonce(self.network_id) \
      .content_type('application/zip') \
      .content(contract_content_bytes) \
      .params(params) \
      .version(self.network_id) \
      .build()

    signed_transaction = SignedTransaction(deploy_transaction, wallet)
    tx_hash = self.icon_service.send_transaction(signed_transaction)
    # print('tx_hash:', tx_hash)

    tx_result = self.get_transaction_result(tx_hash)
    return tx_result

  def get_transaction_result(self, tx_hash):
    max_retries = 10
    retry_count = 0
    sleep_seconds = 5
    tx_result = None

    while retry_count < max_retries:
      tx_result = self.get_transaction_result_once(tx_hash)

      if None != tx_result:
        retry_count = max_retries
      else:
        retry_count += 1
        # print('Retrying {0} in {1} seconds'.format(retry_count, sleep_seconds))
        time.sleep(sleep_seconds)

    # tx_result might be still None if all retries failed.
    return tx_result

  def get_transaction_result_once(self, tx_hash):
    try:
      tx_result = self.icon_service.get_transaction_result(tx_hash)
      # print('tx_result:', tx_result)
      return tx_result
    except:
      error = sys.exc_info()
      # print('get_transaction_result error:', error[1])
      return None
