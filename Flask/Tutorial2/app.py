from flask import  Flask

app = Flask(__name__)


# app.config.from_envvar("FLASK_SETTINGS")     # takes file input from inline environment veriable
app.config.from_object('Tutorial2.settings.Test')

@app.route('/')
def home():
    return f'{app.testing=}'