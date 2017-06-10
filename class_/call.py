#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 20:44
# @Author  : Matrix
# @Site    : 
# @File    : call.py
# @Software: PyCharm

__author__ = 'blackmatrix'


class ClassA:

    def __call__(self, *args, **kwargs):
        print('call ClassA instance')


if __name__ == '__main__':
    # ClassA实现了__call__方法
    a = ClassA()
    '''
    这个时候，ClassA的实例a，就变成可调用对象
    调用a()，输出call ClassA instance，说明是调用了
    __call__函数
    '''
    a()
    # 其实a()等同于a.__call__()，它本质上就是后者的缩写
    a.__call__()
    # 判断是否可调用，输出True
    print(callable(ClassA))
    print(callable(a))
