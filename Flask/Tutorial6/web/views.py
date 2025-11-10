from flask import jsonify, request, url_for
from flask.views import MethodView
import json

from .models import User
from .serializer import users, user
from ..database import db

class Home(MethodView):
    def get(self):
        return '<h1>Hello World!</h1>'

class Greet(MethodView):
    def get(self, name):
        return f'<h1> Hello {name.title()}!</h1>'

class UserListView(MethodView):
    def get(self):
        users_list = User.query.all()
        serializer = users.dump(users_list)

        return jsonify({'message' : 'There should be a list of users here', 'users' : serializer})

class UserDetailView(MethodView):
    def get(self, id):
        user_ = User.query.filter_by(id=id).first_or_404()
        serializer = user.dump(user_)

        return jsonify({'user' : serializer})

    def post(self):
        # print(request.json)
        user_obj = user.load(request.json)
        db.session.add(user_obj)
        db.session.commit()
        serializer = user.dump(user_obj)
        # print(user_obj)
        # print(user_obj)
        return jsonify({'message' : 'user created', 'user' : serializer})