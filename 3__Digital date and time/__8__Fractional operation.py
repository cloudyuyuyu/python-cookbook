from util.separator import separator_content
from fractions import Fraction

if __name__ == "__main__":
    """
    问题
        你进入时间机器，突然发现你正在做小学家庭作业，并涉及到分数计算问题。 
        
        或者你可能需要写代码去计算在你的木工工厂中的测量值。

    解决方案
        fractions 模块可以被用来执行包含分数的数学运算。
    """
    separator_content()
    a = Fraction(5, 4)
    b = Fraction(7, 16)

    print(a + b)
    print(a * b)

    """
        获得分子和分母
    """
    c = a * b
    print(c.numerator)
    print(c.denominator)

    print(c.limit_denominator(8))

    """
        小数和分数相互转换
    """
    print(float(c))

    x = 3.75
    print(Fraction(*x.as_integer_ratio()))

    """
        在大多数程序中一般不会出现分数的计算问题，但是有时候还是需要用到的。 
    
        比如，在一个允许接受分数形式的测试单位并以分数形式执行运算的程序中， 
    直接使用分数可以减少手动转换为小数或浮点数的工作。
    """




