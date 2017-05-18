#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/5/16 21:03
# @Author : Matrix
# @Site : https://github.com/blackmatrix7
# @File : unwrap.py
# @Software: PyCharm
from inspect import unwrap
from functools import wraps

__author__ = 'blackmatrix'


def test_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('test_decorator')
        return func(*args, **kwargs)
    return wrapper


def test_decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('test_decorator2')
        return func(*args, **kwargs)
    return wrapper


def test_decorator3(func):
    def wrapper(*args, **kwargs):
        print('test_decorator3')
        return func(*args, **kwargs)
    return wrapper


# 测试只有一个装饰器的情况下，能否正常解包
@test_decorator
def spam():
    print('spam1', '\n')


# 测试两个装饰器情况下，能否正常解包
@test_decorator2
@test_decorator
def spam2():
    print('spam2', '\n')


# 测试多个装饰器情况下，其中一个装饰器的包装器没有使用@wraps
@test_decorator2
@test_decorator3
@test_decorator
def spam3():
    print('spam3', '\n')


def callback(obj):
    obj()
    print('上面是回调函数的一次执行结果', '\n')


def callback2(obj):
    obj()
    print('上面是回调函数的一次执行结果', '\n')
    return True


def callback3(obj, value):
    print(obj, value)

if __name__ == '__main__':
    print('调用被装饰的函数spam，装饰器生效，输出 test_decorator')
    spam()

    print('使用 unwrap 获取被包装的函数，命名为unwrap_spam')
    unwrap_spam = unwrap(spam)
    print(unwrap_spam, '\n')

    print('调用已经解包装的函数命名为unwrap_spam，装饰器没有生效，没有输出 test_decorator')
    unwrap_spam()

    print('测试两个装饰器情况下，能否正常解包\n'
          '测试结果，两个装饰器也能正常获取到被包装的函数')
    unwrap_spam2 = unwrap(spam2)
    unwrap_spam2()

    print('测试多个装饰器情况下，其中一个装饰器的包装器没有使用@wraps\n'
          '装饰链中，unwrap只能解包到未使用@wraps的装饰器')
    unwrap_spam3 = unwrap(spam3)
    unwrap_spam3()

    print('测试 stop 参数传入的回调函数，回调函数每次接受一个函数对象（比如包装器函数）\n'
          '当回调函数返回True时，会提前中止解包过程\n'
          '如果回调函数没有返回True，则返回装饰链中最后一个对象')
    unwrap(spam2, stop=callback)
    '''
    输出结果：
    ------------------
    test_decorator2
    test_decorator
    spam2
    test_decorator
    spam2
    ------------------
    其中
    ------------------
    test_decorator2
    test_decorator
    spam2
    ------------------
    为第一次解包的运行结果，此时调用依次调用test_decorator2、test_decorator、spam2所以会由如上的输出结果。
    ------------------
    test_decorator
    spam2
    ------------------
    为第二次解包结果，此时调用顺序是test_decorator、spam2，所以会输出上面的结果
    而第三次解包时，因为已经获取到装饰链的最后一个对象，所以不会再调用回调函数，所以不会有输出结果。
    ------------------
    另外还需要再注意下第一次解包的输出结果：test_decorator2、test_decorator、spam2。
    说明第一次解包时，传给回调函数是完整的，整个被test_decorator2、test_decorator两个装饰器装饰后的spam2！
    而不是解包后的函数对象（如果是解包后的函数对象，因为test_decorator2已经成功解包，所以打印结果应该是test_decorator、spam2）！
    也就是说，传给回调函数的对象，实际上应该是本次解包之前的函数对象，而不是解包之后的函数对象！
    '''

    print('如果回调函数能接收两个参数会怎样？')
    # unwrap(spam2, stop=callback3)
    print('结果是直接抛异常，缺少参数value，因为unwrap只会把本次解包的对象传入回调函数', '\n')

    print('再试试回调函数返回True的时候是不是真的可以提前终止解包？')
    unwrap(spam2, stop=callback2)()
    '''
    得到以下输出结果：
    ------------------
    test_decorator2
    test_decorator
    spam2 
    上面是回调函数的一次执行结果 
    test_decorator2
    test_decorator
    spam2 
    ------------------
    第一次输出是回调函数的执行结果，第二输出是解包后的函数执行结果。
    从第二次执行结果来看，spam2并没有被解包。
    所以，整个解包装的流程应该是这样的：
    将当前待解包的函数对象传入回调函数中 --> 回调函数返回 True，解包终止，返回当前待解包的函数对象。
                                                                --> 回调函数返回 False或者没有返回值，解包继续，返回解包后的函数对象。
                                                                
    其中：
    如果解包后的函数对象不是装饰链中的最后一个对象，那么重复第一步，将对象传入回调函数
    如果解包后的函数对象已经是装饰链的最后一个对象（或是一个没有用@wrap装饰的装饰器），那么解包终止。
    如果没有回调函数，则逐层解包，直至装饰链最后一个对象，或遇到一个没有用@wrap装饰的装饰器（会被当成装饰链最后一个对象处理）。
    '''





