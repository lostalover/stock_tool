from typing import List
from src.model.stock_info.basic_info import BasicInfo


class Turtle:
    def __init__(self,
                 ATR_size: int = 20) -> None:
        self.ATR_size = ATR_size
        pass

    def calculate_ATR(self, history: List[BasicInfo]):
        list_atr = []
        len_history = len(history)
        if len_history <= self.ATR_size:
            assert f'need longer history for ATR(20), current len is {len_history}'
        for i in range(len_history - self.ATR_size, len_history):
            list_atr.append(self.calculate_TR(history[i-1], history[i]))
        return sum(list_atr)/self.ATR_size

    def calculate_TR(self, yesterday: BasicInfo, today: BasicInfo):
        tr1 = self.calculate_TR1(today)
        tr2 = self.calculate_TR2(yesterday, today)
        tr3 = self.calculate_TR3(yesterday, today)
        return max(tr1, tr2, tr3)

    def calculate_TR1(self, today: BasicInfo):
        return abs(today.high_price - today.low_price)

    def calculate_TR2(self, yesterday: BasicInfo, today: BasicInfo):
        return abs(yesterday.close_price - today.high_price)

    def calculate_TR3(self, yesterday: BasicInfo, today: BasicInfo):
        return abs(yesterday.close_price - today.low_price)
