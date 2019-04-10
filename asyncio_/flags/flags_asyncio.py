#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 10:32
# @Author  : Matrix
# @Site    : 
# @File    : flags_asyncio.py
# @Software: PyCharm
import asyncio
import aiohttp
from asyncio_.flags.flags_comm import BASE_URL, show, save_flag, main

__author__ = 'BlackMatrix'


@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.ClientSession().get(url)
    image = yield from resp.read()
    return image


@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    # 返回一个生成器组成的list
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    # wait方法将上面的list，转换为一个生成器并返回
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


if __name__ == '__main__':
    main(download_many)
