from util.separator import separator_content
from itertools import permutations, combinations, combinations_with_replacement

if __name__ == "__main__":
    """
    问题
        你想迭代遍历一个集合中元素的所有可能的排列或组合

    解决方案
    itertools 模块提供了三个函数来解决这类问题。 
    
    其中一个是 itertools.permutations() ， 它接受一个集合并产生一个元组序列，每个元组由集合中所有元素的一个可能排列组成。 
    """
    separator_content()
    items = ["a", "b", "c", "d"]
    for permutation in permutations(items):
        print(permutation)

    """
        如果你想得到指定长度的所有排列，你可以传递一个可选的长度参数。就像这样：
    """
    for permutation in permutations(items, r=2):
        print(permutation)

    """
        使用 itertools.combinations() 可得到输入集合中元素的所有的组合
    """
    separator_content()
    for combination in combinations(items, r=4):
        print(combination)

    for combination in combinations(items, r=3):
        print(combination)

    for combination in combinations(items, r=2):
        print(combination)

    """
        在计算组合的时候，一旦元素被选取就会从候选中剔除掉(比如如果元素’a’已经被选取了，那么接下来就不会再考虑它了)。 
    
        而函数 itertools.combinations_with_replacement() 允许同一个元素被选择多次。
    """
    separator_content()
    for _ in combinations_with_replacement(items, 4):
        print(_)
