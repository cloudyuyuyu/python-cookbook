from util.separator import separator_content
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta

if __name__ == "__main__":
    """
    问题
         你需要执行简单的时间转换，比如天到秒，小时到分钟等的转换。

     解决方案
         为了执行不同时间单位的转换和计算，请使用 datetime 模块。 

         比如，为了表示一个时间段，可以创建一个 timedelta 实例，就像下面这样：
    """
    separator_content()
    a = timedelta(days=2,
                  hours=6)
    b = timedelta(hours=4.5)

    c = a + b
    print(c.days)
    print(c.seconds)
    print(c.seconds / 60 / 60)
    print(c.total_seconds() / 60 / 60)

    """
        如果你想表示指定的日期和时间，先创建一个 datetime 实例然后使用标准的数学运算来操作它们。
    """
    separator_content()
    today = datetime(2019, 3, 13)
    print("today is\t", today)
    print("10 days after today is\t", today + timedelta(days=10))

    birthday_of_this_year = datetime(2019, 8, 19)
    print((birthday_of_this_year - today).days)

    now = datetime.today()
    print(now)
    print(now + timedelta(hours=2))

    """
        在计算的时候，需要注意的是 datetime 会自动处理闰年。
    """
    separator_content()
    a = datetime(2016, 3, 1)
    b = datetime(2016, 2, 28)
    print(a - b)

    a = datetime(2019, 3, 1)
    b = datetime(2019, 2, 28)
    print(a - b)

    """
        对大多数基本的日期和时间处理问题， datetime 模块已经足够了。 
    如果你需要执行更加复杂的日期操作，比如处理时区，模糊时间范围，节假日计算等等， 可以考虑使用 dateutil模块

        许多类似的时间计算可以使用 dateutil.relativedelta() 函数代替。 
        但是，有一点需要注意的就是，它会在处理月份(还有它们的天数差距)的时候填充间隙。
    """
    separator_content()
    # print(a + timedelta(months=1)) TypeError: 'months' is an invalid keyword argument for this function

    print(a + relativedelta(months=+1))
    print(a + relativedelta(months=+5))

    b = datetime(2012, 12, 21)

    print(a - b)

    d = relativedelta(a, b)
    print(d)
    print(d.months)
    print(d.days)
    print()