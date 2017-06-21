#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/6/21 21:48
# @Author  : BlackMatrix
# @Site : 
# @File : task_.py
# @Software: PyCharm
import asyncio
from datetime import datetime

__author__ = 'blackmatrix'

async def do_some_work(x):
    print('waiting:', x)

start = datetime.now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()

task = loop.create_task(coroutine)
print(task)
loop.run_until_complete(task)
print(task)
print('Time: ', datetime.now() - start)

if __name__ == '__main__':
    pass
