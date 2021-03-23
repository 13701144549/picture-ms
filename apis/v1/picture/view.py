#!/usr/bin/env python
# @Time    : 2021/3/23 17:37
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : view
# @Project : picture-ms
import logging

from flask import request
from flask_login import current_user
from flask_restplus import Namespace, Resource

v1_picture_admin = Namespace('pictures', description="图片相关接口")
logger = logging.getLogger(__name__)
