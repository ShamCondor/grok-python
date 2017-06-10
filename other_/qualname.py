#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/6/10 上午12:22
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: qualname.py
# @Software: PyCharm

__author__ = 'blackmatix'


class A:

    class InnerA:
        pass


class SubA(A):
    pass


if __name__ == '__main__':
    print(A.__qualname__)
    print(A.InnerA.__qualname__)
    print(SubA.__qualname__)
    a = A()
    # __qualname__ 是类方法,而且没办法通过实例获取
    # print(a.__qualname__)
