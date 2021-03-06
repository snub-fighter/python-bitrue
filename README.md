# python-bitrue
A package to communicate with the Bitrue API 
==================================
Welcome to python-bitrue 0.0.2
==================================

Note
----



This is an unofficial Python wrapper for the [Bitrue exchange REST API v1](https://github.com/Bitrue-exchange/bitrue-official-api-docs). I am in no way affiliated with Bitrue, use at your own risk.

If you came here looking for the [Bitrue exchange](https://www.bitrue.com/activity/task/task-landing?inviteCode=EWHAHT) to purchase cryptocurrencies, then [go here](https://www.bitrue.com/activity/task/task-landing?inviteCode=EWHAHT). If you want to automate interactions with Bitrue stick around.


Source code
  https://github.com/sammchardy/python-bitrue

Documentation
  https://python-bitrue.readthedocs.io/en/latest/  (pending release)

Features
--------

- Implementation of all General, Market Data and Account endpoints.
- Simple handling of authentication
- No need to generate timestamps yourself, the wrapper does it for you
- Response exception handling


| Bitrue Official API | Status | python-bitrue |
| ------------- | ------------- | ----- |
| [General endpoints (PUBLIC)](https://github.com/Bitrue-exchange/bitrue-official-api-docs#general-endpoints)|	 | |
| [Test connectivity](https://github.com/Bitrue-exchange/bitrue-official-api-docs#test-connectivity)	| complete | 			ping |
| [Check server time](https://github.com/Bitrue-exchange/bitrue-official-api-docs#check-server-time)| complete | get_server_time |
| [Exchange information (Some fields not support. only reserved)](https://github.com/Bitrue-exchange/bitrue-official-api-docs#exchange-information-some-fields-not-support-only-reserved)	| complete | get_exchange_info |
| [Symbol Info(From Exchange Info)]	| complete | get_symbol_info |
| Market Data endpoints (PUBLIC)]| | |
| [Order book](https://github.com/Bitrue-exchange/bitrue-official-api-docs#order-book)	| complete | get_order_book |
| [Recent trades list](https://github.com/Bitrue-exchange/bitrue-official-api-docs#recent-trades-list)	| complete | get_recent_trades |
| [Old trade lookup (MARKET_DATA)](https://github.com/Bitrue-exchange/bitrue-official-api-docs#old-trade-lookup-market_data)	| complete | get_historical_trades |
| [Compressed/Aggregate trades list](https://github.com/Bitrue-exchange/bitrue-official-api-docs#compressedaggregate-trades-list)	| complete | get_aggregate_trades |
| | IN DEVELOPMENT | aggregate_trade_iter |
| NOT AVAILABLE	| get_klines |
| NOT AVAILABLE	| REQUIRES KLINES	| _get_earliest_valid_timestamp |
| NOT AVAILABLE	| REQUIRES KLINES	| get_historical_klines |
| NOT AVAILABLE	| REQUIRES KLINES	| get_historical_klines_generator |
| [24hr ticker price change statistics](https://github.com/Bitrue-exchange/bitrue-official-api-docs#24hr-ticker-price-change-statistics)	| complete | get_ticker_24h |
| [Symbol price ticker](https://github.com/Bitrue-exchange/bitrue-official-api-docs#symbol-price-ticker)	| complete | get_ticker_price |
| [Symbol order book ticker](https://github.com/Bitrue-exchange/bitrue-official-api-docs#symbol-order-book-ticker) | complete | get_orderbook_ticker |
| [Account endpoints (PRIVATE)] | | |
| [New order (TRADE)](https://github.com/Bitrue-exchange/bitrue-official-api-docs#new-order--trade) | complete | create_order |
| | complete | order_limit |
| | complete | order_limit_buy |
| | complete | order_limit_sell |
| | complete | order_market |
| | complete | order_market_buy |
| | complete | order_market_sell |
| NOT AVAILABLE | complete | create_test_order |
| [Query order (USER_DATA)](https://github.com/Bitrue-exchange/bitrue-official-api-docs#query-order-user_data)  | complete | get_order |
| [Cancel order (TRADE)](https://github.com/Bitrue-exchange/bitrue-official-api-docs#cancel-order-trade)	 | complete | cancel_order |
| [Current open orders (USER_DATA)](https://github.com/Bitrue-exchange/bitrue-official-api-docs#current-open-orders-user_data) | complete | get_open_orders |
| [All orders (USER_DATA)](https://github.com/Bitrue-exchange/bitrue-official-api-docs#all-orders-user_data) | complete | get_all_orders |
| [Account information (USER_DATA)](https://github.com/Bitrue-exchange/bitrue-official-api-docs#account-information-user_data) | complete | get_account |
| | complete | get_asset_balance
| [Account trade list (USER_DATA)](https://github.com/Bitrue-exchange/bitrue-official-api-docs#account-trade-list-user_data) | complete | get_my_trades |
| NOT AVAILABLE	| complete | get_system_status |
| NOT AVAILABLE	| complete | get_account_status |
| NOT AVAILABLE	| complete | get_dust_log |
| NOT AVAILABLE	| complete | get_trade_fee |
| NOT AVAILABLE	| complete | get_asset_details |
| NOT AVAILABLE	| complete | withdraw |
| NOT AVAILABLE	| complete | get_deposit_history |
| NOT AVAILABLE	| complete | get_withdraw_history |
| NOT AVAILABLE	| complete | get_deposit_address |
| NOT AVAILABLE	| complete | get_withdraw_fee |
| NOT AVAILABLE	| complete | stream_get_listen_key |
| NOT AVAILABLE	| complete | stream_keepalive |
| NOT AVAILABLE	| complete | stream_close |
| 	| complete | _order_format_print (fancy order printing) |

Quick Start
-----------

[Register an account with Bitrue](https://www.bitrue.com/activity/task/task-landing?inviteCode=EWHAHT)

[Generate an API Key](https://www.bitrue.com/account/api)and assign relevant permissions.

Automatic Method

.. code:: bash (PyPi)
 
    pip install bitrue-python  *OFFICIALLY RELEASED - https://pypi.org/project/bitrue-python/
    
Manual Method

     Download zip
     Unzip
     Place package (folder 'python-bitrue') in 'site-packages' directory or preferred location
       ('Python Install Folder ' \Lib\site-packages)
     open command prompt
     Navigate to above folder.
     pip install -e python-bitrue
     
     Linux
     python3 -m venv bitruevenv
     source bitruevenv/bin/activate
     git clone https://github.com/snub-fighter/python-bitrue.git
     cd bitrue
     apt-get install python3-dev
     python3 -m pip install -r requirements.txt
     
.. code:: python

    from bitrue.client import Client
    api_key=''
    api_secret=''
    client = Client(api_key, api_secret)

    # get market depth
    depth = client.get_order_book(symbol='BNBBTC')

    # place a test market buy order, to place an actual order use the create_order function
    order = client.create_order(
        symbol='XRPUSDT',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=100)

    # get all symbol prices
    prices = client.get_all_tickers()

    # withdraw 1000 XRP
    # check docs for assumptions around withdrawals
    from bitrue.exceptions import BitrueAPIException, BitrueWithdrawException
    try:
        result = client.withdraw(
            asset='ETH',
            address='<eth_address>',
            amount=100)
    except BitrueAPIException as e:
        print(e)
    except BitrueWithdrawException as e:
        print(e)
    else:
        print("Success")

    # fetch list of withdrawals
    withdraws = client.get_withdraw_history()

    # fetch list of ETH withdrawals
    eth_withdraws = client.get_withdraw_history(asset='ETH')

    # get a deposit address for BTC
    address = client.get_deposit_address(asset='BTC')

    # Fetch balance of asset, create a sell order - subsequently cancel sell order using orderId
    asset = test.get_asset_balance(asset='XRP')
    asset_free = asset['free']
    order = test.create_order(symbol='XRPUSDT',
                            side=Client.SIDE_SELL,
                            type=Client.ORDER_TYPE_LIMIT,
                            quantity=int(float(asset_free)),
                             price=4.01)
    print(order)
    orderId = order['orderId']
    print('Order ID: ',orderId, 'sleeping for 10')
    time.sleep(10)
    pprint(test.cancel_order(symbol='XRPUSDT', orderId=orderId))

    #check for open orders and format data for easy reading.
    try:
        open = test.get_open_orders(symbol='CSCXRP',orderId=orderId) #,orderId=orderId
        filled = open[0]['executedQty']
        total = open[0]['origQty']
        print('Order status: ', float(filled), 'of',float(total))
    except:
        print('no orders open')
        
        
    try: # Better formatting using tabulate
        open_orders = client.get_open_orders(symbol='XRPUSDT')
        order_formatted = client._order_format_print(open_orders, orient='h')
        print(order_formatted)
    except:
        print('no orders open')
        
        Output Below
        
        symbol      orderId  clientOrderId      price    origQty ...  type    side    stopPrice   ... 
        --------  ---------  ---------------  -------  --------- ...  ------  ------  ----------- ...
        XRPUSDT    53289178                         2     250    ...  LIMIT   SELL                ... 
        XRPUSDT    53289160                         2     127.5  ...  LIMIT   SELL                ... 




Coil
------
 Coil is enabled by default in this package so that if you use it a healdess browser will attempt to load ONLY if you have the coil extension installed on that browser.  It will attempt firefox by default as it is the most stable.  If you do not have the extension installed on firefox nothing happens.  Either way this should be completely transparent to you.  I have put a lot of effort into getting the package itself and coil to function seemlessly.  If you wish to disable it you can either turn the coil_enabled=True flag to False when calling the client.Client class or statically disable it inside client.Client under the __init__ function.

Example Setup (default)

    if __name__ == '__main__':
    client = Client(api_key='2f0982022fc09377f43bc1da4bcb6c2219778ffe256cb96d0e966362908f0d51',
                    api_secret='8ec2561b0b457b6b1695f4bc6e95eb11663723fe510e39baed92998187075150',
                    coil_enabled=True, headless=True, browser='firefox')

Donate
------

If this library helped you out feel free to donate.
- SIGN UP FOR COIL AND ADD EXTENSION TO FIREFOX -> coil.com
- ETH: 0xd6933c5199Aa7Ac295dEff154a6AaF3342F43C90
- XRP: rsCJ7ZKeXKacVSsiBZUZqgKxteradBUEuR
- BTC: 1Dknp6L6oRZrHDECRedihPzx2sSfmvEBys
- BNB: bnb136ns6lfw4zs5hg4n85vdthaad7hq5m4gtkgf23 Memo: 103712985


Special Thanks
--------------
Sam McHardy (sammchardy) - Who did a lot of work on python-binance which I forked and converted to use it for Bitrue .
