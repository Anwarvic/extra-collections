from bst import TreeNode, BST


class TreeNode(TreeNode):
    def __init__(self, value):
        assert value != None, "You can't use None as a value!!"
        self.data = value
        self.parent = None
        self.left = None
        self.right = None

    def set_left(self, value):
        assert value != None, "You can't use None as a value!!"
        new_node = TreeNode(value)
        new_node.parent = self
        self.left = new_node

    def set_right(self, value):
        assert value != None, "You can't use None as a value!!"
        new_node = TreeNode(value)
        new_node.parent = self
        self.right = new_node


class AVL(BST):
    def __init__(self, value):
        self.root = TreeNode(value)

    def __get_depth(self, start_node):
        depth = 0
        if start_node != None:
            left_depth, right_depth = 0, 0
            if start_node.left:
                left_depth = 1 + self.__get_depth(start_node.left)
            if start_node.right:
                right_depth = 1 + self.__get_depth(start_node.right)
            depth += max(left_depth, right_depth)
        return depth

    def __is_balanced(self, start_node):
        """
        Tree is said to be balanced if the difference between the depth of any
        two leaf nodes is one or less.
        """
        # check left subtree
        left_depth = 1 if start_node.left != None else 0
        left_depth += self.__get_depth(start_node.left)
        # check right subtree
        right_depth = 1 if start_node.right != None else 0
        right_depth += self.__get_depth(start_node.right)
        return abs(left_depth - right_depth) <= 1






if __name__ == "__main__":
    avl = AVL(1)
    avl.root.set_right(2)
    avl.root.right.set_right(3)
    avl.root.right.right.set_right(4)
    avl.root.right.right.right.set_right(5)
    # avl.root = avl.left_rotation(avl.root)
    print(avl)

    # avl = AVL(5)
    # avl.root.set_left(4)
    # avl.root.left.set_left(3)
    # avl.root.left.left.set_left(2)
    # avl.root.left.left.left.set_left(1)
    # avl.root = avl.right_rotation(avl.root)
    # print(avl.root.left)
    #######################################
    # initialize tree by list
    # lst = [7,10,12,22,30,11,19,25,9,20,14]
    # avl = BST(lst)
    # print(avl.root.right.right.left)
    #######################################
    # example taken from "Data Structures and Algorithms in Python" book
    # avl = AVL(44)
    # avl.root.left = TreeNode(17)
    # avl.root.left.left = TreeNode(8)
    # avl.root.left.right = TreeNode(32)
    # avl.root.left.right.left = TreeNode(28)
    # avl.root.left.right.left.right = TreeNode(29)
    # avl.root.right = TreeNode(88)
    # avl.root.right.right = TreeNode(97)
    # avl.root.right.right.left = TreeNode(93)
    # avl.root.right.left = TreeNode(65)
    # avl.root.right.left.left = TreeNode(54)
    # avl.root.right.left.right = TreeNode(82)
    # avl.root.right.left.right.left = TreeNode(76)
    # avl.root.right.left.right.left.left = TreeNode(68)
    # avl.root.right.left.right.left.right = TreeNode(80)

    # avl.remove(32)
    # avl.remove(44)

    print("Tree Root:", avl.root)
    print("Tree Nodes:", len(avl))
    print("Tree Height:", avl.get_height())
    print("Tree Depth:", avl.get_depth())
    print("Balanced Tree:", avl.is_balanced())
    print(avl.traverse())
    print("Min value:", avl.get_min())
    print("Max value:", avl.get_max())