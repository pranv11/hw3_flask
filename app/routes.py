from flask import render_template,request, flash, redirect
from app import myobj
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

name = 'Lisa'    
city_names = ["Paris", "London", "Rome", "Tahiti"]
class LoginForm(FlaskForm):
    city = StringField('city', validators=[DataRequired()])
    submit = SubmitField('submit')


@myobj.route("/", methods = ["GET", "POST"])

def home():
    form = LoginForm()
    if form.validate_on_submit():
        flash(format(form.city.data))
        return redirect('/')


    return render_template('home.html', title='home', 
    len = len(city_names), name = name, city_names=city_names, 
    form = form)