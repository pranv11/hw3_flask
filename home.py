from flask import render_template
from flask import Flask

myobj = Flask(__name__)
city_names = ["Paris", "London", "Rome", "Tahiti"]
name = 'Lisa'
@myobj.route("/")

def home():
    
    print = ""
   

    for city in city_names:
        print += f'<li>{city}</li>'
    return f'''
    <html>
        <head>
            <title>home</title>
        </head>
        <body>
            <h1>Welcome {name}!</h1>
            <a href="https://www.google.com/">not google</a>
            <ul>
                {print}<br>
            </ul>
                
        </body>
    </html>
    '''
# myobj.run()