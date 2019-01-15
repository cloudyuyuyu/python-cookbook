from util.separator import separator_content
import re
from calendar import month_abbr

if __name__ == "__main__":
    """
    问题:
        你想在字符串中搜索和匹配指定的文本模式

    解决方案:
        1、对于简单的字面模式，直接使用 str.replace() 方法即可
        
        2、对于复杂的模式，请使用 re 模块中的 sub() 函数。
    """
    separator_content()
    text = 'yeah, but no, but yeah, but no, but yeah'
    text.replace("yeah", "yep")
    print(text)

    """
    sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。
    反斜杠数字比如 \3 指向前面模式的捕获组号。
    
    
    re.sub(pattern, repl, string, count=0, flags=0)
    patter.sub(repl, string, count=0)

    pattern：表示正则表达式中的模式字符串；
    repl：被替换的字符串（既可以是字符串，也可以是函数）；
    string：要被处理的，要被替换的字符串；
    count：匹配的次数, 默认是全部替换
    flags：具体用处不详
    """
    separator_content()
    date_pat = re.compile(r'(\d+)/(\d+)/(\d+)')
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    text_changed = date_pat.sub(r'\3-\1-\2', text)
    print(text)
    print(text_changed)


    def change_date(m):
        month_name = month_abbr[int(m.group(1))]
        return "{} {} {}".format(m.group(2), month_name, m.group(3))

    text_changed = date_pat.sub(change_date, text)
    print(text)
    print(text_changed)

    separator_content()
    match_ = date_pat.findall(text)




