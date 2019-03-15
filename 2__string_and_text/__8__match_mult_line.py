from util.separator import separator_content
import re

if __name__ == "__main__":
    """
    问题
        你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配。

    解决方案
        这个问题很典型的出现在当你用点(.)去匹配任意字符的时候，忘记了点(.)不能匹配换行符的事实。 
    """

    separator_content()
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a */comment */'
    text2 = '/* this is a \n multi_line comment */'
    print(comment.findall(text1))
    print(comment.findall(text2))

    """
    为了修正这个问题，你可以修改模式字符串，增加对换行的支持
    
    在这个模式中， (?:.|\n) 指定了一个非捕获组
    (也就是它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组)。
    """
    separator_content()
    comment = re.compile(r'/\*((?:.|\n)*?)\*/')
    print(comment.findall(text2))

    """
    re.compile() 函数接受一个标志参数叫 re.DOTALL ，在这里非常有用。 
    
    它可以让正则表达式中的点(.)匹配包括换行符在内的任意字符。
    """
    separator_content()
    comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
    print(comment.findall(text2))

    """
    对于简单的情况使用 re.DOTALL 标记参数工作的很好，但是如果模式非常复杂或者是为了构造
    字符串令牌而将多个模式合并起来，这时候使用这个标记参数就可能出现一些问题。 
    
    如果让你选择的话，最好还是定义自己的正则表达式模式，这样它可以在不需要额外的标记参数下也能工作的很好。
    """

