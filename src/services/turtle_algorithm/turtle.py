from pandas import DataFrame, Series


class Turtle:
    def __init__(self,
                 ATR_size: int = 20) -> None:
        self.ATR_size = ATR_size
        pass

    def calculate_ATR(self, history: DataFrame) -> float:
        list_atr = []
        len_history = len(history)
        if len_history <= self.ATR_size:
            assert f'history should be {self.ATR_size} days or longer, given is {len_history} days'
        for i in range(len_history - self.ATR_size, len_history):
            list_atr.append(self.calculate_TR(history.iloc[i-1], history.iloc[i]))
        return sum(list_atr)/self.ATR_size

    def calculate_TR(self, yesterday: Series, today: Series):
        tr1 = self.calculate_TR1(today)
        tr2 = self.calculate_TR2(yesterday, today)
        tr3 = self.calculate_TR3(yesterday, today)
        return max(tr1, tr2, tr3)

    def calculate_TR1(self, today: Series):
        return abs(today.high_price - today.low_price)

    def calculate_TR2(self, yesterday: Series, today: Series):
        return abs(yesterday.close_price - today.high_price)

    def calculate_TR3(self, yesterday: Series, today: Series):
        return abs(yesterday.close_price - today.low_price)
