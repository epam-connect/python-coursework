from flask import  Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World! from app three</h1>'


@app.route('/<string:name>')
def greet(name):
    return f"<h1> Hello {name.title()}</h1>"

if __name__ == "__main__":
    app.run()
