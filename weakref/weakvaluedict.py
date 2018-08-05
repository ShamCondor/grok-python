#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 上午10:21
# @Author  : Matrix
# @Site    : 
# @Software: PyCharm
import weakref
import unittest

__author__ = 'BlackMatrix'


"""
WeakValueDictionary与WeakKeyDictionary

概要：
1.  WeakValueDictionary中的value，如果除dict本身，没有其他引用时，会被收回
2.  WeakValueDictionary中的value，如果除dict本身，还有其他引用时，不会被收回

"""


class TestObject:
    pass


class WeakRefTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_weakvalue_ref(self):
        """
        WeakValueDictionary中的value，如果除了WeakValueDictionary本身的引用外，
        仍有其他应用时，value内的对象不会被回收
        :return:
        """
        weak_value = weakref.WeakValueDictionary()
        obj = TestObject()
        weak_value['obj'] = obj
        self.assertEqual(obj, weak_value['obj'])

    def test_weakvalue_no_ref(self):
        """
        WeakValueDictionary中的value，如果除了WeakValueDictionary本身的引用外，
        没有其他的引用时，此value内的对象会被回收
        :return:
        """
        weak_value = weakref.WeakValueDictionary()
        weak_value['obj'] = TestObject()
        with self.assertRaises(KeyError):
            self.assertIsNotNone(weak_value['obj'])

    def test_weakvalue_valuerefs(self):
        """
        WeakValueDictionary中的value，如果除了WeakValueDictionary本身的引用外，
        没有其他的引用时，此value内的对象会被回收
        :return:
        """
        weak_value = weakref.WeakValueDictionary()
        weak_value['obj'] = TestObject()
        for value in weak_value:
            self.assertIsNotNone(value)

    def test_weakkey_ref(self):
        """
        WeakValueDictionary中的value，如果除了WeakValueDictionary本身的引用外，
        仍有其他应用时，value内的对象不会被回收
        :return:
        """
        weak_key = weakref.WeakKeyDictionary()
        obj = TestObject()
        weak_key[obj] = 'obj'
        self.assertTrue(len(weak_key) == 1)

    def test_weakkey_no_ref(self):
        """
        WeakKeyDictionary中的value，如果除了WeakKeyDictionary本身的引用外，
        没有有其他应用时，key内的对象会被回收
        :return:
        """
        weak_key = weakref.WeakKeyDictionary()
        weak_key[TestObject()] = 'obj'
        self.assertTrue(len(weak_key) == 0)


if __name__ == '__main__':
    unittest.main()
