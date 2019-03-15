from util.separator import separator_content

if __name__ == "__main__":
    """
    问题:
        你需要通过指定的文本模式去检查字符串的开头或者结尾，
        比如文件名后缀，URL Scheme等等。

    解决方案:
        检查字符串开头或结尾的一个简单方法是使用 str.startswith() 
        或者是 str.endswith() 方法
    """
    separator_content()
    filename = 'spam.txt'
    print(filename.endswith(".txt"))

    url = 'http://www.python.org'
    print(url.startswith("http:"))

    """
    如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去， 
    然后传给 startswith() 或者 endswith() 方法：
    """
    separator_content()
    filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
    print([name for name in filenames if name.endswith((".c", ".h"))])
    # endswith first arg must be str or a tuple of str, not list
    # print([name for name in filenames if name.endswith([".c", ".h"])])
    print(any(name.endswith(".py") for name in filenames))

    