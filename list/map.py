#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/8/16 下午8:56
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: map_
# @Software: PyCharm
import unittest
from itertools import starmap

__author__ = 'blackmatrix'

"""
map和starmap的使用

概要：
map
1.  内建的map函数，接受一个函数对象，及N个可迭代对象。
2.  运行时，map会依次取出被迭代对象的每个元素，作为参数传递给接受的函数对象
3.  如果N个可迭代对象的长度不同，以最短的可迭代对象进行迭代，其他较长的可迭代对象中的元素会被忽略
4.  接受的可迭代对象的个数，必须与函数对象的参数个数匹配，否则会抛出缺少参数或参数过多的异常

starmap
1.  starmap 接受一个函数对象及一个可迭代对象，运行时，将可迭代对象中的元素逐个解包，以位置传值的形式，按顺序传递给函数对象
2.  starmap 要求可迭代对象的每个元素仍是可迭代的，并且能够正常解包。
3.  starmap除了要求每个元素都可以解包外，还需要解包后的参数个数，与函数参数个数相匹配
4.  starmap本质上就是将可迭代对象的每个元素，以*args的方式传递给函数

map和starmap的应用范围已越来越小，很多情况下，用列表表达式或者生成器表达式，会更加直观和易于理解
"""


class MapTestCase(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def testMap01(self):
        """
        map会依次取出被迭代对象的每个元素，作为参数传递给接受的函数对象
        """
        foo = [1, -2,  3, -4]
        # map 会将foo的每个元素传递给lamba函数，求绝对值，并返回
        map_obj = map(lambda a:  abs(a), foo)
        # map方法返回一个map object，是个迭代器，将其转换成list，再进行比较
        self.assertEqual(list(map_obj), [1, 2, 3, 4])

    def testMap02(self):
        """
        同时传入多个可迭代对象，取最短的对象进行迭代
        """
        foo = [1, -2,  3, -4]
        bar = [5, 6, 7, 8, 9]
        map_obj = map(lambda a, b:  a+b, foo, bar)
        # 例子中，bar第五个元素9被忽略
        self.assertEqual(list(map_obj), [6, 4, 10, 4])

    def testMap03(self):
        """
        接受的可迭代对象的个数，必须与函数对象的参数个数匹配，否则会抛出缺少参数或参数过多的异常
        """
        foo = [1, -2,  3, -4]
        bar = [5, 6, 7, 8, 9]
        foobar = ['a', 'b', 'c']
        # map 会将foo的每个元素传递给lamba函数，求绝对值，并返回
        # 执行到这里还不会引发一场，因为map返回的是一个迭代器，尚未开始调用函数
        map_obj = map(lambda a, b:  a+b, foo, bar, foobar)
        # 将迭代器转换成list时，开始执行迭代，参数数量无法匹配，触发异常
        with self.assertRaises(TypeError):
            result = list(map_obj)
        
    def testStarMap01(self):
        """
        starmap 接受一个函数对象及一个可迭代对象，运行时，将可迭代对象中的元素逐个解包，以位置传值的形式，按顺序传递给函数对象。
        所以要求，可迭代对象内的每个元素都仍可以解包，并且解包后的元素个数，与函数所需的参数个数相匹配
        """
        foo =  [(1, 4), (2, 5), (3, 6)]
        starmap_obj = starmap(lambda a, b: a + b, foo)
        # 例子中，foo的每个元素解包后，逐一赋值给函数的a、b参数求和，并返回迭代器
        self.assertEqual(list(starmap_obj), [5, 7, 9])
        
    def testStarMap02(self):
        """
        starmap 要求可迭代对象内的每个元素都仍可以解包
        """
        # foo的每个元素都是int类型，不可解包
        foo =  [5, -6, 7, -8, 9]
        starmap_obj = starmap(lambda a: abs(a), foo)
        # 即使starmap的函数，只需要单个参数，但仍会试图将可迭代对象的每个元素进行解包
        # 这里int类型不能解包，所以会引发异常
        with self.assertRaises(TypeError):
            result = list(starmap_obj)
        # 这种情况，用map才对。如果非要用starmap，需要将每个元素组合成tuple或list，保证可以解包
        bar =  [(1,), (-2, ), (3,)]
        starmap_obj = starmap(lambda a: abs(a), bar)
        self.assertEqual(list(starmap_obj), [1, 2, 3])

    def testStarMap03(self):
        """
        starmap除了要求每个元素都可以解包外，还需要解包后的参数个数，与函数参数个数相匹配
        """
        foo =  [(1, 4, 7), (2, 5), (3, 6)]
        starmap_obj = starmap(lambda a, b: a + b, foo)
        # 如果有一个元素解包后的个数与函数参数不匹配，都会引发TypeError
        with self.assertRaises(TypeError):
            result = list(starmap_obj)

    def testOther(self):
        """
        map和starmap的应用范围已越来越小，很多情况下，用列表表达式或者生成器表达式，会更加直观和易于理解
        """
        # 生成器表达式替代map
        foo = [1, -2,  3, -4]
        result = (abs(item) for item in foo)
        self.assertEqual(list(result), [1, 2, 3, 4])
        # 生成器表达式替代starmap
        bar =  [(1, 4), (2, 5), (3, 6)]
        result = (a+b for (a, b) in bar)
        self.assertEqual(list(result), [5, 7, 9])


if __name__ == '__main__':
    unittest.main()