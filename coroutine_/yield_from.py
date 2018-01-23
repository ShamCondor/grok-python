#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/19 上午10:48
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : yield_from.py
# @Software: PyCharm

__author__ = 'blackmatrix'

"""
简单的例子
这里的yield from只是起到一个简化for循环的作用。
foo1 和 foo2是等价的
"""


def foo1(values: list):
    yield from values


def foo2(values: list):
    for var in values:
        yield var

print(list(foo1([1, 2, 3, 4, 5])))
print(list(foo2([1, 2, 3, 4, 5])))
# [1, 2, 3, 4, 5]


"""

"""


def averager():
    """
    使用yield接收数值，并求平均值
    捕获到StopIteration时，返回计算所得的平均值
    :return:
    """
    count = 0
    total = 0.0
    average = 0.0
    while True:
        try:
            value = yield
            count += 1
            total += value
            average = total/count
        except StopIteration:
            break
    return average

"""
假设一个新需求，需要在求平均值之前，需要进行一些数据处理
比如调用接口、操作数据库之类的
但是原有的averager已经在其他模块中使用，为了不影响其他模块的功能，
现在需要重新封装一个求平均值的方法，但是要求复用之前的函数，避免代码的冗余
"""


def averager2():
    """
    看起来有点复杂，这还是只是假设调用者只会throw(StopIteration)的情况
    如果加上预激活生成器、对close方法的处理，还要捕获throw的其他异常等等
    函数会更加复杂
    :return:
    """
    # 假设print是一个很复杂的功能
    print('调用外部接口，并且操作数据库')
    avg = averager()
    next(avg)
    while True:
        try:
            value = yield
            avg.send(value)
        except StopIteration:
            try:
                avg.throw(StopIteration)
            except StopIteration as e:
                return e.value

avg2 = averager2()
next(avg2)
avg2.send(15)
avg2.send(23)
avg2.send(43)
avg2.send(87)
try:
    avg2.throw(StopIteration)
except StopIteration as ex:
    print(ex.value)
    # 42.0


"""
现在改由yield from来实现
"""


def grouper():
    """
    定义一个委托生成器
    :return:
    """
    # 还是这个假设的，很复杂的功能
    print('调用外部接口，并且操作数据库')
    while True:
        yield from averager()

group = grouper()
next(group)
group.send(15)
group.send(23)
group.send(43)
group.send(87)
try:
    group.throw(StopIteration)
except StopIteration as ex:
    print(ex.value)
    # 42.0

