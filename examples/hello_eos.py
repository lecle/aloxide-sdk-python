import time
from aloxidesdk.aloxide_service import AloxideService, EOS_NETWORK

service = AloxideService({
  'type': EOS_NETWORK,
  'endpoint': 'https://jungle3.cryptolions.io:443'
})

contract_name = 'fqrmqfwxdsge'
private_key = 'key'

print('creating poll #101')
tx_result = service.create_data(contract_name, 'poll', private_key, {
  'user': contract_name,
  'id': 101,
  'name': 'Poll #101',
  'body': 'Tien tests poll #101'
})

print(tx_result['transaction_id'])
time.sleep(5)
print('reading polls')

result = service.read_data({
  'code': 'fqrmqfwxdsge',
  'scope': 'fqrmqfwxdsge',
  'table_name': 'poll'
})

print(result)
