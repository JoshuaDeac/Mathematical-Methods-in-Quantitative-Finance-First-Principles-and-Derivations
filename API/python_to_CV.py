# This file here is a continuation of "python_to_excel.py", I hav already gone through the entire code block and what it means,
# but this file will skip all of that and just do what it needs to do.
# This will write to a CSV file that Excel can read, and it will update the file with new data from the API every 10 seconds.


import time
import os
import yfinance as yf

def fetch_live_price(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    try:
        latest_price = ticker.fast_info['lastPrice']
        return latest_price
    except Exception:
        todays_data = ticker.history(period='1d', interval='1m')
        if not todays_data.empty:
            return todays_data['Close'].iloc[-1]
    return None

symbol = "BTC-USD"

script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, "live_price.csv")

print(f"Starting live feed for {symbol} (Writing to {output_file})...")

while True:
    price = fetch_live_price(symbol)
    if price:
        timestamp = time.strftime('%H:%M:%S')
        print(f"Time: {timestamp} | {symbol} Price: ${price:.2f}")
        
        # Write the data to the CSV inside the API folder
        with open(output_file, "w") as f:
            f.write("Ticker,Price,Timestamp\n")
            f.write(f"{symbol},{price},{timestamp}\n")
            
    time.sleep(10)




