# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/15 22:40
"""
from flask import jsonify, render_template

from application import db
from application.models import User
from . import auth
from .forms import RegisterForm


@auth.route('/register', methods=['POST'])
def register():
    form = RegisterForm()
    # if form.validate_on_submit():
    if form.validate():
        u = User(email=form.email.data.lower(),
                 username=form.username.data,
                 password=form.password.data
                 )
        db.session.add(u)
        db.session.commit()
        return jsonify(user=u.to_json())

    return jsonify(msg='create_error',
                   args=dict(email=form.email.data,
                             username=form.username.data,
                             password=form.password.data,
                             password2=form.password2.data)
                   )


@auth.route('/base')
def base():
    return render_template('base.html', title='home')


@auth.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return jsonify(msg='success')

    return render_template('auth/register.html', form=form, title='Register')
