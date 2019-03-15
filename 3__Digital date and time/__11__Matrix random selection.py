from util.separator import separator_content
import random

if __name__ == "__main__":
    """
    问题
        你想从一个序列中随机抽取若干元素，或者想生成几个随机数。

    解决方案
        random 模块有大量的函数用来产生随机数和随机选择元素。 

        比如，要想从一个序列中随机的抽取一个元素，可以使用 random.choice() ：
    """
    values = [1, 2, 3, 4, 5, 6]

    for num in range(10):
        print(random.choice(values))

    separator_content()
    for num in range(10):
        print(random.choices(values,
                             k=2))

    """
        为了提取出N个不同元素的样本用来做进一步的操作，可以使用 random.sample() ：
    """
    separator_content()
    for num in range(10):
        print(random.sample(values, 3))

    """
        如果你仅仅只是想打乱序列中元素的顺序，可以使用 random.shuffle() ：
    """
    separator_content()
    random.shuffle(values)
    print(values)

    random.shuffle(values)
    print(values)

    """
        生成随机整数，请使用 random.randint() ：
    """
    separator_content()
    for num in range(10):
        print(random.randint(0, 100))

    """
        为了生成0到1范围内均匀分布的浮点数，使用 random.random() ：
    """
    separator_content()
    for num in range(10):
        print(random.random())

    """
        为了生成均值为0，方差为1 的高斯分布的浮点数，使用 random.gauss() ：
    """
    separator_content()
    for num in range(10):
        print(random.gauss(0, 1))

    """
    random 模块使用 Mersenne Twister 算法来计算生成随机数。
    
    这是一个确定性算法， 但是你可以通过 random.seed() 函数修改初始化种子。
    """
    separator_content()
    random.seed()  # Seed based on system time or os.urandom()
    random.seed(12345)  # Seed based on integer given
    random.seed(b'bytedata')  # Seed based on byte data

    """
    除了上述介绍的功能，random模块还包含基于均匀分布、高斯分布和其他分布的随机数生成函数。
     
     比如， random.uniform() 计算均匀分布随机数， random.gauss() 计算正态分布随机数。
    """