from abc import ABC

from binary_tree import TreeNode, BinaryTree


class Heap():
    def __init__(self, value):
        assert type(value) in {int, float}, "Heap contains numbers only!!"
        self.heap = [value]

    @abstractmethod
    def heapify(lst):
        length = len(lst)
        if length == 1:
            node = TreeNode(lst[0])
        elif length == 2:
            node = TreeNode(lst[0])
            node.left = TreeNode(lst[1])
        else:
            node = TreeNode(lst[0])
            node.left = self.__heapify(lst[1::2])
            node.right = self.__heapify(lst[2::2])
        btree = BinaryTree(0)
        btree.root = node
        return node



