import yfinance as yf
import datetime as dt
from pandas import DataFrame
from src.services.stock_retriever.i_stock_retriever import IStockRetriever


class YahooStock(IStockRetriever):
    def get_basic_info(self,
                       ticker: str,
                       start_time: dt.datetime = dt.datetime.now() - dt.timedelta(weeks=4),
                       end_time: dt.datetime = dt.datetime.now()) -> DataFrame:
        stock = yf.Ticker(ticker=ticker)
        result = stock.history(start=start_time, end=end_time)
        return result
