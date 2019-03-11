import unittest
from collections import Counter

__author__ = 'blackmatrix'

"""
Counter是dict的子类
"""


class CounterTestCase(unittest.TestCase):

    def setUp(self):
        self.foo = Counter('assfwdasxtr')
        self.bar = Counter([1, 2, 3, 1, 7, 7, 8, 2, 7, 8, 9, 1, 5, 8])
        self.foobar = Counter(a=3, b=2, c=0, d=-1)
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def testCounterSeq(self):
        """
        统计可迭代对象各个元素出现的次数
        :return:
        """
        self.assertEqual(self.foo, Counter({'s': 3, 'a': 2, 'f': 1, 'w': 1, 'd': 1, 'x': 1, 't': 1, 'r': 1}))
        self.assertEqual(self.bar, Counter({1: 3, 7: 3, 8: 3, 2: 2, 3: 1, 9: 1, 5: 1}))

    def testCounterElements(self):
        """
        elements()方法根据Counter计数的结果，返回含有所有元素的生成器
        :return:
        """
        # 返回一个生成器
        elements = self.foo.elements()
        # 将生成器转换成list，进行比较
        self.assertEqual(list(elements), ['a', 'a', 's', 's', 's', 'f', 'w', 'd', 'x', 't', 'r'])
        elements = self.bar.elements()
        # 将生成器转换成list，进行比较
        self.assertEqual(list(elements), [1, 1, 1, 2, 2, 3, 7, 7, 7, 8, 8, 8, 9, 5])

    def testCounterMostCommon(self):
        """
        返回计数最多的前n个元素，如果n省略的话返回全部元素
        返回的的对象为list，每个list的元素都是tuple
        tuple第一个元素为Counter统计的元素名称，第二个元素为统计的次数
        :return:
        """
        most_common = self.foo.most_common(2)
        self.assertEqual(most_common, [('s', 3), ('a', 2)])
        most_common = self.foo.most_common()
        self.assertEqual(most_common, [('s', 3), ('a', 2), ('f', 1), ('w', 1), ('d', 1), ('x', 1), ('t', 1), ('r', 1)])

    def testCounterKeyCount(self):
        """
        counter.get(key)方法，返回序列中key出现的次数，如果key不存在，则返回None
        counter[key]，返回序列中key出现的次数，如果key不存在，则返回0
        在key存在的情况下，counter.get(key) 与 counter[key] 的运行结果相同
        :return:
        """
        key_count = self.foo.get('s')
        self.assertEqual(key_count, 3)
        self.assertEqual(self.foo['s'],  self.foo.get('s'))
        key_count = self.foo.get('z')
        self.assertEqual(key_count, None)
        key_count = self.foo['z']
        self.assertEqual(key_count, 0)

    def testCounterSubtract(self):
        """
        将两个Counter的实例进行相减
        :return:
        """
        x = Counter(a=6, b=5, c=3, d=0)
        first_x_id = id(x)
        y = Counter(a=1, b=2, c=3, d=1)
        # x 减去 y
        x.subtract(y)
        sec_x_id = id(x)
        # 两个Counter实例key相同的情况下，逐个key的统计数量进行相减
        # 可能得到负数的情况
        self.assertEqual(x, Counter({'a': 5, 'b': 3, 'c': 0, 'd': -1}))
        # x 在相减前后id相同，说明是对x对象进行修改，而不是重新创建一个对象再赋值给x
        self.assertEqual(first_x_id, sec_x_id)
        # 当某个key小于0时，使用elements()方法不再输出含有这个key的生成器实例
        self.assertEqual(list(x.elements()), ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b'])
        # 如果减去的counter对象含有被减去counter对象不存在的key，则被减去counter对象不存在的key以0计数
        # 如下的x减去z，z含有x不存在的 f、j、k，则x的f、j、k的计数默认为0
        # 特别是k，x的k为0，z的k为-2，使用最终运算结果，x的k为2
        z = Counter(a=2, b=1, f=3, j=0, k=-2)
        x.subtract(z)
        self.assertEqual(x, Counter({'a': 3, 'b': 2, 'k': 2, 'c': 0, 'j': 0, 'd': -1, 'f': -3}))

    def testCounterSubtract2(self):

        x = Counter(a=6, b=5, c=3, d=0)
        y = Counter(a=1, b=2, c=3, d=1)
        z = x - y
        # 使用减号运算结果，与subtract方法有几个不同：
        # 1. 运算结果小于等于0的key不再被保留，如下例子，为0的c和为-1的d都已经消失
        self.assertEqual(z, Counter(a=5, b=3))
        # 2. 使用减少运算符会创建一个新的对象，而不是对被减的counter实例直接修改
        self.assertNotEqual(id(x), id(z))

    def testCounterAddition(self):
        x = Counter(a=6, b=5, c=0, d=-1)
        y = Counter(a=1, b=2, c=0, d=-2)
        z = x+y
        self.assertEqual(z, Counter({'a': 7, 'b': 7}))
        self.assertNotEqual(id(x), id(z))



if __name__ == "__main__":
    unittest.main()
