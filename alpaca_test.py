from alpaca_trade_api import REST

# Initialize the client with your API credentials
trading_client = REST(key_id="PKD1GXAS5AKA88VBGYLX", secret_key="LFiSUS9plPi4ZmeSCfxVNDhsdEYg8UMYzKD7jwgG","https://paper-api.alpaca.markets ")

# Get account information
account = trading_client.get_account()

# Print account details
print("Account Number:", account.account_number)
print("Buying Power:", account.buying_power)
#import alpaca

#from alpaca.data import StockHistoricalDataClient, StockTradesRequest
#from datetime import datetime
  
#data_client = StockHistoricalDataClient("PKXVFONOMOT9VAQW4S4T","rkLfTSPaeWwNK25LaXOvFmWMOiO8lTq0ZtJbPujx")
  
r#equest_params= StockTradesRequest{
#      symbol_or_symbols="AAPL",
#      start=datetime(2024,1,30,14,30),
 #     end=datetime(2024,1,30,14,45)
#}
  
  #trades = data_client.get_stock(request_params);
  
  #for trade in trades.data["AAPL"]:
     # print(trade)
      #break*/