import os
import pandas as pd
from flask import Flask
from flask import render_template, url_for, request
import Scrape
import QRGenerator


app = Flask(__name__)
novels = {}


@app.route("/", methods=['GET', 'POST'])
def scrapper():
    if request.method == 'POST':
        url = request.form.get("link")
        df = Scrape.scrapper(url)
        df.to_html(classes='table table-striped')
        directory = os.getcwd()
        datatoexcel = pd.ExcelWriter('novels.xlsx')

        # write DataFrame to excel
        df.to_excel(datatoexcel)
        datatoexcel.save()

        return render_template("table.html", df=df, directory=directory)

    return render_template('index.html')


@app.route("/qrcreator", methods=['GET', 'POST'])
def qrcreator():
    df = pd.read_excel('novels.xlsx')
    for row in df.index:
        QRGenerator.qrcreator(df['link'][row], df['name'][row], df['author'][row])
    return "done"
