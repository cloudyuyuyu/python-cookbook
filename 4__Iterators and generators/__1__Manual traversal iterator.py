from util.separator import separator_content

if __name__ == "__main__":
    """
    问题
        你想遍历一个可迭代对象中的所有元素，但是却不想使用for循环。

    解决方案
        为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异常。
    """
    separator_content()


    def manual_iter():
        with open('./__1__Manual traversal iterator.py',
                  encoding="utf-8") as f:
            try:
                while True:
                    line = next(f)
                    print(line, end='')
            except StopIteration:
                pass

    manual_iter()

    """
    通常来讲， StopIteration 用来指示迭代的结尾。
     
    然而，如果你手动使用上面演示的 next() 函数的话，你还可以通过返回一个指定值来标记结尾，比如 None 。 
    """
    separator_content()
    with open('./__1__Manual traversal iterator.py',
              encoding="utf-8") as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')


    """
    大多数情况下，我们会使用 for 循环语句用来遍历一个可迭代对象。 
    
    但是，偶尔也需要对迭代做更加精确的控制，这时候了解底层迭代机制就显得尤为重要了。

    下面的交互示例向我们演示了迭代期间所发生的基本细节：
    """
    items = [1, 2, 3]
    it = iter(items)

    print(next(it))
    print(next(it))
    print(next(it))
    # print(next(it))    StopIteration