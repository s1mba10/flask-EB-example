from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, welcome to my main page!</h1>'
