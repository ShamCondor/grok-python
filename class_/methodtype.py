#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/6/13 20:26
# @Author  : BlackMatrix
# @Site : 
# @File : methodtype.py
# @Software: PyCharm
from types import MethodType
__author__ = 'blackmatrix'

'''
本例演示如何将一个方法绑定到实例或类上
'''


class ClassA:

    def instance_method(self):
        print('instance_method', self)

    @classmethod
    def cls_method(cls):
        print('cls_method', cls)

    @staticmethod
    def static_method():
        print('static_method')


class ClassB:
    pass


def func_a(self=None):
    print('func_a', self)


def func_b(cls):
    print('func_b', cls)


def func_c(self):
    print('func_c', self)


if __name__ == '__main__':
    class_a = ClassA()

    print('测试实例方法、静态方法、类方法与实例和类的关系')
    # 类中的实例方法，与类本身并没有绑定关系
    # <function ClassA.instance_method at 0x0000022744592488>
    print(ClassA.instance_method)
    # 类中的静态方法，与类也没有绑定关系
    # <function ClassA.static_method at 0x0000027A5F6D0598>
    print(ClassA.static_method)
    # 而类中的类方法，是和这个类存在绑定关系的
    # <bound method ClassA.cls_method of <class '__main__.ClassA'>>
    print(ClassA.cls_method)

    print('-' * 50)

    # 实例中的实例方法，与实例存在绑定关系
    # 因为当通过一个实例去访问类中的某方法时，会形成绑定关系，将实例作为第一个参数self传入。
    # <bound method ClassA.instance_method of <__main__.ClassA object at 0x000001B117D07710>>
    print(class_a.instance_method)
    # 类方法与实例也存在绑定关系，所以实例可以直接调用类方法
    # <bound method ClassA.cls_method of <class '__main__.ClassA'>>
    print(class_a.cls_method)
    # 静态方法与实例没有绑定关系
    # <function ClassA.static_method at 0x0000027D36340620>
    print(class_a.static_method)

    print('-' * 50)

    print('通过将函数赋值给类属性，尝试将一个函数绑定到类或实例上')
    ClassA.func_a = func_a
    # 直接将函数赋值给类，不会创建类与函数的绑定关系
    # <function func_a at 0x10e41ff28>
    print(ClassA.func_a)
    # 对于赋值之前创建得实例，因为是通过实例访问，所以也会存在绑定关系
    # <bound method func_a of <__main__.ClassA object at 0x10e4330b8>>
    print(class_a.func_a)

    print('这种方法存在一些局限性，当把一个函数直接赋值给实例时，无法正常创建绑定关系')
    class_a.func_c = func_c
    # <function func_c at 0x10e59f1e0>
    print(class_a.func_c)
    # 下面的调用方式，因为没有绑定关系，无法获取到实例自身，即不会作为self传入
    # class_a.func_c()

    print('-' * 50)

    print('所以就需要引入 MethodType，将一个函数绑定到实例或类上')

