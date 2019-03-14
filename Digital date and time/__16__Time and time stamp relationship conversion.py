from util.separator import separator_content
import time

if __name__ == "__main__":
    """
    问题
        获得当前时间戳，并将时间戳转换为时间
        
        或者将时间转换为时间戳

    解决方案
        time.time       : 当前时间的 时间戳，返回float数据，自1970年1月1日开始按照秒计算的偏移量，可以进行差值计算得到秒差。
        
        time.strptime   : 将 格式字符串 转化成 时间元组
        
        time.strftime   : 通过函数将 时间元组 转成 格式字符串，
        
        time.mktime     : 将一个 时间元组 转化为 时间戳 
        
        time.localtime  : 将 时间戳 转为 时间元组
        
        时间元组        : time.struct_time(tm_year=2019, tm_mon=3, tm_mday=14, tm_hour=23, tm_min=23, tm_sec=7, 
                                           tm_wday=3, tm_yday=73, tm_isdst=0)
    """

    """
        时间戳 转换为 格式化字符串 的步骤
    """
    separator_content()
    current_timestamp = time.time()  # python 里面是秒，java 里面是毫秒
    print(current_timestamp)

    current_struct_time = time.localtime(current_timestamp)
    print(current_struct_time)

    current_format_time = time.strftime("%Y-%m-%d  %H:%M:%S", current_struct_time)
    print(current_format_time)

    """
        格式化字符串 转换为 时间戳 的步骤   
    """
    separator_content()
    current_format_time = time.strftime("%Y-%m-%d  %H:%M:%S")
    print(current_format_time)

    current_struct_time = time.strptime(current_format_time,
                                        "%Y-%m-%d  %H:%M:%S")
    print(current_struct_time)

    current_timestamp = time.mktime(current_struct_time)
    print(current_timestamp)
