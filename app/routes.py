from app import app
from flask import render_template

@app.route("/index")
@app.route("/")
def index():
    return("This is a dummy page, LOL.")

@app.route("/page_1")
def Page1():
    return render_template("page1.html")
