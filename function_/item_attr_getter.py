#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/4/13 下午4:54
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: itemgetter
# @Software: PyCharm
from operator import itemgetter, attrgetter

__author__ = 'blackmatrix'


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
