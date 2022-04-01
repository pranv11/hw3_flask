#Worked with Pranav Arora and Bhagyesh Rathi
from flask import render_template
from flask import Flask

myobj = Flask(__name__)
city_names = ["Paris", "London", "Rome", "Tahiti"]
name = 'Lisa'
@myobj.route("/")

def home():
    
    cities = ""
   

    for city in city_names:
        cities += f'<li>{city}</li>'
    return f'''
    <html>
        <head>
            <title>home</title>
        </head>
        <body>
            <h1>Welcome {name}!</h1>
            <a href="www.google.com">not google</a>
            <ul>
                {cities}<br>
            </ul>
                
        </body>
    </html>
    '''
# myobj.run()