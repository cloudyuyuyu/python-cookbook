from util.separator import separator_content
import textwrap
import os

if __name__ == "__main__":
    """
    问题
        你有一些长字符串，想以指定的列宽将它们重新格式化。

    解决方案
        使用 textwrap 模块来格式化字符串的输出。
    """
    separator_content()
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."
    print(s)

    separator_content()
    print(textwrap.fill(s, 70))

    separator_content()
    print(textwrap.fill(s, 40))

    separator_content()
    print(textwrap.fill(s, 40, initial_indent='    '))

    separator_content()
    print(textwrap.fill(s, 40, initial_indent='    ', subsequent_indent=' '))

    """
    textwrap 模块对于字符串打印是非常有用的，特别是当你希望输出自动匹配终端大小的时候。
     
    你可以使用 os.get_terminal_size() 方法来获取终端的大小尺寸。
    """
    separator_content()
    print(os.get_terminal_size().columns)