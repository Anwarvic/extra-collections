from random import randint
from bst import TreeNode, BST


class TreeNode(TreeNode):
	def __init__(self, key):
        super().__init__(key)
        self.priority = randint(-1000, 1000)



class Treap(BST):
	pass



if __name__ == "__main__":
    t = Treap(1)