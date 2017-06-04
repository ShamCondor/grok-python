#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 19:49
# @Author  : Matrix
# @Site    : 
# @File    : property.py
# @Software: PyCharm

__author__ = 'blackmatrix'


class Person(object):

    def __init__(self, age):
        self._age = age
        self._name = 'lilei'

    # @property 装饰器等同于 age = property(fget=age)
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        print('person proerty age setter')
        self._age = value * 2

    @property
    def name(self):
        return self._name


# 此例子说明property是可以被继承的
class Man(Person):
    pass


class Student(Person):

    # 如果在子类重新定义一个property,会完全覆盖掉父类的同名的property,包括里面的方法
    # 所以没有定义setter方法,age变为只读,无法赋值
    # 实际上,这种方式是在子类重新创建了一个名为age的property对象,覆盖掉了父类名为age的property
    # age = property(fget=..., fset=None)
    @property
    def age(self):
        print('student proerty age getter')
        return self._age


class Teacher(Person):

    # 只有这种方式才能正确的覆盖掉父类的getter方法
    @Person.age.getter
    def age(self):
        print('teacher proerty age getter')
        return self._age

    # 同样, 这样才能正确的覆盖掉父类特性的getter方法
    # property是个类,@Person.age.setter,这个操作相当于找到Person下,这个age(property实例)的方法fset
    # 并用我们在子类的方法将其覆盖。
    @Person.age.setter
    def age(self, value):
        print('teacher proerty age setter')
        self._age = value


if __name__ == '__main__':

    # init的时候并没有执行setter方法,所以年龄不会变
    tom = Man(22)
    print(tom.age)
    # 赋值的时候触发了setter方法,年龄x2
    tom.age = 23
    print(tom.age)
    print(type(tom.age))

    # 如果没有setter方法,则变为只读
    # tom.name = 'hanmeimei'
    # AttributeError: can't set attribute

    # 如果没有实例,property会返回自身
    print(Person.age)
    # 给类赋值一个与property的同名属性时,会覆盖掉原先的特性
    Person.age = 24
    print(Person.age)
    print(type(Person.age))

    # 子类覆盖父类的property
    lilei = Student(age=12)
    print(lilei.age)
    # 无法赋值,报错
    # lilei.age = 13

    jim = Teacher(27)
    jim.age = 30
    print(jim.age)


