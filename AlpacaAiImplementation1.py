import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.data.live import StockDataStream
from datetime import datetime

# fetches data from api
ALPACA_API_KEY = "Public Key"
ALPACA_SECRET_KEY = "Secret Key"


# get data from the Alpaca Api
trading_client = TradingClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)
historical_client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)
stream = StockDataStream(ALPACA_API_KEY, ALPACA_SECRET_KEY)



# gets users current positions for the AI to take in
positions = trading_client.get_all_positions()
position_tickers = []
for position in positions:
    print(position.symbol, position.lastday_price, position.current_price, position.qty)
    position_tickers.append(position.symbol)

while True:
    ticker = input("Which of your stocks would you like our AI to trade?    ").upper()
    if ticker not in position_tickers:
        continue
    else:
        break

'''
Get historical data for the stock they want to trade
'''


'''
AI takes in the current postions and previous data
then gives output based on it

'''


'''
Based on output give options for what they want to do
'''
