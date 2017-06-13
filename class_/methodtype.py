#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/6/13 20:26
# @Author  : BlackMatrix
# @Site : 
# @File : methodtype.py
# @Software: PyCharm

__author__ = 'blackmatrix'

'''
本例演示如何将一个方法绑定到实例或类上
'''


class ClassA:

    def func_b(self):
        print('func_b', self)


def func_a(self=None):
    print('func_a', self)


def func_c(cls):
    print('func_c', cls)


if __name__ == '__main__':
    '''
    第一种方法，直接给类属性赋值，可以通过类进行调用，也可以通过实例调用。
    其中需要注意的是，通过实例调用，会将实例自身作为第一个参数self传入。
    所以，func_a 有个 self 参数，用来接收实例对象。
    '''
    ClassA.func_a = func_a
    class_a = ClassA()
    ClassA.func_a()
    class_a.func_a()
    '''
    第一种方法，存在一些局限性，本质上，只是给类属性赋值，并未建立类与函数的
    绑定关系。
    可以通过下面的方法来验证：
    '''
    print(class_a.func_b)
    print(ClassA.func_a)
