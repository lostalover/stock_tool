from urllib import parse
from ast import literal_eval
import requests


def get_sise(code, start_time, end_time, time_from='day'):
    get_param = {
        'symbol': code,
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


# print(get_sise('005930', '20210601', '20210605', 'day'))
