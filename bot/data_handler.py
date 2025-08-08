


from config import API_KEY, API_SECRET, API_BASE_URL
import pandas as pd
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame

api = tradeapi.REST(API_KEY, API_SECRET, API_BASE_URL, api_version='v2')

# Define symbols and date range
symbols_to_fetch = ['AAPL', 'GOOG']
start_date_iso = '2023-01-01T00:00:00Z' # Use ISO 8601 format
end_date_iso = '2024-01-01T00:00:00Z'

# Use the get_bars() method to retrieve historical data
print(f"Fetching daily bars for {', '.join(symbols_to_fetch)}...")

barset = api.get_bars(
    symbols_to_fetch,
    TimeFrame.Day,
    start=start_date_iso,
    end=end_date_iso,
    adjustment='raw'
)

# The .df property converts the BarSet object into a pandas DataFrame
df = barset.df
# Display the first few rows of the DataFrame
print(df.head())