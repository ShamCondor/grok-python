#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/7/15 下午1:24
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: inlined_async
# @Software: PyCharm
from queue import Queue
from functools import wraps

__author__ = 'blackmatrix'


"""
本例来自《Python Cookbook》 7.11 内联回调函数

概要：
1.  yield语句起到控制程序流的作用
2.  生成器执行到yield处会暂停
3.  yield右侧的值会被产出，作为生成器迭代时的返回值
4.  调用者通过send方法发送给生成器的值，会被yield接收，并赋值给左侧的变量

"""


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


class Async:

    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        # 初始时，向队列推送一个None
        result_queue.put(None)
        while True:
            '''
            从队列中取值，第一次取值时，会取出之前的None
            f.send(None)相当于 next(f)，用于预计活协程
            协程被激活后，生成器执行到第一个yield处暂停
            并产出Async类的实例，赋值给变量 a
            '''
            result = result_queue.get()
            try:
                a = f.send(result)
                '''
                Async实例存储了变量a的函数和参数，通过apply_async得到函数执行结果
                因为回调函数中设置了队列的put方法，所以会把函数执行结果推送到队列中
                '''
                apply_async(a.func, a.args, callback=result_queue.put)
                '''
                因为while循环的关系，第二次继续从队列获取上一次函数的执行结果，并发送给
                生成器的yield，此时yield起到一个类似管道的作用，将send()传递的值，赋值
                给yield左边的变量r，然后将r打印出来。
                '''
            except StopIteration:
                break
    return wrapper


if __name__ == '__main__':

    def add(x, y):
        return x + y

    @inlined_async
    def demo():
        # 第一次send(None)时，生成器执行到此处暂停，
        # 并且把yield右边的实例产出给调用者
        # 调用者对Async中的实例进行"处理"之后，将处理的结果通过send(result)发送给生成器
        # 此时生成器恢复执行，yield接受到发送的值，并赋值给yield左侧的变量 r
        r = yield Async(add, (2, 3))
        # 最后把 r 打印出来
        print(r)
        r = yield Async(add, ('hello', 'python'))
        print(r)
        for n in range(10):
            r = yield Async(add, (n, n))
            print(r)

        print('Goodbye')

    demo()

