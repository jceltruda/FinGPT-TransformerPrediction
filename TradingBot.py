from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime

def getData(symbol):
    return "Unimplemented"

def analyze(symbol):
    data = getData(symbol)
    # Function to determine if we should buy, sell, or hold
    qty = "Unimplemented"
    return qty

if __name__ == '__main__':
    # Login and Access API
    trading_client = TradingClient("PK0X5HPYGPNMYOA5YL0O", "CBZbVoArVU7qrF2LLwHIeuNqnpLBL96Kj3S5Teig")

    # Get Data, Analyze, and Make Decision
    stocksToTrack = [("SPY",0), ("TSLA",0)] # Add all stocks you want to track
    for i, (stock, qty) in enumerate(stocksToTrack):
        qty = analyze(stock)
        stocksToTrack[i] = (stock, qty)
        
    # Execute Decision
        for stock, qty in stocksToTrack:
                if qty != 0:
                    if qty > 0:
                        order = OrderSide.BUY
                    else:
                        order = OrderSide.SELL
                    trade_data = MarketOrderRequest(stock, qty, order, TimeInForce.DAY)
                    trading_client.submit_order(trade_data)