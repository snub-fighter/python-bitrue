from bitrue.client import Client
import pandas as pd

if __name__ == '__main__':
    client = Client(api_key='',
                    api_secret='',
                    )


    trades = client.get_my_trades()
    df = pd.DataFrame(trades)
    df.to_csv('bitrue_trades.csv', sep=',', encoding='utf-8')


