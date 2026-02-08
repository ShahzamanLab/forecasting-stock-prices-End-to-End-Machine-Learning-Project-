import pandas as pd
import numpy as np
import yfinance as yf
import logging
from typing import Optional
import os

class Stock_Data_loader:
    """
    Class for downloading and processing historical stock data from Yahoo Finance.
    """
    def __init__(self,start_date,end_date):
        self.start_date = start_date
        self.end_date = end_date

    def _process_dataframe(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        Keep only Close price and compute daily returns.
        """

        df['Close'] = df['Close'].rename(columns={"Close": "Price"})
        df['Returns'] = df["Price"].pct_change()
        df = df.dropna()
        df.index = pd.to_datetime(df.index).date
        df.index.name = "Date"
        return df
    def load_ticker(self,ticker:str) -> Optional[pd.DataFrame]:
         """
        Load and process data for a single ticker.

        Args:
            ticker: Stock ticker symbol

        Returns:
            Processed DataFrame with 'Price' and 'Returns' or None if failed
        """
         
         try:
            stock = yf.Ticker(ticker)
            df = stock.history(start = self.start_date, end = self.end_date)
            if df.empty:
                logging.warning(f"No data for ticker {ticker}")
                return None
            return self._process_dataframe(df)
         except Exception as e:
             logging.error(f"error downloading {ticker}: {e}")
             return None
         
             








        