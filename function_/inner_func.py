#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/6/6 下午8:51
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: inner_func.py
# @Software: PyCharm

__author__ = 'blackmatix'

'''
本例主要测试,一个函数内嵌另外一个函数时,
如何在外部调用到这个内嵌的函数,即闭包
'''


def func(word):

    _word = word

    def _print_word():
        print(_word)

    # 这里最关键的地方就是给函数自身增加一个内嵌函数后,将函数自身返回
    func.print_word = _print_word

    # 有局限性,对于需要返回其他值的函数就不太适用了
    return func


if __name__ == '__main__':
    func('Hello').print_word()
