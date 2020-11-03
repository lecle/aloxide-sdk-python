from aloxidesdk.aloxide_service import AloxideService, EOS_NETWORK

service = AloxideService({
  'type': EOS_NETWORK,
  'endpoint': 'https://testnet.canfoundation.io'
})

result = service.read_data({
  'code': 'aloxidejs123',
  'scope': 'aloxidejs123',
  'table_name': 'poll',
})

for x in result['rows']:
    if x['id'] == 14:
        print(x)
