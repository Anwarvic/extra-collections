class TreeNode():
    def __init__(self, value):
        assert type(value) in {int, float}, "BST contains only numbers!!"
        self.number = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.number)



class BST:
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


    ######################### HEIGHT/DEPTH #########################
    def __get_height(self, start_node):
        height = 0
        if start_node != None:
            left_height, right_height = 0, 0
            if start_node.left:
                left_height = 1 + self.__get_height(start_node.left)
            if start_node.right:
                right_height = 1 + self.__get_height(start_node.right)
            height += max(left_height, right_height)
            # print(start_node.data, left_height, right_height)
        return height

    def __get_depth(self, start_node):
        return self.__get_height(start_node)

    def get_height(self):
        return self.__get_height(self.root)

    def get_depth(self):
        return self.get_height()


    ############################## BALANCED ##############################
    def is_balanced(self):
        """
        Tree is said to be balanced if the difference between the depth of any
        two leaf nodes is one or less.
        """
        left_depth = self.__get_depth(self.root.left)
        right_depth = self.__get_depth(self.root.right)
        return abs(left_depth - right_depth) <= 1


    ############################## LENGTH ##############################
    def __count_nodes(self, start_node):
        total_nodes = 0
        if start_node != None:
            total_nodes += 1
            if start_node.left:
                total_nodes += self.__count_nodes(start_node.left)
            if start_node.right:
                total_nodes += self.__count_nodes(start_node.right)
        return total_nodes

    def __len__(self):
        return self.__count_nodes(self.root)





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
