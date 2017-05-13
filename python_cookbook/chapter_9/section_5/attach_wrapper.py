#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/5/13 20:52
# @Author : Matrix
# @Site : https://github.com/blackmatrix7
# @File : attach_wrapper.py
# @Software: PyCharm
import logging
from functools import wraps, partial

__author__ = 'blackmatrix'


# 定义一个可由被包装函数修改的装饰器


def test_decorator(func):
    """
    装饰器，测试使用，无功能
    :param func: 
    :return: 
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


# 这个装饰器不太好理解
def attach_wrapper(obj, func=None):
    # 当func 为 None的时候，实际上执行的是下面例子中的attach_wrapper
    # 也就是装饰器的第一层函数，接收装饰器需要的对象
    # @attach_wrapper(obj=wrapper)，将需要处理的对象传入装饰器
    if func is None:
        # 返回的偏函数，实际上是下面例子中的 _attach_wrapper
        # 也就是装饰器的第二层函数，接受被包装的函数对象
        # 通过偏函数，只用一个函数，实现两个函数：外部函数接受需要处理的对象，及其内部包装器的功能
        # 很酷，很巧妙，但是不容易理解
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


# 如果这样写就非常容易理解了，如果被包装的方法存在，就把这个方法附加到被传入的对象中
def my_attach_wrapper(obj):
    def _attach_wrapper(func):
            setattr(obj, func.__name__, func)
    return _attach_wrapper


def logged(level, name=None, message=None):

    def dectorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(obj=wrapper)
        def set_level(newlevel):
            print('set level')
            nonlocal level
            level = newlevel

        @attach_wrapper(obj=wrapper)
        def set_message(newmsg):
            print('set message')
            nonlocal logmsg
            logmsg = newmsg
        return wrapper
    return dectorate


@test_decorator
@logged(logging.DEBUG)
def add(x, y):
    print(x + y)


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


if __name__ == '__main__':
    add(2, 3)
    add.set_level(logging.WARNING)
    spam()
