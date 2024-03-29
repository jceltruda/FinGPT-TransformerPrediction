from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.data.live import StockDataStream

#fetches data from api
ALPACA_API_KEY = "Public Key"
ALPACA_SECRET_KEY = "Secret Key"
trading_client= TradingClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)

market_order_data = MarketOrderRequest(
    symbol = "PAYO",
    qty = 10,
    side = OrderSide.BUY,                # .(side of the order you want)
    time_in_force = TimeInForce.DAY              # .(specifications for when we want the oder to place/act)
)

# market_order = trading_client.submit_order(market_order_data)
# print(market_order)

limit_order_data = LimitOrderRequest(
    symbol = "SPY",
    qty = 3,
    side = OrderSide.BUY,
    time_in_force = TimeInForce.DAY,
    limit_price = 515.00
)

# limit_order = trading_client.submit_order(limit_order_data)
# print(limit_order)

request_params = GetOrdersRequest(
    status = QueryOrderStatus.OPEN
    #side = OrderSide.BUY,
)

# orders = trading_client.get_orders(request_params)
# for order in orders:
#     trading_client.cancel_order_by_id(order.id)

positions = trading_client.get_all_positions()
# for position in positions:
#     print(position.symbol, position.current_price)

# trading_client.close_all_positions(True) to completley liquidate your account

stream = StockDataStream(ALPACA_API_KEY, ALPACA_SECRET_KEY)

# async def handle_trade(data):
#     print(data)

# stream.subscribe_trades(handle_trade, "APPL")

# stream.run()

async def handle_quote(data):
    print(data)

stream.subscribe_quote(handle_trade, "APPL")

stream.run()