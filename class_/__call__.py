#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 20:44
# @Author  : Matrix
# @Site    : 
# @File    : __call__.py
# @Software: PyCharm

__author__ = 'blackmatrix'


'''
本例主要演示__call__方法的使用

概要:
1.  __call__方法可以让一个实例变为可调用对象
2.  __call___是个实例方法,带self参数
3.  __call__方法只对类实例有效,如果想对类生效,需在元类中定义
4.  类定义了__call__方法后,实例instance()相当于instance.__call__()
'''


class ClassMeta(type):

    def __call__(cls, *args, **kwargs):
        print('call')


class ClassA:

    def __call__(self, *args, **kwargs):
        print('call ClassA instance')


class ClassB(metaclass=ClassMeta):
    pass


if __name__ == '__main__':

    '''
    ClassA实现了__call__方法
    这个时候，ClassA的实例a，就变成可调用对象
    调用a()，输出call ClassA instance，说明是调用了__call__方法
    '''
    a = ClassA()
    a()
    # 输出：call ClassA instance
    # 其实a()等同于a.__call__()，它本质上就是后者的缩写
    a.__call__()
    # 输出：call ClassA instance

    # 判断是否可调用
    '''
    类都是可调用对象，因为会返回类的实例
    官方手册：Note that classes are callable (calling a class returns a new instance)
    '''
    print(callable(ClassA))
    # 输出True
    '''
    当实例所属的类定义了__call__方法时，实例也是可调用对象
    官方手册：instances are callable if their class has a __call__() method.
    '''
    print(callable(a))
    # 输出：True

    '''
    如果希望让类本身变为可调用对象，那么需要在元类中定义__call__方法
    因为类是元类的实例。
    下面的例子中，ClassB的元类是ClassMeta，而ClassMeta定义了__call__方法
    所以ClassB()不会进行实例化动作，而是调用__call__方法。
    '''
    # 这里输出True是因为元类实现了__call__方法，而不是因为调用类会返回实例，这个与ClassA不同
    print(callable(ClassB))
    # 输出：True
    ClassB()
    # 输出：call

    '''
    __call__ 是实例方法，只能通过实例调用，所以其实例会成为可调用对象。
    而实例方法的本质就是描述符。
    所以，通过类去访问描述符符时，等同于调用__call__的__get__方法，返回的是__call__自身
    '''
    # 返回__call__函数
    print(ClassA.__call__)
    # 因为
    print(ClassA.__call__.__get__(None, ClassA))
    print(ClassA.__call__ == ClassA.__call__.__get__(None, ClassA))
