import alpaca_backtrader_api as Alpaca
import backtrader as bt
import pytz
from datetime import datetime
from local_settings import alpaca_paper
from config import *

ALPACA_KEY_ID = alpaca_paper[API_KEY]
ALPACA_SECRET_KEY = alpaca_paper[SECRET_KEY]
ALPACA_PAPER = True





