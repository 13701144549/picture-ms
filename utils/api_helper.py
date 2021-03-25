#!/usr/bin/env python
# @Time    : 2021/3/25 10:32
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : api_helper
# @Project : picture-ms
from flask import request

from .constant import PageSize


def api_message(data=None, meta=None, success=True,
                status_code=200, msg="成功！", error_code=0, **kwargs) -> tuple:
    """
    返回值包装器，注意meta是为了兼容旧代码，推荐使用keyword args的写法。比如
        api_message(data=var_a, extra1="str1", extra2=1234)

    :param status_code: 默认返回状态码为200
    :param meta: 存储分页信息数据
    :param data: 默认为空
    :param success: 默认True
    :param msg: 关于成功或失败的说明性文字
    :param error_code: 0代表成功，其它数值代表出错，见const.ErrorCode
    :return: 包装后的字典和HTTP状态码
    >>> api_message()
    ({'success': True, 'error_code': 0, 'msg': 'success'}, 200)
    >>> api_message({"content":"...."})
    ({'success': True, 'error_code': 0, 'data': {'content': '....'}, 'msg': 'success'}, 200)
    >>> api_message({"content":"...."}, {"total": 100})
    ({'success': True, 'error_code': 0, 'data': {'total': 100, 'items': {'content': '....'}}, 'msg': 'success'}, 200)
    >>> api_message(meta= {"page": 1}, error_code=4,
    ...             success=False,
    ...             status_code=404)
    ({'success': False, 'error_code': 4, 'msg': 'success'}, 404)
    >>> api_message(data={'content': '.....'}, msg='....')
    ({'success': True, 'error_code': 0, 'data': {'content': '.....'}, 'msg': '....'}, 200)
    """
    resp = {"success": success, "error_code": error_code}
    if data is not None:
        if meta is not None:
            tmp_data = {}
            tmp_data.update(meta)
            tmp_data['items'] = data
            data = tmp_data
        resp.update({"data": data})
    resp.update({"msg": msg})
    if kwargs:
        resp.update(kwargs)
    return resp, status_code


def get_request_data(key, default=''):
    """
    获取前端请求参数
    :param key: 参数名
    :param default: 获取不到参数时的默认值
    :return: 参数值
    """
    json_data = request.json
    form_data = request.form
    args_data = request.args
    file_data = request.files
    if json_data and key in json_data:
        return json_data.get(key, default)
    elif key in form_data:
        return form_data.get(key, default)
    elif key in args_data:
        # 规范页码信息
        if key in ('pageIndex', 'pageSize'):
            args_data = dict(args_data)
            try:
                pageIndex = int(args_data.get('pageIndex'))
                if pageIndex < 0:
                    args_data['pageIndex'] = 1
            except Exception as e:
                args_data['pageIndex'] = 1
            try:
                pageSize = int(args_data.get('pageSize'))
                if pageSize < 0:
                    args_data['pageSize'] = PageSize.COMMON
            except Exception as e:
                args_data['pageSize'] = PageSize.COMMON
        return args_data.get(key, default)
    elif key in file_data:
        return file_data.get(key, default)
    else:
        return default
