from bst import TreeNode, BST


class TreeNode(TreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.parent = None

    def set_left(self, new_node):
        self.left = new_node
        self.left.parent = self


    def set_right(self, new_node):
        self.right = new_node
        self.right.parent = self




class AVL(BST):
    def __init__(self, value):
        if type(value) == list:
            lst = sorted(value)
            self.root = self.__init_avl(lst)
        else:
            self.root = TreeNode(value)

    def __init_avl(self, lst):
        length = len(lst)
        assert length >0, "Given List must have values!!"
        if length == 1:
            parent = TreeNode(lst[0])
        elif length == 2:
            parent = TreeNode(lst[0])
            parent.set_left( TreeNode(lst[1]) )
        else:
            mid_idx = len(lst)//2
            parent = TreeNode(lst[mid_idx])
            parent.set_left( self.__init_avl(lst[0:mid_idx]) )
            parent.set_right( self.__init_avl(lst[mid_idx+1:]) )
        return parent

    def __rotate_left(self, start_node):
        middle = start_node.right
        middle.parent = start_node.parent
        start_node.right = None
        middle.set_left(start_node)
        return middle

    def __rotate_right(self, start_node):
        middle = start_node.left
        middle.parent = start_node.parent
        start_node.left = None
        middle.set_right(start_node)
        return middle

    def __rotate_left_right(self, start_node):
        middle = start_node.left.right
        middle.parent = start_node.parent
        start_node.left.right = None
        middle.set_left(start_node.left)
        start_node.left = None
        middle.set_right(start_node)
        return middle

    def __rotate_right_left(self, start_node):
        middle = start_node.right.left
        middle.parent = start_node.parent
        start_node.right.left = None
        middle.set_right(start_node.right)
        start_node.right = None
        middle.set_left(start_node)
        return middle

    def __rebalance_subtree(self, start_node):
        if start_node.is_leaf():
            return start_node
        elif start_node.has_one_child():
            # left child
            if start_node.left is not None:
                child = start_node.left
                if child.is_leaf():
                    return start_node
                elif child.has_one_child():
                    # left child
                    if start_node.left is not None:
                        start_node = self.__rotate_right(start_node)
                    # right child
                    else:
                        start_node = self.__rotate_left_right(start_node)
                else:
                    start_node.left = self.__rebalance_subtree(start_node.left)
                    start_node.right = self.__rebalance_subtree(start_node.right)
            # right child
            else:
                child = start_node.right
                if child.is_leaf():
                    return start_node
                elif child.has_one_child():
                    # left child
                    if start_node.left is not None:
                        start_node = self.__rotate_right_left(start_node)
                    # right child
                    else:
                        start_node = self.__rotate_left(start_node)
        start_node.left = self.__rebalance_subtree(start_node.left)
        start_node.right = self.__rebalance_subtree(start_node.right)
        return start_node

    def rebalance(self):
        new_root = self.__rebalance_subtree(self.root)
        self.root = new_root





if __name__ == "__main__":
    # # to test left rotation
    # avl = AVL(1)
    # avl.root.set_right(TreeNode(2))
    # avl.root.right.set_right(TreeNode(3))
    # avl.root.right.right.set_right(TreeNode(4))
    # avl.root.right.right.right.set_right(TreeNode(5))
    # print(avl, '\n')
    # avl.root = avl.__rotate_left(avl.root)
    # avl.root.right = avl.__rotate_left(avl.root.right)
    # print(avl)
    # print('='*50)

    # # to test right rotation
    # avl = AVL(1)
    # avl.root.set_left(TreeNode(2))
    # avl.root.left.set_left(TreeNode(3))
    # avl.root.left.left.set_left(TreeNode(4))
    # avl.root.left.left.left.set_left(TreeNode(5))
    # print(avl, '\n')
    # avl.root = avl.__rotate_right(avl.root)
    # avl.root.left = avl.__rotate_right(avl.root.left)
    # print(avl)
    # print('='*50)

    # # to test left-right rotation
    # avl = AVL(1)
    # avl.root.set_left(TreeNode(2))
    # avl.root.left.set_right(TreeNode(3))
    # print(avl, '\n')
    # avl.root = avl.__rotate_left_right(avl.root)
    # print(avl)
    # print('='*50)
    
    # # to test right-left rotation
    # avl = AVL(1)
    # avl.root.set_right(TreeNode(2))
    # avl.root.right.set_left(TreeNode(3))
    # print(avl, '\n')
    # avl.root = avl.__rotate_right_left(avl.root)
    # print(avl)
    # print('='*50)
    # print(avl.is_balanced())
    
    #######################################
    # initialize tree by list
    # lst = [7,10,12,22,30,11,19,25,9,20,14]
    # avl = AVL(lst)
    # print(avl)
    # print("AVL Balanced:", avl.is_balanced())

    #######################################
    # general tree
    avl = AVL(10)
    avl.root.set_left(TreeNode(5))
    avl.root.left.set_left(TreeNode(2))
    avl.root.left.left.set_left(TreeNode(1))
    avl.root.left.left.left.set_left(TreeNode(0))
    print(avl)
    avl.rebalance()
    print(avl)