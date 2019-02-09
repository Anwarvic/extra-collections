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
        # print("Rotating Right")
        middle = start_node.get_left()
        middle.set_parent( start_node.get_parent() )
        start_node.set_left(middle.get_right())
        middle.set_right(start_node)
        return middle


    ############################## INSERTION ##############################
    def __recolor(self, start_node):
        """
        Recoloring can be done according to these three cases:
        - case I:   parent is 'black'
        - case II:  parent is 'red' and uncle is 'red'
        - case III: parent is 'red' and uncle is 'black'
        """
        # check if start_node is root (parent is None)
        if not start_node.get_parent():
            return start_node
        # get basic info
        uncle = start_node.get_uncle()
        parent = start_node.get_parent()
        grandparent = parent.get_parent()

        # case I
        if parent.get_color() == Color.BLACK:
            pass #do nothing
        else:
            # case II
            if uncle and uncle.get_color() == Color.RED:
                parent.set_color(Color.BLACK)
                uncle.set_color(Color.BLACK)
                grandparent.set_color(Color.RED)
            # case III
            else:
                # parent is left-child and node is left-child
                if parent.is_left_child() and start_node.is_left_child():
                    grandparent.set_color(Color.RED)
                    parent.set_color(Color.BLACK)
                    grandparent = self.rotate_right(grandparent)
                # parent is left-child and node is right-child
                elif parent.is_left_child() and not start_node.is_left_child():
                    parent = self.rotate_left(parent)
                    grandparent.set_left(parent)
                # parent is right-child and node is left-child
                elif not parent.is_left_child() and start_node.is_left_child():
                    parent = self.rotate_right(parent)
                    grandparent.set_right(parent)
                # parent is right-child and node is right-child
                else:
                    grandparent.set_color(Color.RED)
                    parent.set_color(Color.BLACK)
                    grandparent = self.rotate_left(grandparent)
        if grandparent:
            return self.__recolor(grandparent)
        else:
            return self.__recolor(parent)



    def __insert(self, value):
        """
        When inserting a value, we set color as red and then re-color it
        """
        # insert new node
        node = super().insert(value)
        # cast into TreeNode-with-color
        new_node = TreeNode(value) # red by default
        parent = node.get_parent()
        grandparent = parent.get_parent()
        # take care of node-parent connection
        if value > parent.get_data():
            parent.set_right(new_node)
        elif value < parent.get_data():
            parent.set_left(new_node)
        # start recoloring when inserted node has a grandparent
        if grandparent:
            # recolor starting from new_node till grandparent
            self.root = self.__recolor(new_node)


    def insert(self, value):
        # insert new value
        self.__insert(value)
        # make sure the root is black
        self.root.set_color(Color.BLACK)







if __name__ == "__main__":
    rbtree = RedBlackTree(8)
    rbtree.insert(5)
    rbtree.insert(15)
    rbtree.insert(12)
    rbtree.insert(19)
    rbtree.insert(9)
    rbtree.insert(13)
    rbtree.insert(23)
    rbtree.insert(10)
    print(rbtree)

    # test special cases
    # rbtree = RedBlackTree(15)
    # rbtree.insert(5)
    # rbtree.insert(1)
    # print(rbtree)

