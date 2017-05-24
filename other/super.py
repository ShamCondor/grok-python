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
        super(__class__, self).__init__()
        super(B, self).class_method()
        print('leave class B')

    @staticmethod
    def static_method():
        # super().instance_method()
        # python 3 中可以直接使用super()方法进行实例化，本质上它是接收两个参数
        # 第一个参数是这个方法所属类，或这个方法所属的实例的类(type)
        # 第二个参数，官方的类注释比较简单，<first argument>
        # 这个<first argument>是指当前调用方法（或函数）的第一个参数
        # 如果是在实例方法中实例化super()，那么<first argument>就是实例方法的第一个参数self
        # 如果是在类方法中实例化super()，那么<first argument>就是类方法中的第一个参数cls
        # 如果是在静态方法中实例化super()，那么通常是不能正常运行的。除非特意将静态方法的第一个参数，
        # 设置成类的实例，或类的之类，否则都会因为不符合要求抛出如下异常
        # TypeError: super(type, obj): obj must be an instance or subtype of type
        print('B static_method')

    @staticmethod
    def static_method2(value):
        super().instance_method()
        print('B static_method2', value)

    @classmethod
    def class_method(cls):
        print('B class method')

    def instance_method(self):
        super().instance_method()
        print('B instance method')


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
        super(B, C).class_method()
        # 可以调用静态方法
        super(B, C).static_method()
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

        # 无法调用类方法
        # AttributeError: 'super' object has no attribute 'class_method'
        # super(C).class_method()
        # 无法调用静态方法
        # AttributeError: 'super' object has no attribute 'static_method'
        # super(C).static_method()
        # 无法调用实例方法
        # AttributeError: 'super' object has no attribute 'instance_method'
        # super(C).instance_method()
        # AttributeError: 'super' object has no attribute 'instance_method'

    @staticmethod
    def static_method2(value):
        print('C static_method', value)

    @classmethod
    def class_method(cls):
        super(B, C).class_method()
        print('C class method')

    def instance_method(self):
        print('C instance method')


if __name__ == '__main__':
    print(super(B, C).__repr__)
    # c = C()
    # b = B()
    # B.class_method()
