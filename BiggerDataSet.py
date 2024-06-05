import alpaca_trade_api as tradeapi
import pandas as pd
from datetime import datetime, timedelta

# Alpaca API credentials
API_KEY = 'PKBYU5OLPEJ2IGZUR27R'
API_SECRET = 'ruqt41n2SND9PM23R8CQtU1xt3ew5cV3axde3ZNp'
BASE_URL = 'https://paper-api.alpaca.markets'  # Or use 'https://api.alpaca.markets' for live trading

# Initialize API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Get current date and date from 3 months ago
end_date = datetime.now().date()
middle_date = timedelta(days=90)
start_date = end_date - middle_date # 3 months

# Get a list of stock symbols you're interested in
symbols = ['AAPL', 'MSFT', 'GOOG']  # Example symbols

# Fetch historical data for each symbol
historical_data = {}
for symbol in symbols:
    barset = api.get_bars(symbol, '1Day', start=start_date, end=end_date)
    historical_data[symbol] = barset.c

# Convert fetched data to DataFrame
df = pd.DataFrame(historical_data, index=pd.date_range(start=start_date, end=end_date, freq='D'))

# Print the DataFrame
print(df)