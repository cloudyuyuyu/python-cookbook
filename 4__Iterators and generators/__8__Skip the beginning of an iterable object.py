# 1
# 1
# 1
# 1
# 1
# 1

from util.separator import separator_content
import sys
from itertools import dropwhile, islice

if __name__ == "__main__":
    """
    问题
        你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。

    解决方案
        itertools 模块中有一些函数可以完成这个任务。 
        
        首先介绍的是 itertools.dropwhile() 函数。使用时，你给它传递一个函数对象和一个可迭代对象。 
        它会返回一个迭代器对象，丢弃原有序列中直到函数返回 False 之前的所有元素，然后返回后面所有元素。
    """
    separator_content()
    with open(sys.argv[0],
              encoding="utf-8") as file:
        for line in dropwhile(lambda line: line.startswith("#"), file):
            print(line)

    """
        如果你已经明确知道了要跳过的元素的个数的话，那么可以使用 itertools.islice() 来代替。比如
    """
    separator_content()
    items = ["a", "b", "c", 1, 4, 10, 15]
    for x in islice(items, 3, None):
        print(x)

    """
    最后需要着重强调的一点是，本节的方案适用于所有可迭代对象，包括那些事先不能确定大小的， 比如生成器，文件及其类似的对象。
    """
