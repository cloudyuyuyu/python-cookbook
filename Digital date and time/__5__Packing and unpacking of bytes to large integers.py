from util.separator import separator_content
import os

if __name__ == "__main__":
    """
    问题
        你有一个字节字符串并想将它解压成一个整数。或者，你需要将一个大整数转换为一个字节字符串。

    解决方案
        假设你的程序需要处理一个拥有128位长的16个元素的字节字符串。
    """
    separator_content()
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

    """
    为了将bytes解析为整数，使用 int.from_bytes() 方法，并像下面这样指定字节顺序：
    """
    print(len(data))
    print(int.from_bytes(data, "little"))
    print(int.from_bytes(data, "big"))

    """
    为了将一个大整数转换为一个字节字符串，使用 int.to_bytes() 方法，并像下面这样指定字节数和字节顺序：
    """
    separator_content()
    x = 94522842520747284487117727783387188

    print(x.to_bytes(16, "big"))
    print(x.to_bytes(16, "little"))

    """
    字节顺序规则(little或big)仅仅指定了构建整数时的字节的低位高位排列方式。 
    
    我们从下面精心构造的16进制数的表示中可以很容易的看出来：
    """
    separator_content()
    x = 0x01020304
    print(x.to_bytes(4, "big"))
    print(x.to_bytes(4, "little"))

    """
    如果你试着将一个整数打包为字节字符串，那么它就不合适了，你会得到一个错误。 
    
    如果需要的话，你可以使用 int.bit_length() 方法来决定需要多少字节位来存储这个值。
    """
    separator_content()
    x = 523 ** 23
    print(x)

    # print(x.to_bytes(16, "little"))
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # OverflowError: int too big to convert

    print(x.bit_length())
    n_bytes, rem = divmod(x.bit_length(), 8)

    if rem:
        n_bytes += 1
    print(n_bytes, rem, sep="\t")
    print(x.to_bytes(n_bytes, "little"))
