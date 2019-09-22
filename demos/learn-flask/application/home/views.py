# -*- coding:utf-8 -*-
from . import home
from flask import jsonify, render_template
# from application.models import


@home.route('/')
def index():
    return render_template('home.html', title='home')


@home.route('/index')
def admin_index():
    return render_template('index.html')
