#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/4/13 下午4:54
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: itemgetter
# @Software: PyCharm
from operator import itemgetter, attrgetter

__author__ = 'blackmatrix'

"""
Python标准库中的operator的itemgetter, attrgetter方法
提供了从标准库获取元素或属性的方式，可以替代简单的lambda表达式，甚至提供更强大的功能
概要：
1. itemgetter可以从目标中获取元素
2. attrgetter可以从目标中获取属性
3. 两者都可以用于替代简单的获取元素或属性的表达式
4. itemgetter接收多个参数时，将参数值作为索引，提取目标多个元素，并组成tuple返回
5. attrgetter接收多个参数时，将参数值作为属性值，提取目标多个元素，并组成tuple返回
6. attrgetter接收的参数如果带点号"."，会深入嵌套对象，提取指定属性
"""

get_name = lambda user: user['name']

get_address = lambda user: getattr(user, 'address')


class User:

    def __init__(self, name, address):
        self.name = name
        self.address = address


laowang = {'name': '老王', 'address': '隔壁'}
laoli = User('老李', '楼下')


if __name__ == '__main__':
    # itemgetter('name') 和 get_name 作用是相同的
    # 都是接受一个对象，获取对象key为name的值
    # 主要用来替代只是为了获取value的lambda函数
    print(itemgetter('name')(laowang))
    print(get_name(laowang))

    # 同样的，attrgetter('address')也是等同于get_address
    # 用来替代只为了获取attr的lambda函数
    print(attrgetter('address')(laoli))
    print(get_address(laoli))
