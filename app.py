from flask import Flask
from api import get_apis, get_endpoints, get_statistics

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to the Hacker-News-API API</h1>'

@app.route('/all')
def all():
    return get_apis()

@app.route('/endpoints/<aid>')
def endpoints(aid):
    return get_endpoints(aid)

@app.route('/statistics/<aid>')
def statistics(aid):
    return get_statistics(aid)
