#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/7/29 下午10:11
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: slices
# @Software: PyCharm

__author__ = 'blackmatrix'

"""
本例主要演示对有序序列切片的赋值
"""


if __name__ == '__main__':

    foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(foo)

    # 可以对切片进行赋值，并且被赋值的序列切片，会根据赋值的属性长度自动调整
    foo[1:3] = [20, 30, 40, 50]

    print(foo)

    # 如果赋值的列表超出被赋值的序列长度，会自动扩充被赋值的序列
    foo[7:] = [20, 30, 40, 50, 60, 70]

    print(foo)

