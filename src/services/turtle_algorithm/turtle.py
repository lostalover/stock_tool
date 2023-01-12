from pandas import DataFrame, Series

S1_LONG_WINDOW_DAYS = 20
S1_SHORT_WINDOW_DAYS = 10
S2_LONG_WINDOW_DAYS = 55
S2_SHORT_WINDOW_DAYS = 20

class Turtle:
    def __init__(self,
                 ATR_size: int = 20) -> None:
        self.ATR_size = ATR_size
        pass

    def calculate_ATR(self, history: DataFrame) -> float:
        list_atr = []
        if len(history) <= self.ATR_size:
            assert f'history should be {self.ATR_size} days or longer, given is {len(history)} days'
        for i in range(len(history) - self.ATR_size, len(history)):
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

    def is_S1_long(self, history: DataFrame):
        return self._is_long(history, S1_LONG_WINDOW_DAYS)
    
    def is_S1_short(self, history: DataFrame):
        return self._is_short(history, S1_SHORT_WINDOW_DAYS)
    
    def is_S2_long(self, history: DataFrame):
        return self._is_long(history, S2_LONG_WINDOW_DAYS)
    
    def is_S2_short(self, history: DataFrame):
        return self._is_short(history, S2_SHORT_WINDOW_DAYS)
    

    def _is_long(self, history: DataFrame, window_days: int):
        if len(history) < window_days:
            raise ValueError(f'history must be longer than {window_days} days')
        
        return history.tail(window_days).high_price.idxmax() == window_days - 1
        
    
    def _is_short(self, history: DataFrame, window_days: int):
        if len(history) < window_days:
            raise ValueError(f'history must be longer than {window_days} days')
        
        return history.tail(window_days).low_price.idxmin() == window_days - 1