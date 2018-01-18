#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/18 下午3:14
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : yield_.py
# @Software: PyCharm

__author__ = 'blackmatrix'

"""
使用生成器简单的实现求平均值
"""


def averager1():
    """
    使用yield接收数值，并求平均值
    :return:
    """
    count = 0
    total = 0.0
    average = 0.0
    while True:
        value = yield average
        count += 1
        total += value
        average = total/count


avg1 = averager1()
# 预激活协程，程序执行到yield出暂停，产出average，输出0.0
print(next(avg1))
# 0.00
# 向协程发送数字
print(avg1.send(10))
# 10.0
print(avg1.send(20))
# 15.0
print(avg1.send(30))
# 20.0


"""
通过发送哨符终止生成器循环
"""


def averager2():
    """
    使用yield接收数值，并求平均值
    相对于上面的例子，增加了使协程退出的哨符
    :return:
    """
    count = 0
    total = 0.0
    average = 0.0
    while True:
        value = yield average
        # 当value为None时，退出循环
        if value is None:
            break
        count += 1
        total += value
        average = total/count

avg2 = averager2()
# 预激活协程，因为yield右边没有变量，所以不会产出值
print(next(avg2))
# 0.0
# 向协程发送数字
print(avg2.send(10))
# 10.0
print(avg2.send(20))
# 15.0
print(avg2.send(30))
# 20.0
# 生成器循环终止时会抛出StopIteration
# 所以做一个异常捕获
try:
    avg2.send(None)
except StopIteration:
    pass


"""
通过.throw()发送异常来终止生成器对象的循环
1.  将一个异常直接发送给生成器，会导致生成器在yield处暂停时，出现异常
2.  如果生成器能处理传入的异常，那么生成器的代码会继续执行，直到下一次遇到yield表达式暂停
3.  如果生成器不能正确处理这个异常，那么会将异常抛出，返回给调用者
4.  如果收到了GeneratorExit异常，生成器不能返回值，否则会引发RuntimeError异常
"""


# 对第一个函数averager1进行修改，增加处理ValueError的代码
def averager3():
    """
    使用yield接收数值，并求平均值
    对第一个函数averager3进行修改，增加处理ValueError的代码
    :return:
    """
    count = 0
    total = 0.0
    average = 0.0
    while True:
        try:
            value = yield average
            count += 1
            total += value
            average = total/count
        except ValueError:
            # 如果捕获到ValueError，什么都不做
            # 这样生成器会继续循环，直到再次遇到yield暂停
            pass


avg3 = averager3()
next(avg3)
print(avg3.send(10))
# 10.0
print(avg3.send(20))
# 15.0
# throw一个生成器可以处理的异常ValueError，没有任何影响
# 生成器会继续运行，产出average，因为在yield处就报错，后续的代码没有执行
# 所以average仍然为15.0
# yield会将average产出，产出的值作为调用者执行生成器的throw方法的返回值，最终输出15.0
print(avg3.throw(ValueError))
# 15.0
# throw一个生成器不能处理的异常，生成器循环终止
try:
    print(avg3.throw(TypeError))
except TypeError:
    print('生成器无法处理TypeError，异常向上冒泡抛出，循环终止')


# 对第三个函数averager3进行修改，改为捕获GeneratorExit异常并忽略
def averager4():
    """
    使用yield接收数值，并求平均值
    对第三个函数averager3进行修改，改为捕获GeneratorExit异常并忽略
    :return:
    """
    count = 0
    total = 0.0
    average = 0.0
    while True:
        try:
            value = yield average
            count += 1
            total += value
            average = total/count
        except GeneratorExit:
            # 如果捕获到GeneratorExit，什么都不做
            # 这样生成器会继续循环，直到再次遇到yield暂停
            yield 5
avg4 = averager4()
next(avg4)
print(avg4.send(10))
print(avg4.send(20))
avg4.throw(GeneratorExit)


