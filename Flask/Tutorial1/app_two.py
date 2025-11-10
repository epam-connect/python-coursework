from flask import  Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World! from app two</h1>'


@app.route('/<string:name>')
def greet(name):
    return f"<h1> Hello {name.title()}</h1>"


# $env:FLASK_APP="app_two.py"
# run this command to set FLASK_APP environment variable while running flask run