from iconsdk.utils.convert_type import convert_hex_str_to_int
from aloxidesdk.aloxide_service import AloxideService, ICON_NETWORK

service = AloxideService({
  'type': ICON_NETWORK,
  'endpoint': 'https://bicon.net.solidwallet.io',
  'network_id': 3
})

params = {
  '_to': 'hx2b41326239dba22f7fa6b3e7ca308ee128c97d95',
  '_value': 10
}

tx_result = service.write_data({
  'contract_address': 'cx75ebc9841a5b7f84fa12729a251ff54e6572f66a',
  'action_name': 'transfer'
}, {
  'wallet_key': 'key'
}, params)

# txHash': '0x9c8c2a83c157c6ed71d9e0c4c2409c4f366c6d749dd71db16ebb26a0ba09d268'
print(tx_result['txHash'])

params = {
  '_owner': 'hx61fc50bef6442e733febc9747715b27cebbd082b'
}

tx_result = service.read_data({
  'contract_address': 'cx75ebc9841a5b7f84fa12729a251ff54e6572f66a',
  'action_name': 'balanceOf'
}, {
  'wallet_key': 'key'
}, params)

print(convert_hex_str_to_int(tx_result))
