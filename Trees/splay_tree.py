from bst import TreeNode, BST



class SplayTree(BST):
    ############################## SPLAYING ##############################
    def __zig_zig(self, start_node, left_children=True):
        child = start_node
        parent = child.get_parent()
        grand_parent = parent.get_parent()
        # start __zig-__zig
        if left_children:
            # print("Left zig-zig")
            child.set_parent( grand_parent.get_parent() )
            grand_parent.set_left(parent.get_right())
            parent.set_right(grand_parent)
            parent.set_left(child.get_right())
            child.set_right(parent)
        else:
            # print("Right zig-zig")
            child.set_parent( grand_parent.get_parent() )
            grand_parent.set_right(parent.get_left())
            parent.set_left(grand_parent)
            parent.set_right(child.get_left())
            child.set_left(parent)
        #child is now the grand-parent
        return child

    def __zig_zag(self, start_node, left_right_children=True):
        child = start_node
        parent = child.get_parent()
        grand_parent = parent.get_parent()
        # start __zig-zag
        if left_right_children:
            # print("Left-Right zig-zag")
            child.set_parent( grand_parent.get_parent() )
            grand_parent.set_left(child.get_right())
            parent.set_right(child.get_left())
            child.set_right(grand_parent)
            child.set_left(parent)
            pass
        else:
            # print("Right-Left zig-zag")
            child.set_parent( grand_parent.get_parent() )
            grand_parent.set_right(child.get_left())
            parent.set_left(child.get_right())
            child.set_left(grand_parent)
            child.set_right(parent)
        return child

    def __zig(self, start_node, left_child=True):
        child = start_node
        parent = child.get_parent()
        if left_child:
            # print("Left zig")
            child.set_parent( parent.get_parent() )
            parent.set_left(child.get_right())
            child.set_right(parent)
        else:
            # print("Right zig")
            child.set_parent( parent.get_parent() )
            parent.set_right(child.get_left())
            child.set_left(parent)
        return child

    def __splaying(self, start_node):
        child = start_node
        parent = child.get_parent()
        if parent is None:
            return start_node
        grand_parent = parent.get_parent()
        # get the operation type
        if grand_parent is None:
            if child.is_left_child():
                root = self.__zig(child, left_child=True)
            else:
                root = self.__zig(child, left_child=False)
        else:
            # left -> left
            if parent.is_left_child() and child.is_left_child():
                grand_parent = self.__zig_zig(child, left_children=True)
            # left -> right
            elif parent.is_left_child() and not child.is_left_child():
                grand_parent = self.__zig_zag(child, left_right_children=True)
            # right -> left
            elif not parent.is_left_child() and child.is_left_child():
                grand_parent = self.__zig_zag(child, left_right_children=False)
            # right -> right
            else:
                grand_parent = self.__zig_zig(child, left_children=False)
            if grand_parent.get_parent() is not None:
                root = self.__splaying(grand_parent)
            else:
                root = grand_parent
        return root
    

    def splay(self, start_node):
        self.root = self.__splaying(start_node)


    ############################## SEARCH ##############################
    def find(self, find_val):
        node = super().search(find_val)
        self.splay(node)


    ############################## INSERTION ##############################
    def insert(self, value):
        new_node = super().insert(value)
        self.splay(new_node)


    ############################## REMOVAL ##############################
    def remove(self, del_value):
        node = super().remove(del_value)
        self.splay(node)


    ############################## OTHERS ##############################
    def traverse(self):
        raise NotImplementedError("You can't traverse Splay Trees!!")

    def is_balanced(self):
        raise NotImplementedError("You can't check balance of Splay Trees!!")

    def is_perfect(self):
        raise NotImplementedError("You can't check balance of Splay Trees!!")

    def is_strict(self):
        raise NotImplementedError("You can't check balance of Splay Trees!!")

    def get_height(self):
        raise NotImplementedError("You can't check height of Splay Trees!!")

    def get_depth(self):
        raise NotImplementedError("You can't check depth of Splay Trees!!")







if __name__ == "__main__":
    # test insert
    # example from Data Structures and Algorithm in Python (page: 514)
    stree = SplayTree(8)
    stree.root.set_left(TreeNode(3))
    stree.root.get_left().set_right(TreeNode(4))
    stree.root.get_left().get_right().set_right(TreeNode(6))
    stree.root.get_left().get_right().get_right().set_left(TreeNode(5))
    stree.root.get_left().get_right().get_right().set_right(TreeNode(7))
    stree.root.set_right(TreeNode(10))
    stree.root.get_right().set_right(TreeNode(11))
    stree.root.get_right().get_right().set_right(TreeNode(12))
    stree.root.get_right().get_right().get_right().set_right(TreeNode(16))
    stree.root.get_right().get_right().get_right().get_right().set_left(TreeNode(13))
    stree.root.get_right().get_right().get_right().get_right().set_right(TreeNode(17))
    stree.insert(14)
    stree.find(13)
    print(stree)
    stree.find(8)
    print(stree)
    print('='*50)

    # test remove
    # example from Data Structures and Algorithm in Python (page: 517)
    stree = SplayTree(8)
    stree.root.set_left(TreeNode(3))
    stree.root.get_left().set_right(TreeNode(4))
    stree.root.get_left().get_right().set_right(TreeNode(6))
    stree.root.get_left().get_right().get_right().set_left(TreeNode(5))
    stree.root.get_left().get_right().get_right().set_right(TreeNode(7))
    stree.root.set_right(TreeNode(10))
    stree.root.get_right().set_right(TreeNode(11))
    print(stree)
    stree.remove(8)
    print(stree)
    print('='*50)

    # example from https://www.codesdope.com/course/data-structures-splay-trees/
    stree = SplayTree(50)
    stree.root.set_left(TreeNode(20))
    stree.root.get_left().set_right(TreeNode(30))
    stree.root.get_left().set_left(TreeNode(2))
    stree.root.get_left().get_right().set_left(TreeNode(28))
    stree.root.get_left().get_right().set_right(TreeNode(35))
    stree.root.set_right(TreeNode(70))
    stree.root.get_right().set_left(TreeNode(60))
    stree.root.get_right().set_right(TreeNode(80))
    stree.remove(30)
    print(stree)
    print('='*50)


