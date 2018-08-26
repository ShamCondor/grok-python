#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/28 17:57
# @Author  : Matrix
# @Site    : 
# @File    : sorted.py
# @Software: PyCharm
import unittest

__author__ = 'blackmatrix'

"""
使用sorted进行排序

1.  stored 接受一个有序序列，对其进行排序，并返回排序后的结果
2.  stored接受reverse参数，传入布尔值，决定是否对排序结果进行反转
3.  stored还可以接受一个单参数的函数，排序时，将每个元素传递给这个函数，并以函数的返回值进行排序
"""


class SortedTestCase(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def testSorted(self):
        """
        使用sorted进行排序
        """
        foo = [4, -5, 7, 1, -3, 2, -9]
        result = sorted(foo)
        self.assertEqual(result, [-9, -5, -3, 1, 2, 4, 7])

    def testSortedReverse(self):
        """
        sorted 还可以接受第二个参数，对排序结果进行反转
        """
        foo = [4, -5,  7,  1,  -3,  2, -9]
        result = sorted(foo, reverse=True)
        self.assertEqual(result, [7, 4, 2, 1, -3, -5, -9])

    def testSortedKey(self):
        """
        sorted还可以接受一个单参数的函数，排序时将每次元素传递给这个函数，通过函数的返回结果进行排序
        """
        foo = [4, -5,  7,  1,  -3,  2, -9]
        # 将每个元素传入lambda函数，求绝对值，并以绝对值进行排序
        result = sorted(foo, key=lambda item: abs(item))
        self.assertEqual(result, [1, 2, -3, 4, -5, 7, -9])


if __name__ == '__main__':
    unittest.main()

