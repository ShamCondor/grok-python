#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 20:33
# @Author  : Matrix
# @Site    :
# @File    : func_method.py
# @Software: PyCharm
from common_.decorator import test_decorator

__author__ = 'blackmatrix'

'''
本例验证函数与方法的区别

概要:
1.  函数(function)是Python中一个可调用对象(callable), 方法(method)是一种特殊的函数
2.  与类或实例绑定的才能称之为方法,所以类方法和实例方法都是 method
3.  静态方法没有和任何类或实例绑定,所以静态方法是个函数
4.  装饰器不会改变被装饰函数或方法的类型
5.  类实现__call__方法,其实例也不会变成方法或函数,依旧是类的实例
6.  使用callalble() 只能判断对象是否可调用,不能判断是不是函数或方法
7.  判断函数或方法应该使用type(obj)
'''


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
    # 执行结果 class_method type <class_ 'method'>
    print('instance_method type {type} '.format(type=type(the_class.class_method)))
    # 执行结果 instance_method type <class_ 'method'>

    # 函数是Python中一个可调用对象，而方法是一种特殊的类函数
    print('the_function type {type} '.format(type=type(the_function)))
    # 执行结果 the_function type <class_ 'function_'>

    # 比较奇怪的是静态方法，写在类中，却是函数
    # 通过实例调用静态方法
    print('static_method type {type} '.format(type=type(the_class.static_method)))
    # 执行结果 static_method type <class_ 'function_'>
    # 通过类调用静态方法
    print('static_method type {type} '.format(type=type(TheClass.static_method)))
    # 执行结果 static_method type <class_ 'function_'>
    # 从执行结果上看，静态方法无论是类调用还是实例调用，都是函数
    # 从官方文档，对于Method Objects的释义来看，Methods are always bound to an instance of a user-defined class_
    # 方法(Method) 总是和类或类实例绑定，只有满足这个条件才称之为方法，而静态方法，即不和类绑定，也不和实例绑定，所以应该是方法

    # 装饰器本身会不会改变被装饰函数的类型，编写个装饰器试试
    # 测试，装饰器本身也是个函数
    print('test_decorator type {type} '.format(type=type(test_decorator)))
    # 执行结果 test_decorator type <class_ 'function_'>

    # 将装饰器装饰器到实例方法上
    # 检查被装饰的方法的类型
    print('decorated_func type {type} '.format(type=type(the_class.decorated_func)))
    # 执行结果，依旧是方法 decorated_func type <class_ 'method'>
    # 从测试结果得知，装饰器不会影响被装饰方法或函数的类型

    # 如果类实现__call__方法
    # 执行结果True 其实例变为可调用对象
    print('class_instance callable {callable} '.format(callable=callable(the_class)))
    # 实例的类型依旧是这个类，而不会变成函数或方法
    print('class_instance type {type} '.format(type=type(the_class)))
    # 执行结果 class_instance type <class_ '__main__.TheClass'>



