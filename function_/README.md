# Python笔记 - function、method

### 闭包

闭包是在其词法上下文中引用了自由变量的函数。

通俗地说，就是函数嵌套（后续称之为外层函数）另外一个函数（后续称之为内层函数），在内层函数中，引用外层函数的变量，每次对内层函数的调用，外层函数变量的值都会进行保持。

用个简单的例子来说明，使用闭包实现一个函数，求所有传入的数字的平均值。

```python
def averager():
    """
    闭包实现求平均值的例子
    每次传入一个数字，返回所有传入的数字的平均值
    :return:
    """
    count = 0
    total = 0.0

    def _averager(value):
        nonlocal total, count
        total += value
        count += 1
        average = total/count
        return average

    return _averager

# 调用外层函数averager，得到内层函数_averager的对象，赋值给avg
# 此时闭包形成，外层函数的变量total, count, average会被保持
avg = averager()
# 每次调用内层函数avg时，外层函数变量的值都会被记住
# 第一次调用，外层函数的变量count=1, total=10.0, average=10.0
print(avg(10))
# 10.0
# 第二次调用，外层函数变量的值不会重置，仍然保持上次调用的结果
# 此时 count=2, total=30.0, average=15.0
print(avg(20))
# 15.0
# 第三次调用，外层函数变量的值仍然会保持上次调用的结果
# 此时 count=3, total=36.0, average=12.0
print(avg(6))
# 12.0
```

上面的例子中，最重要的部分在调用外层函数averager时，需要返回内层函数的对象_averager，注意这里的`return _averager`没有括号，并不是调用内层函数，而是返回内层函数的对象。

当调用外层函数，返回内层函数对象时，即形成闭包。每次对内层函数的调用，外层函数中的变量的值，都会被记住，即保持上次调用的结果。

如果不容易理解，可以用类实例实现类似上面闭包的功能，实际执行中，因为类实例self的参与，运行速度要略慢于闭包的实现。

```python
# 以类实现类似上面闭包的功能
class Averager:

    def __init__(self):
        self.count = 0
        self.total = 0.0

    def __call__(self, value):
        self.total += value
        self.count += 1
        average = self.total/self.count
        return average

avg_cls = Averager()

print(avg_cls(10))
# 10.0
print(avg_cls(20))
# 15.0
print(avg_cls(6))
# 12.0
```

