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


if __name__ == "__main__":
    unittest.main()
