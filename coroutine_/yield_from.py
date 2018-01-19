#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/19 上午10:48
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : yield_from.py
# @Software: PyCharm

__author__ = 'blackmatrix'


def foo1():
    yield from [1, 2, 3, 4, 5]


def foo2():
    for var in [1, 2, 3, 4, 5]:
        yield var

print(list(foo1()))
print(list(foo2()))
# [1, 2, 3, 4, 5]

if __name__ == '__main__':
    pass
