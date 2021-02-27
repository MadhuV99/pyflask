# app4.py
'''
Command to create virtual environment 'env' for this flask app : 
    python -m venv env 

Command to activate the virtual environment 'env' :
    env\Scripts\activate.bat 

Command to install flask :
    pip install flask 

Command to run this flask app:
    python app4.py

Command to Deactivate the virtual environment 'env' :
    deactivate    
'''
from flask import Flask

app = Flask(__name__) 

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

@app.route('/home')
def home():
    return '<h1>Hello! You are on the HOME page!</h1>'

if __name__ == '__main__':
    app.run()




