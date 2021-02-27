# request_method.py
'''
Command to create virtual environment 'env' for this flask app : 
    python -m venv env 

Command to activate the virtual environment 'env' :
    env\Scripts\activate.bat 

Command to install flask :
    pip install flask 

Command to set the flask-DEBUG environment variable on :
    set FLASK_DEBUG=1

Command to run this flask app:
    python request_method.py

Command to Deactivate the virtual environment 'env' :
    deactivate    
'''

from flask import Flask, jsonify, request

app = Flask(__name__) 
app.config['DEBUG'] = True

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

@app.route('/home', methods=['GET'], defaults={'name': 'Default Name'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>Hello {}! You are on the HOME page!</h1>'.format(name)

@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1, 2, 3]})

@app.route('/query')
def query():
    query_name = request.args.get('name')
    query_location = request.args.get('location')
    return '<h1>Hello {} from {}! You are on the QUERY page!</h1>'.format(query_name, query_location)

@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return  '''
                <form method='POST' action='/theform'>
                    <input type='text' name='name'>
                    <input type='text' name='location'>
                    <input type='submit' value='Submit'>
                </form>
                '''
    else:
        form_name = request.form['name']
        form_location = request.form['location']
        return 'Hi {} from {}, form submitted successfully!'.format(form_name, form_location)


'''
@app.route('/process', methods=['POST'])
def process():
    form_name = request.form['name']
    form_location = request.form['location']
    return 'Hi {} from {}, you have submitted the form successfully!'.format(form_name, form_location)
'''

@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    json_name = data['name']
    json_loc = data['location']
    randomlist = data['randomlist']
    return jsonify({'result': 'Success!',
                    'name': json_name,
                    'location': json_loc,
                    'randomkeyinlist': randomlist[1],
                    })


if __name__ == '__main__':
    app.run()




