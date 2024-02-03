import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def get_sp500_tickers():
    # You can get the list of S&P 500 tickers from various sources
    # Here, we are using the Wikipedia page
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_table = pd.read_html(url, header=0)[0]
    tickers = sp500_table['Symbol'].tolist()
    return tickers

def download_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    return data['Adj Close']

def save_to_csv(data, file_path):
    data.to_csv(file_path)

def plot_stock_data(data):
    data.plot(figsize=(10, 7))
    plt.show()

if __name__ == "__main__":
    # Define the time period for which you want to fetch the data
    start_date = '2023-01-01'
    end_date = '2024-01-01'

    # Get the S&P 500 tickers
    sp500_tickers = get_sp500_tickers()

    # Download stock data for S&P 500 tickers
    stock_data = download_stock_data(sp500_tickers, start_date, end_date)

    # Save the data to a CSV file
    csv_file_path = 'sp500_stock_data.csv'
    save_to_csv(stock_data, csv_file_path)

    # Plot the stock data
    plot_stock_data(stock_data)