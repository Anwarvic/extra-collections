from binary_tree import TreeNode, BinaryTree


class TreeNode(TreeNode):
    def __init__(self, value):
        assert type(value) in {int, float}, "BST contains only numbers!!"
        super().__init__(value)
        self.parent = None

    def get_parent(self):
        return self.parent

    def get_grand_parent(self):
        return self.parent.parent if self.parent else None

    def get_uncle(self):
        parent = self.parent
        if parent is None:
            return None
        grand_parent = parent.parent
        if grand_parent is None:
            return None
        return grand_parent.right if parent.is_left_child() \
                                    else grand_parent.left

    def get_sibling(self):
        # return the brother if found
        parent = self.parent
        if parent is None:
            return None
        return parent.right if self.is_left_child() else parent.left        

    def set_left(self, new_node):
        self.left = new_node
        if new_node is not None:
            self.left.parent = self

    def set_right(self, new_node):
        self.right = new_node
        if new_node is not None:
            self.right.parent = self

    def set_parent(self, new_node):
        self.parent = new_node

    def is_left_child(self):
        parent = self.parent
        return parent.data > self.data



class BST(BinaryTree):
    def __init__(self, value):
        if isinstance(value, TreeNode):
            self.root = value
        elif type(value) in {set, frozenset}:
            lst = sorted(value)
            self.root = self.__init_bst(lst)
        elif hasattr(value, '__iter__'):
            lst = sorted(set(value))
            self.root = self.__init_bst(lst)
        else:
            self.root = TreeNode(value)

    def __init_bst(self, lst):
        length = len(lst)
        assert length >0, "Given list must have t lease on item!!"
        if length == 1:
            node = TreeNode(lst[0])
        elif length == 2:
            node = TreeNode(lst[0])
            node.set_left( TreeNode(lst[1]) )
        else:
            mid_idx = len(lst)//2
            node = TreeNode(lst[mid_idx])
            node.set_left( self.__init_bst(lst[0:mid_idx]) )
            node.set_right( self.__init_bst(lst[mid_idx+1:]) )
        return node


    ############################## MAX/MIN ##############################
    def _get_max_node(self, start_node):
        # get the right-most node
        if start_node.get_right() == None:
            return start_node
        else:
            return self._get_max_node(start_node.get_right())

    def get_max(self):
        max_node = self._get_max_node(self.root)
        return max_node.get_data()

    def _get_min_node(self, start_node):
        # get the left-most node
        if start_node.get_left() == None:
            return start_node
        else:
            return self._get_min_node(start_node.get_left())

    def get_min(self):
        min_node = self._get_min_node(self.root)
        return min_node.get_data()


    ############################## SEARCH ##############################
    def search(self, find_val, start_node = None):
        if start_node is None: start_node = self.root
        if find_val == start_node.get_data():
            return start_node
        elif find_val < start_node.get_data():
            if start_node.get_left():
                return self.search(find_val, start_node.get_left())
            else:
                return start_node
        else:
            if start_node.get_right():
                return self.search(find_val, start_node.get_right())
            else:
                return start_node

    def __contains__(self, find_val):
        assert type(find_val) in {int, float}, "BST contains only numbers!"
        found_node = self.search(find_val)
        return found_node.get_data() == find_val


    ############################## INSERTION ##############################
    def __insert(self, value, start_node):
        if value == start_node.get_data():
            return start_node
        elif value < start_node.get_data():
            if start_node.get_left():
                return self.__insert(value, start_node.get_left())
            else:
                start_node.set_left( TreeNode(value) )
                return start_node.get_left()
        else:
            if start_node.get_right():
                return self.__insert(value, start_node.get_right())
            else:
                start_node.set_right( TreeNode(value) )
                return start_node.get_right()

    def _insert(self, value):
        # used mainly for inheritance
        assert type(value) in {int, float}, "You can insert only numbers!"
        return self.__insert(value, self.root)

    def insert(self, value):
        self._insert(value)


    ############################## REMOVAL ##############################
    def __remove(self, del_value, start_node):
        curr_value = start_node.get_data()
        # when del_value is found
        if del_value == curr_value:
            replacement_node = start_node.get_left() \
                if not start_node.get_right() \
                else self._get_min_node(start_node.get_right())
            if replacement_node is None:
                parent = start_node.get_parent()
                if curr_value < parent.get_data():
                    parent.set_left(replacement_node)
                else:
                    parent.set_right(replacement_node)
                return parent
            else:
                start_node.data = replacement_node.data
                if start_node.get_right():
                    self.__remove(replacement_node.data, start_node.get_right())
                else:
                    self.__remove(replacement_node.data, start_node.get_left())
                return start_node
        # when del_value < current value
        elif del_value < curr_value:
            if start_node.get_left() is None:
                # raise ValueError("Couldn't find given value in the tree!!")
                return start_node
            else:
                return self.__remove(del_value, start_node.get_left())
        # when del_value > current value
        else:
            if start_node.get_right() is None:
                # raise ValueError("Couldn't find given value in the tree!!")
                return start_node
            else:
                return self.__remove(del_value, start_node.get_right())

    def _remove(self, del_value):
        # used mainly for inheritance
        assert type(del_value) in {int, float}, "BST conains numbers only!"
        if self.root.is_leaf() and del_value == self.root.get_data():
            raise ValueError("Can't remove the only item in the tree!")
        return self.__remove(del_value, self.root)

    def remove(self, del_value):
        self._remove(del_value)






if __name__ == "__main__":
    bst = BST(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    print(bst)
    print(1 in bst)
    print(100 in bst)
    print(bst.root.left.get_sibling())
    print('='*50)
    #######################################
    # # initialize tree by list
    # lst = [7,10,12,22,30,11,19,25,9,20,14,12]
    # bst = BST(lst)
    # print(bst)
    # print('='*50)
    # #######################################
    # # example taken from "Data Structures and Algorithms in Python" book
    # bst = BST(44)
    # bst.root.set_left(TreeNode(17))
    # bst.root.left.set_left(TreeNode(8))
    # bst.root.left.set_right( TreeNode(32) )
    # bst.root.left.right.set_left( TreeNode(28) )
    # bst.root.left.right.left.set_right( TreeNode(29) )
    # bst.root.set_right( TreeNode(88) )
    # bst.root.right.set_right( TreeNode(97) )
    # bst.root.right.right.set_left( TreeNode(93) )
    # bst.root.right.set_left( TreeNode(65) )
    # bst.root.right.left.set_left( TreeNode(54) )
    # bst.root.right.left.set_right( TreeNode(82) )
    # bst.root.right.left.right.set_left( TreeNode(76) )
    # bst.root.right.left.right.left.set_left( TreeNode(68) )
    # bst.root.right.left.right.left.set_right( TreeNode(80) )
    # print(bst)

    # bst.remove(80)
    # bst.remove(32)
    # bst.remove(44)
    # bst.remove(4000)
    # bst.remove(65)
    # print(bst)

    # print("Tree Root:", bst.root)
    # print("Tree Nodes:", len(bst))
    # print("Tree Height:", bst.get_height())
    # print("Right-node Depth:", bst.get_depth(bst.root.right))
    # print("Balanced Tree:", bst.is_balanced())
    # print(bst.traverse())
    # print("Min value:", bst.get_min())
    # print("Max value:", bst.get_max())
