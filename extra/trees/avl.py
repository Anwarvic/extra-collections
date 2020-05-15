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




def AVL(BST):
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
            parent = inserted_node.get_parent()
            while(parent is not None):
                parent.increment_height()
                parent = parent.get_parent()



if __name__ == "__main__":
    avl = AVL()
    avl.insert(43)
    print(avl)