from enum import Enum
from bst import TreeNode, BST


class Color(Enum):
    BLACK = 0
    RED = 1


class TreeNode(TreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.color = None



class RedBlackTree(BST):
    def __init__(self, value):
        self.root = TreeNode(value)
        self.root.color = Color.BLACK

    def insert(self, value):
        pass







if __name__ == "__main__":
    rbtree = RedBlackTree(1)
    print(rbtree)
    print(rbtree.root.color)
