from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime

# Returns data needed by analyze function
def getData(symbol):

    currentDate = datetime.datetime.now()
    year = currentDate.year
    month = currentDate.month
    day = currentDate.day
    hour = currentDate.hour
    second = currentDate.minute

    request_params = StockTradesRequest(
    symbol_or_symbols=symbol,
    # Gets most recent trades
        start=datetime(year, month, day, hour, second),
    end=datetime(year, month, day, hour, second - datetime.timedelta(seconds=5))
    )
    
    data_client = StockHistoricalDataClient("PK0X5HPYGPNMYOA5YL0O", "CBZbVoArVU7qrF2LLwHIeuNqnpLBL96Kj3S5Teig")
    trades = data_client.get_stock_trades(request_params)
    
    currentPrice = trades[0]
    predictedClose = getPrediction(symbol, currentPrice)
    return currentPrice, predictedClose


def getPrediction(symbol, actualPrice):
     # Stub Coded
     # Will integrate with google drive to use Fine-tuned model for stock prediction
     return actualPrice

# Function to determine if we should buy, sell, or hold
def analyze(symbol):
    currentPrice, predictedClose = getData(symbol)
    delta = predictedClose - currentPrice
    
    # Change alpha to desired value
    # Bot will sell/buy .02 shares for every dollar the price
    # is expected to increase/decrease by
    alpha = .02
    qty = alpha * delta
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