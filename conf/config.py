#!/usr/bin/env python
# @Time    : 2021/3/23 17:09
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : config
# @Project : picture-ms
from redis import Redis
from datetime import timedelta


class Config:
    DEBUG = True
    # 数据库参数配置
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_DBNAME = 'picture_ms'
    MYSQL_USERNAME = 'root'
    # MYSQL_PASSWORD = '123456'
    MYSQL_PASSWORD = '12345678'
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DBNAME}?charset=utf8mb4&collation=utf8mb4_general_ci'
    SQLALCHEMY_ECHO = True

    # 缓存参数配置
    REDIS_HOST = '127.0.0.1'
    # REDIS_HOST = '182.92.94.178'
    REDIS_PORT = 6379
    REDIS_USERNAME = ''
    # REDIS_PASSWORD = ''
    REDIS_PASSWORD = '123456'
    REDIS_URI = f'redis://{REDIS_USERNAME}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/'

    # session相关配置
    SECRET_KEY = "vNeFddrSwRjqDTnqSuFZy05TQHgEMm6o"
    SESSION_TYPE = 'redis'
    # 设置session存储
    SESSION_REDIS = Redis.from_url(REDIS_URI + '1')
    # 登录过期时间
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

    # flask_security 加密
    SECURITY_PASSWORD_SALT = 'fhasdgihwntlgy8f'
    # 未登录时跳转url
    # SECURITY_LOGIN_URL = ''
    # 启用用户追踪，用于登录审计
    SECURITY_TRACKABLE = True
    LICENSE_FILE_PATH = 'license.txt'
    # cache
    CACHE_TYPE = 'redis'
    CACHE_KEY_PREFIX = ''
    CACHE_DEFAULT_TIMEOUT = 60 * 2

    # 设置为False以禁用所有CSRF保护
    # WTF_CSRF_ENABLED = False

    # 使用CSRF保护扩展时，这可以控制每个视图是否受到默认保护。默认值为True
    WTF_CSRF_CHECK_DEFAULT = False

    # sqlalchemy相关
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # Defaults True
    # SQLALCHEMY_POOL_SIZE = 2000
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_size': 200,
                                 "pool_pre_ping": True,
                                 "pool_recycle": 300,
                                 "connect_args": {
                                     "collation": "utf8mb4_general_ci"
                                 },
                                 "echo": False  # 调试时打开
                                 }

    # SQLALCHEMY_ECHO = True
    # 慢查询追踪
    # SQLALCHEMY_RECORD_QUERIES = True
    # DATABASE_QUERY_TIMEOUT = 2
    SQLALCHEMY_POOL_RECYCLE = 10
