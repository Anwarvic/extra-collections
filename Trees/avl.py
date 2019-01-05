from bst import TreeNode, BST


class TreeNode(TreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.parent = None

    def set_left(self, new_node):
        self.left = new_node
        if new_node is not None:
            self.left.parent = self


    def set_right(self, new_node):
        self.right = new_node
        if new_node is not None:
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
    def __get_children_depths(self, start_node):
        left_depth = 1 if start_node.left != None else 0
        left_depth += super().get_depth(start_node.left)
        right_depth = 1 if start_node.right != None else 0
        right_depth += super().get_depth(start_node.right)
        return left_depth, right_depth


    ######################### ROTATION #########################
    def __rotate_left(self, start_node):
        print("Rotating Left")
        middle = start_node.right
        middle.parent = start_node.parent
        start_node.set_right(middle.left)
        middle.set_left(start_node)
        return middle

    def __rotate_right(self, start_node):
        print("Rotating Right")
        middle = start_node.left
        middle.parent = start_node.parent
        start_node.set_left(middle.right)
        middle.set_right(start_node)
        return middle

    def __rotate_left_right(self, start_node):
        print("Rotating Left-Right")
        middle = start_node.left.right
        middle.parent = start_node.parent
        start_node.left.set_right(middle.left)
        middle.set_left(start_node.left)
        start_node.set_left(middle.right)
        middle.set_right(start_node)
        return middle

    def __rotate_right_left(self, start_node):
        print("Rotating Right-Left")
        middle = start_node.right.left
        middle.parent = start_node.parent
        start_node.right.set_left(middle.right)
        middle.set_right(start_node.right)
        start_node.set_right(middle.left)
        middle.set_left(start_node)
        return middle


    ######################### RE-BALANCE #########################
    def __rebalance_subtree(self, start_node):
        left_depth, right_depth = self.__get_children_depths(start_node)
        # subtree is imbalanced
        if abs(left_depth - right_depth) > 1:
            # left direction
            if left_depth > right_depth:
                child = start_node.left
                left_depth, right_depth = self.__get_children_depths(child)
                # left direction
                if left_depth > right_depth:
                    start_node = self.__rotate_right(start_node)
                # right direction
                else:
                    start_node = self.__rotate_left_right(start_node)
            # right direction
            else:
                child = start_node.right
                left_depth, right_depth = self.__get_children_depths(child)
                # left direction
                if left_depth > right_depth:
                    start_node = self.__rotate_right_left(start_node)
                # right direction
                else:
                    start_node = self.__rotate_left(start_node)
        # recurssively apply __reblanace_subtree()
        if start_node.left is not None:
            start_node.left = self.__rebalance_subtree(start_node.left)
        if start_node.right is not None:
            start_node.right = self.__rebalance_subtree(start_node.right)
        return start_node


    def rebalance(self):
        new_root = self.__rebalance_subtree(self.root)
        self.root = new_root
    
    
    ######################### INSERTION #########################
    def __insert(self, value, start_node):
        if value == start_node.data:
            return
        elif value < start_node.data:
            if start_node.left:
                self.__insert(value, start_node.left)
            else:
                start_node.set_left( TreeNode(value) )
        else:
            if start_node.right:
                self.__insert(value, start_node.right)
            else:
                start_node.set_right( TreeNode(value) )

    def insert(self, value):
        assert type(value) in {int, float}, "You can insert only numbers!"
        self.__insert(value, self.root)
        self.rebalance()




if __name__ == "__main__":
    # to test left rotation
    avl = AVL(22)
    avl.root.set_right(TreeNode(43))
    avl.root.set_left(TreeNode(18))
    avl.root.left.set_left(TreeNode(9))
    avl.root.left.set_right(TreeNode(21))
    avl.root.left.left.set_left(TreeNode(6))
    avl.root.left.left.left.set_left(TreeNode(0))
    print(avl, '\n')
    avl.rebalance()
    print(avl)
    print('='*50)

    #######################################
    # to test left-right rotation
    avl = AVL(78)
    avl.root.set_right(TreeNode(88))
    avl.root.set_left(TreeNode(50))
    avl.root.left.set_left(TreeNode(48))
    avl.root.left.set_right(TreeNode(62))
    avl.root.left.right.set_left(TreeNode(54))
    print(avl, '\n')
    avl.rebalance()
    print(avl)
    print('='*50)

    #######################################
    # test all rotation-operations
    # src: Data Structures and Algorithms in Python Book (page: 506)
    avl = AVL(44)
    avl.root.set_left(TreeNode(17))
    avl.root.left.set_right(TreeNode(32))
    avl.root.set_right(TreeNode(78))
    avl.root.right.set_left(TreeNode(50))
    avl.root.right.set_right(TreeNode(88))
    avl.root.right.left.set_left(TreeNode(48))
    avl.root.right.left.set_right(TreeNode(62))
    avl.root.right.left.right.set_left(TreeNode(54))
    print(avl)
    avl.rebalance()
    print(avl)
    print('='*50)

    #######################################
    # insertion test (src: https://www.youtube.com/watch?v=7m94k2Qhg68)
    avl = AVL(43)
    avl.insert(18)
    avl.insert(22)
    avl.insert(9)
    avl.insert(21)
    avl.insert(6)
    avl.insert(8)
    avl.insert(20)
    avl.insert(63)
    avl.insert(50)
    avl.insert(62)
    avl.insert(51)
    print(avl)
    print('='*50)