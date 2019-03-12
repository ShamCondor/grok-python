#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 17:09
# @Author  : Matrix
# @Site    : 
# @File    : chain_map.py
# @Software: PyCharm
import unittest
from collections import ChainMap

__author__ = 'BlackMatrix'

"""
ChainMap 示例
顾名思义，Chain是拉链，说明它像拉链一样，将多个字典合并在一起。Map是映射，说明建立的是对原dict的映射，也不是创建新的dict
概要：
1. ChainMap将多个dict合并在一起，并返回ChainMap类的实例
2. ChainMap并没有复制dict内容，而至是建立一个映射
3. 多个dict存在相同key时，从左向右覆盖重复key
4. 对ChainMap中key/value的新增、修改实际是对原dict的修改，顺序同样是从左至右
5. new_child 返回一个新的ChainMap实例，包含新添加的dict，原先的ChainMap实例不会修改
"""


class ChainMapTestCase(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def testChainMapMultiDict(self):
        foo = {'a': 1, 'b': 2, 'c': 3}
        bar = {'c': 4, 'd': 5, 'e': 6}
        baz = {'e': 7, 'f': 8, 'g': 9}
        # 使用ChainMap将两个dict进行合并
        foobar = ChainMap(foo, bar)
        """
        foobar 转换成dict，进行比较，可以发现：
        如果ChainMap的多个dict有相同的键，取首次出现的键，后续重复的键被忽略。
        如合并三个dict时，c的值取自首次出现的foo，而第二次出现的bar被忽略。e的值取自首次出现的bar，第二次出现的baz被忽略。
        """
        self.assertDictEqual(dict(foobar), {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 6})
        # 除初始化传入多个dict外，还可以使用new_child添加新的dict，不过添加的dict会返回一个新的ChainMap对象
        foobarbaz = foobar.new_child(baz)
        self.assertDictEqual(dict(foobarbaz), {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 7, 'f': 8, 'g': 9})
        # 比较id可知，foobar和foobarbaz实际没有关系
        self.assertNotEqual(id(foobar), id(foobarbaz))
        # 原先的两个dict没有变化
        self.assertDictEqual(foo, {'a': 1, 'b': 2, 'c': 3})
        self.assertDictEqual(bar, {'c': 4, 'd': 5, 'e': 6})

    def testChangeChainMap(self):
        """
        ChainMap并不是创建新的对象，对ChainMap的内容进行修改，实际是对原dict进行修改
        :return:
        """
        foo = {'a': 1, 'b': 2, 'c': 3}
        bar = {'c': 4, 'd': 5, 'e': 6}
        baz = {'e': 7, 'f': 8, 'g': 9}
        # 两个dict合并并创建ChainMap对象
        foobar = ChainMap(foo, bar)
        # 添加新的dict，并返回一个新的ChainMap对象
        foobarbaz = foobar.new_child(baz)
        # 对ChainMap的值进行修改，实际是对原dict进行修改
        foobarbaz['a'] = 0
        self.assertEqual(foo['a'], foobar['a'], foobarbaz['a'])

    def testChainMapMaps(self):
        """
        chainmap.maps返回映射关系的list，可以使用list的操作对返回值进行修改
        :return:
        """
        foo = {'a': 1, 'b': 2, 'c': 3}
        bar = {'c': 4, 'd': 5, 'e': 6}
        baz = {'e': 7, 'f': 8, 'g': 9}
        foobar = ChainMap(foo, bar)
        # 为foobar的映射list添加一个新的dict：baz
        # 与new_child不同的是，new_child是创建一个新的ChainMap实例，而对maps进行修改，是对原ChainMap直接修改
        foobar.maps.append(baz)
        self.assertDictEqual(dict(foobar), {'f': 8, 'g': 9, 'c': 3, 'b': 2, 'd': 5, 'e': 6, 'a': 1})
        # 移除某个映射
        del foobar.maps[0]
        self.assertDictEqual(dict(foobar), {'g': 9, 'd': 5, 'e': 6, 'c': 4, 'f': 8})



if __name__ == '__main__':
    unittest.main()
