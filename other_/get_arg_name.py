#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 15:58
# @Author  : Matrix
# @Site    : 
# @File    : get_arg_name.py
# @Software: PyCharm
import inspect

__author__ = 'huangxupeng'

if __name__ == '__main__':
    a, b, c, d, e = False, True, False, False, False
    order_list = ['e', 'c', 'a', 'b', 'd']
    args = locals()

    def order(order_list):
        for i in order_list:
            val = args[i]
            if val is True:
                return i
        else:
            return '?'

    print(order(order_list))