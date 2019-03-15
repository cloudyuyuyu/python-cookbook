from util.separator import separator_content

if __name__ == "__main__":
    """
    问题
        你想通过某种对齐方式来格式化字符串

    解决方案
        对于基本的字符串对齐操作，可以使用字符串的 ljust() , rjust() 和 center() 方法
    """
    separator_content()
    text = 'Hello World'
    print(text.ljust(20))
    print(text.rjust(20))
    print(text.center(20))

    """
    所有这些方法都能接受一个可选的填充字符。
    """
    separator_content()
    print(text.ljust(20, "-"))
    print(text.rjust(20, "+"))
    print(text.center(20, "="))

    """
    函数 format() 同样可以用来很容易的对齐字符串。 
    
    你要做的就是使用 <,> 或者 ^ 字符后面紧跟一个指定的宽度。
    """
    separator_content()
    print(format(text, '>20'))
    print(format(text, '<20'))
    print(format(text, '^20'))

    print(format(text, '=>20'))
    print(format(text, '*^20'))
    print(format(text, '*^20'))

    """
    format() 函数的一个好处是它不仅适用于字符串。
    
    它可以用来格式化任何值，使得它非常的通用。 比如，你可以用它来格式化数字：
    """
    separator_content()
    x = 1.2345
    print(format(x, '>10'))
    print(format(x, '^10.2f'))