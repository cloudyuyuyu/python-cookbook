from util.separator import separator_content
from collections import defaultdict
import sys

if __name__ == "__main__":
    """
    问题
        你想在迭代一个序列的同时跟踪正在被处理的元素索引。

    解决方案
        内置的 enumerate() 函数可以很好的解决这个问题：
    """
    separator_content()
    my_list = ["a", "b", "c"]
    for index, value in enumerate(my_list):
        print("{}:{}".format(index, value))

    """
        这种情况在你遍历文件时想在错误消息中使用行号定位时候非常有用
    """
    for index, value in enumerate(my_list, start=1):
        print("{}:{}".format(index, value))


    def parse_data(file_name):
        with open(file_name, 'rt') as f:
            for index, line in enumerate(f, 1):
                fields = line.split()
                try:
                    count = int(fields[1])
                except ValueError as e:
                    print('Line {}: Parse error: {}'.format(index, e))


    """
        enumerate() 对于跟踪某些值在列表中出现的位置是很有用的。 
    
        所以，如果你想将一个文件中出现的单词映射到它出现的行号上去，可以很容易的利用 enumerate() 来完成：
    """
    separator_content()

    word_summary = defaultdict(set)

    with open(sys.argv[0],
              encoding="utf-8") as file:
        lines = file.readlines()

    for index, line in enumerate(lines):
        # Create a list of words in current line
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].add(index)
    print(word_summary)

    """
    enumerate() 函数返回的是一个 enumerate 对象实例， 它是一个迭代器，返回连续的包含一个计数和一个值的元组， 
    
    元组中的值通过在传入序列上调用 next() 返回。
    """

    """
    还有一点可能并不很重要，但是也值得注意， 
    
    有时候当你在一个已经解压后的元组序列上使用 enumerate() 函数时很容易调入陷阱。
    """
    separator_content()
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    for index, (x, y) in enumerate(data):
        print("{}:({},{})".format(index, x, y))

    # for index, x, y in enumerate(data):
    #     print("{}:({},{})".format(index, x, y))  ValueError: not enough values to unpack (expected 3, got 2)
