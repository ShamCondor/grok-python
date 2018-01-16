#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/6/10 下午9:03
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: signature.py
# @Software: PyCharm
from inspect import signature, Signature, Parameter

__author__ = 'blackmatix'


'''
本例主要演示函数签名的使用和获取

概要:
1.  使用标准库的signature获取函数签名
2.  通过函数签名的parameters属性，获取函数参数。
3.  bind创建位置和关键字的参数映射到被绑定的参数中

'''


def foo(value):
    return value

# 获取函数签名
foo_sig = signature(foo)
# 获取函数参数
foo_params = foo_sig.parameters
# OrderedDict([('value', <Parameter "value">)])
print(foo_params)


# 创建一个函数参数列表，列表内的元素由类Parameter的实例组成
# Parameter实例化时，依次接受参数名、参数类型、默认值和参数注解
# 默认值和参数类型默认为空，这里的空值不是None，而是Parameter.empty，代表没有值
parms = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
         Parameter('y', Parameter.POSITIONAL_OR_KEYWORD),
         Parameter('z', Parameter.KEYWORD_ONLY, default=9)]

# 使用Signature类实例化出一个函数签名实例
sig = Signature(parms)


def func(*args, **kwargs):
    # bind 方法, 创建一个签名中的参数映射到函数接受的参数中。
    # 在这个例子中,将外部定义的parms建立映射,绑定到函数接收的参数中。
    # 当函数参数与签名中的参数相匹配时,返回BoundArguments对象,
    # 反之则抛出 TypeError
    bound_value = sig.bind(*args, **kwargs)
    for name, value in bound_value.arguments.items():
        print(name, value)

if __name__ == '__main__':
    func(1, 2, z=3)
    func(1, 2)
    # 引发异常
    # func(1)
