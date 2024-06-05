import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient, StockTradesRequest, StockBarsRequest
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.data.live import StockDataStream
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
import datetime

# fetches data from api
ALPACA_API_KEY = "PKRUR9HNVZF2DLSDQKHR"
ALPACA_SECRET_KEY = "9E57yYbJaugReizfj3vT8YYaehmrsBDo2L6X7QaK"


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
    ticker = input("Which of your stocks would you like our AI to evaluate? ").strip().upper()
    if ticker not in position_tickers:
        continue
    else:
        break



'''
Ges the historical data from alpaca

'''
day = TimeFrame(1, TimeFrameUnit.Day)
now = datetime.datetime.now()
last = datetime.timedelta(days=6)
last_week = now - last
historical_params = StockBarsRequest(
    symbol_or_symbols = ticker,
    timeframe = day,
    start = last_week,
    end = now
)

historical_bars = historical_client.get_stock_bars(historical_params)
print(type(historical_bars))
for bars in historical_bars:
    print(bars)


'''
AI takes in the current postions and previous data
then gives output based on it

'''


'''
Based on output give options for what they want to do
'''
