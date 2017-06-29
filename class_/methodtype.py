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


def func_a(self=None):
    print('func_a', self)


def func_b(cls):
    print('func_b', cls)


def func_c(cls):
    print('func_c', cls)


if __name__ == '__main__':
    class_a = ClassA()
    '''
    先测试下实例方法、静态方法、类方法与实例和类的关系
    '''
    # 类中的实例方法，与类本身并没有绑定关系
    # <function ClassA.instance_method at 0x0000022744592488>
    print(ClassA.instance_method)
    # 类中的静态方法，与类也没有绑定关系
    # <function ClassA.static_method at 0x0000027A5F6D0598>
    print(ClassA.static_method)
    # 而类中的类方法，是和这个类存在绑定关系的
    # <bound method ClassA.cls_method of <class '__main__.ClassA'>>
    print(ClassA.cls_method)

    print('-' * 30)

    # 实例中的实例方法，与实例存在绑定关系
    # 因为在创建实例时，类会将实例方法绑定到实例上
    # <bound method ClassA.instance_method of <__main__.ClassA object at 0x000001B117D07710>>
    print(class_a.instance_method)
    # 类方法与实例也存在绑定关系，所以实例可以直接调用类方法
    # <bound method ClassA.cls_method of <class '__main__.ClassA'>>
    print(class_a.cls_method)
    # 静态方法与实例没有绑定关系
    # <function ClassA.static_method at 0x0000027D36340620>
    print(class_a.static_method)

    print('-' * 30)

    '''
    接着试试几种方法，将一个函数绑定到类或实例上。
    
    第一种方法，直接给类属性赋值，可以通过类进行调用，也可以通过实例调用。
    其中需要注意的是，通过实例调用，会将实例自身作为第一个参数self传入。
    所以，func_a 有个 self 参数，用来接收实例对象。
    '''
    ClassA.func_a = func_a
    # 直接将函数赋值给类，不会创建类与函数的绑定关系
    print(ClassA.func_a)
    # 对于赋值之前创建得实例，也会创建函数与实例的绑定关系
    print(class_a.func_a)

    print('-' * 30)
    '''
    第一种方法，存在一些局限性，本质上，只是给类属性赋值，并未建立类与函数的
    绑定关系。
    可以通过下面的方法来验证：
    '''
    # 只有在实例创建的时候，类才会将实例方法绑定到实例上，形成实例与实例方法的绑定
    # <bound method ClassA.instance_method of <__main__.ClassA object at 0x000002274459C588>>
    print(class_a.instance_method)

    # 在类创建之后赋值的方法，也没不会有绑定关系
    # <function func_a at 0x0000022744592510>
    print(ClassA.func_a)
    # 实例创建后，即使是之后赋值的方法，也会将其绑定到实例上
    print(class_a.func_a)
    # 而在实例创建之后，如果再对实例的属性进行赋值，这个时候是不会创建绑定关系的
    # 这就是这种赋值方式的局限性，只能在实例创建之前
    class_a.func_c = func_c
    print(class_a.func_c)
