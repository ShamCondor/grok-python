#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/6/10 上午10:04
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: decorator_.py
# @Software: PyCharm
from functools import wraps

__author__ = 'blackmatix'


def test_decorator(func):
    """
    装饰器，测试使用，无功能
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    pass
