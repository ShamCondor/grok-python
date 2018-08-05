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
        valuerefs返回一个可迭代的，由弱引用的value组成的列表
        :return:
        """
        weak_value = weakref.WeakValueDictionary()
        obj = TestObject()
        weak_value['obj'] = obj
        self.assertTrue(len(weak_value) == 1)
        # 将 weak_value.values() 转换成list返回，不会受到若引用对象被删除的影响
        valuerefs = weak_value.valuerefs()
        self.assertTrue(len(valuerefs) == 1)
        del obj
        self.assertTrue(len(valuerefs) == 1)
        self.assertTrue(len(weak_value.valuerefs()) == 0)

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

    def test_weakkey_keyrefs(self):
        """
        keyrefs返回一个可迭代的，由弱引用的key组成的列表
        :return:
        """
        weak_key = weakref.WeakKeyDictionary()
        obj = TestObject()
        weak_key[obj] = 'obj'
        self.assertTrue(len(weak_key) == 1)
        # 将 weak_value.values() 转换成list返回，不会受到若引用对象被删除的影响
        keyrefs = weak_key.keyrefs()
        self.assertTrue(len(keyrefs) == 1)
        del obj
        self.assertTrue(len(keyrefs) == 1)
        self.assertTrue(len(weak_key.keyrefs()) == 0)


if __name__ == '__main__':
    unittest.main()
