#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/7/29 下午10:11
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: Slice
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


class SliceTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSlice01(self):
        """
        这个例子中，从左往右，从第0个元素开始取值，直至第3个元素结束
        即取索引为 0 ， 1， 2的三个元素
        :return:
        """
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 切片取List前三个元素
        self.assertEqual(foo[0:3], [1, 2, 3])

    def testSlice02(self):
        """
        stop_index 省略的话，默认取到有序序列的最后一个元素为止
        :return:
        """
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 切片取List后三个元素
        self.assertEqual(foo[6:], [7, 8, 9])

    def testSlice03(self):
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

    def testSlice04(self):
        """
        利用切片让有序序列倒序
        当start_index和stop_index都省略的时候，则取出完整的有序序列
        :return:
        """
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(foo[: :-1], [9, 8, 7, 6, 5, 4, 3, 2, 1])

    def testSlice05(self):
        """
        切片时，start_index为负数，起始位置从右往左数
        :return:
        """
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # -3 即从右往左数3个元素，为 [7, 8, 9]
        self.assertEqual(foo[-3: ], [7, 8, 9])

    def testSlice06(self):
        """
        切片时，stop_index为负数，起始位置从右往左数
        start_index 和 stop_index 都为负数时，也可以混用，只要确保能正确取出值即可
        :return:
        """
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # -3 即从右往左数3个元素，为 [7, 8, 9]
        self.assertEqual(foo[-5:  -2], [5, 6, 7])

    def testSlice07(self):
        """
        list对象进行切片，本质是__getitem__获取接受一个Slice的对象
        同理，如果自定义一种类型，实现__getitem__魔法方法，能够处理slice对象
        也可以实现切片操作
        :return:
        """
        slice_obj = slice(0, 3)
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(foo.__getitem__(slice_obj), foo[0: 3])

    def testSlice08(self):
        """
        当步长step不为0时，则每step个元素取一个元素
        :return:
        """
        foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(foo[::2], [1, 3, 5, 7, 9])


if __name__ == '__main__':
    unittest.main()

