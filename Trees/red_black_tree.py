from bst import TreeNode, BST


class TreeNode(TreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.color = 0 #0 for black, 1 for one


class RedBlackTree(BST):
    pass


if __name__ == "__main__":
    rbt = RedBlackTree(1)
    print(rbt)