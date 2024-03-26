# ACCOUNT SETUP ------------------------------------------------------------------------------------
from alpaca.trading.client import TradingClient

# Connect to account
trading_client = TradingClient("PK0X5HPYGPNMYOA5YL0O", "CBZbVoArVU7qrF2LLwHIeuNqnpLBL96Kj3S5Teig")

# Verify we have connected the account
print(trading_client.get_account().account_number)


from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime

#data_client = StockHistoricalDataClient("PK0X5HPYGPNMYOA5YL0O", "CBZbVoArVU7qrF2LLwHIeuNqnpLBL96Kj3S5Teig")

# TEST RETRIEVING MARKET DATA ------------------------------------------------------------------------------------
request_params = StockTradesRequest(
    symbol_or_symbols="NVDA",
    # Trades on 3/26/24 11:20am
    start=datetime(2024, 3, 26, 11, 20),
    end=datetime(2024, 3, 26, 11, 40)
)

#trades = data_client.get_stock_trades(request_params)
#print(trades)

# TEST TRADING STOCKS ------------------------------------------------------------------------------------
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trade_data = MarketOrderRequest(
    symbol="NVDA",
    qty=6,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY
)
# Should execute trade through alpaca account
trade = trading_client.submit_order(trade_data)
print(trade)