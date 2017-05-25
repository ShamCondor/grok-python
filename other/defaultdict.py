#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 20:12
# @Author  : Matrix
# @Site    : 
# @File    : defaultdict.py
# @Software: PyCharm
from collections import defaultdict


__author__ = 'blackmatrix'


def factory_func():
    return 'default_factory'

test_defaultdict = defaultdict(factory_func)

test_defaultdict2 = defaultdict()

if __name__ == '__main__':
    '''
    当key存在时，返回的是key对应的value
    这个时候和普通的dict没有什么区别
    '''
    test_defaultdict['a'] = '233333'
    print(test_defaultdict['a'])
    '''
    当访问不存在的key时，自动将工厂函数的返回值作为默认值
    '''
    print(test_defaultdict['b'])
    print(test_defaultdict['c'])

    '''
    如果defaultdict在创建的时候没有传入工厂函数，则在访问不存在的key时，会抛出KeyError
    '''
    print(test_defaultdict2['x'])
