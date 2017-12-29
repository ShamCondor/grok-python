# Python 笔记 - class

#### \__call__ 方法

1. \__call__ 方法可以让一个实例像函数那样被调用
2. \__call__ 是个实例方法,带self参数
3. \__call__方法只对类实例有效,如果想对类生效,需在元类中定义
4. 类定义了\__call__ 方法后，调用实例instance() 相当于`instance.__call__()`

```python
class ClassA:

    def __call__(self, *args, **kwargs):
        print('call ClassA instance')


if __name__ == '__main__':
    # ClassA实现了__call__方法
    a = ClassA()
    '''
    这个时候，ClassA的实例a，就变成可调用对象
    调用a()，输出call ClassA instance，说明是调用了
    __call__函数
    '''
    a()
    # 其实a()等同于a.__call__()，它本质上就是后者的缩写
    a.__call__()
    # 判断是否可调用，输出True
    print(callable(ClassA))
    print(callable(a))
```

#### \__getattribute__ 方法

1. \__getattribute__可以无限制的访问**类实例**的所有属性。这里需要注意,是访问类实例而不是类对象,只对实例有效
2. 如果要对类对象自身产生效果，需要在元类中定义\__getattribute__
3. 如果同时定义`__getattr__` 和 `__getattribute__`，`__getattr__`通常不会被调用。除非`__getattribute__`明确抛出AttributeErro 异常。在__getattribute__方法中,直接通过 . 号运算取值和通过\__dict__取值,都会引发无限递归
4. 为了避免无限递归,要调用父类的\__getattribute__方法来获取当前类属性的值
5.  \__getattribute__ 在python 2.x 中,只有新式类可用

```python
class ClassA:

    x = 'a'

    '''
    当在__getattribute__代码块中，再次执行属性的获取操作时，
    会再次触发__getattribute__方法的调用，代码将会陷入无限递归，
    直到Python递归深度限制（重载__setter__方法也会有这个问题）。
    同时，也没办法通过从__dict__取值的方式来避免无限递归。
    为了避免无限递归，应该把获取属性的方法指向一个更高的超类，
    例如object（因为__getattribute__只在新式类中可用，而新式类所有的类都显式或隐式地继承自object，
    所以对于新式类来说，object是所有新式类的超类）。
    '''
    def __getattribute__(self, name):
        # 使用super获取代理类,执行父类的__getattribute__避免无限递归
        return super().__getattribute__(name)
        # 无限递归
        # return self.__dict__[name]


if __name__ == '__main__':
    a = ClassA()
    print(a.x)
```

