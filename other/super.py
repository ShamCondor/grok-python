#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/22 21:48
# @Author  : Matrix
# @Site    : 
# @File    : super.py
# @Software: PyCharm

__author__ = 'blackmatrix'


class A:

    def __init__(self):
        print('enter class A')
        super(A, self).__init__()
        print('leave class A')

    @staticmethod
    def static_method():
        print('A static_method')

    @classmethod
    def class_method(cls):
        print('A class method')

    def instance_method(self):
        print('A instance method')


class B(A):

    def __init__(self):
        print('enter class B')
        super(B, self).__init__()
        super(B, self).class_method()
        print('leave class B')


class C(B):

    def __init__(self):
        print('enter class C')
        super(B, self).__init__()
        print('leave class C')

        print('-' * 20)
        # 可以调用类方法
        super().class_method()
        # 可以调用静态方法
        super().static_method()
        # 可以调用实例方法
        super().instance_method()
        print('-' * 20)

        # 可以调用类方法
        super(C, C).class_method()
        # 可以调用静态方法
        super(C, C).static_method()
        # 无法调用实例方法
        # TypeError: instance_method() missing 1 required positional argument: 'self'
        # super(B, C).instance_method()
        # 应该是没有实例化，但是super对象不是可调用的，无法实例化
        print('-' * 20)

        # 可以调用类方法
        super(C, self).class_method()
        # 可以调用静态方法
        super(C, self).static_method()
        #  可以调用实例方法
        super(C, self).instance_method()
        print('-' * 20)

        # # 无法调用类方法
        # # AttributeError: 'super' object has no attribute 'class_method'
        # super(C).class_method()
        # # 无法调用静态方法
        # # AttributeError: 'super' object has no attribute 'static_method'
        # super(C).static_method()
        # # 无法调用实例方法
        # # AttributeError: 'super' object has no attribute 'instance_method'
        # super(C).instance_method()
        # # AttributeError: 'super' object has no attribute 'instance_method'


if __name__ == '__main__':
    c = C()
