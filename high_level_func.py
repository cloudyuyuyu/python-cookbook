def lazy_sum(args=[]):
    """
    当我们调用 lazy_sum() 时，返回的并不是求和结果，而是求和函数
    :param args:
    :return:
    """

    def _sum():
        result = 0
        print(id(args))
        for _ in args:
            result = result + _
        return result

    return _sum


def count():
    """
    返回函数不要引用任何循环变量，或者后续会发生变化的变量
    :return:
    """
    fs = []
    for i in range(1, 4):
        def func():
            print(id(i))
            return i * i

        fs.append(func)
    return fs


def test_whether_the_same_id(_input=[]):
    print(id(_input))


if __name__ == '__main__':
    parse_list = [1, 2, 3, 4, 5]
    print(id(parse_list))
    """
    当 lazy_sum 返回函数sum时，相关参数和变量都保存在返回的函数中,
    这种称为“闭包（Closure）”的程序结构拥有极大的威力。
    
    f1()和f2()的调用结果互不影响。
    """
    func1 = lazy_sum(parse_list)
    func2 = lazy_sum(parse_list)
    print(func1 == func2)  # return false

    parse_list.append(6)
    print(func2())

    # result = count()
    # print(result[0]())
    # print(result[1]())
    # print(result[2]())
    print(*parse_list)

    print(test_whether_the_same_id(parse_list))
