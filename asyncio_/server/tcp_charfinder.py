#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 10:27
# @Author  : Matrix
# @Site    : 
# @File    : tcp_charfinder.py
# @Software: PyCharm
import sys
import asyncio
from asyncio_.server.charfinder.charfinder import UnicodeNameIndex

"""
例子来自《流畅的Python》 18.6.1 用asyncio包编写TCP服务器

"""

CRLF = b'\r\n'
PROMPT = b'?>'

index = UnicodeNameIndex()

__author__ = 'BlackMatrix'


def handle_queries(reader, writer):
    """
    :param reader: asyncio.StreamReader实例
    :param writer: asyncio.StreamWriter对象的实例
    :return:
    """
    while True:
        # 这行代码仅仅是打印一个提示符?>到控制台上
        writer.write(PROMPT)
        # 刷新writer缓冲
        yield from writer.drain()
        # 返回一个bytes对象
        data = yield from reader.readline()
        try:
            query = data.decode().strip()
        except UnicodeDecodeError:
            # 出现UnicodeDecodeError就把它当空字符串处理
            query = '\x00'
        client = writer.get_extra_info('peername')
        # 在服务器的控制台中记录查询信息
        print('Received from {}: {!r}'.format(client, query))
        if query:
            if ord(query[:1]) < 32:
                break
            lines = list(index.find_description_strs(query))
            if lines:
                writer.writelines(line.encode() + CRLF for line in lines)
            writer.write(index.status(query, len(lines)).encode() + CRLF)
            yield from writer.drain()
            print('Sent {} result'.format(len(lines)))
    print('Close the client socket')
    writer.close()


def main(address='127.0.0.1', port=2323):
    port = int(port)
    loop = asyncio.get_event_loop()
    server_coro = asyncio.start_server(handle_queries, address, port, loop=loop)
    server = loop.run_until_complete(server_coro)
    host = server.sockets[0].getsockname()
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    print('Server shutting down.')
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    main(*sys.argv[1:])
