from app import app
from flask import render_template

@app.route('/')
def hello_world():
    return render_template('index.html', name='Brian')


@app.route('/test')
def hello_test():
    name = 'Brian'
    # name.append('A')
    return 'This is a test!'
