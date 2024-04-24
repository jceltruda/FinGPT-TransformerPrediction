import time
import datetime
import subprocess

# Returns true if market is open, false otherwise
def marketIsOpen():
    marketOpenTime = datetime.time(9, 30)
    marketCloseTime = datetime.time(16, 0)
    currentTime = datetime.datetime.now().time()
    
    # Checks if we fall in correct time and day range
    if (0 <= datetime.datetime.today().weekday() <= 4) and (marketOpenTime <= currentTime <= marketCloseTime):
        return True
    else:
        return False
    
# Runs the bot program
def runBot():
    subprocess.run(['python', 'TradingBot.py'])

# Attempts to run the bot every half hour
if __name__ == "__main__":
    while True:
        if marketIsOpen():
            runBot()
        # Sleeps for half hour
        time.sleep(1800)
