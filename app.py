# To run server, use command: flask --app app run --debug

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_html():
    return render_template('home.html')