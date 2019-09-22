# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/16 21:21
"""
from flask_httpauth import HTTPBasicAuth
from flask import g, jsonify
from . import api


basic_auth = HTTPBasicAuth()


@api.before_request
@basic_auth.login_required
def before_request():
    if not g.current_user.is_anonymous:
        pass
    pass
