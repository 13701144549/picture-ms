#!/usr/bin/env python
# @Time    : 2021/3/23 16:14
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : __init__.py
# @Project : picture-ms
from flask import Blueprint
from flask_restplus import Api

from v1.picture.view import v1_picture_admin
from v1.user.view import v1_user_admin

v1_bp_api_admin = Blueprint('v1_api_admin', __name__, url_prefix='/app/api_admin/v1')

api_admin_resources = Api(v1_bp_api_admin, version='v1')
api_admin_resources.add_namespace(v1_user_admin)
api_admin_resources.add_namespace(v1_picture_admin)
