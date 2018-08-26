#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/1/4 下午9:19
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: string_.py
# @Software: PyCharm
import unittest
from string import Template

__author__ = 'blackmatrix'

"""
以模板的形式，格式化字符串

概要：
1.  默认的界定符是$，即会将$之后内容匹配的字符串进行替换
2.  可以通过继承继承Template类的方式，替换默认界定符
"""


class TemplateTestCase(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def testTemplate(self):
        s = Template('hello, $world!')
        self.assertEqual("hello, python!", s.substitute(world='python'))

    def testCustomerTemplate(self):
        # 可以通过继承Template类的方式进行替换
        class CustomerTemplate(Template):
            delimiter = '*'
        t = CustomerTemplate('hello, *world!')
        self.assertEqual("hello, python!", t.substitute(world='python'))

if __name__=="__main__":
    unittest.main()
