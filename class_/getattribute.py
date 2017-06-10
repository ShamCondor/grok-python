#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 20:08
# @Author  : Matrix
# @Site    : 
# @File    : getattribute.py
# @Software: PyCharm

__author__ = 'blackmatrix'


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
