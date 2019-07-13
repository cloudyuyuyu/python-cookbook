from util.separator import separator_content
import os

if __name__ == "__main__":
    """
    问题
        你想直接读取二进制数据到一个可变缓冲区中，而不需要做任何的中间复制操作。 
        
        或者你想原地修改数据并将它写回到一个文件中去。

    解决方案
        为了读取数据到一个可变数组中，使用文件对象的 readinto() 方法。比如：
    """
    separator_content()

    def read_into_buffer(filename):
        buf = bytearray(os.path.getsize(filename))
        with open(filename, 'rb') as f:
            f.readinto(buf)
        return buf


    buf = read_into_buffer('somefile.bin')
    print(buf)
    buf[0:5] = b'Hi'
    print(buf)

    with open('newsample.bin', 'wb') as f:
        f.write(buf)
