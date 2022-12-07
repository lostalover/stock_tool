from flask import Flask, render_template
from src.services.naver_sise import get_sise


app = Flask(__name__)


@app.route('/')
def index():
    temp = get_sise('005930', '20210601', '20210605', 'day')
    # posts = [{
    #     "title": "t1",
    #     "created": "t2"
    # }]
    return render_template('index.html', posts=temp)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False)
