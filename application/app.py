from flask import Flask
from flask import render_template, url_for, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@app.route("/home")
@app.route("/ekhtebar")
def scrapper():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return 'not now'


