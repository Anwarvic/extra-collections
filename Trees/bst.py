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


    ##############################    MAX    ##############################
    def _get_max_node(self, start_node):
        # get the right-most node
        if start_node.get_right() == None:
            return start_node
        else:
            return self._get_max_node(start_node.get_right())

    def get_max(self):
        max_node = self._get_max_node(self.root)
        return max_node.get_data()


    ##############################    MIN    ##############################
    def _get_min_node(self, start_node):
        # get the left-most node
        if start_node.get_left() == None:
            return start_node
        else:
            return self._get_min_node(start_node.get_left())

    def get_min(self):
        min_node = self._get_min_node(self.root)
        return min_node.get_data()


    ##############################   SEARCH  ##############################
    def _search(self, find_val, start_node):
        if find_val == start_node.get_data():
            return start_node
        elif find_val < start_node.get_data():
            if start_node.get_left():
                return self._search(find_val, start_node.get_left())
            else:
                return start_node
        else:
            if start_node.get_right():
                return self._search(find_val, start_node.get_right())
            else:
                return start_node

    def __contains__(self, find_val):
        assert type(find_val) in {int, float}, "BST contains only numbers!"
        found_node = self._search(find_val, self.root)
        return found_node.get_data() == find_val


    ############################## INSERTION ##############################
    def _insert(self, value, start_node):
        assert type(value) in {int, float}, "You can insert only numbers!"
        if value == start_node.get_data():
            return start_node
        elif value < start_node.get_data():
            if start_node.get_left():
                return self._insert(value, start_node.get_left())
            else:
                start_node.set_left( TreeNode(value) )
                return start_node.get_left()
        else:
            if start_node.get_right():
                return self._insert(value, start_node.get_right())
            else:
                start_node.set_right( TreeNode(value) )
                return start_node.get_right()

    def insert(self, value):
        self._insert(value, self.root)


    ##############################   REMOVAL  ##############################
    def _find_replacement(self, start_node):
        if start_node.get_right():
            # in-order successor
            replacement_node = self._get_min_node(start_node.get_right())
        elif start_node.get_left():
            # in-order predecessor
            replacement_node = self._get_max_node(start_node.get_left())
        else:
            # start_node is leaf
            replacement_node = None
        return replacement_node
    
    def _transplant(self, node, replacement):
        # replace 'node' with 'replacement'
        if replacement is None:
            parent = node.get_parent()
            if parent.get_left() == node:
                parent.set_left(replacement)
            else:
                parent.set_right(replacement)
        else:
            if replacement.is_leaf():
                new_replacement = None
            elif replacement.get_left():
                new_replacement = replacement.get_left()
            else:
                new_replacement = replacement.get_right()
            # swap data
            TreeNode.swap(node, replacement)
            self._transplant(replacement, new_replacement)

    def _remove(self, del_value, start_node):
        assert type(del_value) in {int, float}, "BST conains numbers only!"
        if self.root.is_leaf() and del_value == self.root.get_data():
            raise ValueError("Can't remove the only item in the tree!")
        # search for the del_value node
        removed_node = self._search(del_value, self.root)
        # couldn't find the node
        if removed_node.get_data() != del_value:
            last_accessed_node = removed_node
            return last_accessed_node
        # find replacement
        replacement = self._find_replacement(removed_node)
        # get last accessed node after replacement
        if replacement is None:
            parent = removed_node.get_parent()
        else:
            parent = replacement.get_parent()
        # replace 'del_node' with 'replacement'
        self._transplant(removed_node, replacement)
        # return last accessed node when removing
        last_accessed_node = parent
        return last_accessed_node

    def remove(self, del_value):
        self._remove(del_value, self.root)






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
    # initialize tree by list
    lst = [7,10,12,22,30,11,19,25,9,20,14,12]
    bst = BST(lst)
    print(bst)
    print('='*50)
    #######################################
    # example taken from "Data Structures and Algorithms in Python" book
    bst = BST(44)
    bst.root.set_left(TreeNode(17))
    bst.root.left.set_left(TreeNode(8))
    bst.root.left.set_right( TreeNode(32) )
    bst.root.left.right.set_left( TreeNode(28) )
    bst.root.left.right.left.set_right( TreeNode(29) )
    bst.root.set_right( TreeNode(88) )
    bst.root.right.set_right( TreeNode(97) )
    bst.root.right.right.set_left( TreeNode(93) )
    bst.root.right.set_left( TreeNode(65) )
    bst.root.right.left.set_left( TreeNode(54) )
    bst.root.right.left.set_right( TreeNode(82) )
    bst.root.right.left.right.set_left( TreeNode(76) )
    bst.root.right.left.right.left.set_left( TreeNode(68) )
    bst.root.right.left.right.left.set_right( TreeNode(80) )
    print(bst)

    bst.remove(80)
    bst.remove(32)
    bst.remove(44)
    bst.remove(4000)
    bst.remove(65)
    print(bst)

    print("Tree Root:", bst.root)
    print("Tree Nodes:", len(bst))
    print("Tree Height:", bst.get_height())
    print("Right-node Depth:", bst._get_depth(bst.root.right))
    print("Balanced Tree:", bst.is_balanced())
    print(bst.traverse())
    print("Min value:", bst.get_min())
    print("Max value:", bst.get_max())
