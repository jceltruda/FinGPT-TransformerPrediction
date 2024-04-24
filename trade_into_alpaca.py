import alpaca_trade_api as tradeapi
import time

api = tradeapi.REST(key_id="PKNO5P01U7VS7UGWQC6S", secret_key="GXbVIkaagOgNeGddVGgAxKkj5KUKaMuWYpdVqPXe", base_url="https://paper-api.alpaca.markets")
account = api.get_account()

if __name__ == "__main__":
    # Get the value passed as argument (assuming it's the first argument)
    #stock to be traded or bought
    stock = sys.argv[1]
    current_Val = sys.argv[2]
    predict_Val = sys.argv[3]
    
    qty=0
    
    if(predict_Val-current_Val<0):
        qty=-1*(predict_Val-current_Val)*10
        Sell()
        Short()
        
    if(predict_Val-current_Val>0):
        qty=-1*(predict_Val-current_Val)*10
        Buy()
        
    def Buy():
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
    def Sell():
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
            
    def Short():
        try:
            api.submit_order(
                    symbol=stock,
                    qty=qty,
                    side='option',
                    type='market',
                    time_in_force='gtc'
                )
        except Exception as e:
            print("Error:",e)
