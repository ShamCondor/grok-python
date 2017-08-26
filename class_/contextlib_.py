#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/6/28 21:59
# @Author  : BlackMatrix
# @Site : 
# @File : contextlib_.py
# @Software: PyCharm
from contextlib import contextmanager
__author__ = 'blackmatrix'

"""
本例来自《Python Cookbook》 9.22 以简单的方式定义上下文管理器

主要验证以contextlib装饰器的方式
"""


@contextmanager
def list_transaction(orig_list):
    # 因为list是可变类型，所以通过list(orig_list)，对值进行复制，创建一个新的list，即working。
    working = list(orig_list)
    '''
    以yield为分隔，在yield之前的代码，包括yield working，会在contextmanager装饰器的__enter__方法中被调用。
    代码在执行到yield时暂停，同时yield working，会将working产出。yield产出的值，作为__enter__的返回值，赋值给as之后的变量。
    
    当with块的代码执行完成后（且没有出现未被处理的异常）， 上下文管理器会在yield处恢复，继续执行yield之后的代码，
    将修改后的working赋值给orig_list，改变orig_list的值。
    
    如果with代码块的代码执行出现异常且未被处理时，contextmanager装饰器的__exit__方法会将获取到的异常对象，通过throw方法传递给
    生成器函数。
    此时yield接收到一个异常信息，如果不能处理异常，则yield之后的代码不会执行。
    通常情况下，yield语句应该在try...except中，用于处理with代码块内可能抛出的异常。
    但是在这个例子中，希望在出现异常时，不对orig_list进行修改，以实现事务效果，在这个例子里是正常的。
    '''
    yield working
    orig_list[:] = working


# 上面的上下文管理器函数，大体等同于下面的类
class ListTransaction:

    def __init__(self, orig_list):
        self.orig_list = orig_list
        self.working = list(orig_list)

    def __enter__(self):
        return self.working

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.orig_list[:] = self.working


if __name__ == '__main__':
    # 没有出现异常时，输出结果正常
    items_1 = [1, 2, 3]
    with list_transaction(items_1) as working_1:
        working_1.append(4)
        working_1.append(5)
    print(items_1)

    # 执行引发异常时，由于没有执行yield之后的代码，未对
    # items_2 进行赋值，所以items_2的值不会修改
    items_2 = [1, 2, 3]
    try:
        with list_transaction(items_2) as working_2:
            working_2.append(4)
            working_2.append(5)
            raise RuntimeError('oops')
    except Exception as ex:
        print(ex)
    finally:
        print(items_2)

    # 以另外一种方式实现上下文管理器，当没有出现异常时，
    # 其执行结果与contextmanager装饰器装饰器的上下文管理器函数相同
    items_3 = [1, 2, 3]
    with ListTransaction(items_3) as working_3:
        working_3.append(4)
        working_3.append(5)
    print(items_3)

    """
    两种上下文管理器，最大的区别在于对异常的处理。
    
    实现上下文管理器协议的类，__exit__方法在出现异常时，也可以正常执行。
    
    而以生成器函数实现的上下文管理器，在出现异常时，装饰器的__exit__方法会将异常传递给生成器函数。
    如果生成器函数不能正确处理传递过来的异常，则yield之后的代码不会执行。
    所以通常情况下，yield应在try...except中执行，用于处理异常信息。
    除非设计之初就打算让yield之后的代码在with代码块内出现异常时不被执行。
    """
    items_4 = [1, 2, 3]
    try:
        with ListTransaction(items_4) as working_4:
            working_4.append(4)
            working_4.append(5)
            raise RuntimeError('oops')
    except Exception as ex:
        print(ex)
    finally:
        print(items_4)



