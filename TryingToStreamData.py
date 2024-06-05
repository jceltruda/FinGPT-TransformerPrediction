import alpaca_trade_api as tradeapi
from alpaca.data.live import StockDataStream
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Alpaca API credentials
API_KEY = 'PKBYU5OLPEJ2IGZUR27R'
API_SECRET = 'ruqt41n2SND9PM23R8CQtU1xt3ew5cV3axde3ZNp'
BASE_URL = 'https://paper-api.alpaca.markets' 

# Initialize API
api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL)

# Function to handle incoming trade updates
def on_trade_update(conn, channel, data):
    symbol = data.symbol
    price = data.price
    timestamp = data.timestamp

    print(f"Trade update: Symbol: {symbol}, Price: {price}, Timestamp: {timestamp}")

# Subscribe to trade updates for a specific symbol
symbol_to_watch = 'AAPL'  # Example: Apple stock
api.subscribe_trades(on_trade_update, symbol_to_watch)

# Function to update the plot
def update_plot(i):
    pass  # We'll update the plot based on the incoming data

# Create a blank plot
fig, ax = plt.subplots()
ax.set_title(f"Real-time Trades for {symbol_to_watch}")
ax.set_xlabel("Time")
ax.set_ylabel("Price ($)")

# Start streaming data
api.run()

# Start updating the plot using FuncAnimation
ani = FuncAnimation(fig, update_plot, interval=1000)  # Update every second
plt.show()