#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 20:33
# @Author  : Matrix
# @Site    :
# @File    : func_method.py
# @Software: PyCharm
from functools import wraps

__author__ = 'blackmatrix'

# 关于函数与方法的一些感想和测试


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


def the_function():
    """
    函数
    :return: 
    """
    pass


class TheClass:

    def __call__(self, *args, **kwargs):
        return self

    @classmethod
    def class_method(cls):
        """
        类方法
        :return: 
        """
        pass

    def instance_method(self):
        """实例方法"""
        return self

    @staticmethod
    def static_method():
        """
        静态方法
        :return: 
        """
        pass

    @test_decorator
    def decorated_func(self):
        pass

if __name__ == '__main__':

    the_class = TheClass()

    # 类方法和实例方法都是方法（method）
    print('class_method type {type} '.format(type=type(TheClass.class_method)))
    # 执行结果 class_method type <class 'method'>
    print('instance_method type {type} '.format(type=type(the_class.class_method)))
    # 执行结果 instance_method type <class 'method'>

    # 函数是Python中一个可调用对象，而方法是一种特殊的类函数
    print('the_function type {type} '.format(type=type(the_function)))
    # 执行结果 the_function type <class 'function'>

    # 比较奇怪的是静态方法，写在类中，却是函数
    # 通过实例调用静态方法
    print('static_method type {type} '.format(type=type(the_class.static_method)))
    # 执行结果 static_method type <class 'function'>
    # 通过类调用静态方法
    print('static_method type {type} '.format(type=type(TheClass.static_method)))
    # 执行结果 static_method type <class 'function'>
    # 从执行结果上看，静态方法无论是类调用还是实例调用，都是函数
    # 从官方文档，对于Method Objects的释义来看，Methods are always bound to an instance of a user-defined class
    # 方法(Method) 总是和类或类实例绑定，只有满足这个条件才称之为方法，而静态方法，即不和类绑定，也不和实例绑定，所以应该是方法

    # 装饰器本身会不会改变被装饰函数的类型，编写个装饰器试试
    # 测试，装饰器本身也是个函数
    print('test_decorator type {type} '.format(type=type(test_decorator)))
    # 执行结果 test_decorator type <class 'function'>

    # 将装饰器装饰器到实例方法上
    # 检查被装饰的方法的类型
    print('decorated_func type {type} '.format(type=type(the_class.decorated_func)))
    # 执行结果，依旧是方法 decorated_func type <class 'method'>
    # 从测试结果得知，装饰器不会影响被装饰方法或函数的类型

    # 如果类实现__call__方法
    # 执行结果True 其实例变为可调用对象
    print('class_instance callable {callable} '.format(callable=callable(the_class)))
    # 实例的类型依旧是这个类，而不会变成函数或方法
    print('class_instance type {type} '.format(type=type(the_class)))
    # 执行结果 class_instance type <class '__main__.TheClass'>



