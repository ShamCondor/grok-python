#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/8/16 下午8:56
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: map_
# @Software: PyCharm
from itertools import starmap

__author__ = 'blackmatrix'

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6, 7]
    list_c = [(1, 4), (2, 5), (3, 6)]
    list_d = [(1, 4), (2, 5), (3, 6), 7]

    '''
    内建的map函数，接受一个函数对象，及N个可迭代对象
    运行时，map会依次取出被迭代对象的每个元素，作为参数传递给接受的函数对象
    
    如果N个可迭代对象的长度不同，以最短的可迭代对象进行迭代，其他较长的可迭代对象
    中的元素会被忽略
    '''
    print(list(map(lambda a, b: a + b, list_a, list_b)))
    '''
    接受的可迭代对象的个数，必须与函数对象的参数个数匹配，否则会抛出缺少参数或参数过多的异常
    '''
    # print(list(map(lambda a, b: a + b, list_a)))
    # print(list(map(lambda a, b: a + b, list_a, list_b, list_c)))

    '''
    starmap 接受一个函数对象及一个可迭代对象，运行时，将可迭代对象中的元素逐个解包，
    以位置传值的形式，按顺序传递给函数对象。
    '''
    print(list(starmap(lambda a, b: a + b, list_c)))
    '''
    starmap要求可迭代对象内的每个元素，解包后个数都必须和函数的参数个数相匹配。
    下面的例子中，list_d中的元素7无法解包，故抛出'int' object is not iterable异常
    '''
    # print(list(starmap(lambda a, b: a + b, list_d)))
    '''
    starmap要求可迭代对象的每个元素仍是可迭代的，并且能够正常解包。
    即使函数只接受一个参数，可迭代对象的每个元素仍必须是可迭代的。
    下面的例子中，虽然list_a的每个元素与lambda函数的参数匹配，但是int类型无法解包
    任然会抛出异常TypeError: 'int' object is not iterable
    '''
    # print(list(starmap(lambda a: a, list_a)))
    '''
    正确的做法应该是保证可迭代对象的每个元素仍然是可迭代的，
    对list_a做下修改，得到list_e，保证每个元素可迭代。
    '''
    list_e = [(1,), (2, ), (3,)]
    print(list(starmap(lambda a: a, list_e)))
    '''
    starmap本质上就是将可迭代对象的每个元素，以*args的方式传递给函数。
    就是这么简单
    '''