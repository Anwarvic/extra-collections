from extra.trees.bst import BSTNode, BST



class AVLNode(BSTNode):
    def __name__(self):
        return "extra.AVLNode()"
    

    def __init__(self, value):
        super().__init__(value)
        self._height = 0
    

    def set_left(self, new_node):
        super().set_left(new_node)
        self._height = max(self.get_children_heights())
    

    def set_right(self, new_node):
        super().set_right(new_node)
        self._height = max(self.get_children_heights())
    

    def get_height(self):
        return self._height
    

    def get_left_height(self):
        return 1 + self.get_left().get_height() \
            if self.get_left() is not None else 0
        

    def get_right_height(self):
        return 1 + self.get_right().get_height() \
            if self.get_right() is not None else 0
    

    def get_children_heights(self):
        return [self.get_left_height(), self.get_right_height()]
    

    def set_height(self, new_height):
        if type(new_height) != int:
            raise TypeError("Height has to be an integer number >= 0!!")
        elif new_height < 0:
            raise ValueError("Height has to be an integer number >= 0!!")
        self._height = new_height
    

    def is_balanced(self):
        left_height, right_height = self.get_children_heights()
        return abs(right_height - left_height) <= 1
    

    def __repr__(self):
        return f"AVLNode({self._data})"
    



class AVL(BST):
    _basic_node = AVLNode


    def __name__(self):
        return "extra.AVL()"
    

    ##############################     HEIGHT     ##############################
    def _get_height(self, start_node):
        return start_node.get_height()
    

    ##############################     BALANCE    ##############################
    def _get_unbalanced_node(self, start_node):
        child = start_node
        parent = start_node.get_parent()
        grand_parent = start_node.get_grand_parent()
        while(grand_parent is not None and grand_parent.is_balanced()):
            return self._get_unbalanced_node(parent)
        return grand_parent, parent, child
    

    def _rebalance(self, grand_parent):
        assert isinstance(grand_parent, self._basic_node)

        # get the heavy parent
        left_height, right_height = grand_parent.get_children_heights()
        parent = grand_parent.get_left() \
            if left_height > right_height else grand_parent.get_right()
        # get the heavy child
        left_height, right_height = parent.get_children_heights()
        node = parent.get_left() \
            if left_height > right_height else parent.get_right()
        
        # determine the direction
        if parent.is_left_child():
            if node.is_left_child():
                # left-left
                middle = self._rotate_right(grand_parent)
            else:
                # left-right
                middle = self._rotate_left_right(grand_parent)
        else:
            if node.is_left_child():
                # right-left
                middle = self._rotate_right_left(grand_parent)
            else:
                # right-right
                middle = self._rotate_left(grand_parent)
        return middle
    

    def is_balanced(self):
        """
        BinaryTree is balanced if the difference between the depth of any
        two leaf nodes is less than or equal one.
        """
        if self.is_empty():
            return super().is_balanced()
        return self._root.is_balanced()


    ##############################     INSERT     ##############################
    def _insert(self, value):
        assert type(value) in {int, float} or \
                    isinstance(value, self._basic_node)
        
        if isinstance(value, self._basic_node):
            inserted_node = super()._insert_node(self._root, value)
        else:
            inserted_node = super()._insert_value(self._root, value)
        # update heights & rebalance when needed
        parent = inserted_node.get_parent()
        while(parent is not None):
            grand_parent = parent.get_parent()
            parent.set_height(max(parent.get_children_heights()))
            if not parent.is_balanced():
                parent = self._rebalance(parent)
                self._attach(grand_parent, parent)
            parent = grand_parent
        return inserted_node
    

    ##############################     REMOVE     ##############################
    def _remove(self, del_value, start_node):
        assert type(del_value) in {int, float}
        assert isinstance(start_node, self._basic_node)

        length_before = self._length
        last_accessed_node = super()._remove(del_value, start_node)
        if self._length != length_before:
            parent = last_accessed_node
            while(parent is not None):
                grand_parent = parent.get_parent()
                parent.set_height(max(parent.get_children_heights()))
                if not parent.is_balanced():
                    parent = self._rebalance(parent)
                    self._attach(grand_parent, parent)
                parent = grand_parent
        return last_accessed_node
        

