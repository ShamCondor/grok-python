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

概要：
1.  切片操作要提供三个参数 [start_index:  stop_index:  step]  
    start_index 是切片起始位置
    stop_index 是切片结束位置，不包括切片结束位置的元素
    step 是切片步长，默认值是1
2.  step为正数时，从start_index开始，到stop_index结束，从左向右取值
3.  step为负数时，从start_index开始，到stop_index结束，从右向左取值
4.  
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
        利用切片让有序序列倒序
        :return:
        """
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(foo[: :-1], [9, 8, 7, 6, 5, 4, 3, 2, 1])

    def testSlices05(self):
        """
        切片时，stop_index为负数，起始位置从右往左数
        :return:
        """
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # -3 即从右往左数3个元素，为 [7, 8, 9]
        self.assertEqual(foo[-5:  -2], [5, 6, 7])

    def testSlices06(self):
        """
        切片时，start_index为负数，起始位置从右往左数
        :return:
        """
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # -3 即从右往左数3个元素，为 [7, 8, 9]
        self.assertEqual(foo[-3: ], [7, 8, 9])


if __name__ == '__main__':
    unittest.main()

