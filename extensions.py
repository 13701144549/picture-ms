#!/usr/bin/env python
# @Time    : 2021/3/24 17:46
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : extensions
# @Project : picture-ms

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restplus import Api
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_cors import CORS
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
api = Api()
session = Session()
ma = Marshmallow()


def init_extension(app):
    api.init_app(app)
    db.init_app(app)
    Migrate(app=app, db=db)
    session.init_app(app)
    ma.init_app(app)
    # flask_wtf
    csrf.init_app(app)
    # 跨域支持
    CORS(app, supports_credentials=True)

    login_manager.init_app(app)
    # 指定登录的端点
    login_manager.login_view = 'security.login'
    # 设置session保护级别
    # None：禁用session保护
    # 'basic'：基本的保护，默认选项
    # 'strong'：最严格的保护，一旦用户登录信息改变，立即退出登录
    login_manager.session_protection = 'basic'
    # 需要登录时的提示信息
    login_manager.login_message = '请先登录'
    # login_manager._login_disabled = False
