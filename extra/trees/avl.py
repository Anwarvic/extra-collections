from extra.trees.bst import BSTNode, BST



class AVLNode(BSTNode):
    def __name__(self):
        return "extra.AVLNode()"
    

    def __init__(self, value):
        super().__init__(value)
        self._height = 0
    

    def get_height(self):
        return self._height
    

    def __validate_height(self, new_height):
        if type(new_height) != int:
            raise TypeError("Height has to be an integer number >= 0!!")
        elif new_height < 0:
            raise ValueError("Height has to be an integer number >= 0!!")
    

    def increment_height(self, value=1):
        self.__validate_height(value)
        self._height += value
    

    def decrement_height(self, value=1):
        self.__validate_height(value)
        self._height -= value
    

    def get_children_heights(self):
        left_height  = 1 + self.get_left().get_height() \
                            if self.get_left() is not None else 0
        right_height = 1 + self.get_right().get_height() \
                            if self.get_right() is not None else 0
        return [left_height, right_height]
    

    def is_balanced(self):
        left_height, right_height = self.get_children_heights()
        return abs(right_height - left_height) <= 1
    

    def __repr__(self):
        return f"AVLNode({self._data})"
    

    @staticmethod
    def swap_height(first, second):
        assert first is None or isinstance(first, AVLNode)
        assert first is None or isinstance(first, AVLNode)

        first_height = first.get_height() if first is not None else 0
        second_height = second.get_height() if second is not None else 0
        first._height, second._height = second_height, first_height




class AVL(BST):
    _basic_node = AVLNode


    def __name__(self):
        return "extra.AVL()"

    
    ##############################     ROTATE     ##############################
    def _rotate_left(self, start_node):
        middle = super()._rotate_left(start_node)
        # adjust heights
        AVLNode.swap_height(middle, middle.get_left())
        return middle


    def _rotate_right(self, start_node):
        middle = super()._rotate_right(start_node)
        # adjust heights
        AVLNode.swap_height(middle, middle.get_right())
        return middle
    

    def _rotate_left_right(self, start_node):
        middle = super()._rotate_left_right(start_node)
        # adjust heights
        middle.increment_height()
        middle.get_left().decrement_height()
        middle.get_right().decrement_height(value=2)
        return middle


    def _rotate_right_left(self, start_node):
        middle = super()._rotate_right_left(start_node)
        # adjust heights
        middle.increment_height()
        middle.get_left().decrement_height(value=2)
        middle.get_right().decrement_height()
        return middle

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
        child = inserted_node
        parent = child.get_parent()
        while(parent is not None and parent._height < 1+child._height):
            grand_parent = parent.get_parent()
            parent.increment_height()
            if not parent.is_balanced():
                parent = self._rebalance(parent)
                self._attach(grand_parent, parent)
            child = parent
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
                if parent.is_leaf():
                    parent.decrement_height()
                if not parent.is_balanced():
                    parent = self._rebalance(parent)
                    self._attach(grand_parent, parent)
                parent = grand_parent
        return last_accessed_node
        

        



if __name__ == "__main__":
    avl = AVL()
    avl.insert(44)
    avl.insert(62)
    avl.insert(17)
    avl.insert(32)
    avl.insert(50)
    avl.insert(78)
    avl.insert(48)
    avl.insert(54)
    avl.insert(88)
    print(avl)
    avl.remove(17)
    print()
    print(avl)