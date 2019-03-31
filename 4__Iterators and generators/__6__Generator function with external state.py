from util.separator import separator_content
from collections import deque

if __name__ == "__main__":
    """
    问题
        你想定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值。

    解决方案
        如果你想让你的生成器暴露外部状态给用户， 别忘了你可以简单的将它实现为一个类，
        然后把生成器函数放到 __iter__() 方法中去。
    """
    separator_content()

    class LineHistory:
        def __init__(self, lines, history_len=3):
            self._lines = lines
            self._history = deque(maxlen=history_len)

        def __iter__(self):
            for index, _line in enumerate(self._lines, 1):
                self._history.append((index, _line))
                yield _line

        def clear(self):
            self._history.clear()

    with open("__5__Reverse iteration.py",
              encoding="utf-8") as file:
        line_history = LineHistory(file,
                                   history_len=5)
        for line in line_history:
            if "def" in line:
                for index, _ in line_history._history:
                    print("{}:{}".format(index, _),
                          end="")

    """
    关于生成器，很容易掉进函数无所不能的陷阱。 
    
    如果生成器函数需要跟你的程序其他部分打交道的话(比如暴露属性值，允许通过方法调用来控制等等)， 可能会导致你的代码异常的复杂。
    
    如果是这种情况的话，可以考虑使用上面介绍的定义类的方式。 在 __iter__() 方法中定义你的生成器不会改变你任何的算法逻辑。
    
    由于它是类的一部分，所以允许你定义各种属性和方法来供用户使用。

    一个需要注意的小地方是，如果你在迭代操作时不使用 for 循环语句，那么你得先调用 iter() 函数。
    """
    separator_content()
    with open("__5__Reverse iteration.py",
              encoding="utf-8") as file:
        line_history = LineHistory(file,
                                   history_len=3)

        # print(next(line_history))    TypeError: 'LineHistory' object is not an iterator
        iterable_line_history = iter(line_history)
        print(next(iterable_line_history), end="")
        print(next(iterable_line_history), end="")
        print(next(iterable_line_history), end="")



