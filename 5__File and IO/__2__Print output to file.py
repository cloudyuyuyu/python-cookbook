from util.separator import separator_content

if __name__ == "__main__":
    """
    问题
        你想将 print() 函数的输出重定向到一个文件中去。

    解决方案
        在 print() 函数中指定 file 关键字参数，像下面这样：
    """
    separator_content()

    with open('test.txt', 'w') as f:
        print('Hello World!', file=f)

    with open("test.txt", "r") as f:
        for line in f:
            print(line)

    """
    关于输出重定向到文件中就这些了。
    
    但是有一点要注意的就是文件必须是以文本模式打开。 
    
    如果文件是二进制模式的话，打印就会出错。
    """
