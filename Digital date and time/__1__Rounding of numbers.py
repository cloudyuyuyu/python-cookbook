from util.separator import separator_content

if __name__ == "__main__":
    """
    问题
        你想对浮点数执行指定精度的舍入运算。

    解决方案
        对于简单的舍入运算，使用内置的 round(value, ndigits) 函数即可。
        
        当一个值刚好在两个边界的中间的时候， round 函数返回离它最近的偶数。 
        也就是说，对1.5或者2.5的舍入运算都会得到2。
    """
    separator_content()
    print(round(1.23, 0))

    print(round(1.27, 2))

    print(round(-1.27, 1))

    print(round(1.25361, 3))

    """
    传给 round() 函数的 ndigits 参数可以是 负数，这种情况下， 舍入运算会作用在十位、百位、千位等上面。
    """
    separator_content()
    a = 1627731
    print(round(a, -1))

    print(round(a, -2))

    print(round(a, -3))

    """
    不要将舍入和格式化输出搞混淆了。
     
    如果你的目的只是简单的输出一定宽度的数，你不需要使用 round() 函数。 
    
    而仅仅只需要在格式化的时候指定精度即可。
    """
    separator_content()
    x = 1.23456
    print(format(x, '0.2f'))

    print(format(x, '0.3f'))

    print('value is {:0.3f}'.format(x))

    """
    同样，不要试着去舍入浮点值来”修正”表面上看起来正确的问题
    
    对于大多数使用到浮点的程序，没有必要也不推荐这样做。 
    尽管在计算的时候会有一点点小的误差，但是这些小的误差是能被理解与容忍的。
    """
    separator_content()
    a = 2.1
    b = 4.2
    c = a + b
    print(c)

    print(round(c, 2))