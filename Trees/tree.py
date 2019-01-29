class TreeNode:
    def __init__(self, item=None):
        self.data = item
        self.children = []

    def __repr__(self):
        return "Node: {}".format(self.data)


class Tree:
    def __init__(self, item=None):
        self.root = TreeNode(item)





if __name__ == "__main__":
    # create simple tree
    print(t.root.children)
