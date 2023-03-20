from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def hello_test():
    name = 'Brian'
    # name.append('A')
    return 'This is a test!'
