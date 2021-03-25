#!/usr/bin/env python
# @Time    : 2021/3/23 17:37
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : view
# @Project : picture-ms
import logging

from models import User
from utils.api_helper import api_message
from utils.constant import UserStatus

from flask import request
from flask_login import current_user, login_user, logout_user
from flask_restplus import Namespace, Resource

v1_user_admin = Namespace('user', description="用户相关接口")
logger = logging.getLogger(__name__)


@v1_user_admin.route('/register')
class UserRegisterApi(Resource):
    """用户注册管理"""

    def post(self):
        """
        处理用户注册请求
        """
        data = request.form.to_dict()
        user_obj = User.query.filter(User.username == data['username']).first()
        if user_obj:
            return api_message(success=False, msg='该用户名已存在！')

        try:
            data['passwords'] = data.pop('password')
            user_obj = User(**data)
            user_obj.save()
        except Exception as e:
            logger.exception('用户注册失败：%s' % e)
            return api_message(success=False, msg='用户注册失败：%s' % e)

        logger.info('用户%s注册成功！' % data['username'])
        return api_message(msg='用户注册成功！')


@v1_user_admin.route('/login')
class LoginApi(Resource):
    """用户登录管理"""

    def post(self):
        """
        处理用户登录请求
        :return:
        """
        username = request.values.get('username', '')
        password = request.values.get('password', '')

        user_obj = User.query.filter(User.username == username).first()
        if not user_obj:
            return api_message(msg='用户未注册！', success=False)

        if user_obj.status == UserStatus.CLOSED:
            return api_message(msg='该账户已禁用！', success=False)

        if current_user.is_authenticated:
            return api_message(msg='该用户已经登录！', success=True)

        # 校验密码
        if not user_obj.check_password(password):
            return api_message(msg='密码错误！', success=False)
        login_user(user_obj)
        logger.info('用户%s登录成功！' % current_user.username)
        return api_message(msg='登录成功！')


@v1_user_admin.route('/logout')
class LogoutApi(Resource):
    """用户注销管理"""

    def post(self):
        """
        处理用户注销请求
        :return:
        """
        cur_user = current_user.username
        logout_user()
        logger.info('用户%s注销成功！' % cur_user)
        return api_message(msg='用户注销成功！')
