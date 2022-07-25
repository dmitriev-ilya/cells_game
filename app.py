from flask import Flask
from flask import render_template
from game_of_life import *

app = Flask(__name__)

@app.route('/')
def index():
    GameOfLife(20, 20)
    return render_template('index.html')

@app.route('/live/')
def live():
    cells = GameOfLife()
    if cells.counter > 0:
        cells.form_new_generation()
    else:
        cells.counter += 1
    return render_template('live.html', cells=cells)

if __name__ == '__main__':
    app.run(debug=True)


