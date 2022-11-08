import datetime
from flask import Flask
from flask import render_template
from waitress import serve

from mino import MouIkutsuNerutoOshogatsu

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    mino = MouIkutsuNerutoOshogatsu()
    h = mino.answer(datetime.date.today())
    return render_template('mino.html', answer = h)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
 