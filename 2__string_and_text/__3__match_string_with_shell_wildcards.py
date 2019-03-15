from util.separator import separator_content
from fnmatch import fnmatch, fnmatchcase

if __name__ == "__main__":
    """
    问题:
        你想使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去
        匹配文本字符串

    解决方案:
        fnmatch 模块提供了两个函数—— fnmatch() 和 fnmatchcase() ，可以用来
        实现这样的匹配。
        
        要匹配变长的字符，在正则表达式中，
        用 * 表示任意个字符（包括0个），
        用 + 表示至少一个字符，
        用 ? 表示 0 个或 1 个字符，
        用 {n} 表示 n 个字符，
        用 {n,m} 表示 n-m 个字符
        
        ^表示行的开头，^\d表示必须以数字开头。
        $表示行的结束，\d$表示必须以数字结束。
    """
    separator_content()
    print(fnmatch('foo.txt', '*.txt'))
    print(fnmatch('foo.txt', '?oo.txt'))
    print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

    file_names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print([name for name in file_names if fnmatch(name, "Dat*.csv")])

    """
    fnmatch() 函数使用底层操作系统的大小写敏感规则(不同的系统是不一样的)来匹配模式。
    
    如果你对这个区别很在意，可以使用 fnmatchcase() 来代替。它完全使用你的模式大小写匹配。
    
    这两个函数在处理非文件名的字符串时候它们也是很有用的
    
    fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。 
    如果在数据处理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案。
    """
    separator_content()
    print(fnmatch("foo.txt", "*.TXT"))
    print(fnmatchcase("foo.txt", "*.TXT"))

    separator_content()
    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]
    print([addr for addr in addresses if fnmatch(addr, "* ST")])
    print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] * CLARK *')])
