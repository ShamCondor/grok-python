#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 22:00
# @Author  : Matrix
# @Site    : 
# @File    : singleton.py
# @Software: PyCharm

__author__ = 'blackmatrix'


class Singleton(type):

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    # __call__ 是对于类实例有效，比如说Spam类，是type类的实例
    def __call__(cls, *args, **kwargs):
        print('__call__ running')
        if cls.__instance is None:
            '''
            目前能理解的是，元类定义__call__方法，可以抢在类运行 __new__ 和 __init__ 之前执行，
            也就是创建单例模式的前提，在类实例化前拦截掉。
            不能理解的是，为什么是调用 super().__call__(*args, **kwargs)，而不是__new__ 或 __init__ ？
            '''
            #  TODO type 的 __call__ 到底执行了什么？
            cls.__instance = super().__call__(*args, **kwargs)
            # cls.__instance = super().__new__(cls, cls.__name__, *args, **kwargs)
            # cls.__instance.__init__(cls.__instance, *args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class Spam(metaclass=Singleton):

    def __init__(self):
        print('Creating Spam')

if __name__ == '__main__':
    a = Spam()
    b = Spam()
    print(a is b)
    c = Spam()
    print(a is c)
