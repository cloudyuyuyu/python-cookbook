from util.separator import separator_content
import os

if __name__ == "__main__":
    """
    问题
        你需要使用路径名来获取文件名，目录名，绝对路径等等。

    解决方案
        使用 os.path 模块中的函数来操作路径名。 
    """
    separator_content()
    path = 'C:\\Users\\qy201\\Desktop\\study\\python\\python-cookbook\\5__File and IO\\data'

    # Get the last component of the path
    print(os.path.basename(path))

    # Get the directory name
    print(os.path.dirname(path))

    # Join path components together
    print(os.path.join('tmp', 'data', os.path.basename(path)))

    # Expand the user's home directory
    print(os.path.expanduser("data"))

    # Split the file extension
    print(os.path.splitext(path))

    """
        对于任何的文件名的操作，你都应该使用 os.path 模块，而不是使用标准字符串操作来构造自己的代码。 
        
        特别是为了可移植性考虑的时候更应如此， 因为 os.path 模块知道Unix和Windows系统之间的差异并且能够可靠地处理
        类似 Data/data.csv 和 Data\data.csv 这样的文件名。
         
        其次，你真的不应该浪费时间去重复造轮子。通常最好是直接使用已经为你准备好的功能。
    """