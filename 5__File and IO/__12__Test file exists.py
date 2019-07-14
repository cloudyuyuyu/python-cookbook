from util.separator import separator_content
import os
import time

if __name__ == "__main__":
    """
    问题
        你想测试一个文件或目录是否存在。

    解决方案
        使用 os.path 模块来测试一个文件或目录是否存在。
    """
    separator_content()
    print(os.path.exists('/etc/passwd'))
    print(os.path.exists('/tmp/spam'))

    """
        你还能进一步测试这个文件时什么类型的。 
        
        在下面这些测试中，如果测试的文件不存在的时候，结果都会返回False：
    """
    separator_content()
    # Is a regular file
    print(os.path.isfile('/etc/passwd'))

    # Is a directory
    print(os.path.isdir('/etc/passwd'))

    # Is a symbolic link
    print(os.path.islink('/usr/local/bin/python3'))

    # Get the file linked to
    print(os.path.realpath('data'))

    """
        如果你还想获取元数据(比如文件大小或者是修改日期)，也可以使用 os.path 模块来解决：
    """
    separator_content()
    print(os.path.getsize('data'))
    print(os.path.getmtime('data'))
    print(time.ctime(os.path.getmtime('data')))

    """
        使用 os.path 来进行文件测试是很简单的。 
        
        在写这些脚本时，可能唯一需要注意的就是你需要考虑文件权限的问题，特别是在获取元数据时候。
    """
    separator_content()