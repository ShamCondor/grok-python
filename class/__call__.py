#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 20:44
# @Author  : Matrix
# @Site    : 
# @File    : __call__.py
# @Software: PyCharm
import unittest

__author__ = 'blackmatrix'


'''
本例主要演示__call__方法的使用

概要:
1.  __call__方法可以让一个实例变为可调用对象
2.  __call___是个实例方法,带self参数
3.  __call__方法只对类实例有效,如果想对类生效,需在元类中定义
4.  类定义了__call__方法后,实例instance()相当于instance.__call__()
'''


class ClassMeta(type):

    def __call__(cls, *args, **kwargs):
        return 'ClassMeta.__call__  running'


class Foo:

    def __call__(self, *args, **kwargs):
        return 'Foo.__call__  running'


class Bar(metaclass=ClassMeta):
    pass


class CallTestCase(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def testFooCall(self):
        """
        类对象Foo增加__call__方法后，其实例就变为可调用对象
        调用实例foo(), 会返回__call__的执行结果
        """
        foo = Foo()
        # 类一直都是可调用对象
        self.assertTrue(Foo)
        # foo已经变成可调用对象
        self.assertTrue(callable(foo))
        # foo()的调用结果，就是Foo.__call__的结果
        self.assertEqual(foo(), 'Foo.__call__  running')
        # __call__是实例方法，需要传入self，所以这里传入实例foo
        self.assertEqual(foo(), Foo.__call__(foo))

    def testMetaTypeCall(self):
        """
        __call__是实例方法
        如果希望让类本身变为可调用对象，那么需要在元类中定义__call__方法
        因为类是元类的实例
        --------------------------------------
        类Bar中，因为元类是ClassMeta，而ClassMeta定义了__call__方法
        所以，在调用Bar()时，不会执行类的实例化，而是执行元类的__call__方法
        """
        self.assertEqual(Bar(), 'ClassMeta.__call__  running')

    def testInstanceMethod(self):
        """
        实例方法的本质就是描述符
        所以，通过类去访问描述符符时，等同于调用__call__的__get__方法，返回的是__call__自身
        """
        # 这个例子可以看出 Foo.__call__ 就是 Foo.__call__.__get__(None, Foo)
        self.assertTrue(Foo.__call__ is Foo.__call__.__get__(None, Foo))


if __name__ == '__main__':
    unittest.main();
