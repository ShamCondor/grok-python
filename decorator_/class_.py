#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/6/12 20:37
# @Author  : BlackMatrix
# @Site : 
# @File : class_.py
# @Software: PyCharm
import types
from functools import wraps, update_wrapper

__author__ = 'blackmatrix'

'''
本例来自《Python Cookbook》 9.9 把装饰器定义成类
'''


class Profiled:

    def __init__(self, func):
        # update_wrapper(wrapped=func, wrapper=self)
        wraps(func)(self)
        '''
        通常，装饰器的包装器是这么写的
        @wraps(func)
        def wrapper(*args, **kwargs):
            pass
        -----------------
        而 wraps(func)(self) 等同于
        @wraps(func)
        self
        实际上是把self当成包装器(wrapper)进行处理。
        因为类实现了__call__方法，那么它的实例self就是可调用对象
        所以可以使用wraps来装饰实例self
        ------------------
        而wraps方法实际上是update_wrapper的偏函数，
        update_wrapper 接受如下参数：
        update_wrapper(wrapper,  wrapped,  assigned = WRAPPER_ASSIGNMENTS, updated = WRAPPER_UPDATES)
        其中 assigned 和 updated 带有默认值，在这个例子中先忽略。
        ------------------
        接着看下 wraps的实现：
        def wraps(wrapped, assigned = WRAPPER_ASSIGNMENTS, updated = WRAPPER_UPDATES):
              return partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)
        ------------------
        偏函数wraps中，默认传入update_wrapper的参数 wrapped，也就是被包装函数。
        即 wraps(func) 实际上，是把 func 作为参数 wrapped 传入，即被包装的函数，
        等同于 wraps(wrapped=func)
        所以wraps(func) 返回一个偏函数，等同于函数 update_wrapper，
        这里需要注意的是，wraps返回的是一个可调用的对象，而不是update_wrapper执行结果。
        那么update_wrapper现在必须的参数还缺一个wrapper，即包装器。
        此时把self，作为包装器传入，即类似 update_wrapper(wrapper=self)
        至于参数wrapped 已经在偏函数里完成赋值
        ------------------
        最终，wraps(func)(self) 等于 update_wrapper(wrapped=func, wrapper=self)
        即实现传入两个参数：被包装函数func，包装器self。
        '''
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        '''
        在update_wrapper中，会执行如下命令
        wrapper.__wrapped__ = wrapped，将被包装的函数，赋值给包装器的__wrapped__属性
        在这个例子中，前面说过，把类的实例self，作为参数wrapper传入，
        所以包装器是类实例self，所以能通过self.__wrapped__获取到被包装的函数。
        __call__方法本身是实例方法，所以在调用类实例的时候，可以获取到self，进一步得到self.__wrapped__。
        '''
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            '''
            MethodType 会在类内部创建一个链接，指向外部的的方法，在创建实例的同时，这个绑定后的方法也会复制到实例中
            MethodType 接受两个参数，第一个是被绑定的函数，第二个是需要绑定到的对象
            根据描述符协议，instance为实例对象，上文说过self为包装其wrapper，通过MethodType使实例本身和包装器建立
            绑定关系
            '''
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x+y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

if __name__ == '__main__':
    print(add(1, 2))
    print(add(2, 3))
    print(add.ncalls)
    s = Spam()
    s.bar(x=1)