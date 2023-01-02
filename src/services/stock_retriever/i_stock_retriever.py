from abc import ABCMeta, abstractmethod
import datetime as dt


class IStockRetriever(metaclass=ABCMeta):
    @abstractmethod
    def get_basic_info(self,
                       ticker: str,
                       start_time: dt.datetime,
                       end_time: dt.datetime):
        pass
