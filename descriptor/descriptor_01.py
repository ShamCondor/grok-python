#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/7/13 下午3:17
# @Author : Matrix
# @Site : https://github.com/blackmatrix7/apizen
# @File : descriptor_base
# @Software: PyCharm

__author__ = 'blackmatrix'


class Descriptor:

    def __init__(self):
        pass

    def __get__(self, instance, owner):
        return self, instance, owner

    def __set__(self, instance, value):
        print(self, instance, value)

    def __delete__(self, instance):
        print(self, instance)


class ClassA(object):

    descriptor = Descriptor()


if __name__ == '__main__':
    # 实例化为对象a
    a = ClassA()
    # 从实例取值
    print(a.descriptor)
    # (<__main__.Descriptor object at 0x10c157438>, <__main__.ClassA object at 0x10c1574a8>, <class '__main__.ClassA'>)

    # 从类取值
    print(ClassA.descriptor)
    # (<__main__.Descriptor object at 0x10c157438>, None, <class '__main__.ClassA'>)

    # 对描述符进行赋值
    a.descriptor = 2
    # <__main__.Descriptor object at 0x10f0b1518> <__main__.ClassA object at 0x10f0b1588> 2
