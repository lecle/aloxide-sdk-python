from aloxidesdk.aloxide_service import AloxideService, EOS_NETWORK

service = AloxideService({
  'type': EOS_NETWORK,
  'endpoint': 'https://jungle3.cryptolions.io:443'
})

result = service.read_data({
  'code': 'aloxidejs123',
  'scope': 'aloxidejs123',
  'table_name': 'poll',
})

for x in result['rows']:
    if x['id'] == 3:
        print(x)
