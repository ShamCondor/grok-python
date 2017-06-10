#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 20:08
# @Author  : Matrix
# @Site    : 
# @File    : getattribute.py
# @Software: PyCharm

__author__ = 'blackmatrix'


'''
本例主要演示 __getattribute__ 的使用

概要:
1.  __getattribute__ 可以无限制的访问类实例的所有属性。
    这里需要注意,是访问类实例而不是类对象,只对实例有效。
    如果要对类对象自身产生效果,需要在元类中定义__getattribute__
2.  如果同时定义了__getattr__和__getattribute__,
    __getattr__通常不会被调用,除非__getattribute__明确抛出
    AttributeErro 异常
3.  在__getattribute__方法中,直接通过 . 号运算取值和通过__dict__
    取值,都会引发无限递归
4.  为了避免无限递归,要调用父类的__getattribute__方法来获取当前类属性的值
5.  __getattribute__ 在python 2.x 中,只有新式类可用
'''


class ClassA:

    x = 'a'

    '''
    当在__getattribute__代码块中，再次执行属性的获取操作时，
    会再次触发__getattribute__方法的调用，代码将会陷入无限递归，
    直到Python递归深度限制（重载__setter__方法也会有这个问题）。
    同时，也没办法通过从__dict__取值的方式来避免无限递归。
    为了避免无限递归，应该把获取属性的方法指向一个更高的超类，
    例如object（因为__getattribute__只在新式类中可用，而新式类所有的类都显式或隐式地继承自object，
    所以对于新式类来说，object是所有新式类的超类）。
    '''
    def __getattribute__(self, name):
        # 使用super获取代理类,执行父类的__getattribute__避免无限递归
        return super().__getattribute__(name)
        # 无限递归
        # return self.__dict__[name]


if __name__ == '__main__':
    a = ClassA()
    print(a.x)
