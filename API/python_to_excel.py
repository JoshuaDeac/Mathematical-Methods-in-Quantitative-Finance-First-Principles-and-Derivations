# This script will take data from an API and write it to an Excel file using Python and to its inbuilt function real time data (RTD) to update the Excel file with new data from the API.

import time
# This "yfinance" library is the one used to fetch the data from the free API by Yahoo Finance.
import yfinance as yf

def fetch_live_price(ticker_symbol):
    """ function used to get prices from free API Yahoo Finance, the ticker_symbol is just the asset or stock you want to fetch data from. """
    #Ticker is part of the library that allows you to get data from the API, and it takes the ticker symbol as the asset or stock it will read.
    ticker = yf.Ticker(ticker_symbol)
    # try- except function will try get latest price from the API, if it fails it will get the last price from the history of the asset instead.
    # This is to ensure that if the API is down or not working, it will still get the last price from the history of the asset.
    try:
        # fast_info is a function that gets the latest price from the API, and lastPrice is the latest price of the asset or stock.
        latest_price = ticker.fast_info['lastPrice']
        return latest_price
    except Exception:
        # The fallback basically downloads todays prices minute by minute and gets the last price from the history of the asset or stock.
        todays_data = ticker.history(period='1d', interval='1m')
        if not todays_data.empty:
            # just returns the last price ( -1  for indexing the last row )
            return todays_data['Close'].iloc[-1]
    # and if everything fail return nothing
    return None
# Choose your asset!!
symbol = "BTC-USD"  # this is which asset or stock you want to fetch the data for, in this case.
#printing this to the console so you know its working and fetching data for the asset.
print(f"Its working on getting prices for {symbol} (Press Ctrl+C to stop)...")
# A simple while loop that doesn't stop until you stop it manually( could be optimized to stop when a trading day stops for that price )

while True:

    price = fetch_live_price(symbol) # just putting a number to the asset.
    # First checks if its a valid price, if it is then it prints the time and the price of the asset, if not it prints that it could not fetch the price.
    if price:
        # just prints out local time for console along with the price.
        print(f"Time: {time.strftime('%H:%M:%S')} | {symbol} Price: ${price:.2f}")
    else:
        print("Could not fetch price.")
    # This is the interval at which you want the data to come in at. I chose 10 seconds since its a reasonable time and wont make the API choke or call too much.
    time.sleep(10)




