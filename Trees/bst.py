class TreeNode():
    def __init__(self, value):
        assert type(value) in {int, float}, "BST contains only numbers!!"
        self.number = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)



class BST:
    def __init__(self, value):
        self.root = TreeNode(value)




if __name__ == "__main__":
    tree = BST(4)