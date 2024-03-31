import requests
from config import *
import json

ENDPOINT_URL = "https://paper-api.alpaca.markets/v2"
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

def get_account():
    ACCOUNT_URL = f"{ENDPOINT_URL}/account"
    
    r = requests.get(ACCOUNT_URL, headers={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY})

    return json.loads(r.content)
    
def create_order(symbol, qty, side, type, time_in_force):
    
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    
    ORDER_URL = f"{ENDPOINT_URL}/orders"
    
    r = requests.post(ORDER_URL, headers=HEADERS, json=data)
    
    return json.loads(r.content)

def get_orders():
    r = requests.get(f"{ENDPOINT_URL}/orders", headers=HEADERS)
    
    return json.loads(r.content)



# response = create_order("AAPL", 1, "buy", "market", "gtc")
# response = create_order("MSFT", 10, "buy", "market", "gtc")

# print(response)

print(get_orders())