#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/7/11 21:19
# @Author  : BlackMatrix
# @Site : 
# @File : closure.py
# @Software: PyCharm
import  sys
__author__ = 'blackmatrix'


class ClosureInstance:

    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
            self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()


def Stack():

    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


if __name__ == '__main__':
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(len(s))
