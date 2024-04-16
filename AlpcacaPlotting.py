import alpaca_trade_api as tradeapi
import matplotlib.pyplot as plt
from datetime import datetime

# Alpaca API credentials
API_KEY = 'PKBYU5OLPEJ2IGZUR27R'
API_SECRET = 'ruqt41n2SND9PM23R8CQtU1xt3ew5cV3axde3ZNp'
BASE_URL = 'https://paper-api.alpaca.markets'  # Or use 'https://api.alpaca.markets' for live trading

# Initialize API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Get historical data
symbol = 'AAPL'  # Example: Apple stock
timeframe = '1Week'  # 'day', 'minute', 'hour', 'week'
start_date = '2022-01-01'
end_date = '2022-12-31'

barset = api.get_bars(symbol, timeframe, start=start_date, end=end_date)

# Extracting data
dates = [bar.t for bar in barset]
prices = [bar.c for bar in barset]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(dates, prices, label=symbol)
plt.title(f'{symbol} Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('my_plot.pdf')