import re
from flask import Flask, jsonify, render_template, request
from flask import Flask, make_response
from candleCharts.candle_crawling import candleController
from flask_cors import CORS
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html', name='')


@app.route('/stocks/candle/<symbol>', methods=['GET'])
def getCandle(symbol):
    symbol = symbol
    a = candleController()
    app_result = a.candle_crawling(symbol = symbol)
    return json.dumps(app_result)


CORS(app)
if __name__ == '__main__':
    app.run()
