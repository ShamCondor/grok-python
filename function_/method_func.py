#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 20:33
# @Author  : Matrix
# @Site    :
# @File    : func_method.py
# @Software: PyCharm
from common_.decorator import test_decorator

__author__ = 'blackmatrix'

'''
本例验证函数与方法的区别

概要:
1.  函数(function)是Python中一个可调用对象(callable), 方法(method)是一种特殊的函数
2.  一个可调用对象是方法和函数，和这个对象无关，判断条件：是否与类或实例绑定（bound method）
3.  实例方法，在类中未和类绑定，是函数。在实例中，此实例方法与实例绑定，即变成方法
4.  静态方法没有和任何类或实例绑定，所以静态方法是个函数
5.  装饰器不会改变被装饰函数或方法的类型
6.  类实现__call__方法,其实例也不会变成方法或函数,依旧是类的实例
7.  使用callalble() 只能判断对象是否可调用,不能判断是不是函数或方法
8.  判断对象是函数或方法应该使用type(obj)

'''


def the_function():
    """
    函数
    :return: 
    """
    pass


class TheClass:

    def __call__(self, *args, **kwargs):
        return self

    @classmethod
    def class_method(cls):
        """
        类方法
        :return: 
        """
        pass

    def instance_method(self):
        """
        实例方法
        """
        return self

    @staticmethod
    def static_method():
        """
        静态方法
        :return: 
        """
        pass

    @test_decorator
    def decorated_func(self):
        pass

if __name__ == '__main__':

    the_class = TheClass()

    print('''
     类方法和实例方法都是方法（method）
    ''')
    print('class_method type {type} '.format(type=type(TheClass.class_method)))
    # class_method type <class_ 'method'>
    print('instance_method type {type} '.format(type=type(the_class.instance_method)))
    # instance_method type <class_ 'method'>

    print('- ' * 40)

    print('''
    为什么说类方法和实例方法都是方法，通过下面的代码，
    可以获取到类方法，和实例方法，都是 bound method，
    与类或实例建立了绑定关系，所以它们都是方法。
    ''')
    print(TheClass.class_method)
    # <bound method TheClass.class_method of <class '__main__.TheClass'>>
    print(the_class.instance_method)
    # <bound method TheClass.instance_method of <__main__.TheClass object at 0x00000275DEB3FC50>>

    print('- ' * 40)

    print('''
    比较特别的是
    通过类去访问实例方法，得到的结果并非是绑定方法，
    也就是说，如果类中的一个实例方法， 并没有和类创建绑定关系，
    所以，它是函数而不是方法。
    当类被实例化时，实例方法才会绑定到类创建出的实例上，此时实例方法
    与实例形成绑定关系，是方法而不是函数。
    总结下，当一个实例方法，通过类去访问时，因为不存在绑定关系，它是函数而不是方法。
    通过实例去访问时，存在绑定关系，那么它就成了方法。
    ''')
    print('instance_method type {type} '.format(type=type(TheClass.instance_method)))
    # instance_method type <class 'function'>
    print(TheClass.instance_method)
    # <function TheClass.instance_method at 0x00000275DEB3D840>

    print('- ' * 40)

    print('''
    接着试试静态方法，先通过实例去访问静态方法，得出结果，它是函数而不是方法
    ''')
    print('static_method type {type} '.format(type=type(the_class.static_method)))
    # static_method type <class_ 'function_'>
    print('''
    再通过类去访问静态方法，得出的结果依旧是函数，而不是方法
    ''')
    #
    print('static_method type {type} '.format(type=type(TheClass.static_method)))
    # static_method type <class 'function'>
    print('''
    直接打印这两种访问静态方法的方式， 发现它们并不是绑定方法
    ''')
    print(TheClass.static_method, the_class.static_method, sep='\n')
    # <function TheClass.static_method at 0x0000024BC5EAD950>
    # <function TheClass.static_method at 0x0000024BC5EAD950>
    print('''
    那么，结论就很清楚了，判断一个可调用对象，是函数还是方法，
    跟它是类方法、实例方法、静态方法或者外部函数，都关系不大。
    唯一的判断条件，就是这个对象，是否和某个类或实例进行绑定，如果
    绑定，即方法，如果未绑定，即函数。
    ''')

    # 对于一个函数，因为不会和任何类或实例绑定（除非使用MethodType将函数绑定到某个实例上)
    # 必然不是方法。
    print('the_function type {type} '.format(type=type(the_function)))
    # the_function type <class_ 'function_'>

    """
    关于装饰器的测试
    """
    # 装饰器本身会不会改变被装饰函数的类型
    # 装饰器本身也是个函数
    print('test_decorator type {type} '.format(type=type(test_decorator)))
    # test_decorator type <class_ 'function_'>

    # 将装饰器装饰器到实例方法上
    # 检查被装饰的方法的类型
    print('decorated_func type {type} '.format(type=type(the_class.decorated_func)))
    # decorated_func type <class_ 'method'>
    # 从测试结果得知，装饰器不会影响被装饰方法或函数的类型

    """
    一个类实现__call__()方法，其实例既不会是方法也不会是函数
    """
    # 如果类实现__call__方法
    # 执行结果True 其实例变为可调用对象
    print('class_instance callable {callable} '.format(callable=callable(the_class)))
    # 实例的类型依旧是这个类，而不会变成函数或方法
    print('class_instance type {type} '.format(type=type(the_class)))
    # class_instance type <class_ '__main__.TheClass'>



