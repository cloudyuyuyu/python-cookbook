from util.separator import separator_content

if __name__ == "__main__":
    """
    Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
    
    基本语法是通过 {} 和 : 来代替以前的 % 。

    format 函数可以接受不限个参数，位置可以不按顺序。
    """
    separator_content()

    # 不设置指定位置，按默认顺序
    print("{} {}".format("hello", "world"))

    # 设置指定位置
    print("{0} {1}".format("hello", "world"))

    # 设置指定位置
    print("{1} {0} {1}".format("hello", "world"))

    print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

    # 通过字典设置参数
    site = {"name": "菜鸟教程", "url": "www.runoob.com"}
    print("网站名：{name}, 地址 {url}".format(**site))

    # 通过列表索引设置参数
    my_list = ['菜鸟教程', 'www.runoob.com']
    print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

    """
    也可以向 str.format() 传入对象：
    """
    separator_content()
    class AssignValue(object):
        def __init__(self, value):
            self.value = value

    my_value = AssignValue(6)
    print('value 为: {0.value}'.format(my_value))  # "0" 是可选的


    """
    数字格式化
    
    下表展示了 str.format() 格式化数字的多种方法：
    
    数字	            格式	       输出   	    描述
    3.1415926	    {:.2f}	   3.14	        保留小数点后两位
    3.1415926	    {:+.2f}	   +3.14	    带符号保留小数点后两位
    -1	            {:+.2f}	   -1.00	    带符号保留小数点后两位
    2.71828	        {:.0f}	    3	        不带小数
    5	            {:0>2d}	    05	        数字补零 (填充左边, 宽度为2)
    5	            {:x<4d}	    5xxx	    数字补x (填充右边, 宽度为4)
    10	            {:x<4d}	    10xx	    数字补x (填充右边, 宽度为4)
    1000000 	    {:,}	  1,000,000	    以逗号分隔的数字格式
    0.25	        {:.2%}	    25.00%	    百分比格式
    1000000000	    {:.2e}	    1.00e+09	指数记法
    13	            {:10d}	        13	    右对齐 (默认, 宽度为10)
    13	            {:<10d}	   13	        左对齐 (宽度为10)
    13	            {:^10d}	      13	    中间对齐 (宽度为10)
        
    11      '{:b}'.format(11)    1011
            '{:d}'.format(11)    11
            '{:o}'.format(11)    13
            '{:x}'.format(11)    b
            '{:#x}'.format(11)   0xb
            '{:#X}'.format(11)   0XB
            
            
    ^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。

    + 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格

    b、d、o、x 分别是二进制、十进制、八进制、十六进制。
    """
    separator_content()
    print("{:.2f}".format(3.1415926))

