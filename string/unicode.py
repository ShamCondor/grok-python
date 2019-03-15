#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 10:29
# @Author  : Matrix
# @Site    : 
# @File    : unicode.py
# @Software: PyCharm
import unittest

__author__ = 'blackmatrix'


class TestStrUnicode(unittest.TestCase):
    def setUp(self):
        self.cafe_str = 'café'
        self.cafe = bytes(self.cafe_str, encoding='utf_8')
        pass

    def tearDown(self):
        pass

    def testStrEncodeBytes(self):
        # 返回bytes类型的字节序列
        self.assertTrue(isinstance(self.cafe, bytes))
        # 验证字节序列的值
        self.assertEqual(self.cafe, b'caf\xc3\xa9')

    def testBytesSlice(self):
        # bytes字节序列每个元素都是0~255(含)之间的整数
        self.assertTrue(self.cafe[0], int)
        # bytes的切片还是bytes，即使只有单个元素
        self.assertTrue(isinstance(self.cafe[:1], bytes))
        # 验证字节序列的值
        self.assertEqual(self.cafe[:1], b'c')


if __name__ == '__main__':
    unittest.main()
