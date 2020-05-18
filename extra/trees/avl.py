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




class AVL(BST):
    _basic_node = AVLNode


    def __name__(self):
        return "extra.AVL()"

    
    ##############################     ROTATE     ##############################
    def _rotate_left(self, start_node):
        print("HERE")
        middle = super()._rotate_left(start_node)
        # adjust heights
        middle.get_left().decrement_height(value=2)
        return middle


    def _rotate_right(self, start_node):
        middle = super()._rotate_right(start_node)
        # adjust heights
        middle.get_right().decrement_height(value=2)
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
    

    def _rebalance(self, grand_parent, parent):
        assert isinstance(grand_parent, self._basic_node)
        assert isinstance(parent, self._basic_node)

        # get the cause of the imbalance
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
            inserted_node = self._insert_node(self._root, value)
        else:
            inserted_node = self._insert_value(self._root, value)
        # update heights & rebalance when needed
        child = inserted_node
        parent = child.get_parent()
        while(parent is not None and parent._height < 1+child._height):
            grand_parent = parent.get_parent()
            parent.increment_height()
            if not parent.is_balanced():
                middle = self._rebalance(parent, child)
                self._attach(grand_parent, middle)
                parent = middle
            child = parent
            parent = grand_parent
        return inserted_node
    

    ##############################     REMOVE     ##############################
    # def remove(self, del_value):
    #     if self.is_empty() or type(del_value) not in {int, float}:
    #         super().remove(del_value)
    #     elif 




if __name__ == "__main__":
    avl = AVL()
    