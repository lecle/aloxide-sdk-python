from aloxidesdk.aloxide_service import AloxideService, EOS_NETWORK

service = AloxideService({
  'type': EOS_NETWORK,
  'endpoint': 'https://testnet.canfoundation.io'
})

params = {
  'user': 'aloxidejs123',
  'id': '14',
  'name': 'name',
  'body': 'body'
}

tx_result = service.write_data({
  'contract_name': 'aloxidejs123',
  'action_name': 'crepoll'
}, {
  'name': 'aloxidejs123',
  'private_key': '5JHQ3GuzcQtEQgG3SGvtDU7v2b7ioKznYBizA1V5mBUUsLNcXdQ'
}, params)

print(tx_result['transaction_id'])
