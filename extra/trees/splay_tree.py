from extra.trees.bst import BSTNode, BST




class SplayTree(BST):
    def __name__(self):
        return "extra.SplayTree()"
    

    ############################## SPLAYING ##############################
    def __zig_zig(self, start_node, is_child_left=True):
        assert isinstance(start_node, BSTNode)
        assert type(is_child_left) == bool
        child = start_node
        parent = child.get_parent()
        grand_parent = child.get_grand_parent()
        # start zig-zig
        if is_child_left:
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


    def __zig_zag(self, start_node, is_child_left=True):
        assert isinstance(start_node, BSTNode)
        assert type(is_child_left) == bool
        child = start_node
        parent = child.get_parent()
        grand_parent = child.get_grand_parent()
        # start __zig-zag
        if is_child_left:
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
        assert isinstance(start_node, BSTNode)
        child = start_node
        parent = child.get_parent()
        if parent is None:
            return start_node
        grand_parent = child.get_grand_parent()
        # get the operation type
        if grand_parent is None:
            if child.is_left_child():
                root = self.__zig(child, left_child=True)
            else:
                root = self.__zig(child, left_child=False)
        else:
            # left -> left
            if parent.is_left_child() and child.is_left_child():
                grand_parent = self.__zig_zig(child, is_child_left=True)
            # left -> right
            elif parent.is_left_child() and not child.is_left_child():
                grand_parent = self.__zig_zag(child, is_child_left=True)
            # right -> left
            elif not parent.is_left_child() and child.is_left_child():
                grand_parent = self.__zig_zag(child, is_child_left=False)
            # right -> right
            else:
                grand_parent = self.__zig_zig(child, is_child_left=False)
            if grand_parent.get_parent() is not None:
                root = self.__splaying(grand_parent)
            else:
                root = grand_parent
        return root
    
    
    def splay(self, start_node):
        self.root = self.__splaying(start_node)


    ############################## SEARCH ##############################
    def find(self, find_val):
        node = super()._search(find_val, self.root)
        self.splay(node)


    ############################## INSERTION ##############################
    def insert(self, value):
        new_node = super()._insert_value(self.root, value)
        self.splay(new_node)


    ############################## REMOVAL ##############################
    def remove(self, del_value):
        node = super()._remove(del_value, self.root)
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
    stree.root.set_left(BSTNode(3))
    stree.root.get_left().set_right(BSTNode(4))
    stree.root.get_left().get_right().set_right(BSTNode(6))
    stree.root.get_left().get_right().get_right().set_left(BSTNode(5))
    stree.root.get_left().get_right().get_right().set_right(BSTNode(7))
    stree.root.set_right(BSTNode(10))
    stree.root.get_right().set_right(BSTNode(11))
    stree.root.get_right().get_right().set_right(BSTNode(12))
    stree.root.get_right().get_right().get_right().set_right(BSTNode(16))
    stree.root.get_right().get_right().get_right().get_right().set_left(BSTNode(13))
    stree.root.get_right().get_right().get_right().get_right().set_right(BSTNode(17))
    stree.insert(14)
    stree.find(13)
    print(stree)
    stree.find(8)
    print(stree)
    print('='*50)

    # test remove
    # example from Data Structures and Algorithm in Python (page: 517)
    stree = SplayTree(8)
    stree.root.set_left(BSTNode(3))
    stree.root.get_left().set_right(BSTNode(4))
    stree.root.get_left().get_right().set_right(BSTNode(6))
    stree.root.get_left().get_right().get_right().set_left(BSTNode(5))
    stree.root.get_left().get_right().get_right().set_right(BSTNode(7))
    stree.root.set_right(BSTNode(10))
    stree.root.get_right().set_right(BSTNode(11))
    print(stree)
    stree.remove(8)
    print(stree)
    print('='*50)

    # example from https://www.codesdope.com/course/data-structures-splay-trees/
    stree.root.set_left(BSTNode(20))
    stree.root.get_left().set_right(BSTNode(30))
    stree.root.get_left().set_left(BSTNode(2))
    stree.root.get_left().get_right().set_left(BSTNode(28))
    stree.root.get_left().get_right().set_right(BSTNode(35))
    stree.root.set_right(BSTNode(70))
    stree.root.get_right().set_left(BSTNode(60))
    stree.root.get_right().set_right(BSTNode(80))
    stree.remove(30)
    print(stree)
    print('='*50)


