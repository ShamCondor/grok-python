#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/5/16 21:03
# @Author : Matrix
# @Site : https://github.com/blackmatrix7
# @File : unwrap.py
# @Software: PyCharm
from inspect import unwrap, signature
from functools import wraps

__author__ = 'blackmatrix'


def test_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('test_decorator')
        return func(*args, **kwargs)
    return wrapper


def test_decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('test_decorator2')
        return func(*args, **kwargs)
    return wrapper


def test_decorator3(func):
    def wrapper(*args, **kwargs):
        print('test_decorator3')
        return func(*args, **kwargs)
    return wrapper


def test_decorator4(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('test_decorator4')
        return func(*args, **kwargs)
    return wrapper


# 测试只有一个装饰器的情况下，能否正常解包
@test_decorator
def spam(value):
    print(value, '\n')


# 测试两个装饰器情况下，能否正常解包
@test_decorator2
@test_decorator
def spam2(value):
    print(value, '\n')


# 测试多个装饰器情况下，其中一个装饰器的包装器没有使用@wraps
@test_decorator3
@test_decorator2
@test_decorator
def spam3(value):
    print(value, '\n')


def callback(obj):
    sig = signature(obj=obj)
    params = sig.parameters
    print(params)

if __name__ == '__main__':
    print('调用被装饰的函数spam，装饰器生效，输出 test_decorator')
    spam(value='decorated_spam')

    print('使用 unwrap 获取被包装的函数，命名为unwrap_spam')
    unwrap_spam = unwrap(spam)
    print(unwrap_spam, '\n')

    print('调用已经解包装的函数命名为unwrap_spam，装饰器没有生效，没有输出 test_decorator')
    unwrap_spam(value='unwrap_spam')

    print('测试两个装饰器情况下，能否正常解包\n'
          '测试结果，两个装饰器也能正常获取到被包装的函数')
    unwrap_spam2 = unwrap(spam2)
    unwrap_spam2(value='unwrap_spam2')

    print('测试多个装饰器情况下，其中一个装饰器的包装器没有使用@wraps\n'
          '装饰链中，unwrap只能解包到未使用@wraps的装饰器')
    unwrap_spam3 = unwrap(spam3)
    unwrap_spam3(value='unwrap_spam3')

    print('测试 stop 参数传入的回调函数，回调函数每次接受一个函数对象（比如包装器函数）\n'
          '当回调函数返回True时，会提前中止解包过程\n'
          '如果回调函数没有返回True，则返回装饰链中最后一个对象')
    unwrap_spam = unwrap(spam, stop=callback)


