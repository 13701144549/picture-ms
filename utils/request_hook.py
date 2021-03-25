#!/usr/bin/env python
# @Time    : 2021/3/25 14:25
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : request_hook
# @Project : picture-ms
import re

from flask import request
from flask_security import current_user, login_user
# from flask_wtf.csrf import generate_csrf
from utils.api_helper import get_request_data


class RequestHook(object):
    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.exempt_path = []
            e_path = app.config.get("LOGIN_EXEMPT_PATH", [])
            for p in e_path:
                self.exempt_path.append(re.compile(p))

    def init_app(self, app):
        self.__init__(app)

        @app.after_request
        def after_request(response):
            return response
            # 调用函数生成 csrf_token
            # csrf_token = generate_csrf()
            # 通过 cookie 将值传给前端
            # response.set_cookie("csrf_token", csrf_token)
            # return response

        @app.before_request
        def before_request():
            """
            在所有的请求开始之前，检查登录状态。设计本功能的主要目的是防止出现漏加
            @login_required装饰器的情况导致安全问题。但可能会对性能造成一定的影响。
            """
            # 统一获取前端请求参数
            request.values.get = get_request_data
            # if not current_user.is_authenticated:
            #     return app.login_manager.unauthorized()
