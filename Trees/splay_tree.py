from bst import TreeNode, BST



class SplayTree(BST):
    ############################## SPLAYING ##############################
    def zig_zig(self, start_node, left_children=True):
        child = start_node
        parent = child.parent
        grand_parent = parent.parent
        # start zig-zig
        if left_children:
            print("Left zig-zig")
            child.parent = grand_parent.parent
            grand_parent.set_left(parent.right)
            parent.set_right(grand_parent)
            parent.set_left(child.right)
            child.set_right(parent)
        else:
            print("Right zig-zig")
            child.parent = grand_parent.parent
            grand_parent.set_right(parent.left)
            parent.set_left(grand_parent)
            parent.set_right(child.left)
            child.set_left(parent)
        #child is now the grand-parent
        return child

    def zig_zag(self, start_node, left_right_children=True):
        child = start_node
        parent = child.parent
        grand_parent = parent.parent
        # start zig-zag
        if left_right_children:
            print("Left-Right zig-zag")
            child.parent = grand_parent.parent
            grand_parent.set_left(child.right)
            parent.set_right(child.left)
            child.set_right(grand_parent)
            child.set_left(parent)
            pass
        else:
            print("Right-Left zig-zag")
            child.parent = grand_parent.parent
            grand_parent.set_right(child.left)
            parent.set_left(child.right)
            child.set_left(grand_parent)
            child.set_right(parent)
        return child

    def zig(self, start_node, left_child=True):
        child = start_node
        parent = child.parent
        if left_child:
            print("Left zig")
            child.parent = parent.parent
            parent.set_left(child.right)
            child.set_right(parent)
        else:
            print("Right zig")
            child.parent = parent.parent
            parent.set_right(child.left)
            child.set_left(parent)
        return child

    def __splaying(self, start_node):
        child = start_node
        parent = child.parent
        if parent is None:
            return start_node
        grand_parent = parent.parent
        # get the operation type
        if grand_parent is None:
            if child.is_left_child():
                root = self.zig(child, left_child=True)
            else:
                root = self.zig(child, left_child=False)
        else:
            # left -> left
            if parent.is_left_child() and child.is_left_child():
                grand_parent = self.zig_zig(child, left_children=True)
            # left -> right
            elif parent.is_left_child() and not child.is_left_child():
                grand_parent = self.zig_zag(child, left_right_children=True)
            # right -> left
            elif not parent.is_left_child() and child.is_left_child():
                grand_parent = self.zig_zag(child, left_right_children=False)
            # right -> right
            else:
                grand_parent = self.zig_zig(child, left_children=False)
            if grand_parent.parent is not None:
                root = self.__splaying(grand_parent)
            else:
                root = grand_parent
        return root
    

    def splay(self, start_node):
        self.root = self.__splaying(start_node)


    ############################## INSERTION ##############################
    def __find(self, find_val, start_node):
        if find_val == start_node.data:
            self.splay(start_node)
        elif find_val < start_node.data:
            if start_node.left:
                self.__find(find_val, start_node.left)
            else:
                self.splay(start_node)
        else:
            if start_node.right:
                self.__find(find_val, start_node.right)
            else:
                self.splay(start_node)

    def find(self, find_val):
        assert type(find_val) in {int, float}, "You can insert only numbers!"
        if find_val != self.root.data:
            self.__find(find_val, self.root)

    
    ############################## INSERTION ##############################
    def __insert(self, value, start_node):
        if value == start_node.data:
            return
        elif value < start_node.data:
            if start_node.left:
                self.__insert(value, start_node.left)
            else:
                start_node.set_left( TreeNode(value) )
                # splay
                self.splay(start_node.left)
        else:
            if start_node.right:
                self.__insert(value, start_node.right)
            else:
                start_node.set_right( TreeNode(value) )
                # splay
                self.splay(start_node.right)

    def insert(self, value):
        assert type(value) in {int, float}, "You can insert only numbers!"
        self.__insert(value, self.root)


    ############################## REMOVAL ##############################
    def __get_max_node(self, start_node):
        # get the right-most node
        if start_node.right == None:
            return start_node
        else:
            return self.__get_max_node(start_node.right)

    def __remove(self, del_value, start_node):
        parent = start_node.parent
        if del_value == start_node.data:
            if start_node.is_leaf():
                if del_value <= parent.data:
                    parent.set_left( None )
                else:
                    parent.set_right( None )
                self.splay(parent)
            elif start_node.left != None and start_node.right == None:
                if del_value <= parent.data:
                    parent.set_left( start_node.left )
                else:
                    parent.set_right( start_node.left )
                self.splay(parent)
            elif start_node.left == None and start_node.right != None:
                if del_value <= parent.data:
                    parent.set_left( start_node.right )
                else:
                    parent.set_right( start_node.right )
                self.splay(parent)
            else:
                replacement_node = self.__get_max_node(start_node.left)
                start_node.data = replacement_node.data
                self.__remove(replacement_node.data, start_node.left)
                self.splay(start_node)
            
        elif del_value < start_node.data:
            if not start_node.left:
                self.splay(start_node)
            else:
                self.__remove(del_value, start_node.left)
        else:
            if not start_node.right:
                self.splay(start_node)
            else:
                self.__remove(del_value, start_node.right)


    def remove(self, del_value):
        assert type(del_value) in {int, float}, "BST conains numbers only!"
        if self.root.is_leaf() and del_value == self.root.data:
            raise ValueError("Can't remove the only item in the tree!")
        self.__remove(del_value, self.root)
    

    def traverse(self):
        raise NotImplementedError("You can't traverse a Splay Tree!!")


    # don't forget to disable:
    # traverse
    # height
    # balance
    # perfect
    # ...






if __name__ == "__main__":
    # test insert
    # example from Data Structures and Algorithm in Python (page: 514)
    # stree = SplayTree(8)
    # stree.root.set_left(TreeNode(3))
    # stree.root.left.set_right(TreeNode(4))
    # stree.root.left.right.set_right(TreeNode(6))
    # stree.root.left.right.right.set_left(TreeNode(5))
    # stree.root.left.right.right.set_right(TreeNode(7))
    # stree.root.set_right(TreeNode(10))
    # stree.root.right.set_right(TreeNode(11))
    # stree.root.right.right.set_right(TreeNode(12))
    # stree.root.right.right.right.set_right(TreeNode(16))
    # stree.root.right.right.right.right.set_left(TreeNode(13))
    # stree.root.right.right.right.right.set_right(TreeNode(17))
    # stree.insert(14)
    # stree.find(13)
    # print(stree)

    # # test remove
    # # example from Data Structures and Algorithm in Python (page: 517)
    # stree = SplayTree(8)
    # stree.root.set_left(TreeNode(3))
    # stree.root.left.set_right(TreeNode(4))
    # stree.root.left.right.set_right(TreeNode(6))
    # stree.root.left.right.right.set_left(TreeNode(5))
    # stree.root.left.right.right.set_right(TreeNode(7))
    # stree.root.set_right(TreeNode(10))
    # stree.root.right.set_right(TreeNode(11))
    # print(stree)
    # stree.remove(8)
    # print(stree)

    # example from https://www.codesdope.com/course/data-structures-splay-trees/
    stree = SplayTree(50)
    stree.root.set_left(TreeNode(20))
    stree.root.left.set_right(TreeNode(30))
    stree.root.left.set_left(TreeNode(2))
    stree.root.left.right.set_left(TreeNode(28))
    stree.root.left.right.set_right(TreeNode(35))
    stree.root.set_right(TreeNode(70))
    stree.root.right.set_left(TreeNode(60))
    stree.root.right.set_right(TreeNode(80))
    stree.remove(30)
    print(stree)
    print(stree.traverse())


