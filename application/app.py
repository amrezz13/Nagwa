import os
import pandas as pd
from flask import Flask
from flask import render_template, url_for, request
import Scrape

app = Flask(__name__)


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
