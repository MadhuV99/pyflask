# app2.py
'''
Command to create virtual environment 'env' for this flask app : 
    python -m venv env 

Command to activate the virtual environment 'env' :
    env\Scripts\activate.bat 

Command to install flask :
    pip install flask    

Command to set the flask environment variable to this pgm :
    set FLASK_APP=app2.py

Command to run the flask app :
    flask run

Command to Deactivate the virtual environment 'env' :
    deactivate    
'''
from flask import Flask

app = Flask(__name__) 

@app.route('/<name>')
def index(name):
    return '<h1>Hello! {}</h1>'.format(name)



