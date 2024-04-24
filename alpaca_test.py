import alpaca_trade_api as tradeapi
import time

api = tradeapi.REST(key_id="PKUECQA1XVBAK3A8SZKY", secret_key="dblUm8BvJfzM6a87JOLuhWCut3AZQdkmOiH00rdl")

def get_account_with_retry(retries=3, delay=1):
    for _ in range(retries):
        try:
            account = api.get_account()
            return account
        except tradeapi.rest.APIError as error:
            print(f"An error occurred: {error}")
            print(f"Error code: {error.code}")
            print(f"Error message: {str(error)}")
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)
    raise RuntimeError("Maximum retries exceeded. Unable to get account information.")

try:
    account = get_account_with_retry()
    print(account.status)
    print("Account Number:", account.account_number)
    print("Buying Power:", account.buying_power)
except RuntimeError as e:
    print(e)

# Get account information
account = trading_client.get_account()

# Print account details

import alpaca

from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime
  
data_client = StockHistoricalDataClient("PKXVFONOMOT9VAQW4S4T","rkLfTSPaeWwNK25LaXOvFmWMOiO8lTq0ZtJbPujx")
  
request_params= StockTradesRequest{
     symbol_or_symbols="AAPL",
      start=datetime(2024,1,30,14,30),
     end=datetime(2024,1,30,14,45)
}
  
  trades = data_client.get_stock(request_params);
  
  for trade in trades.data["AAPL"]:
      print(trade)
      break*/
