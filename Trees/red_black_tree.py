"""
Red-Black Trees are self-balanced BSTs (Binary Search Trees) which means that
they have a guaranteed height of O(log(n)) where n is the number of nodes within
the tree. The color is used only to re-balance trees and has nothing to do with
any thing else.

Red black trees have the following characteristics:
- A node is either 'red' or 'black'.
- Root is always 'black'.
- A node is 'red' if it has two 'black' children.
- Any child of a red-node is always 'black'.

Some other properties:
- "Black depth": is the depth of all black nodes.
- "Shortest path": (from parent to leaf-node) is equal to the black depth.
- "Longest path": is the one with alternating red and black nodes.
- The longest path can't be bigger than (2*shortest-path).

Considering the following BST:
  __B
 /   \
A     C
 \
  Z
We can say that:
- B is parent of A and C
- A and C are children for B
- B is grandparent for Z
- A is parent of Z
- C is uncle of Z (important)
"""
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



    bst = BST([0,2,3])
    bst.insert(1)
    print(bst)