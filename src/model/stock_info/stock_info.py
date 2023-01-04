from typing import List
from src.model.stock_info.basic_info import BasicInfo


class StockInfo:
    def __init__(self,
                 ticker: str,
                 record: List[BasicInfo] = []):
        self.ticker = ticker
        self.record = record
