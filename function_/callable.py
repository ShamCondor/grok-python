#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/6/10 上午11:01
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: callable.py
# @Software: PyCharm

__author__ = 'blackmatix'


'''
本例演示使用callable()函数判断对象是否可调用

概要:
1.  callable(obj)判断对象是否可调用,返回bool
2.  返回True仍有可能调用失败,但是返回False绝对不可调用
3.  类定义了__call__方法,那么其实例就会变成可调用对象,返回True
4.  函数(function)和方法(method)都是可调用对象
'''


class A:
    pass


class B(A):

    def __call__(self):
        pass


def c():
    pass

if __name__ == '__main__':
    a = A()
    print(callable(a))
    b = B()
    print(callable(b))
    print(callable(c))



