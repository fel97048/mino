from markupsafe import escape
from flask import Flask
from flask import render_template

from mino import MouIkutsuNerutoOshogatsu

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    mino = MouIkutsuNerutoOshogatsu()
    h = mino.answer()
    return render_template('mino.html', answer = h)