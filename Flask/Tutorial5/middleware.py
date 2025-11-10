from flask import request, jsonify

def before():
    print('Run before request')
    if 'Authorization' not in request.headers:
        return jsonify({'message' : 'Unauthorized Access'}), 401

def after(req):
    print('Run after request')
    return req


def init_middilewares(app):
    app.before_request_funcs = {'greet' : [before, ]}
    app.after_request(after)