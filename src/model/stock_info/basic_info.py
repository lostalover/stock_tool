class BasicInfo:
    def __init__(self,
                 open_price: str,
                 high_price: str,
                 low_price: str,
                 close_price: str):
        self.open_price = float(open_price)
        self.high_price = float(high_price)
        self.low_price = float(low_price)
        self.close_price = float(close_price)
