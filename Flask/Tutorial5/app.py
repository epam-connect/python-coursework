from flask import Flask, request, Blueprint

from .middleware import init_middilewares

app = Flask(__name__)

bp1 = Blueprint('web', __name__)
bp2 = Blueprint('greet', __name__)

def index():
    print('inside request')
    return f'{request.query_string=}'

def greet(name=None):
    if not name:
        return '<h1>hello world!</h1>'
    return f'<h1>hello {name.title()}</h1>'

bp1.add_url_rule('/', 'index', index)
bp2.add_url_rule('/greet', 'greet', greet)
bp2.add_url_rule('/greet/<string:name>', 'greet_user', greet)


app.register_blueprint(bp1)
app.register_blueprint(bp2)

app.debug = True


init_middilewares(app)