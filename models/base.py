#!/usr/bin/env python
# @Time    : 2021/3/24 14:54
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : base
# @Project : picture-ms

from datetime import datetime
from extensions import db, ma
from marshmallow import fields


class BaseModel(db.Model):
    """
    所有数据模型的公共基类
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='id')  # id
    creator_id = db.Column(db.Integer, comment='创建人id')  # 创建人id
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')  # 创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')  # 更新时间
    description = db.Column(db.Text, comment='描述信息')  # 描述信息

    def save(self):
        """
        保存当前模型的实例，适合小数据量的新建操作，或者数据更新操作，如果
        是批量保存大量数据，不要使用此方法。
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        从数据库删除当前模型所对应的数据记录。
        """
        db.session.delete(self)
        db.session.commit()

    @property
    def create_time_str(self):
        return self.create_time.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def update_time_str(self):
        return self.update_time.strftime("%Y-%m-%d %H:%M:%S")

    def add_and_gen_id(self):
        """
        数据入库之前生成入库后的id值
        :return: 数据记录id
        """
        db.session.add(self)
        db.session.flush()
        return self.id


class BaseSchema(ma.Schema):
    """
    提供一个MarshMellow的基础数据模型，用于简化其它数据模型的开发工作。
    """

    create_time = fields.Method('get_create_time')
    update_time = fields.Method('get_update_time')
    something = fields.Method('get_something')

    def get_create_time(self, obj):
        create_time = ''
        if obj and hasattr(obj, 'create_time') and obj.create_time:
            create_time = obj.create_time.strftime("%Y-%m-%d %H:%M:%S")
        return create_time

    def get_update_time(self, obj):
        update_time = ''
        if obj and hasattr(obj, 'update_time') and obj.update_time:
            update_time = obj.update_time.strftime("%Y-%m-%d %H:%M:%S")
        return update_time

    def get_something(self, obj):
        return 'sample schema'

    def format_time(self, time):
        """
        对时间进行格式化处理
        :param time: 时间对象
        :return: 标准格式时间字符串
        """
        return time.strftime("%Y-%m-%d %H:%M:%S")
