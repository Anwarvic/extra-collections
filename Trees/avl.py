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


    ######################### BALANCED #########################
    def is_subtree_balanced(self, start_node):
        left_depth = 1 if start_node.left != None else 0
        left_depth += super().get_depth(start_node.left)
        right_depth = 1 if start_node.right != None else 0
        right_depth += super().get_depth(start_node.right)
        return abs(left_depth - right_depth) <= 1


    ######################### ROTATION #########################
    def rotate_left(self, start_node):
        middle = start_node.right
        middle.parent = start_node.parent
        start_node.right = middle.left
        middle.set_left(start_node)
        return middle

    def rotate_right(self, start_node):
        middle = start_node.left
        middle.parent = start_node.parent
        start_node.left = middle.right
        middle.set_right(start_node)
        return middle

    def rotate_left_right(self, start_node):
        middle = start_node.left.right
        middle.parent = start_node.parent
        start_node.left.right = None
        middle.set_left(start_node.left)
        start_node.left = None
        middle.set_right(start_node)
        return middle

    def rotate_right_left(self, start_node):
        middle = start_node.right.left
        middle.parent = start_node.parent
        start_node.right.left = None
        middle.set_right(start_node.right)
        start_node.right = None
        middle.set_left(start_node)
        return middle





if __name__ == "__main__":
    # to test left rotation
    avl = AVL(22)
    avl.root.set_right(TreeNode(43))
    avl.root.set_left(TreeNode(18))
    avl.root.left.set_left(TreeNode(9))
    avl.root.left.set_right(TreeNode(21))
    avl.root.left.left.set_left(TreeNode(6))
    print(avl, '\n')
    avl.root = avl.rotate_right(avl.root)
    print(avl)
    print('='*50)

    