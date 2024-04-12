import alpaca_trade_api as tradeapi
import time

api = tradeapi.REST(key_id="PKNO5P01U7VS7UGWQC6S", secret_key="GXbVIkaagOgNeGddVGgAxKkj5KUKaMuWYpdVqPXe", base_url="https://paper-api.alpaca.markets")
account = api.get_account()

if __name__ == "__main__":
    # Get the value passed as argument (assuming it's the first argument)
    #stock to be traded or bought
    stock = sys.argv[1]
    #qty to buy/sell
    qty = sys.argv[2]
    # 0 = buy, 1 = sell
    buy_sell = sys.argv[3]

if(buy_sell=='1'):
    try:
        api.submit_order(
                symbol=stock,
                qty=qty,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
    except Exception as e:
        print("Error:",e)
elif (buy_sell=='2'):
    try:
        api.submit_order(
                symbol=stock,
                qty=qty,
                side='sell',
                type='market',
                time_in_force='gtc'
            )
    except Exception as e:
        print("Error:",e)
else:
    print("Error no buy/sell command")
