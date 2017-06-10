#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 20:08
# @Author  : Matrix
# @Site    : 
# @File    : getattribute.py
# @Software: PyCharm

__author__ = 'blackmatrix'


class ClassA:

    x = 'a'

    def __getattribute__(self, name):
        return self.__dict__[name]


if __name__ == '__main__':
    a = ClassA()
    # 无限递归
    a.x