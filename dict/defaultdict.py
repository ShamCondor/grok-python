#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 20:12
# @Author  : Matrix
# @Site    : 
# @File    : defaultdict.py
# @Software: PyCharm
import random
import unittest
from collections import defaultdict

__author__ = 'blackmatrix'


"""
defaultdict的说明与使用

通常情况下，获取dict中不存在的key时，会引发KeyError的异常。
使用defaultdict，可以在获取不存在的Key时，为这个Key的Value赋一个默认值

概要：
1.  defaultdict的第一个参数可以接受一个无参数的函数，当获取不存在的Key时，将这个函数的执行结果作为Value返回
2.  defaultditc的第二个参数，还可以接受一个类型
3.  defaultdict的第二个参数为初始化时的值
"""


class DefaultDictTestCase(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def testDefaultDictValue(self):
        """
        通常情况下，defaultdict的赋值和取值，与普通的dict没什么区别
        第二个参数为defaultdict初始化时的值，如果不传入，则默认为{}
        """
        foo = defaultdict(lambda: "hello", {'x': 'x'})
        self.assertEqual(foo['x'], 'x')

    def testDefaultDictFactoryFunc(self):
        """
        defaultdict可以接受一个无参数的函数，当获取不存在的Key时，将这个函数的执行结构作为Value返回
        """
        # 这里为了便于阅读，将一个无参数的lamda函数传递给defaultdict
        foo = defaultdict(lambda: "hello")
        self.assertEqual(foo['x'], 'hello')
        self.assertEqual(foo['y'], 'hello')

    def testDefaultDictNotFactoryFunc(self):
        """
        如果在初始化的时候，没有传入工厂函数
        那么在访问不存在的Key时，跟普通的dict一样会引发KeyError
        """
        foo = defaultdict()
        with self.assertRaises(KeyError):
            assert foo['x']

    def testDefaultKeyMissing(self):
        """
        defaultdict，对于dict，增加__missing__的魔法方法
        当访问的key不存在时，则调用__missing__方法，方法会调用defaultdict初始化时的工厂函数
        返回默认值
        """
        foo = defaultdict(lambda: "hello")
        # 这个例子可以看出，foo.__missing__('x')和foo['x']是等价的
        self.assertEqual(foo.__missing__('x'), 'hello')

    def testDefaultDcitRandomValue(self):
        """
        Python官方手册关于defaultdict的描述
        https://docs.python.org/3/library/collections.html#collections.defaultdict
        其中有一句话"this value is inserted in the dictionary for the key, and returned."
        就是说当调用工厂函数，返回一个值时，这个值已经被插入到defaultdict中
        所以，每次读取做个Key对应的value，应该是完全一样的
        """
        # 为了验证，将工厂函数设置为返回一个随机数
        foo = defaultdict(lambda: random.random())
        # 读取一次 x 的值，并赋值给变量 x
        x = foo['x']
        # 每次foo读取x的值，都是固定的
        # 可见在读取x的值时，只有第一次会调用工厂函数返回默认值，后续都是从defaultdict中直接返回做个值
        self.assertEqual(foo['x'], x)
        # 进一步做验证，可见x的值，在foo.values()中，可见这个值已经被插入到defaultdict中
        self.assertIn(x, foo.values())
       


if __name__ == '__main__':
    unittest.main()
