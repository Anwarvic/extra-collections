from binary_tree import TreeNode, BinaryTree


class TreeNode(TreeNode):
    def __init__(self, value):
        assert type(value) in {int, float}, "BST contains only numbers!!"
        self.data = value
        self.left = None
        self.right = None


class BST(BinaryTree):
    def __init__(self, value):
        if isinstance(value, TreeNode):
            self.root = value
        elif type(value) == list:
            lst = sorted(value)
            self.root = self.__init_bst(lst)
        else:
            self.root = TreeNode(value)

    def __init_bst(self, lst):
        length = len(lst)
        assert length >0, "Given List must have values!!"
        if length == 1:
            node = TreeNode(lst[0])
        elif length == 2:
            node = TreeNode(lst[0])
            node.left = TreeNode(lst[1])
        else:
            mid_idx = len(lst)//2
            node = TreeNode(lst[mid_idx])
            node.left = self.__init_bst(lst[0:mid_idx])
            node.right = self.__init_bst(lst[mid_idx+1:])
        return node


    ############################## MAX/MIN ##############################
    def __get_max_node(self, start_node):
        # get the right-most node
        if start_node.right == None:
            return start_node
        else:
            return self.__get_max_node(start_node.right)

    def get_max(self):
        max_node = self.__get_max_node(self.root)
        return max_node.data

    def __get_min_node(self, start_node):
        # get the left-most node
        if start_node.left == None:
            return start_node
        else:
            return self.__get_min_node(start_node.left)

    def get_min(self):
        min_node = self.__get_min_node(self.root)
        return min_node.data


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

    def __contains__(self, find_val):
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
            if not start_node.left:
                # raise ValueError("Couldn't find given value in the tree!!")
                pass
            else:
                self.__remove(del_value, start_node, start_node.left)
        else:
            if not start_node.right:
                # raise ValueError("Couldn't find given value in the tree!!")
                pass
            else:
                self.__remove(del_value, start_node, start_node.right)


    def remove(self, del_value):
        assert type(del_value) in {int, float}, "BST conains numbers only!"
        if self.root.is_leaf() and del_value == self.root.data:
            raise ValueError("Can't remove the only item in the tree!")
        self.__remove(del_value, None, self.root)









if __name__ == "__main__":
    bst = BST(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    print(bst)
    print(1 in bst)
    print(100 in bst)
    print('='*50)
    #######################################
    # initialize tree by list
    lst = [7,10,12,22,30,11,19,25,9,20,14]
    bst = BST(lst)
    print(bst)
    print('='*50)
    #######################################
    # example taken from "Data Structures and Algorithms in Python" book
    bst = BST(44)
    bst.root.left = TreeNode(17)
    bst.root.left.left = TreeNode(8)
    bst.root.left.right = TreeNode(32)
    bst.root.left.right.left = TreeNode(28)
    bst.root.left.right.left.right = TreeNode(29)
    bst.root.right = TreeNode(88)
    bst.root.right.right = TreeNode(97)
    bst.root.right.right.left = TreeNode(93)
    bst.root.right.left = TreeNode(65)
    bst.root.right.left.left = TreeNode(54)
    bst.root.right.left.right = TreeNode(82)
    bst.root.right.left.right.left = TreeNode(76)
    bst.root.right.left.right.left.left = TreeNode(68)
    bst.root.right.left.right.left.right = TreeNode(80)
    print(bst)

    bst.remove(32)
    bst.remove(44)
    bst.remove(4000)
    print(bst)

    print("Tree Root:", bst.root)
    print("Tree Nodes:", len(bst))
    print("Tree Height:", bst.get_height())
    print("Right-node Depth:", bst.get_depth(bst.root.right))
    print("Balanced Tree:", bst.is_balanced())
    print(bst.traverse())
    print("Min value:", bst.get_min())
    print("Max value:", bst.get_max())
