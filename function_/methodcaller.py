#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/7/2 20:38
# @Author  : BlackMatrix
# @Site : 
# @File : methodcaller.py
# @Software: PyCharm
from operator import methodcaller
__author__ = 'blackmatrix'

"""
测试内建函数 methodcaller的用法

概要：
1   methodtype返回一个可调用对象
2   methodtype接受若干个参数，第一个参数为函数名，后续的参数为第一个函数所需的参数
3   methodtype返回的对象接受一个对象，并调用这个对象的函数，函数名即第二步传入的函数名
"""


class A:

    @staticmethod
    def func_a(*args, **kwargs):
        print(args, kwargs)


class B:
    pass


if __name__ == '__main__':
    # 返回可调用对象f，f接受一个对象，并调用它的func_a方法，并返回结果
    f = methodcaller('func_a', 'hello', word='python')
    # f接受参数类A，同时调用A的func_a方法
    r = f(A)
    # 等同于A.func_a( 'hello', word='python')
    A.func_a('hello', word='python')
    # 如果f接受的对象没有方法func_a，会引发AttributeError异常
    r = f(B)

