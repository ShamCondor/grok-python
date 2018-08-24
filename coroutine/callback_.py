#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/6/21 21:54
# @Author  : BlackMatrix
# @Site : 
# @File : callback_.py
# @Software: PyCharm
import asyncio
from datetime import datetime

__author__ = 'blackmatrix'

async def do_some_work(x):
    print('Waiting:', x)
    return 'Done after {0}s'.format(x)


def callback(future):
    print('callback: ', future.result())

start = datetime.now()

coroutine = do_some_work(2)

loop = asyncio.get_event_loop()

task = asyncio.ensure_future(coroutine)

task.add_done_callback(callback)

loop.run_until_complete(task)

print('Time: ', datetime.now() - start)

if __name__ == '__main__':
    pass
