from util.separator import separator_content

if __name__ == "__main__":
    """
    问题
        你写的最新的网络认证方案代码遇到了一个难题，并且你唯一的解决办法就是使用复数空间。 
        再或者是你仅仅需要使用复数来执行一些计算操作。

    解决方案
        复数可以用使用函数 complex(real, imag) 或者是带有后缀j的浮点数来指定。
    """
    separator_content()
    a = complex(2, 4)
    b = 3 - 5j

    print(a)
    print(b)

    """
        对应的实部、虚部和共轭复数可以很容易的获取。就像下面这样：
    """
    print(a.real)
    print(a.imag)
    print(a.conjugate())

    """
    另外，所有常见的数学运算都可以工作：
    """
    separator_content()
    print(a + b)
    print(a - b)
    print(a / b)
    print(a * b)
    print(abs(a))

    """
    如果要执行其他的复数函数比如正弦、余弦或平方根，使用 cmath 模块：
    """
    separator_content()
    import cmath

    print(cmath.sin(a))
    print(cmath.cos(a))
    print(cmath.exp(a))

    """
    Python中大部分与数学相关的模块都能处理复数。 
    
    比如如果你使用 numpy ，可以很容易的构造一个复数数组并在这个数组上执行各种操作：
    """
    separator_content()
    import numpy as np
    a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
    print(a)
    print(a + 2)
    print(np.sin(a))

    """
    Python的标准数学函数确实情况下并不能产生复数值，因此你的代码中不可能会出现复数返回值。
    """
    separator_content()
    import math
    # print(math.sqrt(-1))

    print(cmath.sqrt(-1))



