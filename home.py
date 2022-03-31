from flask import render_template
from flask import Flask

myapp_obj = Flask(__name__)

@myapp_obj.route("/")

def home():
    name = 'Lisa'
    print = ""
    city_names = ["Paris", "London", "Rome", "Tahiti"]

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
            <ul>{print}</ul>
                
        </body>
    </html>
    '''
myapp_obj.run()