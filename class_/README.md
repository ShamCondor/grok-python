# Python 笔记 - class

#### `__call__` 方法

1. `__call__` 方法可以让一个实例像函数那样被调用
2. `__call__` 是个实例方法,带self参数
3. `__call__`方法只对类实例有效,如果想对类生效,需在元类中定义
4. 类定义了`__call__` 方法后，调用实例 `instance()` 相当于`instance.__call__()`

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

#### `__getattribute__` 方法

1. `__getattribute__`可以无限制的访问**类实例**的所有属性。这里需要注意,是访问类实例而不是类对象,只对实例有效
2. 如果要对类对象自身产生效果，需要在元类中定义`__getattribute__`
3. 如果同时定义`__getattr__` 和 `__getattribute__`，`__getattr__`通常不会被调用。除非`__getattribute__`明确抛出AttributeError 异常。在`__getattribute__`方法中,直接通过 . 号运算取值和通过`__dict__`取值,都会引发无限递归
4. 为了避免无限递归,要调用父类的`__getattribute__`方法来获取当前类属性的值
5. `__getattribute__` 在python 2.x 中,只有新式类可用

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

#### property 特性

1. 特性是对类的一个特定属性进行拦截，在操作这个属性时，执行特定的函数，对属性的操作进行拦截。

2. 特性使用property类来实现，也可以使用property装饰器实现，二者本质是一样的。

3. property类的`__init__`函数接收4个参数，来实现属性的获取、赋值、删除及文档。**4个参数都不是必须的，如果没有传入对应的操作函数，取默认值None，则对应的操作不受支持，试图调用默认值None时，会引发异常。**

4. 特性仅在实例中生效。

5. 特性可以继承

   1. 如果在子类重新定义一个property,会完全重写掉父类的同名的property,包括里面的所有方法

      ```python
      class Student(Person):
          # 如果在子类重新定义一个property,会完全重写掉父类的同名的property,包括里面的所有方法
          # 所以没有定义setter方法,age变为只读,无法赋值
          # 实际上,这种方式是在子类重新创建了一个名为age的property对象,重写掉了父类名为age的property
          # age = property(fget=..., fset=None)
          @property
          def age(self):
              print('student property age getter')
              return self._age
      ```

   2. 如果只希望重写部分父类的property方法，建议完全覆盖掉父类的同名property，在实现的时候，通过super()调用父类的方法

      ```python
      class Girl(Person):

          @property
          def age(self):
              print('girl property age getter')
              return super().age

          @age.setter
          def age(self, value):
              print('girl property age setter')
              super(Girl, Girl).age.__set__(self, value)
      ```

#### 类、实例与方法的绑定关系

类与方法的绑定关系：

1. 类中的实例方法，与类本身并没有绑定关系 （function）
2. 类中的静态方法，与类也没有绑定关系 （function）
3. 类中的类方法，是和这个类存在绑定关系的  (bound method)

实例与方法的绑定关系：

1. 因为当通过一个实例去访问类中的某方法时，会形成绑定关系，将实例作为第一个参数self传入 (bound method)
2. 类方法与实例也存在绑定关系，所以实例可以直接调用类方法 (bound method)
3. 静态方法与实例没有绑定关系（function）

手动创建绑定关系：

1. 如果直接将函数赋值给类，不会创建类与函数的绑定关系，相当于实例方法

   ```python
   # 创建实例 class_a
   class_a = ClassA()
   ClassA.func_a = func_a
   # 直接将函数赋值给类，不会创建类与函数的绑定关系
   # <function func_a at 0x10e41ff28>
   print(ClassA.func_a)
   ```

2. 对于赋值之前创建的实例，因为是通过实例访问，实例不存在这个方法，会调用类中的方法（根据第一点，可以理解为给类创建了一个实例方法），通过实例去调用实例方法， 所以也会存在绑定关系

   ```python
   # 对于赋值之前创建得实例，因为是通过实例访问，所以也会存在绑定关系
   # <bound method func_a of <__main__.ClassA object at 0x10e4330b8>>
   print(class_a.func_a)
   ```

3. 直接将函数赋值实例，不会创建绑定关系，没有绑定关系，通过实例调用函数不会传入self

   ```python
   class_a.func_c = func_c
   # <function func_c at 0x10e59f1e0>
   print(class_a.func_c)
   # 下面的调用方式，因为没有绑定关系，无法获取到实例自身，即不会作为self传入
   # class_a.func_c()
   ```

#### MethodType 将一个可调用对象绑定到类或实例上

上面的例子可以看出，手动将函数赋值给类或实例，并不能保证成功创建绑定关系，所以就需要引入MethodType，用于将一个可调用对象绑定到类或实例上。

1. MethodType 接受两个参数，第一个是被绑定的函数，第二个是需要绑定到的对象
2. MethodType 会在类内部创建一个链接，指向外部的的方法，在创建实例的同时，这个绑定后的方法也会复制到实例中