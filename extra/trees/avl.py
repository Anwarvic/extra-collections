from extra.trees.bst import BSTNode, BST



class AVLnode(BSTNode):
    def __init__(self, value):
        super().__init__(value)
        self._height = 0
    

    def get_height(self):
        return self._height
    

    def increment_height(self):
        self._height += 1
    
    
    def decrement_height(self):
        self._height -= 1