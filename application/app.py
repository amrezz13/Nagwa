from flask import Flask
from flask import render_template, url_for, request

app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/ekhtebar")
def scrapper():
    return render_template('index.html')


