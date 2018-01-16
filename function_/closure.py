#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/7/11 21:19
# @Author  : BlackMatrix
# @Site : 
# @File : closure.py
# @Software: PyCharm
import sys
__author__ = 'blackmatrix'

"""
闭包的一些例子
"""


def averager():
    """
    闭包实现求平均值的例子
    每次传入一个数字，返回所有传入的数字的平均值
    :param value: 传入的数字
    :return:
    """
    count = 0
    total = 0.0
    average = None

    def _averager(value):
        nonlocal total, count, average
        total += value
        count += 1
        average = total/count
        return average

    return _averager


avg = averager()
print(avg(10))
# 10.0
print(avg(20))
# 15.0
print(avg(6))
# 12.0


class ClosureInstance:
    """
    把闭包模拟成类
    """

    def __init__(self, locals=None):
        if locals is None:
            # 等同于函数内部获取的local()
            locals = sys._getframe(1).f_locals
        self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()


def Stack():

    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    _locals = locals()

    return ClosureInstance(_locals)


if __name__ == '__main__':
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(len(s))
