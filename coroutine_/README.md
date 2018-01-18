# Python 笔记 - 协程

## 生成器（yield）作为协程

yield实际上是生成器，在python 2.5中，为生成器增加了.send(value)方法。这样调用者可以使用send方法对生成器发送数据，发送的数据在生成器中会赋值给yield左侧的变量（如果有的话），可以生成器可以作为协程使用。

下面是一个使用生成器实现的，求平均值的函数

```python
def averager1():
    """
    使用yield接收数值，并求平均值
    :return:
    """
    count = 0
    total = 0.0
    average = 0.0
    while True:
        value = yield average
        count += 1
        total += value
        average = total/count


avg1 = averager1()
# 预激活协程，程序执行到yield出暂停，产出average，输出0.0
print(next(avg1))
# 0.00
# 向协程发送数字
print(avg1.send(10))
# 10.0
print(avg1.send(20))
# 15.0
print(avg1.send(30))
# 20.0
```

yield在函数中，起到一个函数流程控制的作用。

首先，调用生成器函数，创建一个生成器对象avg。然后对生成器对象进行预激活，这里的预激活指的是让生成器对象执行到yield除，然后会暂停。因为生成器对象只有在yield除暂停时，才能接收到调用者通过send方法发送给生成器的值，所以没有进行预激活的生成器对象无法正常工作。

这里yield起到一个类似桥梁的作用，连接生成器调用者，和生成器对象内部的变量。我们知道，python的赋值语句，是从右向左执行的，所以在这里例子中，`yield average`会先执行，将average产出。

这个时候程序的控制器转交给调用者，继续执行print语句，所以`print(next(avg))`会输出yield产出的值，即average，输出0.00。

生成器的调用者继续往下执行，调用生成器的send方法，将10发送给生成器对象。开头说过，调用生成器对象的send方法，发送的数据，会赋值给yield左边的变量。在这个例子中，value = yield ~~average~~， 暂时先把yield右侧的average忽略掉，只看value = yield，可以理解为，将yield获取到了调用者通过send方法发送给生成器的值，然后把这个值赋值给左侧的变量value，接着是简单的计算平均值，这样就实现了调用者给生成器对象发送数据。

注意生成器内部有个while的无限循环，生成器内部的代码会继续执行，直到再次遇到yield，程序暂停，再次把average的值产出，并将程序的控制器再次转交回调用者。

这个时候调用者继续执行print语句，输出average的值：10.0。后面的几次send也是一样的效果。

## 终止生成器对象的循环

之前的例子，`while True`会导致生成器对象无限循环，每次都会在yield除暂停，产出平均值average，并等待接收调用者再次通过send方法传入的新值。

如果需要终止生成器对象的无限循环，可以用三种方式：

- 发送哨符终止循环
- 调用生成器的.throw()方法终止循环
- 调用生成器的.close()方法终止循环

### 发送哨符终止循环

从最简单的发送哨符终止循环开始，简单的说，就是发送一个特定的值给生成器对象，当生成器获取到这个值时，就通过break语句退出while循环。

```python
def averager2():
    """
    使用yield接收数值，并求平均值
    相对于上面的例子，增加了使协程退出的哨符
    :return:
    """
    count = 0
    total = 0.0
    average = 0.0
    while True:
        value = yield average
        # 当value为None时，退出循环
        if value is None:
            break
        count += 1
        total += value
        average = total/count

avg2 = averager2()
# 预激活协程，因为yield右边没有变量，所以不会产出值
print(next(avg2))
# 0.0
# 向协程发送数字
print(avg2.send(10))
# 10.0
print(avg2.send(20))
# 15.0
print(avg2.send(30))
# 20.0
# 生成器循环终止时会抛出StopIteration
# 所以做一个异常捕获
try:
    avg2.send(None)
except StopIteration:
    pass
```

上面的生成器函数，做了一个简单的判断，当value为None时，就执行break语句退出生成器对象的循环。生成器循环终止时会抛出StopIteration，这个也会作为后面生成器返回值的途径。

### 调用.throw()方法终止循环

调用生成器的.throw()方法，会将异常发送给生成器，生成器的处理规则如下：

1. 生成器在yield处暂停时，会接收到throw方法传入的异常
2. 如果生成器能正确处理传入的异常，那么生成器的代码会继续执行，yield产出右侧的值（如果右侧有值的话），并作为调用者调用生成器.throw()方法的返回值
3. 如果生成器不能处理传入的异常，那么生成器的代码会中止运行，并将异常向上冒泡，再次发给调用者

看一个例子

```python
# 对第一个函数averager1进行修改，增加处理ValueError的代码
def averager3():
    """
    使用yield接收数值，并求平均值
    对第一个函数averager3进行修改，增加处理ValueError的代码
    :return:
    """
    count = 0
    total = 0.0
    average = 0.0
    while True:
        try:
            value = yield average
            count += 1
            total += value
            average = total/count
        except ValueError:
            # 如果捕获到ValueError，什么都不做
            # 这样生成器会继续循环，直到再次遇到yield暂停
            pass


avg3 = averager3()
next(avg3)
print(avg3.send(10))
# 10.0
print(avg3.send(20))
# 15.0
# throw一个生成器可以处理的异常ValueError，没有任何影响
# 生成器会继续运行，产出average，因为在yield处就报错，后续的代码没有执行
# 所以average仍然为15.0
# yield会将average产出，产出的值作为调用者执行生成器的throw方法的返回值，最终输出15.0
print(avg3.throw(ValueError))
# 15.0
# throw一个生成器不能处理的异常，生成器循环终止
try:
    print(avg3.throw(TypeError))
except TypeError:
    print('生成器无法处理TypeError，异常向上冒泡抛出，循环终止')
```

### 调用.close()方法终止循环