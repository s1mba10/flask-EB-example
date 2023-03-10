from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, welcome to my main page!</h1>'

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)