#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/6/9 下午10:01
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: prepare.py
# @Software: PyCharm
from collections import OrderedDict


__author__ = 'blackmatix'

"""
本例来自《Python cookbook》 9.14 获取类属性的定义顺序
"""


class Typed:
    _except_type = type(None)

    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._except_type):
            raise TypeError
        instance.__dict__[self.name] = value


class Integer(Typed):
    _except_type = int


class String(Typed):
    _except_type = str


class Float(Typed):
    _except_type = float


class OrderMeta(type):

    def __new__(mcs, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(mcs, clsname, bases, d)

    '''
    __prepare__会返回类的命名空间,一个类字典对象, 作为__new__方法的clsdict参数
    因为,在此例中返回的是OrderDict,所以在__new__方法接收的参数中,是存在顺序的,
    可以通过for循环将这个顺序存储到列表中。
    那么,可以这么理解, 在一个类的创建过程中,先由__prepare__返回的类字典对象作为命名空间(如果
    元类没有定义__prepare__,那么会通过元类的父类type去实现它), 接着一次获取类定义(为什么说
    是定义,因为这个时候类还未创建出来)中的成员(属性、也有可能是函数或方法), 存储到这个命名空间
    中,最后传递给元类的__new__方法, 元类调用这个命名空间的映射型对象,完成类对象的创建工作,最终
    返回一个创建之后的类对象。
    为进行测试,在返回的命名空间中,增加了一个hello值为python的属性,可以正常的在类实例中打印出来。
    '''
    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict(hello='python')

    '''
    做个总结:
    1.  即使元类不需要__prepare__方法,在默认的元类type也会实现它,便于后续的子类通过super()调用
    2.  __prepare__返回一个类dict对象, 用于在处理类定义体(evaluation of the class body)时,存储类的成员
    3.  __prepare__可以返回一个普通的dict,获取自定义的映射型对象
    4.  __prepare__通常都需要加上类方法装饰器,因为它是在类对象(元类的实例)时创建的, 这个时候元类的实例(就是类对象)还没有创建出来,
        所以无法定义为实例方法
    '''


class Structrue(metaclass=OrderMeta):
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)


class Stock(Structrue):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('Good', 100, 490.1)
    print(s.name)
    print(s.hello)
    print(s.as_csv())
