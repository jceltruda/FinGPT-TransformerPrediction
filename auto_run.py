from google.colab import drive
import os
import time

# Mount Google Drive
drive.mount('/content/drive')

# Path to the directory containing your files in Google Drive
directory_path = '/content/drive/My Drive/Colab Notebooks/'

# Name of your file
file_name = 'TradingBot_Model.ipynb'

while True:
    # Run your file
    file_path = os.path.join(directory_path, file_name)
    print(f"Running file: {file_name}")
    %run "$file_path"
    
    # Wait for some time before running again (e.g., 60 seconds)
    time.sleep(6000)  # Adjust the sleep interval as needed