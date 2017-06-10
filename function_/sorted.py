#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/28 17:57
# @Author  : Matrix
# @Site    : 
# @File    : sorted.py
# @Software: PyCharm

__author__ = 'blackmatrix'

temp_list = [4, -5, 7, 1, -3, 2, -9]

if __name__ == '__main__':
    print(sorted(temp_list))
    # 反转
    print(sorted(temp_list, reverse=True))
    # 根据绝对值排序
    print(sorted(temp_list, key=lambda key: abs(key)))
