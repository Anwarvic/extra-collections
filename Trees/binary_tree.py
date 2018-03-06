class TreeNode():
    def __init__(self, value):
        assert value != None, "You can't use None as a value!!"
        self.data = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)
        
    def is_leaf(self):
        return self.left == self.right == None

    def has_one_child(self):
        return (self.left==None or self.right==None) and self.left!=self.right




class BinaryTree():
    def __init__(self, value):
        if type(value) == list:
            self.root = self.__create_subtree(value)
        else:
            self.root = TreeNode(value)


    ############################ PRINT ############################
    def __print_subtree(self, start_node):
        out = []
        node = str(start_node.data)
        # left_branch
        left_node = str(start_node.left) if start_node.left else ''
        left_margin = len(left_node)//2

        # right_branch
        right_node = str(start_node.right) if start_node.right else ''
        right_margin = len(right_node)//2

        # levels
        first_line = (' '*left_margin) + '┌' + ('─'*left_margin) \
                   + node \
                   + ('─'*right_margin) + '┬'
        out.append(first_line)
        if start_node.left or start_node.right:
            second_line = (' '*left_margin) + '│' + (' '*left_margin) \
                        + (' '*len(node)) \
                        + (' '*right_margin) + '│'
            third_line = left_node + (' '*(len(node)+right_margin)) + right_node
            print("HERE", third_line)
            out.extend([second_line, third_line])
        return "\n".join(out)

    def __repr__(self):
        return self.__print_subtree(self.root)


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
        left_depth = 1 if self.root.left != None else 0
        left_depth += self.__get_depth(self.root.left)
        right_depth = 1 if self.root.right != None else 0
        right_depth += self.__get_depth(self.root.right)
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


    ########################### LEAF NODES ###########################
    def __count_leaf_nodes(self, start_node):
        total_nodes = 0
        if start_node != None:
            if start_node.is_leaf():
                total_nodes += 1
            if start_node.left:
                total_nodes += self.__count_leaf_nodes(start_node.left)
            if start_node.right:
                total_nodes += self.__count_leaf_nodes(start_node.right)
        return total_nodes

    def count_leaf_nodes(self):
        return self.__count_leaf_nodes(self.root)


    ############################## NODES ##############################
    def __get_nodes_per_level(self, start_node, level, level_nodes):
        if start_node != None:
            if level == len(level_nodes):
                level_nodes.append([])
            level_nodes[level].append(start_node)
            if start_node.left:
                self.__get_nodes_per_level(start_node.left,
                                           level+1,
                                           level_nodes)
            if start_node.right:
                self.__get_nodes_per_level(start_node.right,
                                           level+1,
                                           level_nodes)
        return level_nodes

    def get_nodes(self):
        return self.__get_nodes_per_level(self.root, 0, [])


    ######################### Pre-Order TRAVERSE #########################
    def __preorder_traverse(self, start_node):
        nodes = []
        if start_node != None:
            nodes.append(start_node.data)
            if start_node.left:
                nodes.extend(self.__preorder_traverse(start_node.left))
            if start_node.right:
                nodes.extend(self.__preorder_traverse(start_node.right))
        return nodes

    def preorder_traverse(self):
        return self.__preorder_traverse(self.root)

    def depth_first_traverse(self):
        return self.__preorder_traverse(self.root)


    ######################### Post-Order TRAVERSE #########################
    def __postorder_traverse(self, start_node):
        nodes = []
        if start_node != None:
            if start_node.left:
                nodes.extend(self.__postorder_traverse(start_node.left))
            if start_node.right:
                nodes.extend(self.__postorder_traverse(start_node.right))
            nodes.append(start_node.data)
        return nodes

    def postorder_traverse(self):
        return self.__postorder_traverse(self.root)


    ######################### In-Order TRAVERSE #########################
    def __inorder_traverse(self, start_node):
        nodes = []
        if start_node != None:
            if start_node.left:
                nodes.extend(self.__inorder_traverse(start_node.left))
            nodes.append(start_node.data)
            if start_node.right:
                nodes.extend(self.__inorder_traverse(start_node.right))
        return nodes

    def inorder_traverse(self):
        return self.__inorder_traverse(self.root)


    #################### breadth-first TRAVERSE ####################
    def breadth_first_traverse(self):
        output = []
        for nodes in self.get_nodes():
            output.extend(nodes)
        return output


    ############################## TRAVERSE ##############################
    def traverse(self, method='inorder'):
        trav_methods = {"inorder", "postorder", "preorder", "depth-first", \
                        "breadth-first"}
        method = method.lower()
        if method == 'inorder':
            return self.inorder_traverse()
        elif method == 'postorder':
            return self.postorder_traverse()
        elif method in {"preorder", "depth-first"}:
            return self.preorder_traverse()
        elif method == "breadth-first":
            return self.breadth_first_traverse()
        else:
            raise AssertionError("given method must be one of these: " \
                                                        + str(trav_methods))


    ############################## PARSE ##############################
    def __create_subtree(self, lst):
        if type(lst) == list:
            if len(lst) == 1:
                parent = TreeNode(lst[0])
            elif len(lst) == 2:
                parent = TreeNode(lst[0])
                parent.left = self.__create_subtree(lst[1])
            elif len(lst) == 3:
                parent = TreeNode(lst[0])
                parent.left = self.__create_subtree(lst[1])
                parent.right = self.__create_subtree(lst[2])
            else:
                raise AssertionError("Given list can not be parsed!")
            return parent
        else:
            return TreeNode(lst)










if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    print(tree)
    # tree.root.right.right = TreeNode(7)
    # tree.root.left.left = TreeNode(4)
    # tree.root.left.right = TreeNode(5)
    # tree.root.left.left.right = TreeNode(10)
    # #################################
    # print("Tree Nodes:", len(tree))
    # print("Tree Height:", tree.get_height())
    # print("Tree Depth:", tree.get_depth())
    # print("Nodes per level:", tree.get_nodes())
    # print("Total Leaf Nodes:", tree.count_leaf_nodes())
    # print("Balanced Tree:", tree.is_balanced())
    # print("PreOrder Traverse:")
    # print(tree.preorder_traverse())
    # print("\npostOrder Traverse:")
    # print(tree.postorder_traverse())
    # print("\ninOrder Traverse:")
    # print(tree.inorder_traverse())
    # print("\nbreadth-first Traverse:")
    # print(tree.breadth_first_traverse())
    # print("\nTraverse:")
    # print(tree.traverse(method='POSTORDER'))
    # #####################################
    # lst = ["S", ["NP", ["DET", "There"]], ["S", ["VP", ["VERB", "is"], ["VP", ["NP", ["DET", "no"], ["NOUN", "asbestos"]], ["VP", ["PP", ["ADP","in"], ["NP", ["PRON", "our"]]], ["ADVP", ["ADV","now"]]]]]]]
    # tree = BinaryTree(lst)
