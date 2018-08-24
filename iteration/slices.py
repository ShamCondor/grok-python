#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/7/29 下午10:11
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: slices
# @Software: PyCharm
import unittest

__author__ = 'blackmatrix'

"""
本例主要演示对有序序列的切片
"""


class SlicesTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSlices01(self):
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 切片取List前三个元素
        self.assertEqual(foo[0:3], [1, 2, 3])

    def testSlices02(self):
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 切片取List后三个元素
        self.assertEqual(foo[len(foo)-3:], [7, 8, 9])

    def testSlices03(self):
        """
        对切片进行赋值，被赋值的切片，会根据赋值的变量长度自动调整
        :return:
        """
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 被赋值的切片，会根据赋值的变量长度自动调整
        foo[0:3] = [20, 30, 40, 50]
        self.assertEqual(foo, [20, 30, 40, 50, 4, 5, 6, 7, 8, 9])
        bar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 被赋值的切片，会根据赋值的变量长度自动调整
        bar[7:] = [20, 30, 40, 50, 60, 70]
        self.assertEqual(bar, [1, 2, 3, 4, 5, 6, 7, 20, 30, 40, 50, 60, 70])

    def testSlices04(self):
        """
        对切片进行赋值，如果被
        :return:
        """


if __name__ == '__main__':
    unittest.main()

    # foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #
    # print(foo)
    #
    # # 可以对切片进行赋值，并且被赋值的序列切片，会根据赋值的属性长度自动调整
    # foo[1:3] = [20, 30, 40, 50]
    #
    # print(foo)
    #
    # # 如果赋值的列表超出被赋值的序列长度，会自动扩充被赋值的序列
    # foo[7:] = [20, 30, 40, 50, 60, 70]
    #
    # print(foo)

