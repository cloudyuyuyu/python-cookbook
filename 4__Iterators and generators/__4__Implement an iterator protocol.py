from util.separator import separator_content


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node{!r}".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        """
        它首先返回自己本身并迭代每一个子节点并通过调用子节点的 depth_first() 方法
        (使用 yield from 语句)返回对应元素。
        """
        yield self
        for _child in self:
            yield from _child.depth_first()


if __name__ == "__main__":
    """
    问题
        你想构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法。

    解决方案
        目前为止，在一个对象上实现迭代最简单的方式是使用一个生成器函数。 
        
        在4.2小节中，使用Node类来表示树形数据结构。你可能想实现一个以深度优先方式遍历树形节点的生成器。
    """
    separator_content()

    root = Node(0)
    left_node = Node(1)
    right_node = Node(2)
    root.add_child(left_node)
    root.add_child(right_node)

    left_node.add_child(Node(3))
    left_node.add_child(Node(4))
    right_node.add_child(Node(5))

    for child in root.depth_first():
        print(child)

