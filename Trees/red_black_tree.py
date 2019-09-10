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
        self.root.set_color(Color.BLACK)


    ############################## HEIGHT ##############################
    def get_black_height(self):
        #TODO
        pass

    ############################## ROTATION ##############################
    def __rotate_left(self, start_node):
        # print("Rotating Left")
        middle = start_node.get_right()
        middle.set_parent( start_node.get_parent() )
        start_node.set_right(middle.get_left())
        middle.set_left(start_node)
        return middle

    def __rotate_right(self, start_node):
        # print("Rotating Right")
        middle = start_node.get_left()
        middle.set_parent( start_node.get_parent() )
        start_node.set_left(middle.get_right())
        middle.set_right(start_node)
        return middle


    ############################## INSERTION ##############################
    def __recolor_case3(self, start_node):
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
        # insert new node
        tmp_node = super()._insert(value)
        # create new TreeNode with red color
        new_node = TreeNode(value) #red by default
        parent = tmp_node.get_parent()
        # take care of node-parent connection
        if not parent or value == parent.get_data():
            return
        elif value > parent.get_data():
            parent.set_right(new_node)
        elif value < parent.get_data():
            parent.set_left(new_node)
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


    def __get_node_and_replacement(self, del_value, start_node):
        #TODO: try to get rid of this function and use find() or search instead.
        curr_value = start_node.get_data()
        # when del_value is found
        if del_value == curr_value:
            replacement = self._find_replacement(start_node)
            return start_node, replacement
        # search left-side
        elif del_value < curr_value:
            if start_node.get_left() is None:
                # raise ValueError("Couldn't find given value in the tree!!")
                return start_node, None
            else:
                return self.__get_node_and_replacement(del_value,
                                                       start_node.get_left())
        # search right-side
        else:
            if start_node.get_right() is None:
                # raise ValueError("Couldn't find given value in the tree!!")
                return start_node, None
            else:
                return self.__get_node_and_replacement(del_value,
                                                       start_node.get_right())


    def __transplant(self, node, replacement):
        parent = node.get_parent()
        if replacement is None:
            if parent is None:
                self.__transplant(replacement, None)
                node.data = replacement.data
                return parent, node
            else:
                if node.is_left_child():
                    parent.set_left(replacement)
                    return parent, parent.get_left()
                else:
                    parent.set_right(replacement)
                    return parent, parent.get_right()
        else:
            if replacement.is_leaf():
                new_replacement = None
            elif replacement.get_left():
                new_replacement = replacement.get_left()
            else:
                new_replacement = replacement.get_right()
            # transplant data & color
            node.data = replacement.data
            node.set_color(replacement.get_color())
            self.__transplant(replacement, new_replacement)
            return parent, node

    
    def __handle_double_black_case1(self, parent, double_black_node):
        pass
    
    def __handle_double_black_case2(self, parent, double_black_node, sibling):
        parent.set_color(Color.RED)
        sibling.set_color(Color.BLACK)
        if sibling.is_left_child():
            parent = self.__rotate_right(parent)
        else:
            parent = self.__rotate_left(parent)
        return parent

    def __handle_double_black_case3(self, parent, double_black_node, sibling):
            sibling.set_color(Color.RED)
            grandparent = parent.get_parent()
            if 

    def __handle_double_black_case4(self, parent, double_black_node):
        pass

    def __handle_double_black_case5(self, parent, double_black_node):
        pass

    def __handle_double_black_case6(self, parent, double_black_node):
        pass
    
    def __handle_double_black(self, parent, double_black_node):
        """
        SRC: https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
        When dealing with double black nodes, we have six cases to consider:
        Case I  : if double_black_node is root
        Case II : (s) is red
        Case III: (p) and (s) are black and the two children of (s) are black
        Case IV : (p) is red, (s) is black and the two children of (s) are black
        Case V  : (s) is black, left-child of (s) is red, right-child of (s) is
                  black and (s) is the right-child
        Case VI : (s) is black, right-child of (s) is red, and (s) is the right-
                  child
        
        Note: (s) is the sibling of the double_black_node and (p) is the parent
        """
         # Case I
        if parent is None:
            return double_black_node
        else:
            grandparent = parent.get_parent()
            sibling = double_black_node.get_sibling() \
                    if double_black_node \
                    else parent.get_left() \
                        if parent.get_left() else parent.get_right()
            print("sibling:", sibling)
            if sibling is None:
                pass
            else:
                s_left_child = sibling.get_left()
                s_right_child = sibling.get_right()
                # get colors of sibling's children
                s_left_color = s_left_child.get_color() if s_left_child \
                                                        else Color.BLACK
                s_right_color = s_right_child.get_color() if s_right_child \
                                                          else Color.BLACK
                # Case II
                if sibling.get_color() == Color.RED:
                    parent = self.__handle_double_black_case2(parent,
                                                            double_black_node)
                # Case III
                elif (parent.get_color() == Color.BLACK and
                    sibling.get_color() == Color.BLACK and
                    s_left_color == Color.BLACK and
                    s_right_color == Color.BLACK):


    def remove(self, del_value):
        """
        Case I  : removed_node is 'red', replacement is either 'red' or None
        Case II : removed_node is 'red', replacement is 'black'
        Case III: removed_node is 'black', replacement is either 'black' or None
        Case IV : removed_node is 'black', replacement is 'red'
        """
        removed_node, replacement = self.__get_node_and_replacement(del_value,
                                                                    self.root)
        print("replacement:", replacement)
        # couldn't find the del_value in the tree
        if removed_node.get_data() != del_value:
            return

        # Case I (replace red-node with red-node/None)
        if removed_node.get_color() == Color.RED and \
            (replacement is None or replacement.get_color() == Color.RED):
            print("Case I (replace red-node with red-node/None)")
            self.__transplant(removed_node, replacement)
        
        # Case II (replace red-node with black-node)
        elif removed_node.get_color() == Color.RED and \
            replacement.get_color() == Color.BLACK:
            print("Case II (replace red-node with black-node)")
            raise ValueError("This case shouldn't occur!!")
        
        # Case III (replace black-node with black-node)
        elif removed_node.get_color() == Color.BLACK and \
            (replacement is None or replacement.get_color() == Color.BLACK):
            print("Case III (double black-node)")
            parent, transplanted = self.__transplant(removed_node, replacement)
            double_black_node = transplanted
            # handle this double black
            root = self.__handle_double_black(parent, double_black_node)
            self.root = root
        
        # Case IV (replace black-node with red-node/None)
        elif removed_node.get_color() == Color.BLACK and \
            replacement.get_color() == Color.RED:
            print("Case IV (replace black-node with black-node/None)")
            self.__transplant(removed_node, replacement)
        








if __name__ == "__main__":
    ######################### Test insertion #########################
    # # src: https://www.youtube.com/watch?v=eO3GzpCCUSg
    # rbtree = RedBlackTree(8)
    # rbtree.insert(8)
    # rbtree.insert(5)
    # rbtree.insert(15)
    # rbtree.insert(12)
    # rbtree.insert(19)
    # rbtree.insert(9)
    # rbtree.insert(13)
    # rbtree.insert(23)
    # rbtree.insert(10)
    # print(rbtree)
    # print('='*50, '\n')

    # # test special case
    # rbtree = RedBlackTree(15)
    # rbtree.insert(5)
    # rbtree.insert(1)
    # print(rbtree)
    # print('='*50, '\n')

    # # src: https://www.geeksforgeeks.org/red-black-tree-set-2-insert/
    # rbtree = RedBlackTree(10)
    # rbtree.insert(20)
    # rbtree.insert(30)
    # rbtree.insert(15)
    # print(rbtree)
    # print('='*50, '\n')

    # # src: http://www.btechsmartclass.com/data_structures/red-black-trees.html
    # rbtree = RedBlackTree(8)
    # rbtree.insert(18)
    # rbtree.insert(5)
    # rbtree.insert(15)
    # rbtree.insert(17)
    # rbtree.insert(25)
    # rbtree.insert(40)
    # rbtree.insert(80)
    # print(rbtree)
    # print('='*50, '\n')

    # # src: Data Structures and Algorithms in Python Book (Page: 539)
    # rbtree = RedBlackTree(4)
    # rbtree.insert(7)
    # rbtree.insert(12)
    # rbtree.insert(15)
    # rbtree.insert(3)
    # rbtree.insert(5)
    # rbtree.insert(14)
    # rbtree.insert(18)
    # rbtree.insert(16)
    # rbtree.insert(17)
    # print(rbtree)
    # print('='*50, '\n')

    ######################### Test Removal #########################
    # src: https://www.youtube.com/watch?v=eO3GzpCCUSg&t=1s
    rbtree = RedBlackTree(7)
    rbtree.insert(3)
    rbtree.insert(18)
    rbtree.insert(10)
    rbtree.insert(22)
    rbtree.insert(8)
    rbtree.insert(11)
    rbtree.insert(26)
    print(rbtree, '\n')
    rbtree.remove(3)
    print(rbtree)

    # rbtree = RedBlackTree(13)
    # rbtree.insert(8)
    # rbtree.insert(17)
    # rbtree.insert(1)
    # rbtree.insert(11)
    # rbtree.insert(1)
    # rbtree.insert(15)
    # rbtree.insert(25)
    # rbtree.insert(6)
    # rbtree.insert(22)
    # rbtree.insert(27)
    # print(rbtree, '\n')
    # rbtree.remove(11)
    # print(rbtree)

    #################### THESE TO TEST double-black nodes ####################
    # # test case 2.1 (left-left)
    # rbtree = RedBlackTree(40)
    # rbtree.insert(30)
    # rbtree.insert(50)
    # rbtree.insert(20)
    # rbtree.insert(35)
    # print(rbtree)
    # rbtree.remove(50)
    # print(rbtree, '\n')

    # # test case 2.2 (left-right)
    # rbtree = RedBlackTree(40)
    # rbtree.insert(30)
    # rbtree.insert(50)
    # rbtree.insert(35)
    # print(rbtree)
    # rbtree.remove(50)
    # print(rbtree)

    # # test case 2.3 (right-left)
    # rbtree = RedBlackTree(30)
    # rbtree.insert(20)
    # rbtree.insert(40)
    # rbtree.insert(35)
    # print(rbtree)
    # rbtree.remove(20)
    # print(rbtree)

    # test case 2.4 (right-right)
    # rbtree = RedBlackTree(30)
    # rbtree.insert(20)
    # rbtree.insert(40)
    # rbtree.insert(50)
    # print(rbtree)
    # rbtree.remove(20)
    # print(rbtree)

    