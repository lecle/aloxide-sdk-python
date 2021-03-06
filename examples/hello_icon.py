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

print('creating poll #101')
tx_result = service.create_data(contract_address, 'poll', wallet_key, {
  'id': 101,
  'name': 'Poll #101',
  'body': 'Tien tests poll #101'
})

# txHash': '0xc35d23841be1773c84f424b8e1b0650fe4086471464becfa35aac5466189b47c'
print(tx_result['txHash'])
time.sleep(5)
print('reading polls')

tx_result = service.read_data({
  'contract_address': contract_address,
  'table_name': 'poll'
}, {
  'wallet_key': wallet_key
}, {
  'id': 101
})

print(tx_result)
