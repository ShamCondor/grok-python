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

主要验证以contextlib装饰器的方式，定义上下文管理器，遇到异常时，
是否能正常执行__exit__代码块
"""


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    '''
    因为list是可变类型，所以需要先对list进行一次复制，创建出复制后的变量working
    上下文管理器函数执行到yield时会暂停，在yield之前，包括yield working，
    都等同于__enter__代码块。
    yield working 会将复制出来的 working 产出，等同于__enter__代码块的return working
    当函数执行到 yield 时暂停，此时开始执行上下文中的代码
    当执行完毕，且没有异常时，上下文管理器中的 yield 恢复执行
    开始执行yield之后的代码，将修改后的working赋值给orig_list，改变orig_list的值。
    如果执行过程有异常抛出（重要！），那么yield之后的代码不会执行，那么orig_list不会被修改
    从而实现事务的效果
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
    重要！ 这是两种上下文管理器中非常重要的差别！书中没有提及！
    当执行过程中出现异常时，这种时候的执行结果与list_transaction这个函数完全不同。
    list_transaction 不能处理上下文内出现异常的情况，直接会导致 yield 之后的代码不会执行
    而 一般来说，我们编写的上下文管理器（类），__exit__方法在出现异常时，也可以正常执行
    所以在第4个例子中，输出的items_4，仍旧是被修改后的list，并没有实现事务
    （除非在 __exit__ 代码块中对出现异常的情况做些判断）
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



