from bitrue.client import Client
from tabulate import tabulate
from pprint import pprint
import os

if __name__ == '__main__':
    client = Client(api_key='2f0982022fc09377f43bc1da4bcb6c2219778ffe256cb96d0e966362908f0d51',
                    api_secret='8ec2561b0b457b6b1695f4bc6e95eb11663723fe510e39baed92998187075150',
                    )

    sell_price = .470
    sell_qty = 5
    buyback_price = .40

    usdvalue = sell_price*sell_qty
    buyback_qty = usdvalue/buyback_price

    #Create intial sell order
    create_order = client.order_limit_sell(symbol='XRPUSDT', quantity=sell_qty, price=sell_price)
    pprint(create_order)
    orderId_Sell = create_order['orderId']

    while True:
        #check order status
        orderstatus = client.get_open_orders(symbol='XRPUSDT', orderid=orderId_Sell)
        if orderstatus[0]['status'] == 'FILLED':
            #buy back using gains
            buyback_order = client.order_limit_buy(symbol='XRPUSDT', quantity=buyback_qty, price=buyback_price)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # For Windows
            print('OrderId: {} - still open'.format(orderId_Sell))
'''

{'clientOrderId': '',
 'orderId': 53322247,
 'symbol': 'XRPUSDT',
 'transactTime': 1559674713334}
 
 
OrderId: 53322247 - still open
'''