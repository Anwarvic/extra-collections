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
    

    def __repr__(self):
        return f"AVLNode({self._data})"




class AVL(BST):
    _basic_node = AVLNode


    def __name__(self):
        return "extra.AVL()"

    
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




if __name__ == "__main__":
    avl = AVL()
    avl.insert(43)
    avl.insert(18)
    avl.insert(22)
    avl.insert(9)
    avl.insert(21)
    avl.insert(6)
    avl.insert(8)
    avl.insert(20)
    avl.insert(63)
    avl.insert(50)
    avl.insert(62)
    avl.insert(51)
    print(avl)
    print('='*50)