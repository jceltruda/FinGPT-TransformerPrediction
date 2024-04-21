import yfinance as yf
import jsonlines
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Get DJIA data from Yahoo Finance
djia = yf.download("^DJI", start=datetime(datetime.now().year, 1, 1), end=datetime.now())

# Convert the data to JSON
djia_json = djia.to_json(orient="records")

# Write the JSON data to a file
# with open("djia_data.json", "w") as file:
#    file.write(djia_json)

# create a figure of the DJIA data
plt.figure(figsize=(10, 6))
plt.plot(djia["Close"])
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.title("DJIA Close Price")
plt.show()


# TODO: Add code to overlay the DJIA data with the predicted values
# from the trained model - output a json file with predicted values and have script parse
# the json file