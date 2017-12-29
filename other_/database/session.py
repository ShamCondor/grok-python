#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/9/27 下午10:17
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: session
# @Software: PyCharm
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

__author__ = 'blackmatrix'


class Scope(object):

    def __init__(self):
        self._current_scope = None

    def set(self, scope):
        self._current_scope = scope

    def get(self):
        return self._current_scope


scope = Scope()
db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=True,
                                 expire_on_commit=False,
                                 bind=engine
                                 scopefunc=scope.get))

Base = declarative_base()
Base.query = db.query_property()


if __name__ == '__main__':
    pass
