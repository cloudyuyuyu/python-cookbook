from util.separator import separator_content
import unicodedata
import sys

if __name__ == "__main__":
    """
    问题
        一些无聊的幼稚黑客在你的网站页面表单中输入文本”pýtĥöñ”，然后你想将这些字符清理掉。

    解决方案
        文本清理问题会涉及到包括文本解析与数据处理等一系列问题。 
        
        在非常简单的情形下，你可能会选择使用字符串函数(比如 str.upper() 和 str.lower() )将文本转为标准格式。
         
        使用 str.replace() 或者 re.sub() 的简单替换操作能删除或者改变指定的字符序列。 
        
        你同样还可以使用 2.9 小节的 unicodedata.normalize() 函数将 unicode 文本标准化。
        
        然后，有时候你可能还想在清理操作上更进一步。
        比如，你可能想消除整个区间上的字符或者去除变音符。 
        为了这样做，你可以使用经常会被忽视的 str.translate() 方法。
    """
    separator_content()
    s = 'pýtĥöñ\fis\tawesome\r\n'
    print(s)

    remap = {ord('\t'): ' ',
             ord('\f'): ' ',
             ord('\r'): None}
    a = s.translate(remap)
    print(a)

    cmb_chrs = \
        dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    b = unicodedata.normalize("NFD", a)
    print(b)

    print(b.translate(cmb_chrs))

    print(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

    """
    上面例子中，通过使用 dict.fromkeys() 方法构造一个字典，每个Unicode和音符作为键，对应的值全部为 None 。

    然后使用 unicodedata.normalize() 将原始输入标准化为分解形式字符。 
    
    然后再调用 translate 函数删除所有重音符。 
    
    同样的技术也可以被用来删除其他类型的字符(比如控制字符等)。
    
    这里构造一个将所有 Unicode 数字字符映射到对应的ASCII字符上的表格：
    """
    separator_content()
    digit_map = {c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if
                 unicodedata.category(chr(c)) == 'Nd'}
    print(len(digit_map))
    x = '\u0661\u0662\u0663'
    print(x)
    print(x.translate(digit_map))

    """
    另一种清理文本的技术涉及到I/O解码与编码函数。
    
    这里的思路是先对文本做一些初步的清理，然后再结合 encode() 或者 decode() 操作来清除或修改它。
    """
    separator_content()
    print(unicodedata.normalize('NFD', a))
    print(b.encode('ascii', 'ignore').decode('ascii'))

    """
    文本字符清理一个最主要的问题应该是运行的性能。
    
    对于简单的替换操作，str.replace() 方法通常是最快的，甚至在你需要多次调用的时候。
    
    
    """
    separator_content()


    def clean_spaces(s):
        """
        如果你去测试的话，你就会发现这种方式会比使用 translate() 或者正则表达式要快很多。
        :param s:
        :return:
        """
        s = s.replace('\r', '')
        s = s.replace('\t', ' ')
        s = s.replace('\f', ' ')
        return s

    """
    另一方面，如果你需要执行任何复杂字符对字符的重新映射或者删除操作的话， tanslate() 方法会非常的快。
    """
