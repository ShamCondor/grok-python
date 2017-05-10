#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/10 22:30
# @Author  : Matrix
# @Site    : 
# @File    : extend.py
# @Software: PyCharm
from inspect import signature, Parameter
__author__ = 'blackmatrix'


def spam(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    print(signature(spam))
    sig = signature(spam)
    parms = [Parameter(name='d', kind=Parameter.KEYWORD_ONLY)]
    spam.__signature__ = sig.replace(parameters=parms)
    # 当对象中存在__signature__属性时，获取装饰链中的函数签名，都会返回__signature__的值，但是只是在signature()函数中返回__signature__的值，本身并不会改变函数的参数
    print(signature(spam))
    # 并不会影响函数的参数
    spam(1, 2, 3)
