from binary_tree import TreeNode, BinaryTree


class TreeNode(TreeNode):
    def __init__(self, value):
        assert type(value) in {int, float}, "BST contains only numbers!!"
        self.data = value
        self.left = None
        self.right = None


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

    def __get_min_node(self, start_node):
        if start_node.left == None:
            return start_node
        else:
            return self.__get_min_node(start_node.left)

    def get_min(self):
        return self.__get_min_node(self.root)


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


    ############################## REMOVAL ##############################
    def __remove(self, del_value, parent, start_node):
        # handle edge case
        if parent == None and start_node.is_leaf():
            raise ValueError("Can't remove the only item in the tree!")
        # handle general case
        if del_value == start_node.data:
            if start_node.is_leaf():
                if del_value < parent.data:
                    parent.left = None
                else:
                    parent.right = None
            elif start_node.left != None and start_node.right == None:
                if del_value < parent.data:
                    parent.left = start_node.left
                else:
                    parent.right = start_node.left
            elif start_node.left == None and start_node.right != None:
                if del_value < parent.data:
                    parent.left = start_node.right
                else:
                    parent.right = start_node.right
            else:
                replacement_node = self.__get_max_node(start_node.left)
                start_node.data = replacement_node.data
                self.__remove(replacement_node.data, start_node, start_node.left)
        elif del_value < start_node.data:
            self.__remove(del_value, start_node, start_node.left)
        else:
            self.__remove(del_value, start_node, start_node.right)


    def remove(self, del_value):
        assert type(del_value) in {int, float}, "BST conains numbers only!"
        if self.search(del_value):
            self.__remove(del_value, None, self.root)









if __name__ == "__main__":
    # btree = BST(4)
    # btree.insert(2)
    # btree.insert(1)
    # btree.insert(3)
    # btree.insert(5)
    # print(btree.search(1))
    # print(btree.search(100))
    #######################################
    # initialize tree by list
    # lst = [7,10,12,22,30,11,19,25,9,20,14]
    # btree = BST(lst)
    # print(btree.root.right.right.left)
    #######################################
    # example taken from "Data Structures and Algorithms in Python" book
    btree = BST(44)
    btree.root.left = TreeNode(17)
    btree.root.left.left = TreeNode(8)
    btree.root.left.right = TreeNode(32)
    btree.root.left.right.left = TreeNode(28)
    btree.root.left.right.left.right = TreeNode(29)
    btree.root.right = TreeNode(88)
    btree.root.right.right = TreeNode(97)
    btree.root.right.right.left = TreeNode(93)
    btree.root.right.left = TreeNode(65)
    btree.root.right.left.left = TreeNode(54)
    btree.root.right.left.right = TreeNode(82)
    btree.root.right.left.right.left = TreeNode(76)
    btree.root.right.left.right.left.left = TreeNode(68)
    btree.root.right.left.right.left.right = TreeNode(80)

    btree.remove(32)
    btree.remove(44)

    print("Tree Root:", btree.root)
    print("Tree Nodes:", len(btree))
    print("Tree Height:", btree.get_height())
    print("Tree Depth:", btree.get_depth())
    print("Balanced Tree:", btree.is_balanced())
    print(btree.traverse())
    print("Min value:", btree.get_min())
    print("Max value:", btree.get_max())
    print(btree)
