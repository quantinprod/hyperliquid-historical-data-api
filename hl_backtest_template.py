"""
Hyperliquid Historical Data Fetcher
Get your free API key by signing up here: https://rapidapi.com/jereful/api/hyperliquid-historical-funding-oi
"""
import os
import requests
import pandas as pd

# --- USER CONFIGURATION ---
# 1. Get your free API key from the link above.
# 2. Set it as an environment variable OR paste it directly here.
API_KEY = os.environ.get("RAPIDAPI_KEY", "PASTE_YOUR_API_KEY_HERE")
API_HOST = "hyperliquid-historical-funding-oi.p.rapidapi.com"

def get_hl_data(coin="BTC", days_back=30, resolution="1h"):
    """
    Fetches historical data from the Hyperliquid Data API.
    Returns a Pandas DataFrame.
    """
    if API_KEY == "PASTE_YOUR_API_KEY_HERE":
        print("❌ ERROR: Please paste your own RapidAPI key into the API_KEY variable.")
        return None

    url = f"https://{API_HOST}/api/v1/historical"
    headers = {"x-rapidapi-host": API_HOST, "x-rapidapi-key": API_KEY}
    params = {"coin": coin, "days_back": days_back, "resolution": resolution}
    
    print(f"Fetching {days_back} days of {coin} data at {resolution} resolution...")
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json().get("data", [])
        if not data:
            print("No data returned. Check your parameters.")
            return None
        df = pd.DataFrame(data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)
        return df
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# --- EXAMPLE USAGE ---
if __name__ == "__main__":
    # Example 1: Get the last 14 days of hourly WIF data
    wif_df = get_hl_data(coin="WIF", days_back=14, resolution="1h")
    if wif_df is not None:
        print("\n--- WIF Hourly Data ---")
        print(wif_df.head())
        print(f"\nSuccessfully fetched {len(wif_df)} data points for WIF.")

    # Example 2: Get the last 2 days of 1-minute TST data
    tst_df = get_hl_data(coin="TST", days_back=2, resolution="1m")
    if tst_df is not None:
        print("\n--- TST 1-Minute Data ---")
        print(tst_df.head())
        print(f"\nSuccessfully fetched {len(tst_df)} data points for TST.")
