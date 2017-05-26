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
        print('Singleton __call__ running')
        if cls.__instance is None:
            '''
            元类定义__call__方法，可以抢在类运行 __new__ 和 __init__ 之前执行，
            也就是创建单例模式的前提，在类实例化前拦截掉。
            type的__call__实际上是调用了type的__new__和__init__
            '''
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class Spam(metaclass=Singleton):

    """
    一些说明：
    如果__new__没有返回类实例的情况下，
    __init__的方法是不会被调用的。因为__init__需要类实例作为第一个参数self
    这个是时候，单例模式不会起作用，因为__init__都没有运行
    没有实例创建出来，何来的单例模式
    """

    def __new__(cls):
        print('Spam __new__ running')
        return super().__new__(cls)

    def __init__(self):
        print('Spam __init__ running')

if __name__ == '__main__':
    a = Spam()
    b = Spam()
    print(a is b)
    c = Spam()
    print(a is c)
    '''
    输出结果：
    Singleton __call__ running
    Spam __new__ running
    Spam __init__ running
    Singleton __call__ running
    True
    Singleton __call__ running
    True
    '''