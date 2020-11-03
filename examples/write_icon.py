import time
from iconsdk.utils.convert_type import convert_hex_str_to_int
from aloxidesdk.aloxide_service import AloxideService, ICON_NETWORK

service = AloxideService({
  'type': ICON_NETWORK,
  'endpoint': 'https://bicon.net.solidwallet.io',
  'network_id': 3
})
contract_address = 'cx26d2757d45ea7e559940d86761330005b0e9f2d8'
wallet_key = '592eb276d534e2c41a2d9356c0ab262dc233d87e4dd71ce705ec130a8d27ff0c'

tx_result = service.create_data(contract_address, 'poll', wallet_key, {
  'id': '109',
  'name': 'name',
  'body': 'body'
})
print(tx_result['txHash'])
