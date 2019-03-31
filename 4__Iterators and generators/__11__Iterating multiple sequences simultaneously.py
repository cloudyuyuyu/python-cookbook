from util.separator import separator_content
from itertools import zip_longest
from collections import Iterator, Iterable, Generator

if __name__ == "__main__":
    """
    问题
        你想同时迭代多个序列，每次分别从一个序列中取一个元素。

    解决方案
        为了同时迭代多个序列，使用 zip() 函数。
    """
    separator_content()

    x_axis = [1, 5, 4, 2, 10, 7]
    y_axis = [101, 78, 37, 15, 62, 99]
    for x, y in zip(x_axis, y_axis):
        print(x, y)

    """
    zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中 x 来自 a，y 来自 b。 

    一旦其中某个序列到底结尾，迭代宣告结束。 因此迭代长度跟参数中最短序列长度一致。
    """
    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']

    for pair in zip(a, b):
        print(pair)

    """
        如果这个不是你想要的效果，那么还可以使用 itertools.zip_longest() 函数来代替。
    """
    separator_content()
    for pair in zip_longest(a, b):
        print(pair)

    separator_content()
    for pair in zip_longest(a, b, fillvalue=0):
        print(pair)

    """
        当你想成对处理数据的时候 zip() 函数是很有用的。 

        比如，假设你头列表和一个值列表，就像下面这样：
    """
    separator_content()
    keys = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]

    for key, value in dict(zip(keys, values)).items():
        print(key, value, sep=":")

    for key, value in zip(keys, values):
        print(key, value, sep=":")

    """
        虽然不常见，但是 zip() 可以接受多于两个的序列的参数。

        这时候所生成的结果元组中元素个数跟输入序列个数一样。
    """
    separator_content()
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    for triple in zip(a, b, c):
        print(triple)

    print(list(zip(a, b, c)))

    """
        最后强调一点就是， zip() 会创建一个迭代器来作为结果返回。 

        如果你需要将结对的值存储在列表中，要使用 list() 函数。

        《迭代器只能遍历一次》
    """
    separator_content()
    _list = [1, 2, 3]
    print(dir(_list))
    iter_list = iter(_list)
    for _ in iter_list:
        print(_)

    for _ in iter_list:
        print(_)

    separator_content()
    for _ in _list:
        print(_)

    for _ in _list:
        print(_)

    print(isinstance(_list, Iterable))
    print(isinstance(_list, Iterator))
    print(isinstance(iter(_list), Iterator))

    separator_content()
    print(isinstance(zip(a, b, c), Iterable))
    print(isinstance(zip(a, b, c), Iterator))
    print(isinstance(zip(a, b, c), Generator))

    separator_content()
    generator_list = (x for x in range(10))
    print(isinstance(generator_list, Iterable))
    print(isinstance(generator_list, Iterator))
    print(isinstance(generator_list, Generator))