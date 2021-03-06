from util.separator import separator_content
import re
import os

if __name__ == "__main__":
    """
    问题
        你想在字节字符串上执行普通的文本操作(比如移除，搜索和替换)。

    解决方案
        字节字符串同样也支持大部分和文本字符串一样的内置操作。
    """
    separator_content()
    data = b'Hello World'
    print(data)

    print(data[0:5])

    print(data.startswith(b"Hello"))

    """
    这些操作同样也适用于字节数组
    """

    print(data.split(b" "))

    print(data.replace(b'Hello', b'Hello Cruel'))
    separator_content()
    data = bytearray(b'Hello World')

    print(data)

    print(data[0:5])

    print(data.startswith(b"Hello"))

    print(data.split(b" "))

    print(data.replace(b'Hello', b'Hello Cruel'))

    """
    你可以使用正则表达式匹配字节字符串，但是正则表达式本身必须也是字节串
    """
    separator_content()
    data = b'FOO:BAR,SPAM'
    print(re.split(b'[:,]', data))

    """
    大多数情况下，在文本字符串上的操作均可用于字节字符串。 
    
    然而，这里也有一些需要注意的不同点。首先，字节字符串的索引操作返回整数而不是单独字符。
    """
    separator_content()

    a = 'Hello World'  # Text string
    print(a[0])

    b = b'Hello World'  # Text string
    print(b[0])

    """
    字节字符串不会提供一个美观的字符串表示，也不能很好的打印出来，除非它们先被解码为一个文本字符串。
    """
    separator_content()
    s = b'Hello World'
    print(s)
    print(s.decode("ascii"))

    """
    类似的，也不存在任何适用于字节字符串的格式化操作
    
    如果你想格式化字节字符串，你得先使用标准的文本字符串，然后将其编码为字节字符串。
    """
    separator_content()

    print(b'%10s %10d %10.2f' % (b'ACME', 100, 490.1))


    print('{:>10s} {:^10d} {:<10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

    """
    最后需要注意的是，使用字节字符串可能会改变一些操作的语义，特别是那些跟文件系统有关的操作。
    
    比如，如果你使用一个编码为字节的文件名，而不是一个普通的文本字符串，会禁用文件名的编码/解码。比如：
    """
    separator_content()
    with open('jalape\xf1o.txt', 'w') as f:
        f.write('spicy')
    print(os.listdir('.')) # Text string (names are decoded))

    print(os.listdir(b'.'))

    """
    注意例子中的最后部分给目录名传递一个字节字符串是怎样导致结果中文件名以未解码字节返回的。 
    在目录中的文件名包含原始的UTF-8编码。 

    最后提一点，一些程序员为了提升程序执行的速度会倾向于使用字节字符串而不是文本字符串。 
    尽管操作字节字符串确实会比文本更加高效(因为处理文本固有的Unicode相关开销)。 
    
    这样做通常会导致非常杂乱的代码。你会经常发现字节字符串并不能和Python的其他部分工作的很好， 
    并且你还得手动处理所有的编码/解码操作。 
    
    坦白讲，如果你在处理文本的话，就直接在程序中使用普通的文本字符串而不是字节字符串。
    """


