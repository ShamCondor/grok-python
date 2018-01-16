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
    :return:
    """
    count = 0
    total = 0.0

    def _averager(value):
        nonlocal total, count
        total += value
        count += 1
        average = total/count
        return average

    return _averager

# 调用外层函数averager，得到内层函数_averager的对象，赋值给avg
# 此时闭包形成，外层函数的变量total, count, average会被保持
avg = averager()
# 每次调用内层函数avg时，外层函数变量的值都会被记住
# 第一次调用，外层函数的变量count=1, total=10.0, average=10.0
print(avg(10))
# 10.0
# 第二次调用，外层函数变量的值不会重置，仍然保持上次调用的结果
# 此时 count=2, total=30.0, average=15.0
print(avg(20))
# 15.0
# 第三次调用，外层函数变量的值仍然会保持上次调用的结果
# 此时 count=3, total=36.0, average=12.0
print(avg(6))
# 12.0


# 以类实现类似上面闭包的功能
class Averager:

    def __init__(self):
        self.count = 0
        self.total = 0.0

    def __call__(self, value):
        self.total += value
        self.count += 1
        average = self.total/self.count
        return average

avg_cls = Averager()

print(avg_cls(10))
# 10.0
print(avg_cls(20))
# 15.0
print(avg_cls(6))
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
