#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/1/4 下午9:19
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: string_.py
# @Software: PyCharm
from string import Template

__author__ = 'blackmatrix'

"""
以模板的形式，格式化字符串
"""

# 默认的定界符是$，即会将$之后花括号中的内容进行替换
s = Template('hello, ${world}!')
print(s.substitute(world='python'))


# 可以通过继承Template类的方式进行替换
class CustomerTemplate(Template):
    delimiter = '*'

t = Template('hello, *{world}!')
print(s.substitute(world='python'))
