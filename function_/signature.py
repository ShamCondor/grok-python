#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/6/10 下午9:03
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: signature.py
# @Software: PyCharm
from inspect import Signature, Parameter

__author__ = 'blackmatix'


'''
本例主要演示函数签名的使用和获取

概要:
1.  bind创建位置和关键字的参数映射到被绑定的参数中

'''

parms = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
         Parameter('y', Parameter.POSITIONAL_OR_KEYWORD),
         Parameter('z', Parameter.KEYWORD_ONLY, default=9)]


sig = Signature(parms)


def func(*args, **kwargs):
    # bind 方法, 创建一个签名中的参数映射到函数接受的参数中。
    # 在这个例子中,将外部定义的parms建立映射,绑定到函数接收的参数中。
    # 当函数参数与签名中的参数相匹配时,返回BoundArguments对象,
    # 反之则抛出 TypeError
    bound_value = sig.bind(*args, **kwargs)
    for name, value in bound_value.arguments.items():
        print(name, value)

if __name__ == '__main__':
    func(1, 2, z=3)
    func(1, 2)
    # 引发异常
    # func(1)
