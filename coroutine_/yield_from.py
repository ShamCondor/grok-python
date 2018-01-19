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
yield只能向直接调用者产出值
不能封装到独立的函数中向函数的调用者产出值
"""


def bar():
    yield foo2([1, 2, 3, 4, 5])


print(bar())




"""

"""


# def averager():
#     """
#     使用yield接收数值，并求平均值
#     :return:
#     """
#     count = 0
#     total = 0.0
#     average = 0.0
#     while True:
#         try:
#             value = yield
#             count += 1
#             total += value
#             average = total/count
#         except StopIteration:
#             return average
#
#
# items_list = [[19, 23, 12, 43, 12], [76, 14, 43, 64, 17, 36], [45, 51, 64, 34, 64, 13, 75]]
#
#
# for items in items_list:
#     avg = averager()
#     next(avg)
#     for item in items:
#         avg.send(item)
#     else:
#         try:
#             avg.throw(StopIteration)
#         except StopIteration as ex:
#             print(ex)
#
#
# def grouper():
#     """
#     定义一个委托生成器
#     :return:
#     """
#     yield from averager()
#
# group = grouper()
# next(group)
# for items in items_list:
#     group.send(items)
#     try:
#         group.throw(StopIteration)
#     except StopIteration as ex:
#         print(ex)



if __name__ == '__main__':
    pass
