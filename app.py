from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world liberty test 23 nov!!!'
