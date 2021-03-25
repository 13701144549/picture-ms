#!/usr/bin/env python
# @Time    : 2021/3/24 14:46
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : common
# @Project : picture-ms
import logging
from extensions import db
from .base import BaseModel
from utils.constant import UserStatus

from flask_security import current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

logger = logging.getLogger(__name__)


class User(BaseModel, UserMixin):
    """用户表"""
    __tablename__ = 'user'

    username = db.Column(db.String(150), index=True, nullable=False, comment='用户名')  #: 用户名
    password = db.Column(db.String(128), nullable=False, comment='密码')  #: 密码
    nickname = db.Column(db.String(100), default='', comment='昵称')  #: 昵称
    phone = db.Column(db.String(20), default='', comment='手机号码')  # 手机号码
    email = db.Column(db.String(150), default='', comment='邮箱')  #: 邮箱
    gender = db.Column(db.String(15), default='', comment='性别')  # 性别
    status = db.Column(db.Integer, default=UserStatus.OPEN, comment='状态')  # 状态
    active = db.Column(db.Boolean(), default=True, comment='激活状态')  #: 激活状态

    def __repr__(self):
        return "<Db.Model.User:%r>" % self.username

    @property
    def passwords(self):
        raise AttributeError("当前属性不可读")

    @passwords.setter
    def passwords(self, value):
        """
        密码加密
        :param value: 密码
        :return: None
        """
        self.password = generate_password_hash(value)

    def check_password(self, raw_password):
        """
        校验密码正确性
        :param raw_password: 待校验的密码
        :return: True/False
        """
        return check_password_hash(self.password, raw_password)


class Pictures(BaseModel):
    """图片表"""
    __tablename__ = 'picture'

    path = db.Column(db.String(150), nullable=False, comment='图片路径')  #: 图片路径
    name = db.Column(db.String(150), comment='图片名称')  # 图片名称
