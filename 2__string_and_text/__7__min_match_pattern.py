from util.separator import separator_content
import re

if __name__ == "__main__":
    """
    问题
        你正在试着用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹配。
        而你想修改它变成查找最短的可能匹配。
        
         这个问题一般出现在需要匹配一对分隔符之间的文本的时候(比如引号包含的字符串)。

    解决方案
       
    """
    separator_content()
    str_pat = re.compile(r'"(.*)"')
    text1 = 'Computer says "no."'
    print(str_pat.findall(text1))

    text2 = 'Computer says "no." Phone says "yes."'
    print(str_pat.findall(text2))

    """
    模式 r'\"(.*)\"' 的意图是匹配被双引号包含的文本。 
    
    但是在正则表达式中 * 操作符是贪婪的，因此匹配操作会查找最长的可能匹配。
    
    可以在模式中的 * 操作符后面加上 ? 修饰符, 这样就使得匹配变成非贪婪模式，
    从而得到最短的匹配，也就是我们想要的结果。
    """
    separator_content()
    str_pat = re.compile(r'"(.*?)"')
    print(str_pat.findall(text2))

    """
    在一个模式字符串中，点(.)匹配除了换行外的任何字符。 
    
    然而，如果你将点(.)号放在开始与结束符(比如引号)之间的时候，那么匹配操作会查找符合模式的最长可能匹配。 
    
    这样通常会导致很多中间的被开始与结束符包含的文本被忽略掉，并最终被包含在匹配结果字符串中返回。 
    
    通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配。
    """




