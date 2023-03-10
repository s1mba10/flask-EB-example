from flask import Flask, request, render_template

application = Flask(__name__)

@application.route('/')
def index():
    return '<h1>Hello, welcome to my main page!</h1>'
