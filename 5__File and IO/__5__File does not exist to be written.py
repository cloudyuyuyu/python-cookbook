from util.separator import separator_content

if __name__ == "__main__":
    """
    问题
        你想向一个文件中写入数据，但是前提必须是这个文件在文件系统上不存在。 
        
        也就是不允许覆盖已存在的文件内容。

    解决方案
        可以在 open() 函数中使用 x 模式来代替 w 模式的方法来解决这个问题。比如：
    """
    separator_content()
    with open("test.txt",
              "xt") as f:
        f.write("Hello\t")

    """
        如果文件是二进制的，使用 xb 来代替 xt
        
        要注意的是 x 模式是一个 Python3 对 open() 函数特有的扩展。
         
        在 Python 的旧版本或者是 Python 实现的底层 C 函数库中都是没有这个模式的
    """
