from src.Data_loader import StockDataLoader
import numpy as np
import pandas as pd

## CHECKING IS OUR DATA IS THE LOADING PROPERLY OR NOT

loader = StockDataLoader(start_date = "2023-01-01", end_date = "2026-01-01")
apple_df = loader.load_ticker("AAPL")
print(apple_df.head())

tickers = ["AAPL", "GOOG", "MSFT"]
stocks_data = loader.load_multiple(tickers)
for t, df in stocks_data.items():
    print(f"{t}:\n", df.head())