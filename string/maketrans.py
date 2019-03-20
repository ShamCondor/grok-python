#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 10:54 PM
# @Author  : Matrix
# @Site    : 
# @Software: PyCharm
import string
import unicodedata

__author__ = 'BlackMatrix'


# 创建字符映射关系的转换表，接收两个相同长度的字符串，两字符串通过位置的字符即代表转换前和转换后的字符
# 返回的类型是dict
single_map = str.maketrans(""",ƒ,,†ˆ‹‘’“”•––˜›""", """'f"*^<''""---~ >""")

multi_map = str.maketrans({
    '€': '< euro >',
    '…': '...',
    # 'OE': 'OE',
    '™': '( TM)',
    # 'oe': 'oe',
    '‰': '< per mille >',
    '‡': '**',
})

# 合并两个dict
multi_map.update(single_map)


def shave_marks_latin(txt):
    # 使用NFD进行规范化，可以将拉丁基字符和变音符号拆分开。
    # café会被拆成cafe加上变音符号́:，这样就为后续的遍历，过滤非拉丁基字符提供条件。
    norm_txt = unicodedata.normalize('NFD', txt)
    # str规范化后依旧是str，已经将基字符和变音符号拆开
    # 但是如果直接print(norm_txt)的话，依旧会打印出café，属于正常情况
    assert isinstance(norm_txt, str)
    latin_base = False
    keepers = []
    for c in norm_txt:
        # combining配合NFD的规范化使用
        # 判断使用NFD规范化后的字符串中每个字符，是否是组合字符
        # 通俗的说，NFD把cafè拆成cafe和 ́:
        # 这样在做迭代时，判断到e时，combining返回0，判断到变音符号́ : 时，combining返回230
        # 这样可以得知最后一个c是组合字符，再结合latin_base变量，等于True时表明上个迭代的项是英文字母，可以认为当前c是变音符号。
        # 所以使用continue跳过循环，实现过滤掉变音符号的效果
        if unicodedata.combining(c) and latin_base:
            continue
        keepers.append(c)
        # 判断迭代的元素是不是拉丁基字符，拉丁基字符会返回0，所以要加not
        if not unicodedata.combining(c):
            # string.ascii_letters需import string
            # ascii_letters 返回所有的ascii字符
            # 如果c是英文字母，那么把latin_base设置为True，为下次循环做准备
            # 即告知下次循环时，上个元素是个英文字母，那么下个循环如果是组合字符，就认为是变音符号。
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)


def dewinize(txt):
    # str.translate(table[, deletechars]);
    # table即映射表，由maketrans创建
    # deletechars 字符串中需要过滤的字符列表
    return txt.translate(multi_map)


def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)


if __name__ == '__main__':

    order = '“ Herr Vo ß: • ½ cup of OEtker ™ caff è latte • bowl of a ç a í.”'

    print(dewinize(order))
    print(asciize(order))

