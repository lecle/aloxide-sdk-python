from aloxidesdk.aloxide_service import AloxideService, EOS_NETWORK

service = AloxideService({
  'type': EOS_NETWORK,
  'endpoint': 'https://jungle3.cryptolions.io:443'
})

result = service.read_data({
  'code': 'fqrmqfwxdsge',
  'scope': 'fqrmqfwxdsge',
  'table_name': 'accounts'
})

print('read from table accounts')
print(result)

params = {
  'from': 'fqrmqfwxdsge',
  'to': 'daniel111111',
  'quantity': '1.0000 EOS',
  'memo': 'Python is a cool language'
}

tx_result = service.write_data({
  'contract_name': 'fqrmqfwxdsge',
  'action_name': 'transfer'
}, {
  'name': 'fqrmqfwxdsge',
  'private_key': 'key'
}, params)

print('write data')
print(tx_result['transaction_id'])
