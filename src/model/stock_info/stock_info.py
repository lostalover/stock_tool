from pandas import DataFrame


# Placeholder report model
class StockInfo:
    def __init__(self,
                 ticker: str,
                 record: DataFrame = []):
        self.ticker = ticker
        self.record = record
