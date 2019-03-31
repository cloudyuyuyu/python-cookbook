from util.separator import separator_content

if __name__ == "__main__":
    """
    问题
        你想反方向迭代一个序列

    解决方案
        使用内置的 reversed() 函数
    """
    separator_content()
    a = [1, 2, 3, 4, 5]
    for x in reversed(a):
        print(x)

    """
    反向迭代仅仅当 对象的大小可预先确定 或者 对象实现了 __reversed__() 的特殊方法时才能生效。 
    
    如果两者都不符合，那你必须先将对象转换为一个列表才行。
    
    要注意的是如果可迭代对象元素很多的话，将其预先转换为一个列表要消耗大量的内存。
    """
    separator_content()
    with open("__5__Reverse iteration.py",
              encoding="utf-8") as file:
        for line in reversed(list(file)):
            print(line, end="")


    """
        很多程序员并不知道可以通过在自定义类上实现 __reversed__() 方法来实现反向迭代。
        
        定义一个反向迭代器可以使得代码非常的高效， 因为它不再需要将数据填充到一个列表中然后再去反向迭代这个列表。
    """
    separator_content()
    class CountDown:
        def __init__(self, start):
            self._start = start

        def __iter__(self):
            n = self._start
            while n > 0:
                yield n
                n = n - 1

        def __reversed__(self):
            n = 1
            while n <= self._start:
                yield n
                n = n + 1

    for num in reversed(CountDown(10)):
        print(num)

    for num in CountDown(10):
        print(num)