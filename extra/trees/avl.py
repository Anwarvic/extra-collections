from extra.trees.bst import BSTNode, BST



class AVLNode(BSTNode):
    def __name__(self):
        return "extra.AVLNode()"
    

    def __init__(self, value):
        super().__init__(value)
        self._height = 0
    

    def get_height(self):
        return self._height
    

    def increment_height(self):
        self._height += 1
    

    def decrement_height(self):
        self._height -= 1
    
    def set_height(self, new_height):
        if type(new_height) != int:
            raise TypeError("Height has to be an integer number >= 0!!")
        elif new_height < 0:
            raise ValueError("Height has to be an integer number >= 0!!")
        self._height = new_height
    

    def get_children_heights(self):
        left_height  = self.get_left().get_height() \
                            if self.get_left() is not None else 0
        right_height = self.get_right().get_height() \
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
        middle = super()._rotate_left(start_node)
        # adjust heights
        left_height, _ = middle.get_children_heights()
        middle.get_left().set_height(left_height-2)
        return middle


    def _rotate_right(self, start_node):
        middle = super()._rotate_right(start_node)
        # adjust heights
        _, right_height = middle.get_children_heights()
        middle.get_right().set_height(right_height-2)
        return middle
    

    def _rotate_left_right(self, start_node):
        middle = super()._rotate_left_right(start_node)
        # adjust heights
        _, right_height = middle.get_children_heights()
        middle.increment_height()
        middle.get_left().decrement_height()
        middle.get_right().set_height(right_height-2)
        return middle


    def _rotate_right_left(self, start_node):
        middle = super()._rotate_left_right(start_node)
        # adjust heights
        left_height, _ = middle.get_children_heights()
        middle.increment_height()
        middle.get_left().set_height(left_height-2)
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
            

    def _rebalance(self, start_node):
        if start_node is None:
            return
        # general case
        grand_parent, parent, node = self._get_unbalanced_node(start_node)
        if grand_parent is not None:
            if parent.is_left_child():
                if node.is_left_child():
                    # left-left
                    middle = super()._rotate_right(grand_parent)
                    self._attach(grand_parent.get_parent(), middle)
                else:
                    # left-right
                    middle = super()._rotate_left_right(grand_parent)
                    self._attach(grand_parent.get_parent(), middle)
            else:
                if node.is_left_child():
                    # right-left
                    middle = super()._rotate_right_left(grand_parent)
                    self._attach(grand_parent.get_parent(), middle)
                else:
                    # right-right
                    middle = super()._rotate_left(grand_parent)
                    self._attach(grand_parent.get_parent(), middle)
            self._rebalance(grand_parent.get_parent())

        

    ##############################     INSERT     ##############################
    def insert(self, value):
        self._validate_item(value)
        if self.is_empty():
            self._root = self._basic_node(value)
            self._length += 1
        else:
            inserted_node = self._insert(value)
            child = inserted_node
            parent = child.get_parent()
            while(parent is not None and parent._height < 1+child._height):
                parent.increment_height()
                child = parent
                parent = child.get_parent()
            # rebalance child
            self._rebalance(inserted_node)





if __name__ == "__main__":
    avl = AVL()
    avl.insert(44)
    avl.insert(17)
    avl.insert(78)
    avl.insert(32)
    avl.insert(50)
    avl.insert(88)
    avl.insert(48)
    avl.insert(62)
    avl.insert(54)
    print(avl)
    print('='*50)