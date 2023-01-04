import unittest
import csv
from typing import List
from src.services.turtle_algorithm.turtle import Turtle
from src.model.stock_info.basic_info import BasicInfo


class TestTurtle(unittest.TestCase):
    def setUp(self):
        self.turtle = Turtle()
        self.yesterday_record = BasicInfo(512, 512.5, 511.25, 516.5)
        self.today_record = BasicInfo(517.0, 524.0, 513.0, 521.5)
        self.history = self.__get_stock_history()

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

    def __get_stock_history(self) -> List[BasicInfo]:
        result = []
        f = open('/app/tests/test_data/history_data.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            print(line)
            result.append(BasicInfo(*line))
        f.close()
        return result
