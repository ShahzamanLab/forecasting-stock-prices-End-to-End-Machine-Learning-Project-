import logging
from typing import Optional
import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)

class StockDataLoader:
    """
    Class for downloading and processing historical stock data from Yahoo Finance.
    Keeps all columns and computes daily returns.
    """

    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

    def _process_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Compute daily returns and clean index, keeping all columns.
        """
        df = df.copy() # keeping all the columns
        df["Returns"] = df["Close"].pct_change()
        df = df.dropna()
        df.index = pd.to_datetime(df.index).date
        df.index.name = "Date"
        return df

    def load_ticker(self, ticker: str) -> Optional[pd.DataFrame]:
        """
        Load and process data for a single ticker.
        """
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(start=self.start_date, end=self.end_date)
            if df.empty:
                logger.warning(f"No data for ticker {ticker}")
                return None
            return self._process_dataframe(df)
        except Exception as e:
            logger.error(f"Error downloading {ticker}: {e}")
            return None

    def load_multiple(self, tickers: list[str]) -> dict[str, pd.DataFrame]:
        """
        Load and process data for multiple tickers.
        """
        data = {}
        for ticker in tickers:
            df = self.load_ticker(ticker)
            if df is not None:
                data[ticker] = df
        return data
