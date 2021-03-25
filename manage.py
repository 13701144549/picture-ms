#!/usr/bin/env python
# @Time    : 2021/3/23 16:31
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : manage
# @Project : picture-ms
from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Manager

from extensions import init_extension
from conf.config import Config
from apis import v1_bp_api_admin
import models


def create_manager():
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)
    print("Using mysql config: ", app.config.get('SQLALCHEMY_DATABASE_URI'))
    # logging_config = app.config.get("CRLOGGING")
    # LoggingManager(logging_config, BASE_DIR)
    # print("Using logging config: ", logging_config)

    # 注册通用blueprint
    app.register_blueprint(v1_bp_api_admin)
    init_extension(app=app)
    manager = Manager(app=app)
    manager.add_command('db', MigrateCommand)
    return app, manager


this_app, this_manager = create_manager()


if __name__ == '__main__':
    this_manager.run()
