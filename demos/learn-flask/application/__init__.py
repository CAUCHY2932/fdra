# coding: utf-8
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_cors import CORS
from config import config
from flask_admin import Admin
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # 注册日志之类的
    config[config_name].init_app(app)

    # register blueprint
    from application.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from application.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from application.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # register plugins
    db.init_app(app=app)
    mail.init_app(app=app)
    admin = Admin(app=app,name='API-admin', template_mode='bootstrap3')
    # ad.init_app(app=app)
    CORS(app=app)
    bootstrap.init_app(app=app)

    from application.models import User, Post
    admin.add_view(ModelView(User, db.session, name='用户管理'))
    admin.add_view(ModelView(Post, db.session, name='投递管理'))

    return app
