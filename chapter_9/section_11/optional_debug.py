#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/10 20:49
# @Author  : Matrix
# @Site    : 
# @File    : optional_debug.py
# @Software: PyCharm
from inspect import signature, Parameter
from functools import wraps

__author__ = 'blackmatrix'

# 编写装饰器为被包装的函数添加参数


def optional_debug(func):
    @wraps(func)
    # 在包装器的位置，增加debug参数
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling ', func.__name__)

        # 因为加了@wraps装饰器，所以当使用signature获取函数签名时，返回的是被包装函数的签名
        # 书中采用一个很巧妙的方法，先获取被包装函数的签名，给它新增一个Parameter，将debug参数写入函数签名的Parameter
        # 虽然原理不复杂，但是十分有效

        # 获取被包装的函数签名
        sig = signature(func)
        # 通过函数签名，获取被包装函数的参数
        parms = list(sig.parameters.values())
        # 为params增加debug的参数
        # 从源码得知，Parameter可以接收5个参数
        # name为参数名称
        # kind为参数类型，一共4种：POSITIONAL_OR_KEYWORD、VAR_POSITIONAL、VAR_KEYWORD、KEYWORD_ONLY
        #   参数类型为VAR_POSITIONAL时，即*args参数，只能通过位置传值
        #   参数类型为VAR_KEYWORD，即 **kwargs参数，只能通过关键字传值
        #   参数的类型为POSITIONAL_OR_KEYWORD时，说明此参数前面没有VAR_POSITIONAL类型的参数，可以通过位置或关键字传值
        #   参数类型为KEYWORD_ONLY时，说明此参数前面存在VAR_POSITIONAL类型的参数，只能通过关键字传值
        # default 为参数默认值
        # annotation 从字面的意义是注释的意思，没有试验不清楚传入值会怎么样
        # 还有个*，也暂时不清楚什么作用
        # TODO 有空试试传入annotation，还有折腾看看这个*是什么意思
        parms.append(Parameter(name='debug', kind=Parameter.KEYWORD_ONLY, default=False))
        # 关于__signature__，官方文档的描述： signature() uses this to stop unwrapping if any object in the chain has a __signature__ attribute defined.
        # 当对象中存在__signature__属性时，获取装饰链中的函数签名，都会返回__signature__的值，但是只是在signature()函数中返回__signature__的值，本身并不会改变函数的参数
        wrapper.__signature__ = sig.replace(parameters=parms)
        return func(*args, **kwargs)
    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    spam(1, 2, 3)
    spam(1, 2, 3, debug=True)
    # 上面的等同于
    # optional_debug(spam)(1, 2, 3, debug=True)

    # 获取函数签名
    # 采用手动添加debug参数的方式
    func_signature = signature(spam)
    print(func_signature)

    # 尝试过直接通过 signature(callable, *, follow_wrapped=False) 的方式获取函数签名 （Python 3.5 以后支持）
    # 测试后发现 follow_wrapped=False 获取的是包装器的函数签名，follow_wrapped=True 获取的被装饰函数的签名
    # 两者都不能符合要求，书中需要实现的目标是被装饰函数的签名，加上包装器上新增的参数，组成一个新的函数签名参数
    # 所以，似乎只能按书上的方法进行，将parameters组合完成后，再进行替换

    # 在Python 3.5 之后，可以用下面的方法，获取包装器的函数签名
    # 测试这个代码需要把 wrapper.__signature__ = sig.replace(parameters=parms) 注释掉，否则获取的依旧是修改后的函数签名
    print(signature(spam, follow_wrapped=False))
    # 当follow_wrapped 为 True时（默认为True）, 获取被包装函数的签名
    print(signature(spam, follow_wrapped=True))




