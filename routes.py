from flask import render_template, Flask, request
from app import myobj

@myobj.route("/", methods = ["GET", "POST"])

def home():
    name = 'Lisa'
    print = ""
    city_names = ["Paris", "London", "Rome", "Tahiti"]

    return render_template('home.html', title='home', 
    len = len(city_names), name = name, city_names=city_names, 
    name1 = request.form.get("fname"))