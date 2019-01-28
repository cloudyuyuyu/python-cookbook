from util.separator import separator_content

if __name__ == "__main__":
    """
    问题
        你需要将数字格式化后输出，并控制数字的位数、对齐、千位分隔符和其他的细节。

    解决方案
        格式化输出单个数字的时候，可以使用内置的 format() 函数，
    """
    separator_content()
    x = 1234.5678
    print(format(x, '0.2f'))

    print(format(x, '#>10.1f'))

    print(format(x, '#<10.1f'))

    print(format(x, "#^10.1f"))

    print(format(x, ','))

    print(format(x, '0,.1f'))

    """
    如果你想使用指数记法，将f改成e或者E(取决于指数输出的大小写形式)。
    """
    separator_content()
    print(format(x, "e"))

    print(format(x, '0.2e'))

    """
    数字格式化输出通常是比较简单的。上面演示的技术同时适用于浮点数和 decimal 模块中的 Decimal 数字对象。

    当指定数字的位数后，结果值会根据 round() 函数同样的规则进行四舍五入后返回
    """
    separator_content()
    print(format(x, '0.1f'))
    print(format(-x, '0.1f'))

    """
    包含千位符的格式化跟本地化没有关系。 如果你需要根据地区来显示千位符，你需要自己去调查下 locale 模块中的函数了。 
    
    你同样也可以使用字符串的 translate() 方法来交换千位符。
    """
    separator_content()
    swap_separators = {ord('.'): ',', ord(','): '.'}
    print(format(x, ',').translate(swap_separators))

    """
    在很多Python代码中会看到使用%来格式化数字的
    
    这种格式化方法也是可行的，不过比更加先进的 format() 要差一点。 
    
    比如，在使用%操作符格式化数字的时候，一些特性(添加千位符)并不能被支持。
    """
    separator_content()
    print('%0.2f' % x)
    print('%10.1f' % x)
    print('%-10.1f' % x)