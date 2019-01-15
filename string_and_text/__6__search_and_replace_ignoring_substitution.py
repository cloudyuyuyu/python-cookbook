from util.separator import separator_content
import re

if __name__ == "__main__":
    """
    问题:
        你需要以忽略大小写的方式搜索与替换文本字符串

    解决方案:
        为了在文本操作时忽略大小写，你需要在使用 re 模块的时候给这些操作提供 re.IGNORECASE 标志参数。
    """
    separator_content()
    text = 'UPPER PYTHON, lower python, Mixed Python'
    match_list = re.findall('python', text, flags=re.IGNORECASE)
    print(match_list)

    replace_list = re.sub("python", "snack", text, flags=re.IGNORECASE)
    print(replace_list)

    """
    替换字符串并不会自动跟被匹配字符串的大小写保持一致
    
    为了修保持大小写，可能需要一个辅助函数
    
    match_case('snake') 返回了一个回调函数(参数必须是 match 对象)
    """
    separator_content()


    def match_case(word):
        def replace(m):
            text = m.group()
            if text.isupper():
                return word.upper()
            elif text.islower():
                return word.lower()
            elif text[0].isupper():
                return word.capitalize()
            else:
                return word

        return replace

    keep_sub_list = re.sub('python', match_case('snake'), text, flags=re.IGNORECASE)
    print(keep_sub_list)

