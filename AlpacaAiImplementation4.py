import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient, StockTradesRequest, StockBarsRequest
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.data.live import StockDataStream
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
import datetime


ALPACA_API_KEY = input("Please input your public Alpca API Key ").strip()
ALPACA_SECRET_KEY = input("Please input your secret Alpca API Key ").strip()


# fetches data from api
# ALPACA_API_KEY = "<public key>"
# ALPACA_SECRET_KEY = "<secret key>"


# get data from the Alpaca Api
trading_client = TradingClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)
historical_client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)
stream = StockDataStream(ALPACA_API_KEY, ALPACA_SECRET_KEY)



# gets users current positions for the AI to take in
positions = trading_client.get_all_positions()
position_tickers = []
for position in positions:
    print("Ticker:", position.symbol, " Yesterday price:",position.lastday_price," Current price:",position.current_price, "Quantity Held:",position.qty)
    position_tickers.append(position.symbol)

while True:
    ticker = input("Which of your stocks would you like our AI to evaluate? ").strip().upper()
    if ticker not in position_tickers:
        print("\n")
        continue
    else:
        break



'''
Ges the historical data from alpaca

'''
day = TimeFrame(1, TimeFrameUnit.Day)
now = datetime.datetime.now()
last = datetime.timedelta(days=7)
last_week = now - last
historical_params = StockBarsRequest(
    symbol_or_symbols = ticker,
    timeframe = day,
    start = last_week,
    end = now
)

evalstring = ""
historical_bars = historical_client.get_stock_bars(historical_params)
for i in range(len(historical_bars[ticker])):
    evalstring = evalstring + "Day "+str(i+1)+": Open:{"+str(historical_bars[ticker][i].open)+"} High:{"+str(historical_bars[ticker][i].high)+"} Low:{"+str(historical_bars[ticker][i].low)+"} Close:{"+str(historical_bars[ticker][i].close)+"} Volume:{"+str(historical_bars[ticker][i].volume)+"}\n"

    


'''
AI takes in the eval string and evaluates the stock then generates output

'''


'''
Give the user options for what they want to do after seeing the output from out models
'''
while True:
    choice = input("Based on our models advice, ould you like to buy or sell? B for buy or S for sell, or C to cancel ").strip().upper()
    if choice == "B" or choice == "S" or choice == "C":
        break
    else:
        continue

if choice == "B":
    quant = int(input("How much would you like to buy? "))
    market_order_data = MarketOrderRequest(
        symbol = ticker,
        qty = quant,
        side = OrderSide.BUY,
        time_in_force = TimeInForce.DAY
    )
    print("Order Placed, Goodbye!")

elif choice == "S":
    quant = int(input("How much would you like to sell? "))
    market_order_data = MarketOrderRequest(
        symbol = ticker,
        qty = quant,
        side = OrderSide.SELL,
        time_in_force = TimeInForce.DAY
    )
    market_order = trading_client.submit_order(market_order_data),
    print("Order Placed, Goodbye!")


else:
    print("Hope our model helped. Goodbye")