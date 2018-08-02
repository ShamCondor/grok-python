#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 19:49
# @Author  : Matrix
# @Site    : 
# @File    : property.py
# @Software: PyCharm
import unittest

__author__ = 'blackmatrix'


class Person:

    def __init__(self, age):
        self._age = age
        self._name = 'lilei'

    # @property 装饰器等同于 age = property(fget=age)
    @property
    def age(self):
        print('person property age getter')
        return self._age

    @age.setter
    def age(self, value):
        print('person property age setter')
        self._age = value * 2

    @property
    def name(self):
        return self._name


# 此例子说明property是可以被继承的
class Man(Person):
    pass


# 此例子说明property是可以被继承的
class Boy(Person):
    pass


class Student(Person):

    # 如果在子类重新定义一个property,会完全重写掉父类的同名的property,包括里面的所有方法
    # 所以没有定义setter方法,age变为只读,无法赋值
    # 实际上,这种方式是在子类重新创建了一个名为age的property对象,重写掉了父类名为age的property
    # age = property(fget=..., fset=None)
    @property
    def age(self):
        print('student property age getter')
        return self._age


class Teacher(Person):

    # 只有这种方式才能正确的重写父类的getter方法
    @Person.age.getter
    def age(self):
        print('teacher property age getter')
        return self._age

    # 同样, 这样才能正确的重写掉父类特性的getter方法
    # property是个类,@Person.age.setter,这个操作相当于找到Person下,这个age(property实例)的方法fset
    # 并用我们在子类的方法将其重写。
    @Person.age.setter
    def age(self, value):
        print('teacher property age setter')
        self._age = value


'''
上面的方法,其实有个缺陷,我们必须清楚的知道,需要重写的propery所属的父类
这对于单继承通常的是没有问题的,但是对于多继承就会存在问题,比如继承树中存在多个同名的property
那么到底应该继承哪个property就会产生疑惑。
比较合理的解决办法是,如student这个类一样,彻底重写property的实例,再使用super()方法去调用父类的方法
'''


class Girl(Person):

    @property
    def age(self):
        print('girl property age getter')
        return super().age

    @age.setter
    def age(self, value):
        print('girl property age setter')
        super(Girl, Girl).age.__set__(self, value)


class PythonTestCase(unittest.TestCase):

    def setUp(self):
        self.man = Man(22)

    def test_init_class(self):
        # init的时候并没有执行setter方法,所以年龄不会变
        self.man = Man(35)
        self.assertEqual(self.man.age, 35)

    def test_set_tom_age(self):
        # 赋值的时候触发了setter方法,年龄x2
        self.man.age = 23
        self.assertEqual(self.man.age, 46)
        self.assertTrue(type(self.man.age) is int)

    def test_set_man_name(self):
        with self.assertRaises(AttributeError):
            self.man.name = 'tom'

    def test_set_person_age(self):
        # 如果没有实例,property会返回自身
        self.assertTrue(isinstance(Boy.age, property))
        # 给类赋值一个与property的同名属性时,会重写掉原先的特性
        Boy.age = 24
        self.assertEqual(Boy.age, 24)
        self.assertTrue(type(Boy.age) is int)

    def test_set_student_age(self):
        lilei = Student(age=12)
        self.assertEqual(lilei.age, 12)
        # 无法赋值,报错
        with self.assertRaises(AttributeError):
            lilei.age = 13

    def test_set_teacher_age(self):
        teacher = Teacher(age=28)
        self.assertEqual(teacher.age, 28)
        teacher.age = 26

    def test_set_girl_age(self):
        girl = Girl(age=13)
        self.assertEqual(girl.age, 13)
        girl.age = 14


if __name__ == '__main__':

    unittest.main()


