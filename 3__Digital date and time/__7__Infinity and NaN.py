from util.separator import separator_content
import math

if __name__ == "__main__":
    """
    问题
        你想创建或测试正无穷、负无穷或NaN(非数字)的浮点数。

    解决方案
        Python并没有特殊的语法来表示这些特殊的浮点值，但是可以使用 float() 来创建它们。
    """
    separator_content()

    a = float("inf")
    b = float("-inf")
    c = float("nan")

    print(a)
    print(b)
    print(c)

    """
        为了测试这些值的存在，使用 math.isinf() 和 math.isnan() 函数。比如：
    """
    separator_content()
    print(math.isinf(a))
    print(math.isfinite(b))
    print(math.isnan(c))

    """
        有一些地方需要你特别注意，特别是跟比较和操作符相关的时候。

        无穷大数在执行数学计算的时候会传播，比如：
    """
    separator_content()
    a = float("inf")
    print(a + 45)
    print(a * 10)
    print(10 / a)

    """
        但是有些操作时未定义的并会返回一个NaN结果。比如：
    """
    print(a / a)
    print(a + float("-inf"))

    """
        NaN值会在所有操作中传播，而不会产生异常。比如：
    """
    separator_content()
    c = float("nan")
    print(c + 23)
    print(c / 2)
    print(c * 2)
    print(math.sqrt(c))

    """
        NaN值的一个特别的地方时它们之间的比较操作总是返回False。
        
        由于这个原因，测试一个NaN值得唯一安全的方法就是使用 math.isnan() 
    """
    separator_content()
    d = float("nan")

    print(c == d)
    print(c is d)
