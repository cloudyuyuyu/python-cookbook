from util.separator import separator_content
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

if __name__ == "__main__":
    """
    问题
        你需要查找星期中某一天最后出现的日期，比如星期五。

    解决方案
        Python的 datetime 模块中有工具函数和类可以帮助你执行这样的计算。
    """
    separator_content()

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']


    def get_previous_by_day(day_name,
                            start_date=None):
        """
        获得上一个星期几是几号
        :param day_name:
        :param start_date:
        :return:
        """
        if start_date is None:
            start_date = datetime.today()
        day_num = start_date.weekday()
        day_num_target = weekdays.index(day_name)
        days_ago = (7 + day_num - day_num_target) % 7

        if days_ago == 0:
            days_ago = 7

        return start_date - timedelta(days=days_ago)


    print(datetime.today())
    print(get_previous_by_day(weekdays[0]))
    print(get_previous_by_day(weekdays[2]))
    print(get_previous_by_day(weekdays[3]))
    print(get_previous_by_day(weekdays[4]))

    print(get_previous_by_day(day_name=weekdays[0],
                              start_date=datetime(2018, 8, 19)))

    print(datetime(2019, 3, 14).weekday())

    """
        上面的算法原理是这样的：先将开始日期和目标日期映射到星期数组的位置上(星期一索引为0)， 
    然后通过模运算计算出目标日期要经过多少天才能到达开始日期。然后用开始日期减去那个时间差即得到结果日期。

        如果你要像这样执行大量的日期计算的话，你最好安装第三方包 python-dateutil 来代替。
    """
    separator_content()
    now = datetime.now()

    print(now)
    print(now + relativedelta(weekday=FR(1)))
    print(now + relativedelta(weekday=FR(2)))

    print(now + relativedelta(weekday=FR(-1)))
    print(now + relativedelta(weekday=FR(-2)))
