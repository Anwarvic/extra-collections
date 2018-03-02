from binary_tree import BinaryTree


class TreeNode():
    def __init__(self, value):
        assert type(value) in {int, float}, "BST contains only numbers!!"
        self.data = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

    def is_leaf(self):
        return self.left == self.right == None


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


    ############################## MAX/MIN ##############################
    def __get_max_node(self, start_node):
        if start_node.right == None:
            return start_node
        else:
            return self.__get_max_node(start_node.right)

    def get_max(self):
        return self.__get_max_node(self.root)


    ############################## INSERTION ##############################
    def __insert(self, value, start_node):
        if value == start_node.data:
            return
        elif value < start_node.data:
            if start_node.left:
                self.__insert(value, start_node.left)
            else:
                start_node.left = TreeNode(value)
        else:
            if start_node.right:
                self.__insert(value, start_node.right)
            else:
                start_node.right = TreeNode(value)

    def insert(self, value):
        assert type(value) in {int, float}, "You can insert only numbers!"
        self.__insert(value, self.root)


    ############################## SEARCH ##############################
    def __search(self, find_val, start_node):
        if find_val == start_node.data:
            return True
        elif find_val < start_node.data:
            if start_node.left:
                return self.__search(find_val, start_node.left)
            else:
                return False
        else:
            if start_node.right:
                return self.__search(find_val, start_node.right)
            else:
                return False

    def search(self, find_val):
        assert type(find_val) in {int, float}, "You can insert only numbers!"
        return self.__search(find_val, self.root)







if __name__ == "__main__":
    # initialize tree by numbers
    btree = BST(4)
    # Insert elements
    btree.insert(2)
    btree.insert(1)
    btree.insert(3)
    btree.insert(5)
    print(btree.search(1))
    print(btree.search(100))
    # initialize tree by list
    # lst = [7,10,12,22,30,11,19,25,9,20,14]
    # btree = BST(lst)
    # print(btree.root.right.right.left)
    print("Tree Nodes:", len(btree))
    print("Tree Height:", btree.get_height())
    print("Tree Depth:", btree.get_depth())
    print("Balanced Tree:", btree.is_balanced())
    print(btree.traverse())
    print("Max value:", btree.get_max())
