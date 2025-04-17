import pandas as pd
import yfinance as yf

def fetch_data(ticker='AAPL', period='2y', interval='1d'):
    df = yf.download(ticker, period=period, interval=interval)
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    return df

