# Hyperliquid Historical Data API & Datasets
*Clean, 1-minute resolution historical data for Hyperliquid Perps (Price, Funding Rate, Open Interest).*

## 📊 Why This Data Matters (Case Study)
Using 1-minute resolution data reveals alpha that 1-hour aggregates miss. 
*   **Case 1:** Found that extreme funding spikes (>0.04%/hr) led to a **75% mean-reversion hit rate** within 48 hours across 16 major pairs.
*   **Case 2:** Reconstructed the **$1.3B HYPE Open Interest anomaly**, showing how basis dislocations front-run price discovery during high-leverage regimes.

## 📥 Free Sample Dataset
Want to test the data quality instantly? I've open-sourced a 10-day sample of high-volatility 1-minute data. 
👉 **[Download the 10-Day Sample CSV Here](./hyperliquid_1min_funding_oi_sample.csv.zip)**

## 🔌 Live API Access (RapidAPI)
If you want the full 60+ day archive or a live data feed for production trading, you can access my PostgreSQL database via RapidAPI.
*   **1m, 15m, 1h, 1d aggregates**
*   **Live Funding Opportunities Endpoint**

👉 **[Get Your API Key Here (100 Free Calls/Mo)](https://rapidapi.com/jereful/api/hyperliquid-historical-funding-oi)**

## 🐍 Quickstart Template
Don't waste time writing the fetch logic. Here is a ready-to-use Pandas template to pull the data directly into your backtester.
👉 **[View the Python Template](./hl_backtest_template.py)**
