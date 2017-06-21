#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/6/21 21:29
# @Author  : BlackMatrix
# @Site : 
# @File : loop_.py
# @Software: PyCharm
from datetime import datetime
import asyncio

__author__ = 'blackmatrix'


async def do_somee_work(x):
    print('Wating: ', x)

start = datetime.now()

coroutine = do_somee_work(2)

loop = asyncio.get_event_loop()

loop.run_until_complete(coroutine)


if __name__ == '__main__':
    print('Time:', datetime.now() - start)
