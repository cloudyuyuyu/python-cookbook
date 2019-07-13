from util.separator import separator_content
import sys

if __name__ == "__main__":
    """
    问题
        你需要读写各种不同编码的文本数据，比如ASCII，UTF-8或UTF-16编码等。

    解决方案
        使用带有 rt 模式的 open() 函数读取文本文件。
    """
    separator_content()
    # Read the entire file as a single string
    source_file_name = sys.argv[0]
    print(source_file_name)
    with open(source_file_name,
              'rt',
              encoding="utf-8") as f:
        data = f.read()

    # Iterate over the lines of the file
    # with open(source_file_name,
    #           'rt',
    #           encoding="utf-8") as f:
    #     for line in f:
    #         print(line, end="")

    """
    类似的，为了写入一个文本文件，使用带有 wt 模式的 open() 函数， 如果之前文件内容存在则清除并覆盖掉。
    
    如果是在已存在文件中添加内容，使用模式为 at 的 open() 函数。
    
    Python支持非常多的文本编码。几个常见的编码是ascii, latin-1, utf-8和utf-16。 
    
    在web应用程序中通常都使用的是UTF-8。
    
    ascii对应从U+0000到U+007F范围内的7位字符。 
    
    latin-1是字节0-255到U+0000至U+00FF范围内Unicode字符的直接映射。
    当读取一个未知编码的文本时使用latin-1编码永远不会产生解码错误。 
    使用latin-1编码读取一个文件的时候也许不能产生完全正确的文本解码数据， 但是它也能从中提取出足够多的有用数据。
    同时，如果你之后将数据回写回去，原先的数据还是会保留的。
    """

    """
    另外一个问题是关于换行符的识别问题，在Unix和Windows中是不一样的(分别是 \n 和 \r\n )。 
    
    默认情况下，Python会以统一模式处理换行符。 
    
    这种模式下，在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个 \n 字符。 
    
    类似的，在输出时会将换行符 \n 转换为系统默认的换行符。
    
    为了说明两者之间的差异，下面我在Unix机器上面读取一个Windows上面的文本文件，里面的内容是 hello world!\r\n ：
    """
    separator_content()
    with open("test.txt",
              'rt',
              encoding=sys.getdefaultencoding(),
              newline='') as f:
        for line in f:
            print(line)

    with open("test.txt",
              'rt',
              encoding=sys.getdefaultencoding()) as f:
        for line in f:
            print(line)

    """
    最后一个问题就是文本文件中可能出现的编码错误。 
    
    但你读取或者写入一个文本文件时，你可能会遇到一个编码或者解码错误。
    
    如果出现这个错误，通常表示你读取文本时指定的编码不正确。
     
    你最好仔细阅读说明并确认你的文件编码是正确的(比如使用UTF-8而不是Latin-1编码或其他)。 
    
    如果编码错误还是存在的话，你可以给 open() 函数传递一个可选的 errors 参数来处理这些错误。 
    """
    separator_content()
    f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
    g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')