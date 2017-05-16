#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/5/16 21:03
# @Author : Matrix
# @Site : https://github.com/blackmatrix7
# @File : common.py
# @Software: PyCharm
from functools import wraps


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


__author__ = 'blackmatrix'

if __name__ == '__main__':
    pass
 