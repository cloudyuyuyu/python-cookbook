from util.separator import separator_content
from collections import Iterable

if __name__ == "__main__":
    """
    问题
        你想将一个多层嵌套的序列展开成一个单层列表

    解决方案
        可以写一个包含 yield from 语句的递归生成器来轻松解决这个问题
    """
    separator_content()

    def flatten(items,
                ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_types):
                yield from flatten(x)
            else:
                yield x


    items = [1, 2, [3, 4, [5, 6], 7], 8]
    for x in flatten(items=items):
        print(x)

    """
        在上面代码中， isinstance(x, Iterable) 检查某个元素是否是可迭代的。 
    如果是的话， yield from 就会返回所有子例程的值。最终返回结果就是一个没有嵌套的简单序列了。
    
        额外的参数 ignore_types 和检测语句 isinstance(x, ignore_types) 用来将字符串和字节排除在可迭代对象外，
    防止将它们再展开成单个的字符。 这样的话字符串数组就能最终返回我们所期望的结果了。
    """
    separator_content()
    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items=items):
        print(x)

    """
    语句 yield from 在你想在生成器中调用其他生成器作为子例程的时候非常有用。 
    
    如果你不使用它的话，那么就必须写额外的 for 循环了。
    """
    def flatten(items, ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_types):
                for i in flatten(x):
                    yield i
            else:
                yield x
