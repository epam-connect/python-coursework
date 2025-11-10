from flask import Flask

from .routes import init_route

app = Flask(__name__)

init_route(app)