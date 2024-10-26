from app import app
from flask import render_template

@app.route("/index")
@app.route("/")
def Render_DefaultPage():
    return("This is a dummy page, LOL.")

@app.route("/page_1")
def Render_FirstTestPage():
    return render_template("page1.html")
