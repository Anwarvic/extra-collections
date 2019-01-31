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





if __name__ == "__main__":
    rbt = RedBlackTree(1)
    print(rbt.root.color)
