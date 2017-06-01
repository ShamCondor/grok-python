#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/6/1 20:15
# @Author : BlackMatrix
# @Site : 
# @File : lazyproperty
# @Software: PyCharm
import math

__author__ = 'blackmatrix'


class lazyproperty:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if isinstance is None:
            return self
        else:
            # 传入self，计算出值
            value = self.func(instance)
            '''
            在实例内部赋值一个同名的变量，以此替换掉原来的实例方法
            但不认为这是一个好的方式，一个原因是书中说的，实例方法会变成可赋值的对象
            二是改变调用方式，原先是函数调用，现在只能直接读取实例属性的值
            '''
            # setattr 会再次触发描述符的__set__方法
            # setattr(instance, self.func.__name__, value)
            # 下面的方式不会触发描述符的__set__方法
            instance.__dict__[self.func.__name__] = value
            return value

    '''
    如果加入set方法，惰性求值就会失效，因为如果一个描述符只定义了__get__方法，
    那么它和类的绑定关系就会比较弱。这个时候，如果类的实例的__dict__中定于了同名的
    属性，那么会直接访问这个属性，而不会执行描述符的__get__方法。
    所以，如果在lazyproperty类中加入了__set__方法，那么每次访问被装饰的方法时，
    就会去执行描述符的__get__方法，而重新计算值
    '''
    def __set__(self, instance, value):
        print('lazyproperty __set__')
        pass


class Circle:
    def __init__(self,  radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(4.0)
    print(c.radius)
    print(c.area)
    print(c.area)
    print(c.__dict__)
    # c.area = 25
    print(c.area)
