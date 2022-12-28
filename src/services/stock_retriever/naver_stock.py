from urllib import parse
from ast import literal_eval
# from requests import Response
import requests


class NaverStock():
    def get_korean_stock(self, ticker, start_time, end_time, time_from='day'):
        get_param = {
            'symbol': ticker,
            'requestType': 1,
            'startTime': start_time,
            'endTime': end_time,
            'timeframe': time_from
        }
        get_param = parse.urlencode(get_param)
        url = f"https://api.finance.naver.com/siseJson.naver?{get_param}"
        response = requests.get(url)
        result = literal_eval(response.text.strip())
        return result

    def get_foreign_stock(self, ticker):
        params = {
            'page': 1,
            'pageSize': 20
        }
        params = parse.urlencode(params)
        url = f"https://api.stock.naver.com/stock/{ticker}.O/price?{params}"
        response = requests.get(url)
        result = literal_eval(response.text.strip())
        return result

    # def __create_form_for_foreign_stock(self, response):
    #     result = [['현지시간', '시가', '고가', '저가', '종가', '거래량', '외국인소진율']]
    #     received_data = literal_eval(response.text.strip())
    #     for data in received_data:
    #         temp = [
    #             data['localTradedAt'],
    #             data['openPrice'],
    #             data['highPrice'],
    #             data['lowPrice'],
    #             data['closePrice'],
    #             data['']
    #         ]
    #     return result


# NaverStock().get_foreign_stock('AAPL')
