import yfinance as yf
import pandas as pd


class DataCollector:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def fetch_data(self):
        ticker = yf.Ticker(self.symbol)
        df = ticker.history(start=self.start_date, end=self.end_date)
        df.columns = df.columns.str.lower()
        self.data = df
        return self.data

    def preprocess_data(self):
        target = "close"
        df_close = self.data[[target]].copy()
        df_close.index = pd.to_datetime(df_close.index.date)
        df_close = df_close.reset_index()
        df_close.columns = ["ds", "y"]
        df_close["unique_id"] = 1
        return df_close
