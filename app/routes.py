from flask import render_template, request
from app import myobj
name = 'Lisa'

city_names = ["Paris", "London", "Rome", "Tahiti"]
@myobj.route("/", methods = ["GET", "POST"])

def home():


    return render_template('home.html', title='home', 
    len = len(city_names), name = name, city_names=city_names, 
    name1 = request.form.get("fname"))