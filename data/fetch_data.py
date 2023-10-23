import requests
from config import ALPHA_VANTAGE_API_KEY

BASE_URL = "https://www.alphavantage.co/query"

def fetch_time_series_data(symbol, interval="5min"):
    """Fetch time series data for a given symbol."""
    endpoint = f"{BASE_URL}"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    return data

# Example usage:
# apple_data = fetch_time_series_data("AAPL")

