from binary_tree import BinaryTree


class TreeNode():
    def __init__(self, value):
        assert type(value) in {int, float}, "BST contains only numbers!!"
        self.data = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)



class BST(BinaryTree):
    def __init__(self, value):
        if type(value) == list:
            lst = sorted(value)
            self.root = self.__init_bst(lst)
        else:
            self.root = TreeNode(value)

    def __init_bst(self, lst):
        length = len(lst)
        if length == 1:
            parent = TreeNode(lst[0])
        elif length == 2:
            parent = TreeNode(lst[0])
            parent.left = TreeNode(lst[1])
        else:
            mid_idx = len(lst)//2
            parent = TreeNode(lst[mid_idx])
            parent.left = self.__init_bst(lst[0:mid_idx])
            parent.right = self.__init_bst(lst[mid_idx+1:])
        return parent


    ############################## INSERTION ##############################
    def insert(self, value):
        pass







if __name__ == "__main__":
    # initialize tree by numbers
    tree = BST(4)

    # initialize tree by list
    lst = [7,10,12,22,30,11,19,25,9,20,14]
    btree = BST(lst)
    print(btree.root.right.right.left)
    print("Tree Nodes:", len(btree))
    print("Tree Height:", btree.get_height())
    print("Tree Depth:", btree.get_depth())
    print("Balanced Tree:", btree.is_balanced())
    print(btree.traverse())
