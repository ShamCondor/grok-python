#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 9:42
# @Author  : Matrix
# @Site    : 
# @File    : combining.py
# @Software: PyCharm
from unicodedata import combining, normalize

__author__ = 'blackmatrix'

"""
combining对字符做检查，判断它是否为组合字符。
结合规范化方法normalize及NFD，可以判断某个字符是否用于跟其他字符组合。
例如café，使用NFD进行规范化后，会得到 cafe ́
依次将5个元素应用到combining进行判断，cafe应用combining方法的值是0
而́  应用方法的值是230，从而可以得知最后一个字符是用来和其他字符组合的
"""

if __name__ == '__main__':
    foo = normalize('NFD', 'cafe')
    bar = normalize('NFD', 'café')
    baz = normalize('NFD', '½€Ω')
    foobar = normalize('NFD', 'SãoPaulo')

    # c: 0
    # a: 0
    # f: 0
    # e: 0
    for letter in foo:
        print("{letter}: {result}".format(letter=letter, result=combining(letter)))

    # c: 0
    # a: 0
    # f: 0
    # e: 0
    # ́: 230
    for letter in bar:
        print("{letter}: {result}".format(letter=letter, result=combining(letter)))

    # ½: 0
    # €: 0
    # Ω: 0
    for letter in baz:
        print("{letter}: {result}".format(letter=letter, result=combining(letter)))

    # S: 0
    # a: 0
    # ̃: 230
    # o: 0
    # P: 0
    # a: 0
    # u: 0
    # l: 0
    # o: 0
    for letter in foobar:
        print("{letter}: {result}".format(letter=letter, result=combining(letter)))
