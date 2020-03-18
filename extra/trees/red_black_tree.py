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
from abc import abstractmethod

from extra.trees.bst import BSTNode, BST




class Color(Enum):
    BLACK = 0
    RED = 1




class RedBlackNode(BSTNode):  
    def __init__(self, value):
        super().__init__(value)
        self.color = Color.RED


    def get_color(self):
        return self.color


    def set_color(self, color):
        if color not in {Color.RED, Color.BLACK}:
            raise ValueError("Invalid color!!")
        self.color = color


    def _represent(self):
        if self.color == Color.RED:
            return str(self.data)+'|R'
        elif self.color == Color.BLACK:
            return str(self.data)+'|B'


    @staticmethod
    def swap(node1, node2):
        #TODO: use super().swap(node1, node2) here
        node1.data, node2.data = node2.data, node1.data
        node1.color, node2.color = node2.color, node1.color




class RedBlackTree(BST):
    ############################## INIT ##############################
    _basic_node = RedBlackNode


    def __name__(self):
        return "extra.RedBlackTree()"
    

    def __init__(self, value):
        super().__init__(value)
        self.root.set_color(Color.BLACK)


    @staticmethod
    def from_iterable(iterable):
        #TODO: convert this to classmethod like the one with LinkedList
        # do that after applying clear()
        if not hasattr(iterable, "__iter__"):
            raise TypeError("The given object isn't iterable!!")
        if len(iterable) == 0:
            raise ValueError("The given iterable is empty!!")
        rbtree = None
        for item in iterable:
            if rbtree is None:
                rbtree = RedBlackTree(item)
            else:
                rbtree.insert(item)
        return rbtree
    

    ############################## HEIGHT ##############################
    def get_black_height(self):
        """
        Number of black nodes from root till to any leaf node, the root node
        is not counted
        """
        black_height = 0
        start_node = self.root.get_left()
        while(start_node is not None):
            if start_node.get_color() == Color.BLACK:
                black_height += 1
            start_node = start_node.get_left()
        # +1 to include NIL node
        return black_height + 1

    ############################## ROTATION ##############################
    def __rotate_left(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("Rotating Left")
        middle = start_node.get_right()
        middle.set_parent( start_node.get_parent() )
        start_node.set_right(middle.get_left())
        middle.set_left(start_node)
        return middle


    def __rotate_right(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("Rotating Right")
        middle = start_node.get_left()
        middle.set_parent( start_node.get_parent() )
        start_node.set_left(middle.get_right())
        middle.set_right(start_node)
        return middle


    ############################## INSERTION ##############################
    def __recolor_case3(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # get basic info
        uncle = start_node.get_uncle()
        parent = start_node.get_parent()
        grandparent = parent.get_parent() if parent else None
        # parent is left-child and start_node is left-child
        if parent.is_left_child() and start_node.is_left_child():
            grandparent.set_color(Color.RED)
            parent.set_color(Color.BLACK)
            grandparent = self.__rotate_right(grandparent)
        # parent is left-child and start_node is right-child
        elif parent.is_left_child() and not start_node.is_left_child():
            # first rotation
            parent = self.__rotate_left(parent)
            grandparent.set_left(parent)
            grandparent.set_color(Color.RED)
            # second rotation
            grandparent = self.__rotate_right(grandparent)
            grandparent.set_color(Color.BLACK)
        # parent is right-child and start_node is left-child
        elif not parent.is_left_child() and start_node.is_left_child():
            # first rotation
            parent = self.__rotate_right(parent)
            grandparent.set_right(parent)
            grandparent.set_color(Color.RED)
            # second rotation
            grandparent = self.__rotate_left(grandparent)
            grandparent.set_color(Color.BLACK)
        # parent is right-child and start_node is right-child
        else:
            grandparent.set_color(Color.RED)
            parent.set_color(Color.BLACK)
            grandparent = self.__rotate_left(grandparent)
        return grandparent


    def __recolor(self, start_node):
        """
        Recoloring can be done according to these three cases:
        - case I:   parent is 'black'
        - case II:  parent is 'red' and uncle is 'red'
        - case III: parent is 'red' and uncle is 'black'
        """
        # get basic info
        uncle = start_node.get_uncle()
        parent = start_node.get_parent()
        grandparent = parent.get_parent() if parent else None
        # recolor when node has a grandparent
        if parent is None or grandparent is None:
            return parent if parent else start_node

        # case I
        if parent.get_color() == Color.BLACK:
            #do nothing
            # print("Case I")
            return self.root
        else:
            # case II
            if uncle and uncle.get_color() == Color.RED:
                # print("Case II")
                parent.set_color(Color.BLACK)
                uncle.set_color(Color.BLACK)
                grandparent.set_color(Color.RED)
            # case III
            else:
                # print("Case III")
                # get great grandparent
                great_grandparent = grandparent.get_parent()
                grandparent = self.__recolor_case3(start_node)
                # set connection
                if great_grandparent:
                    if great_grandparent.data > grandparent.get_data():
                        great_grandparent.set_left(grandparent)
                    else:
                        great_grandparent.set_right(grandparent)
            # recursively do the same over grandparent 
            return self.__recolor(grandparent)

    def insert(self, value):
        super()._validate_item(value)
        # insert new node
        new_node = super()._insert(value)
        # recolor starting from new_node till root
        self.root = self.__recolor(new_node)
        # root is black (isn't essential tho!!)
        self.root.set_color(Color.BLACK)


    ############################## REMOVAL ##############################
    def _find_replacement(self, start_node):
        """
        NOTE: Here, we're tyring to exploit two characteristics of Red-black
        trees and they are: 
            - red-nodes are good replacements.
            - when removing a red node, there must be at least one red-node as
              a replacement at least.
        """
        assert isinstance(start_node, RedBlackNode)
        if start_node.is_leaf():
            replacement_node = None
        else:
            # in-order successor
            successor = super()._get_min_node(start_node.get_right()) \
                if start_node.get_right() else None
            # in-order predecessor
            predecessor = super()._get_max_node(start_node.get_left()) \
                if start_node.get_left() else None
            # find the red-node
            if successor and successor.get_color() == Color.RED:
                replacement_node = successor
            elif predecessor and predecessor.get_color() == Color.RED:
                replacement_node = predecessor
            else:
                replacement_node = successor if successor else predecessor
        return replacement_node


    def __attach(self, parent, child):
        assert parent is None or isinstance(parent, RedBlackNode)
        assert isinstance(child, RedBlackNode)
        if parent is None:
            self.root = child
        else:
            if parent.get_data() > child.get_data():
                parent.set_left(child) 
            else:
                parent.set_right(child)


    def __handle_double_black(self, parent, double_black_node):
        """
        When dealing with double black nodes, we have four cases:
        Case I  : if double_black_node is root
        Case II : (s) is black and one child of sibling's children is red (r)
        Case III: (s) is black and the two children of s are black
        Case IV : (s) is red
        
        Note: (s) is the sibling of the double_black_node
        SRC: https://www.programiz.com/dsa/deletion-from-a-red-black-tree
        """
        #TODO: should be refactored
        assert isinstance(parent, RedBlackNode)
        assert double_black_node is None or \
            isinstance(double_black_node, RedBlackNode)
        while double_black_node != self.root and (not double_black_node \
            or double_black_node.get_color() == Color.BLACK):
            # double black node is the left-child
            if double_black_node == parent.get_left():
                sibling = parent.get_right()
                # Case IV
                if sibling and sibling.get_color() == Color.RED:
                    sibling.set_color(Color.BLACK)
                    parent.set_color(Color.RED)
                    grandparent = parent.get_parent()
                    parent = self.__rotate_left(parent)
                    self.__attach(grandparent, parent)
                    # update parent and sibling
                    parent = parent.get_left()
                    sibling = parent.get_right()
                # check sibling children
                s_left_child = sibling.get_left()
                s_right_child = sibling.get_right()
                # get colors of sibling's children
                s_left_color = s_left_child.get_color() if s_left_child \
                                                        else Color.BLACK
                s_right_color = s_right_child.get_color() if s_right_child \
                                                          else Color.BLACK
                # Case III
                if s_left_color==Color.BLACK and s_right_color==Color.BLACK:
                    sibling.set_color(Color.RED)
                    double_black_node = parent
                # Case II
                else:
                    if s_right_color == Color.BLACK:
                        s_left_child.set_color(Color.BLACK)
                        sibling.set_color(Color.RED)
                        sibling = self.__rotate_right(sibling)
                        self.__attach(parent, sibling)
                        sibling = parent.get_right()

                    sibling.set_color(parent.get_color())
                    parent.set_color(Color.BLACK)
                    s_right_child = sibling.get_right()
                    s_right_child.set_color(Color.BLACK)
                    grandparent = parent.get_parent()
                    parent = self.__rotate_left(parent)
                    self.__attach(grandparent, parent)
                    double_black_node = self.root
            ##### Mirror image of the previous if-condition ######
            # double black node is the right-child
            else:
                sibling = parent.get_left()
                # Case IV
                if sibling and sibling.get_color() == Color.RED:
                    sibling.set_color(Color.BLACK)
                    parent.set_color(Color.RED)
                    grandparent = parent.get_parent()
                    parent = self.__rotate_right(parent)
                    self.__attach(grandparent, parent)
                    # update parent and sibling
                    parent = parent.get_right()
                    sibling = parent.get_left()
                # check sibling children
                s_left_child = sibling.get_left()
                s_right_child = sibling.get_right()
                # get colors of sibling's children
                s_left_color = s_left_child.get_color() if s_left_child \
                                                        else Color.BLACK
                s_right_color = s_right_child.get_color() if s_right_child \
                                                          else Color.BLACK
                # Case III
                if s_right_color==Color.BLACK and s_right_color==Color.BLACK:
                    sibling.set_color(Color.RED)
                    double_black_node = parent
                # Case II
                else:
                    if s_left_color == Color.BLACK:
                        s_right_child.set_color(Color.BLACK)
                        sibling.set_color(Color.RED)
                        sibling = self.__rotate_left(sibling)
                        self.__attach(parent, sibling)
                        sibling = parent.get_left() 

                    sibling.set_color(parent.get_color())
                    parent.set_color(Color.BLACK)
                    s_left_child = sibling.get_left()
                    s_left_child.set_color(Color.BLACK)
                    grandparent = parent.get_parent()
                    parent = self.__rotate_right(parent)
                    self.__attach(grandparent, parent)
                    double_black_node = self.root
        # make sure root is always black
        self.root.set_color(Color.BLACK)


    def remove(self, del_value):
        """
        Case I  : removed_node is 'red', replacement is either 'red' or None
        Case II : removed_node is 'red', replacement is 'black'
        Case III: removed_node is 'black', replacement is either 'black' or None
        Case IV : removed_node is 'black', replacement is 'red'
        """
        super()._validate_item(del_value)
        # check edge case
        if self.root.is_leaf() and del_value == self.root.get_data():
            raise ValueError("Can't remove the only item in the tree!")

        # search for the del_value node
        removed_node = super()._search(del_value, self.root)
        # couldn't find the node
        if removed_node.get_data() != del_value:
            return
        # find replacement
        replacement = self._find_replacement(removed_node)
        print("replacement:", replacement)

        # Case I (replace red-node with red-node/None)
        if removed_node.get_color() == Color.RED and \
            (replacement is None or replacement.get_color() == Color.RED):
            print("Case I (replace red-node with red-node/None)")
            super()._transplant(removed_node, replacement)
        
        # Case II (replace red-node with black-node)
        elif removed_node.get_color() == Color.RED and \
            replacement.get_color() == Color.BLACK:
            print("Case II (replace red-node with black-node)")
            raise ValueError("This case shouldn't occur!!")
        
        # Case III (replace black-node with black-node)
        elif removed_node.get_color() == Color.BLACK and \
            (replacement is None or replacement.get_color() == Color.BLACK):
            print("Case III (double black-node)")
            if replacement:
                parent = replacement.get_parent()
            else:
                parent = removed_node.get_parent()
            # do the transplant
            super()._transplant(removed_node, replacement)
            # get double black node
            if replacement is None:
                if parent.get_left() is None:
                    double_black_node = parent.get_left()
                else:
                    double_black_node = parent.get_right()
            else:
                if replacement.get_data() < parent.get_data():
                    double_black_node = parent.get_left() 
                else:
                    double_black_node = parent.get_right() 
            # handle this double black
            self.__handle_double_black(parent, double_black_node)
        
        # Case IV (replace black-node with red-node/None)
        elif removed_node.get_color() == Color.BLACK and \
            replacement.get_color() == Color.RED:
            replacement.set_color(Color.BLACK)
            print("Case IV (replace black-node with red-node/None)")
            super()._transplant(removed_node, replacement)
        

