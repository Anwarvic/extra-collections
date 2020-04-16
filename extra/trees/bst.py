from extra.trees.binary_tree import BinaryTreeNode, BinaryTree




class BSTNode(BinaryTreeNode):
    def __init__(self, value):
        if type(value) not in {int, float}:
            raise TypeError(f"{self.__name__()} contains only numbers!!")
        super().__init__(value)
        self._parent = None


    def get_parent(self):
        return self._parent


    def get_grand_parent(self):
        return self._parent.get_parent() if self._parent is not None else None


    def get_uncle(self):
        parent = self._parent
        if parent is None:
            return None
        grand_parent = parent.parent
        if grand_parent is None:
            return None
        return grand_parent.right \
            if parent.is_left_child() else grand_parent.left


    def get_sibling(self):
        # return the brother if found
        parent = self._parent
        if parent is None:
            return None
        return parent.right if self.is_left_child() else parent.left        


    def set_left(self, new_node):
        if not (new_node is None or isinstance(new_node, BSTNode)):
            raise TypeError(f"Can't set {type(new_node)} as a left child!!")
        self.left = new_node
        if new_node is not None:
            self.left.parent = self


    def set_right(self, new_node):
        if not (new_node is None or isinstance(new_node, BSTNode)):
            raise TypeError(f"Can't set {type(new_node)} as a right child!!")
        self.right = new_node
        if new_node is not None:
            self.right.parent = self


    def set_parent(self, new_node):
        if not (new_node is None or isinstance(new_node, BSTNode)):
            raise TypeError(f"Can't set {type(new_node)} as a child's parent!!")
        self._parent = new_node


    def is_left_child(self):
        return self._parent.data > self._data


    def __repr__(self):
        return f"BSTNode({self._data})"




class BST(BinaryTree):
    _basic_node = BSTNode

    ##TODO: __len__() needs to be O(1)

    def __name__(self):
        return "extra.BST()"


    def _validate_item(self, item):
        super()._validate_item(item)
        if type(item) not in {int, float}:
            raise TypeError(f"{self.__name__()} accepts only numbers!!")
    

    @staticmethod
    def from_iterable(iterable):
        #TODO: convert this to classmethod like the one with LinkedList
        # do that after applying clear()
        if not hasattr(iterable, "__iter__"):
            raise TypeError("The given object isn't iterable!!")
        if len(iterable) == 0:
            raise ValueError("The given iterable is empty!!")
        bst = None
        for item in iterable:
            if bst is None:
                bst = BST(item)
            else:
                bst.insert(item)
        return bst


    ##############################    MAX   ##############################
    def _get_max_node(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # get the right-most node
        if start_node.get_right() == None:
            return start_node
        else:
            return self._get_max_node(start_node.get_right())


    def get_max(self):
        if self.is_empty():
            raise IndexError(\
                f"Can't get the maximum value of an empty {self.__name__()}")
        max_node = self._get_max_node(self.root)
        return max_node.get_data()


    ##############################    MIN   ##############################
    def _get_min_node(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # get the left-most node
        if start_node.get_left() == None:
            return start_node
        else:
            return self._get_min_node(start_node.get_left())


    def get_min(self):
        if self.is_empty():
            raise IndexError(\
                f"Can't get the minimum value of an empty {self.__name__()}")
        min_node = self._get_min_node(self.root)
        return min_node.get_data()


    ##############################   SEARCH  ##############################
    def _search(self, find_val, start_node):
        assert isinstance(start_node, self._basic_node)
        assert type(find_val) in {float, int}
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
        if self.is_empty() or type(find_val) not in {int, float}:
            return False
        found_node = self._search(find_val, self.root)
        return found_node.get_data() == find_val


    ############################## INSERTION ##############################
    def _insert_node(self, start_node, inserted_node):
        assert isinstance(start_node, self._basic_node)
        assert inserted_node is None or \
            isinstance(inserted_node, self._basic_node)
        value = inserted_node.get_data()
        if value == start_node.get_data():
            return start_node
        elif value < start_node.get_data():
            if start_node.get_left():
                return self._insert_node(start_node.get_left(), inserted_node)
            else:
                start_node.set_left( inserted_node )
                return inserted_node
        else:
            if start_node.get_right():
                return self._insert_node(start_node.get_right(), inserted_node)
            else:
                start_node.set_right( inserted_node )
                return inserted_node


    def _insert_value(self, start_node, value):
        assert isinstance(start_node, self._basic_node)
        assert type(value) in {float, int}
        inserted_node = self._basic_node(value)
        return self._insert_node(start_node, inserted_node)


    def _insert(self, value):
        assert type(value) in {int, float} or \
                    isinstance(value, self._basic_node)
        if isinstance(value, self._basic_node):
            return self._insert_node(self.root, value)
        else:
            return self._insert_value(self.root, value)


    def insert(self, value):
        self._validate_item(value)
        self._insert(value)


    ##############################   REMOVAL  ##############################
    def _find_replacement(self, start_node):
        assert isinstance(start_node, self._basic_node)
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
        assert isinstance(node, self._basic_node)
        assert replacement is None or isinstance(replacement, self._basic_node)
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
            self._basic_node.swap(node, replacement)
            self._transplant(replacement, new_replacement)


    def _remove(self, del_value, start_node):
        assert type(del_value) in {int, float}
        assert isinstance(start_node, self._basic_node)
        if self.root.is_leaf() and del_value == self.root.get_data():
            raise IndexError("Can't remove the only item in the tree!")
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
        if self.is_empty or type(del_value) not in {int, float}:
            return 
        self._validate_item(del_value)
        self._remove(del_value, self.root)


    ##############################   ROTATION  ##############################
    def _rotate_left(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("Rotating Left")
        middle = start_node.get_right()
        middle.set_parent( start_node.get_parent() )
        start_node.set_right(middle.get_left())
        middle.set_left(start_node)
        return middle


    def _rotate_right(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("Rotating Right")
        middle = start_node.get_left()
        middle.set_parent( start_node.get_parent() )
        start_node.set_left(middle.get_right())
        middle.set_right(start_node)
        return middle
    

    def _rotate_left_right(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("Rotating Left-Right")
        middle = start_node.get_left().get_right()
        middle.set_parent( start_node.get_parent() )
        start_node.get_left().set_right(middle.get_left())
        middle.set_left(start_node.get_left())
        start_node.set_left(middle.get_right())
        middle.set_right(start_node)
        return middle


    def _rotate_right_left(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("Rotating Right-Left")
        middle = start_node.get_right().get_left()
        middle.set_parent( start_node.get_parent() )
        start_node.get_right().set_left(middle.get_right())
        middle.set_right(start_node.get_right())
        start_node.set_right(middle.get_left())
        middle.set_left(start_node)
        return middle


    def _attach(self, parent, child):
        assert parent is None or isinstance(parent, self._basic_node)
        assert isinstance(child, self._basic_node)
        if parent is None:
            self.root = child
        else:
            if parent.get_data() > child.get_data():
                parent.set_left(child) 
            else:
                parent.set_right(child)


