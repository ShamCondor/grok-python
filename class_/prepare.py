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
原书中代码带有类型判断的描述符, 为了易于理解, 将此部分代码去除,并做一些简化和修改
注释部分为个人理解

本例最核心的代码就是__prepare__返回一个OrderDict,这样在处理类定义体的时候,会将类属性的
创建顺序在OrderDict中保存下来

参考:
https://www.python.org/dev/peps/pep-3115/#abstract
"""


class OrderMeta(type):

    def __new__(mcs, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            '''
            书中代码,对value类型做了判断,只对描述符的类属性进行记录,而其他的属性不会记录顺序
            如果不做类型判断,那就会出现Stock 没有 __qualname__ 的异常
            原因是Structrue的as_csv读取的是实例成员,而__qualname__这个类属性比较特殊,无法通过
            实例去获取到,所以在使用类的实例self去获取__qualname__属性时就会引发异常。
            针对此问题,在as_csv函数中做了判断。
            '''
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
    中,最后传递给元类的__new__方法, __new__方法,调用这个命名空间的映射型对象,完成类对象的
    创建工作,最终返回一个创建之后的类对象。
    为进行测试,在返回的命名空间中,增加了一个hello值为python的属性,可以正常的在类实例中打印出来。
    '''
    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict(hello='python')

    '''
    做个总结:
    1.  即使元类不需要__prepare__方法,在默认的元类type也会实现它,便于后续的子类通过super()调用
    2.  __prepare__返回一个类dict对象, 用于在处理类定义体(evaluation of the class_ body)时,存储类的成员
    3.  __prepare__可以返回一个普通的dict,获取自定义的映射型对象
    4.  __prepare__通常都需要加上类方法装饰器,因为它是在类对象(元类的实例)时创建的, 这个时候元类的实例(就是类对象)还没有创建出来,
        所以无法定义为实例方法
    '''


class Stock(metaclass=OrderMeta):
    name = 'Good'
    shares = 100
    price = 490.1

    '''
    此处对原书代码做了修改,增加hasattr的判断，主要为避免
    类实例读取__qualname__方法导致的异常
    '''
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order if hasattr(self, name))


if __name__ == '__main__':
    s = Stock()
    # stock_dict = Stock.__dict__
    # print(stock_dict)
    # print(getattr(Stock, '__qualname__'))
    print(s.name)
    print(s.hello)
    print(s.as_csv())
