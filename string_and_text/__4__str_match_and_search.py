from util.separator import separator_content
import re

if __name__ == "__main__":
    """
    问题
        你想匹配或者搜索特定模式的文本

    解决方案
        如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串方法就行， 
        比如 str.find() , str.endswith() , str.startswith() 或者类似的方法：
    """
    separator_content()
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text == "yeah")
    print(text.startswith("yeah"))
    print(text.endswith('no'))
    print(text.find("no"))

    """
    对于复杂的匹配需要使用正则表达式和 re 模块。
    """
    separator_content()
    date_num = '11/27/2012'
    date_str = 'Nov 27, 2012'
    if re.match(r'\d+/\d+/\d+', date_num):
        print("yes")
    else:
        print("no")

    """
    如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象。
    """


    def match_or_not(input):
        date_pat = re.compile(r'\d+/\d+/\d+')
        if date_pat.match(input):
            print("match")
        else:
            print("do not match")


    separator_content()
    match_or_not(date_num)
    match_or_not(date_str)

    """
    match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置， 
    使用 findall() 方法去代替。
    """
    separator_content()
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    date_pat = re.compile(r'\d+/\d+/\d+')
    print(date_pat.findall(text))

    """
    在定义正则式的时候，通常会利用括号去捕获分组
    
    捕获分组可以使得后面的处理更加简单，因为可以分别将每个组的内容提取出来。
    """
    separator_content()
    date_pat_group = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = date_pat_group.match("11/27/2012")
    print(m.groups())
    for month, day, year in date_pat_group.findall(text):
        print("{}年, {}月, {}日".format(year, month, day))

    """
    findall() 方法会搜索文本并以列表形式返回所有的匹配。
     
    如果你想以迭代方式返回匹配，可以使用 finditer() 方法来代替
    """
    separator_content()
    for m in date_pat_group.finditer(text):
        print(m.groups())