import yfinance as yf
import pandas as pd
from tqdm import tqdm

def fetch_sp500_data():
    # Download S&P 500 data
    sp500_data = yf.download('^GSPC', start='2012-01-01', end='2022-01-01')
    return sp500_data

def create_huggingface_dataset(sp500_data):
    # Resample data to monthly frequency
    monthly_data = sp500_data.resample('M').last()

    # Create a DataFrame for the Hugging Face dataset
    dataset = pd.DataFrame(columns=['date', 'open', 'high', 'low', 'close', 'volume'])

    # Populate the dataset
    for date, row in tqdm(monthly_data.iterrows(), total=len(monthly_data), desc='Processing data'):
        dataset = dataset._append({
            'date': date.strftime('%Y-%m-%d'),
            'open': row['Open'],
            'high': row['High'],
            'low': row['Low'],
            'close': row['Close'],
            'volume': row['Volume']
        }, ignore_index=True)
        
    return dataset

def save_dataset(dataset, filename):
    # Save dataset to CSV file
    dataset.to_csv(filename, index=False)
    print(f"Dataset saved to {filename}")

if __name__ == "__main__":
    # Fetch S&P 500 data
    sp500_data = fetch_sp500_data()

    # Create Hugging Face dataset
    huggingface_dataset = create_huggingface_dataset(sp500_data)

    # Save dataset to file
    save_dataset(huggingface_dataset, "sp500_dataset.csv")
