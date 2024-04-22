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

#print(type(djia["Close"]))


## create a figure of the DJIA data
#plt.figure(figsize=(10, 6))
#plt.plot(djia["Close"])
#plt.xlabel("Date")
#plt.ylabel("Close Price")
#plt.title("DJIA Close Price")
#plt.show()


# TODO: Add code to overlay the DJIA data with the predicted values
# from the trained model - output a json file with predicted values and have script parse
# the json file
predicted_data = None
# open ../data/djia_stock_numerical_output.json
with open("../data/djia_stock_numerical_output.json", "r") as file:
    predicted_data = [float(num) for num in json.load(file)]

djia_values = []
dates = []
set_dates = []
for i in range(6, len(djia["Close"])-1):
    
    # date is i days before today in the format of "YYYY-MM-DD"
    date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
    dates.insert(0, date)
    if i % 15 == 0:
        set_dates.insert(0, str(date))
    #else:
    #    dates.append("")
    
    djia_values.append(djia["Close"][i])

print(len(djia_values))

# plot predicted data with DJIA data and every 15th date on x-axis
fig, ax = plt.subplots()
ax.plot(dates, djia_values, label="DJIA Close Price", color="blue")
ax.plot(dates, predicted_data, label="Predicted Close Price", color="red")
ax.set_xticks(set_dates)
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.title("DJIA Close Price vs Predicted Close Price")
plt.legend()
plt.show()

