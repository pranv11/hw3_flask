#Worked with Pranav Arora and Bhagyesh Rathi
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import flash, redirect, render_template
from app import myobj

name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

class Login(FlaskForm):
    city = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@myobj.route("/", methods =["GET", "POST"])
def home():
    
    cityform = Login()
    if cityform.validate_on_submit():
        flash(format(cityform.city.data))
        return redirect("/")

    return render_template('home.html', title='home',  
    name=name, city_names=city_names, form=cityform)