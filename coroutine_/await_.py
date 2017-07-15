#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/6/21 22:05
# @Author  : BlackMatrix
# @Site : 
# @File : await_.py
# @Software: PyCharm
import asyncio
from datetime import datetime

__author__ = 'blackmatrix'

async def do_some_work(x):
    print('Wating {0} s'.format(x))
    await asyncio.sleep(x)
    return 'Done after {0} s'.format(x)

start = datetime.now()

coroutine1 = do_some_work(2)
coroutine2 = do_some_work(5)
coroutine3 = do_some_work(10)

loop = asyncio.get_event_loop()
task1 = asyncio.ensure_future(coroutine1)
task2 = asyncio.ensure_future(coroutine2)
task3 = asyncio.ensure_future(coroutine3)

tasks = (task1, task2, task3)

loop.run_until_complete(asyncio.wait(tasks))

# 必须loop执行完才能执行下面的代码

for task in tasks:
    print('Task ret: ', task.result())

print('Time: ', datetime.now() - start)


if __name__ == '__main__':
    pass