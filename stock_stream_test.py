# Streams current stock price
from alpaca.data.live import StockDataStream

stream = StockDataStream("PK0X5HPYGPNMYOA5YL0O", "CBZbVoArVU7qrF2LLwHIeuNqnpLBL96Kj3S5Teig")

async def handle_trade(data):
    print(data)

stream.subscribe_trades(handle_trade, "SNP")

stream.run()