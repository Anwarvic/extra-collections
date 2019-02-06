"""
Red-Black Trees are self-balancing BSTs (Binary Search Trees) which means that
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
        self.color = Color.RED

    def get_color(self):
        return self.color

    def set_color(self, color):
        assert color in {Color.RED, Color.BLACK}, "Invalid color!!"
        self.color = color

    def represent_data(self):
        if self.color == Color.RED:
            return str(self.data)+'r'
        elif self.color == Color.BLACK:
            return str(self.data)+'b'





class RedBlackTree(BST):
    def __init__(self, value):
        if isinstance(value, TreeNode):
            self.root = value
        else:
            self.root = TreeNode(value)
        self.root.color = Color.BLACK


    ############################## ROTATION ##############################
    def rotate_left(self, start_node):
        # print("Rotating Left")
        middle = start_node.get_right()
        middle.set_parent( start_node.get_parent() )
        start_node.set_right(middle.get_left())
        middle.set_left(start_node)
        return middle

    def rotate_right(self, start_node):
        pass


    ############################## INSERTION ##############################
    # def insert(self, value):
    #     """
    #     When inserting a value, we set color as red and then re-color it
    #     according to these three cases:
    #     - parent is 'black'
    #     - parent is 'red' and uncle is 'red'
    #     - parent is 'red' and uncle is 'black'
    #     """
    #     new_node = super().insert(value)
    #     parent = new_node.get_parent()
    #     grand_parent = parent.get_parent() if parent else None
    #     uncle = new_node.get_uncle()
    #     if parent.get_color() == Color.BLACK:
    #         pass #do nothing
    #     elif parent.get_color() == Color.RED:
    #         if uncle.get_color() == Color.RED:
    #             parent.set_color(Color.BLACK)
    #             uncle.set_color(Color.BLACK)
    #             grand_parent.set_color(Color.RED) if grand_parent




    #         GetParent(n)->color = BLACK;
    #         GetUncle(n)->color = BLACK;
    #         GetGrandParent(n)->color = RED;
    #         InsertRepairTree(GetGrandParent(n));








if __name__ == "__main__":
    rbtree = RedBlackTree(10)
    rbtree.root.set_right(TreeNode(50))
    rbtree.root.right.set_right(TreeNode(100))
    rbtree.root.set_left(TreeNode(5))
    rbtree.root.left.set_left(TreeNode(3))
    nnode = rbtree.insert(6)
    print(rbtree)

    # check uncle
    print(nnode.get_uncle())

