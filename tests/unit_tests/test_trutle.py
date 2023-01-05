import unittest
import csv
import pandas
from src.services.turtle_algorithm.turtle import Turtle


class TestTurtle(unittest.TestCase):
    def setUp(self):
        self.turtle = Turtle()
        self.history = self.__get_stock_history()
        self.yesterday_record = self.history.iloc[0]
        self.today_record = self.history.iloc[1]

    def test_calculate_TR1(self):
        result = self.turtle.calculate_TR1(self.today_record)
        expected_result = 11.0
        assert result == expected_result

    def test_calculate_TR2(self):
        result = self.turtle.calculate_TR2(self.yesterday_record, self.today_record)
        expected_result = 7.5
        assert result == expected_result

    def test_calculate_TR3(self):
        result = self.turtle.calculate_TR3(self.yesterday_record, self.today_record)
        expected_result = 3.5
        assert result == expected_result

    def test_calculate_TR(self):
        result = self.turtle.calculate_TR(self.yesterday_record, self.today_record)
        expected_result = 11.0
        assert result == expected_result

    def test_calculate_ATR(self):
        result = self.turtle.calculate_ATR(self.history)
        expected_result = 11.9375
        assert result == expected_result

    def __get_stock_history(self) -> pandas.DataFrame:
        record = []
        f = open('/app/tests/test_data/history_data.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            print(line)
            record.append([float(val) for val in line])
        f.close()
        history = pandas.DataFrame(record, columns=['open_price', 'high_price', 'low_price', 'close_price'])
        return history
