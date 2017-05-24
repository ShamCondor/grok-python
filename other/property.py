#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 19:49
# @Author  : Matrix
# @Site    : 
# @File    : property.py
# @Software: PyCharm

__author__ = 'blackmatrix'


class Person(object):

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value * 2


class Man(Person):
    pass


if __name__ == '__main__':

    tom = Man(22)
    print(tom.age)
    tom.age = 23
    print(tom.age)
    print(Person.age)
