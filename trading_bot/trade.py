from config import *
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import alpaca_trade_api as tradeapi

def setup():
    ENDPOINT_URL = "https://paper-api.alpaca.markets/"

    api = tradeapi.REST(key_id=API_KEY, secret_key=SECRET_KEY, 
                        base_url=ENDPOINT_URL, api_version='v2')

    account = api.get_account()
    print(account)
    
    return api


def check_price_and_trade(api, symbol, qty, price_threshold):
    current_price = api.get_latest_trade(symbol).price
    
    if current_price > price_threshold:
        print(f"Placing a buy order for {qty} shares of {symbol} at ${current_price}")
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
    else:
        print(f"Placing a sell order for {qty} shares of {symbol} at ${current_price}")
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='sell',
            type='market',
            time_in_force='gtc'
        )

def trade_stock(api, symbol, decision, qty):
    current_price = api.get_latest_trade(symbol).price
    
    if current_price > price_threshold:
        print(f"Placing a buy order for {qty} shares of {symbol} at ${current_price}")
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
    else:
        print(f"Placing a sell order for {qty} shares of {symbol} at ${current_price}")
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='sell',
            type='market',
            time_in_force='gtc'
        )



if __name__ == "__main__":
    api = setup()
    
    symbol = 'AAPL'
    qty = 2
    price_threshold = 150
    check_price_and_trade(api, symbol, qty, price_threshold)
    
    symbol = input('Enter a Stock Ticker to trade ==> ')
    decision = input('Enter B/S for buying and selling ==> ')
    qty = input('Enter the number of stocks you wish to buy/sell ==> ')
