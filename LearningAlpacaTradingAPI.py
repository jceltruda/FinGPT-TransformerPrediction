#import alpaca_trade_api as tradeapi
#from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime


#fetches data from api
ALPACA_API_KEY = "<PUBLIC KEY>"
ALPACA_SECRET_KEY = "<SECRET KEY>"

# trading_client= TradingClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)

# print(trading_client.get_account().account_number)
# print(trading_client.get_account().buying_power)

data_client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)

request_params = StockTradesRequest(
    symbol_or_symbols = "AAPL",
    start = datetime(2024, 1, 30, 14, 30), 
    end = datetime(2024, 1, 30, 14, 45)
)

trades = data_client.get_stock_trades(request_params)

for trade in trades.data["AAPL"]:
    print(trade)
    break

# Instantiate REST API Connection
# api = tradeapi.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, base_url=BASE_URL, api_version='v2')

# account = api.get_account()
# print(account.id, account.equity, account.status)
