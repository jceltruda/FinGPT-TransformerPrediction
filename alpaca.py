import alpaca_trade_api as tradeapi
import time

api = tradeapi.REST(key_id="PKUECQA1XVBAK3A8SZKY", secret_key="dblUm8BvJfzM6a87JOLuhWCut3AZQdkmOiH00rdl", base_url="https://paper-api.alpaca.markets")
account = api.get_account()
print("Account Number:", account.account_number)
print("Buying Power:", account.buying_power)


from alpaca_trade_api.rest import REST, TimeFrame

api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df
def process_bar(bar):
    # process bar
    print(bar)

bar_iter = api.get_bars_iter("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw')
for bar in bar_iter:
    process_bar(bar)
    
def process_quote(quote):
    # process quote
    print(quote)

quote_iter = api.get_quotes_iter("AAPL", "2021-06-08", "2021-06-08", limit=10)
for quote in quote_iter:
    process_quote(quote)

def process_trade(trade):
    # process trade
    print(trade)

trades_iter = api.get_trades_iter("AAPL", "2021-06-08", "2021-06-08", limit=10)
for trade in trades_iter:
    process_trade(trade)    
    
api.submit_order(
    symbol='SPY',
    side='buy',
    type='market',
    qty='100',
    time_in_force='day',
    order_class='bracket',
    take_profit=dict(
        limit_price='600.0',
    ),
    stop_loss=dict(
        stop_price='295.5',
        limit_price='295.5',
    )
)    