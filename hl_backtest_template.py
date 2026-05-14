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
    # Example 1: Get the last 14 days of hourly WIF data for backtesting
    wif_df = get_hl_data(coin="WIF", days_back=14, resolution="1h")
    if wif_df is not None:
        print("\n--- WIF Hourly Data ---")
        print(wif_df.head())

    # Example 2: Ping the Live Opportunities Endpoint
    print("\n--- Live Funding Opportunities ---")
    url_opps = f"https://{API_HOST}/api/v1/opportunities"
    headers = {"x-rapidapi-host": API_HOST, "x-rapidapi-key": API_KEY}
    params_opps = {"min_funding_rate": 0.0001, "min_oi": 1000000}
    
    res = requests.get(url_opps, headers=headers, params=params_opps)
    if res.status_code == 200:
        opps_data = res.json()
        print(f"Found {opps_data['opportunities_found']} coins in the Danger Zone:")
        for coin in opps_data['data']:
            print(f"[{coin['suggested_trade']}] {coin['coin']} | Funding: {coin['funding_rate_pct_per_hour']}%/hr | OI: ${coin['close_open_interest']:,.0f}")
