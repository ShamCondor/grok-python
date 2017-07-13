#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/7/13 下午3:41
# @Author : Matrix
# @Site : https://github.com/blackmatrix7/apizen
# @File : descriptor_02
# @Software: PyCharm

__author__ = 'blackmatrix'


class Point:

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        # 通常情况下，通过类属性访问描述符时，返回描述符自身
        if instance is None:
            return self
        # 通过实例属性访问描述符时，返回实例
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        try:
            # 检查坐标格式是否有异常
            x, y = value
            instance.__dict__[self.name] = x, y
        except TypeError:
            raise TypeError('无效的坐标信息')


class Address:

    home = Point('myhome')


if __name__ == '__main__':
    addr = Address()
    # 将坐标信息赋值给home
    addr.home = 123, 321
    print(addr.home)
    # (123, 321)

    # 错误的赋值
    addr.home = 123
    # TypeError: 无效的坐标信息
