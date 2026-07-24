import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import yfinance as yf

from datetime import date, datetime, time, timezone
def get_stock_data(ticker, start_date, end_date):
    data = yf.download(tickers = [ticker], start = start_date, end = end_date)
    data.insert(0, 'Ticker', ticker)
    return data

ticker = 'DIS'
start_date = datetime(2020, 1, 1)
end_date = datetime.today()
d = get_stock_data(ticker, start_date, end_date)
d.head()