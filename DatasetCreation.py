# This file was inspired by my teammates Yash Garala and Ethan Zhang
# I used it to generate multiple datasets at a time for fine-tuning
from datetime import datetime, timedelta
import yfinance as yf
import json
from google.colab import drive


# Fetching the data
tickers = ["NVDA", "META", "GME", "T", "REGN"]
# Mount your Google Drive
from google.colab import drive
drive.mount("/content/drive")

# Read the data from the file
import pandas as pd
import json
import jsonlines

#Loop through once per ticker
for ticker in  tickers:
  data = yf.download(ticker, start="2023-01-01", end="2023-01-08")  # Example: Data for 2023
  
  # Step 1: Download the data
  data = yf.download(tickers='GOOG', period='5d', interval='1m')

  # Step 2: Convert the data to a list of dictionaries
  data_list = data.to_dict('records')

  # Step 3: Write the data to a .jsonl file
  with open('data.jsonl', 'w') as f:
      for item in data_list:
          json.dump(item, f)
          f.write('\n')
          
  end_date = datetime.now().date()
  start_date = end_date - timedelta(days=7)
  # Fetch the ticker stock data
  stock_data = yf.download(ticker, start=start_date, end=end_date)

  # Convert the DataFrame to a list of dictionaries
  stock_records = stock_data.reset_index().to_dict('records')
  output_file = ticker + "_stock_data.jsonl"
  with open(output_file, 'w') as f:
    pass

    for i in range(7, len(stock_records)):
      input_days = stock_records[i-7:i]
      output_day = stock_records[i]

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

      # write the record to the JSON Lines file
      with jsonlines.open(output_file, mode='a') as writer:
          writer.write(record)

  # Open the .jsonl file
  with open(output_file, 'r') as file:
      for line in file:
          json_object = json.loads(line)