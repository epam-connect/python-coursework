from flask import jsonify, request, render_template, redirect, url_for
from flask.views import MethodView

from .forms import UserForm
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

        return render_template('user_list.html', users=serializer)


class UserDetailView(MethodView):
    def get(self, id):
        user_ = User.query.filter_by(id=id).first_or_404()
        serializer = user.dump(user_)

        return jsonify({'user' : serializer})


class UserCreateView(MethodView):
    def get(self):
        form = UserForm()
        return render_template('user_create.html', form=form)

    def post(self):
        form = UserForm()

        if form.validate_on_submit():
            print(form.data)
            user_ = User(first_name=form.data['first_name'], last_name=form.data['last_name'],
                         email=form.data['email'], password=form.data['password'])
            db.session.add(user_)
            db.session.commit()

            return redirect(url_for('web.user_detail', id=user_.id))

        return render_template('user_create.html', form=form)