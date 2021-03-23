#!/usr/bin/env python
# @Time    : 2021/3/23 16:31
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : manage
# @Project : picture-ms
import os

from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restplus import Api
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_cors import CORS

from conf.config import Config
from apis import v1_bp_api_admin


migrate = Migrate()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
api = Api()
session = Session()


def create_manager():
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)
    print("Using mysql config: ", app.config.get('SQLALCHEMY_DATABASE_URI'))
    # logging_config = app.config.get("CRLOGGING")
    # LoggingManager(logging_config, BASE_DIR)
    # print("Using logging config: ", logging_config)

    # 注册通用blueprint
    app.register_blueprint(v1_bp_api_admin)

    db.app = app
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db=db)
    session.init_app(app)
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

    manager = Manager(app=app)
    manager.add_command('db', MigrateCommand)
    return manager


if __name__ == '__main__':
    manager = create_manager()
    manager.run()
