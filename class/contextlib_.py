#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/6/28 21:59
# @Author  : BlackMatrix
# @Site : 
# @File : contextlib_.py
# @Software: PyCharm
import unittest
from contextlib import contextmanager

__author__ = 'blackmatrix'

"""
本例来自《Python Cookbook》 9.22 以简单的方式定义上下文管理器

主要验证以contextlib装饰器的方式

概要：
1.  生成器函数加上@contextmanager装饰器，可以很方便的实现上下文管理器
2.  通过类实现__enter__ 和 __exit__方法也可以实现上下文管理器
3.  第一种方法实现的上下文管理器，在出现异常时，yield之后的代码不会运行
4.  第二种方法实现的上下文管理器，在出现异常时，__exit__之后的代码继续运行
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


class ContextlibTestCase(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def testListTransactionYield(self):
        """
        生成器函数实现的上下文管理器
        没有出现异常时，输出结果正常
        """
        foo = [1, 2, 3]
        with list_transaction(foo) as working:
            working.append(4)
            working.append(5)
        self.assertEqual(foo, [1, 2, 3, 4, 5])

    def testListTransactionYieldError(self):
        """
        生成器函数实现的上下文管理器
        执行引发异常时，由于没有执行yield之后的代码，
        未对foo 进行赋值，所以foo的值不会修改
        """
        foo = [1, 2, 3]
        with self.assertRaises(RuntimeError):
            with list_transaction(foo) as working:
                working.append(4)
                working.append(5)
                raise RuntimeError('oops')
        # yield之后的代码没有执行，所以foo的值不会修改
        self.assertEqual(foo, [1, 2, 3])

    def testListTransactionClass(self):
        """
        以类实现的上下文管理器，当执行没有出现异常时
        foo被修改，输出结果正常
        """
        foo = [1, 2, 3]
        with ListTransaction(foo) as working:
            working.append(4)
            working.append(5)
        self.assertEqual(foo, [1, 2, 3, 4, 5])

    def testListTransactionClassError(self):
        """
        以类实现的上下文管理器，即使出现异常，__exit__方法也会正常执行
        foo被修改，输出结果正常
        """
        foo = [1, 2, 3]
        with self.assertRaises(RuntimeError):
            with ListTransaction(foo) as working:
                working.append(4)
                working.append(5)
                raise RuntimeError('oops')
        self.assertEqual(foo, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()

