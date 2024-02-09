# ライブラリ呼び出し
from flask import Flask, render_template
import pandas as pd 
from datetime import datetime
from flask import request
from flask import Flask, request, jsonify



# クラス呼び出し
app = Flask(__name__)
from sqlalchemy import create_engine



@app.route('/')
def index2():

    # HTMLにデータを渡して表示
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)







    















