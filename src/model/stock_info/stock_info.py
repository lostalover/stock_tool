from pandas import DataFrame


class StockInfo:
    def __init__(self,
                 ticker: str,
                 record: DataFrame = []):
        self.ticker = ticker
        self.record = record
