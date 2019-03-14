#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/4/13 下午4:54
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: itemgetter
# @Software: PyCharm
import unittest
from operator import itemgetter, attrgetter

__author__ = 'blackmatrix'

"""
Python标准库中的operator的itemgetter, attrgetter方法
提供了从标准库获取元素或属性的方式，可以替代简单的lambda表达式，甚至提供更强大的功能
概要：
1. itemgetter可以从目标中获取元素
2. attrgetter可以从目标中获取属性
3. 两者都可以用于替代简单的获取元素或属性的表达式
4. itemgetter接收多个参数时，根据参数值提取目标多个元素，并组成tuple返回
5. attrgetter接收多个参数时，将参数值作为属性值，提取目标多个元素，并组成tuple返回
6. attrgetter接收的参数如果带点号"."，会深入嵌套对象，提取指定属性
"""


class Person:

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.son = None

# 示例使用，本身不符合PEP8规范，应使用def
get_name = lambda user: user.name
get_address = lambda user: getattr(user, 'address')


class TestOperatorFunc(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAttrGetter(self):
        # 实例化两个Person
        father = Person('张三', '厦门')
        son = Person('张一一', '上海')
        # 构建父子关系
        father.son = son
        # 获取父亲姓名
        father_name = attrgetter('name')(father)  # 张三
        # 可以替代简单的lambda表达式
        self.assertEqual(father_name, get_name(father))
        # 同时获取姓名和城市
        name_city = attrgetter('name', 'city')(father)
        # 返回包含有姓名和城市的元组
        self.assertTrue(isinstance(name_city, tuple))
        self.assertEqual(attrgetter('name', 'city')(father), ('张三', '厦门'))
        # 处理含有点号的情况，自动获取son实例的name属性
        son_name = attrgetter('son.name')(father)
        self.assertTrue(isinstance(son_name, str))
        self.assertEqual(son_name, '张一一')

    def testItemGetter(self):
        # itemgetter可用于list
        citys = ['厦门', '上海', '北京']
        result = itemgetter(0, 1)(citys)
        self.assertTrue(isinstance(result, tuple))
        self.assertEqual(result, ('厦门', '上海'))
        # 也可用于dict
        father = {'name': '张三', 'city': '厦门'}
        name_city = itemgetter('name', 'city')(father)
        self.assertTrue(isinstance(result, tuple))
        self.assertEqual(name_city, ('张三', '厦门'))


if __name__ == '__main__':
    unittest.main()
