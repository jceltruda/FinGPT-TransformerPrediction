import yfinance as yf
import jsonlines
import json
from datetime import datetime, timedelta

# Define the start and end dates
end_date = datetime.now().date()
start_date = end_date - timedelta(days=2*365)

# Define the ticker symbol for DJIA
ticker_symbol = "^DJI"

# Fetch the DJIA stock data
djia_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Convert the DataFrame to a list of dictionaries
djia_records = djia_data.reset_index().to_dict('records')

# Write the data to a JSON Lines file
output_file = "djia_stock_data.jsonl"
# with jsonlines.open(output_file, mode='w') as writer:
#     writer.write_all(djia_records)

print(f"Length of data: {len(djia_records)}")

# start from 7 days after the start date
# day 7 is the output day and days 1-6 are the input days
# for each day in the data, create a new record with the input and output days

# Open the file in 'write' mode to clear it
with open(output_file, 'w') as f:
    pass

for i in range(7, len(djia_records)):
    input_days = djia_records[i-7:i]
    output_day = djia_records[i]
    
    # make each input a string and each output a string with the following format:
    # input: 
    # "Market Values for previous 6 days: 
    # Day 1: Open:{open} High:{high} Low:{low} Close:{close} Adj Close:{adj close} Volume:{volume}, ... 
    # Day 6: Open:{open} High:{high} Low:{low} Close:{close} Adj Close:{adj close} Volume:{volume}."
    # output: "Today's Market Values: Open:{open} High:{high} Low:{low} Close:{close} Adj Close:{adj close} Volume:{volume}"
    input_str = "Market Values for previous 6 days:"
    for j in range(6):
        input_str += (
            f"Day {j+1}: Open:{input_days[j]['Open']} High:{input_days[j]['High']} "
            f"Low:{input_days[j]['Low']} Close:{input_days[j]['Close']} Adj "
            f"Close:{input_days[j]['Adj Close']} Volume:{input_days[j]['Volume']}, " 
            if j != 5 else 
            f"Day {j+1}: Open:{input_days[j]['Open']} High:{input_days[j]['High']} "
            f"Low:{input_days[j]['Low']} Close:{input_days[j]['Close']} Adj "
            f"Close:{input_days[j]['Adj Close']} Volume:{input_days[j]['Volume']}."
        )

    output_str = (
        f"Today's Market Values: Open:{output_day['Open']} High:{output_day['High']} "
        f"Low:{output_day['Low']} Close:{output_day['Close']} Adj "
        f"Close:{output_day['Adj Close']} Volume:{output_day['Volume']}"
    )
    
    # create a new record with the input and output strings
    record = {"input": input_str, "output": output_str}
    
    # print(str(record) + "\n")

    # write the record to the JSON Lines file
    with jsonlines.open(output_file, mode='a') as writer:
        writer.write(record)


print(f"Data written to {output_file}")