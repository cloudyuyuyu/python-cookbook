from util.separator import separator_content
import numpy as np

if __name__ == "__main__":
    """
    问题
        你需要执行矩阵和线性代数运算，比如矩阵乘法、寻找行列式、求解线性方程组等等。

    解决方案
        NumPy 库有一个矩阵对象可以用来解决这个问题。
    """
    separator_content()
    matrix = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])

    print(matrix)
    print("矩阵的转置： ", matrix.T)
    print("逆矩阵： ", matrix.I)

    vector = np.matrix([[2], [3], [4]])

    print(matrix * vector)

    print(np.multiply(vector, vector))

    """
    可以在 numpy.linalg 子包中找到更多的操作函数，比如：
    """
    separator_content()
    print(np.linalg.det(matrix))

    print(np.linalg.eigvals(matrix))

    # Solve for x in mx = v
    x = np.linalg.solve(matrix, vector)
    print(x)

    print(all(matrix * x == vector))
