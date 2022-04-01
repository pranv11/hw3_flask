#Worked with Pranav Arora and Bhagyesh Rathi
from flask import Flask


myobj = Flask(__name__)

myobj.config.from_mapping(SECRET_KEY = "hello")

 
from app import routes