#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/7/12 21:27
# @Author  : BlackMatrix
# @Site : 
# @File : descriptor.py
# @Software: PyCharm

__author__ = 'blackmatrix'

"""
本例主要测试不同情况下的描述符，对类属性、实例属性的控制程度

概要：
1.  实现描述符协议的类即是描述符，通常是含有__get__ 、 __set__ 、__delete__方法的类
2.  实现 __set__ 方法的类，称之为 覆盖型描述符， 没有实现 __set__ 方法的类，称之为非覆盖型描述符
3.  同时实现 __set__ 和 __get__ 方法的类，通常称之为 强制描述符
4.  实现 __set__ 方法的描述符，会接管实例属性的赋值操作，但是不能接管类属性的赋值操作。
     如果需要使用描述符接管类属性的赋值操作，需要通过在元类中定义描述符来实现
5.  实现 __get__ 方法的描述符，会同时接管 类属性和 实例属性的赋值操作，这点和 4 不同
6.  对于非覆盖型描述符（没有实现__set__方法），当实例对描述符同名属性进行赋值时，
    不会触发描述符的__set___方法（本来就没有）， 而是直接在实例属性中，创建一个同名的变量。
    对这个变量进行取值时，优先返回实例自身的属性，而不去访问类中的描述符，所以描述符的 __get__ 方法不会运行
"""


class OverAll:

    """
    描述符是指含有__get__ 、 __set__ 、__delete__方法的类， 
    对于实现了 __set__方法的类，称之为覆盖描述符，
    如果同时也实现了 __get__ 方法，则称之为强制描述符
    """

    def __get__(self, instance, owner):
        print("强制描述符 __get__ 被运行")
        return self, instance, owner

    def __set__(self, instance, value):
        print("强制描述符 __set__ 被运行")
        return self, instance, value

    def __delete__(self, instance):
        print("强制描述符 __delete__ 被运行")


class OnlySet:
    """
    对于覆盖型描述符，因为实现了__set__方法，
    会覆盖掉实例属性的赋值操作
    但不会影响类属性的赋值操作
    """
    def __set__(self, instance, value):
        print("覆盖型描述符 __set__ 被运行")
        return self, instance, value


class OnlyGet:
    """
    如果描述符没有实现 __set__ 方法（即只有 __get__ 或 __delelte__），
    则称之为非覆盖型描述符
    """

    def __get__(self, instance, owner):
        print("非覆盖型描述符 __get__ 被运行")
        return self, instance, owner


class Spam:
    """
    定义一个类，类属性是上面三种描述符
    """
    over_all = OverAll()
    only_set = OnlySet()
    only_get = OnlyGet()


if __name__ == '__main__':

    # 实例化Spam
    spam = Spam()

    # 获取 实例的 强制描述符时，会发现描述符的 __get__ 方法被执行
    print(spam.over_all)
    # (<__main__.OverAll object at 0x000002C120637630>, <__main__.Spam object at 0x000002C1206376A0>, <class '__main__.Spam'>)

    # 获取实例的覆盖型描述符时，因为没有 __get__ 方法，直接获取到的是类属性，即描述符自身
    print(spam.only_set)
    # <__main__.OnlySet object at 0x000002C1206375F8>

    # 获取实例的非覆盖型描述符时，会发现描述符的 __get__ 方法被执行
    print(spam.only_get)
    # 非覆盖型描述符 __get__ 被运行
    # (<__main__.OnlyGet object at 0x000002C120637668>, <__main__.Spam object at 0x000002C1206376A0>, <class '__main__.Spam'>)

    # 对实例的强制描述符进行赋值
    # 发现描述符的 __set__ 被执行，打印出 "强制描述符 __set__ 被运行"
    spam.over_all = 1
    # 再进行取值，发现还是调用描述符的 __get__ 方法
    # 说明实例的属性读写，被强制描述符接管
    print(spam.over_all)
    # 强制描述符 __get__ 被运行
    # (<__main__.OverAll object at 0x000001899995C5C0>, <__main__.Spam object at 0x000001899995C630>, <class '__main__.Spam'>)

    # 对实例的覆盖性描述符进行赋值
    # 发现描述符的 __set__ 方法被执行，打印出 “覆盖型描述符 __set__ 被运行”
    spam.only_set = 2
    # 同样进行取值， 因为没有__get__方法，描述符不会接管实例属性的读取，
    # 所以还是直接通过类属性，返回描述符对象
    print(spam.only_set)
    # <__main__.OnlySet object at 0x000001A3C49575C0>

    # 前面试验过，对实例的覆盖性描述符取值，会返回描述符对象
    # 对实例的非覆盖描述符进行赋值，因为没有 __set__ 方法
    # 所以描述符本身没有接管实例属性的赋值操作
    spam.only_get = 3
    # 这个时候，会实例属性进行取值，就会发现描述符的 __get__ 方法也不会执行
    # 所以打印结果应该是 3
    print(spam.only_get)
    '''
    出现这种情况的原因是通过实例去获取属性时，优先返回的是实例自身的属性，
    只有在实例自身没有这个属性的情况下，才会到类中查找对应的属性
    描述符本身也是属于类属性，所以受到这个规则的影响。
    在 spam.only_get = 3 语句，对 only_get 进行赋值时，实际上已经在
    实例中创建出一个同名的属性 only_get， 后续再对 only_get 进行读取，
    获取的是实例的属性only_get，而不是类属性，即描述符 only_get。
    所以 描述符的 __get__ 方法不会触发
    《Python Cookbook》中有一个例子，巧妙利用这个特点，实现惰性求值！
    '''
    # 将实例属性删除，再获取一次 spam.only_get ，就会发现描述符的__get__正常执行了
    del spam.only_get
    print(spam.only_get)
    # (<__main__.OnlyGet object at 0x0000017EFBAC7668>, <__main__.Spam object at 0x0000017EFBAC76A0>, <class '__main__.Spam'>)

    '''
    对于实现了 __get__ 方法的描述符，不仅对实例属性的读取有效，对类属性的读取也是有效的。
    '''
    print(Spam.over_all)
    # 强制描述符 __get__ 被运行
    # (<__main__.OverAll object at 0x00000283A7C275F8>, None, <class '__main__.Spam'>)
    print(Spam.only_get)
    # 非覆盖型描述符 __get__ 被运行
    # (<__main__.OnlyGet object at 0x00000283A7C27630>, None, <class '__main__.Spam'>)

    '''
    比较特别的是，无论描述符是否实现 __set__ 方法，对于类属性的赋值来说，都是会被直接覆盖掉的。
    也就是说，描述符无法接管类属性的赋值操作。
    '''
    # 对类属性描述符进行赋值，会直接把描述符覆盖掉，并且不会触发描述符的__set__方法
    Spam.over_all = 1
    # 因为作为类属性的描述符已经被覆盖，所以会打印出 1
    print(Spam.over_all)

    '''
    这个时候，实例读取描述符，会发现已经被修改。
    谨慎进行这种操作！
    '''
    # 打印结果也是 1，因为实例本身没有存储这个描述符属性，而是通过类属性去获取
    # 这个时候类型属性的描述符已经被 int 类型的 1 覆盖掉了
    # 如果原先实例的 over_all 已经进行赋值，这个时候可能会导致实例属性over_all丢失
    print(spam.over_all)


