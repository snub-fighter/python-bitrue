from bitrue.client import Client
from tabulate import tabulate
from pprint import pprint

if __name__ == '__main__':
    client = Client(api_key='2f0982022fc09377f43bc1da4bcb6c2219778ffe256cb96d0e966362908f0d51',
                    api_secret='8ec2561b0b457b6b1695f4bc6e95eb11663723fe510e39baed92998187075150',
                    )
    open_orders = client.get_open_orders(symbol='XRPUSDT')
    #pprint(open_orders)
    order_formatted = client._order_format_print(open_orders, orient='h')
    print(order_formatted)

'''
Standard output
[{'clientOrderId': '',
  'cummulativeQuoteQty': '0.0000000000000000',
  'executedQty': '0.0000000000000000',
  'icebergQty': '',
  'isWorking': False,
  'orderId': '53096850',
  'origQty': '11.3000000000000000',
  'price': '0.4470000000000000',
  'side': 'SELL',
  'status': 'NEW',
  'stopPrice': '',
  'symbol': 'XRPUSDT',
  'time': 1559593125000,
  'timeInForce': '',
  'type': 'LIMIT',
  'updateTime': 1559593126000}]

symbol      orderId  clientOrderId      price    origQty    executedQty    cummulativeQuoteQty  status    timeInForce    type    side    stopPrice    icebergQty             time     updateTime  isWorking
--------  ---------  ---------------  -------  ---------  -------------  ---------------------  --------  -------------  ------  ------  -----------  ------------  -------------  -------------  -----------
XRPUSDT    53289178                         2     250                 0                      0  NEW                      LIMIT   SELL                               1559664112000  1559664114000  False
XRPUSDT    53289160                         2     127.5               0                      0  NEW                      LIMIT   SELL                               1559664102000  1559664104000  False
'''