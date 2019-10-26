from abc import abstractmethod
from tree import TreeNode




class TreeNode(TreeNode):
    def __init__(self, value):
        assert value != None, "You can't use None as a value!!"
        self.data = value
        self.left = self.right = None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_children(self):
        children = []
        if self.left != None: children.append(self.left)
        if self.right != None: children.append(self.right)
        return children

    def set_left(self, new_node):
        self.left = new_node

    def set_right(self, new_node):
        self.right = new_node
        
    def is_leaf(self):
        return self.left == self.right == None

    def has_one_child(self):
        return not self.is_leaf() \
                and (self.left is None or self.right is None)

    @abstractmethod
    def swap(node1, node2):
        node1.data, node2.data = node2.data, node1.data




class BinaryTree:
    def __init__(self, value):
        if isinstance(value, TreeNode):
            self.root = value
        elif hasattr(value, '__iter__'):
            self.root = self.__create_subtree(value)
        else:
            self.root = TreeNode(value)


    ############################ PRINT ############################
    def __print_subtree(self, root, curr_index):
        """
        src: https://github.com/joowani/binarytree/blob/master/binarytree
        """
        if root is None:
            return [], 0, 0, 0
        else:
            line1 = []
            line2 = []
            node_repr = str(root)
            new_root_width = gap_size = len(node_repr)

            # Get the left and right sub-boxes, their widths, and root repr positions
            l_box, l_box_width, l_root_start, l_root_end = \
                self.__print_subtree(root.get_left(), 2 * curr_index + 1)
            r_box, r_box_width, r_root_start, r_root_end = \
                self.__print_subtree(root.right, 2 * curr_index + 2,)

            # Draw the branch connecting the current root node to the left sub-box
            # Pad the line with whitespaces where necessary
            if l_box_width > 0:
                l_root = (l_root_start + l_root_end) // 2 + 1
                line1.append(' ' * (l_root + 1))
                line1.append('_' * (l_box_width - l_root))
                line2.append(' ' * l_root + '/')
                line2.append(' ' * (l_box_width - l_root))
                new_root_start = l_box_width + 1
                gap_size += 1
            else:
                new_root_start = 0

            # Draw the representation of the current root node
            line1.append(node_repr)
            line2.append(' ' * new_root_width)

            # Draw the branch connecting the current root node to the right sub-box
            # Pad the line with whitespaces where necessary
            if r_box_width > 0:
                r_root = (r_root_start + r_root_end) // 2
                line1.append('_' * r_root)
                line1.append(' ' * (r_box_width - r_root + 1))
                line2.append(' ' * r_root + '\\')
                line2.append(' ' * (r_box_width - r_root))
                gap_size += 1
            new_root_end = new_root_start + new_root_width - 1

            # Combine the left and right sub-boxes with the branches drawn above
            gap = ' ' * gap_size
            new_box = [''.join(line1), ''.join(line2)]
            for i in range(max(len(l_box), len(r_box))):
                l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
                r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
                new_box.append(l_line + gap + r_line)

            # Return the new box, its width and its root repr positions
            return new_box, len(new_box[0]), new_root_start, new_root_end


    def __repr__(self):
        lines, _, _, _ = self.__print_subtree(self.root, 0)
        return '\n'.join((line.rstrip() for line in lines[:-1]))


    ######################### HEIGHT/DEPTH #########################
    def _get_depth(self, start_node):
        if start_node is None:
            return -1
        return max( 1 + self._get_depth(start_node.get_left()), #left depth
                    1 + self._get_depth(start_node.get_right())) # right depth

    def get_height(self):
        return self._get_depth(self.root)


    ############################## BALANCED ##############################
    def is_balanced(self):
        """
        BinaryTree is balanced if the difference between the depth of any
        two leaf nodes is less than or equal one.
        """
        left_depth = 0 if self.root.get_left() is None \
                        else 1 + self._get_depth(self.root.get_left()) 
        right_depth = 0 if self.root.get_right() is None \
                        else 1 + self._get_depth(self.root.get_right()) 
        return abs(left_depth - right_depth) <= 1


    ############################## PERFECT ##############################
    def is_perfect(self):
        """
        BinaryTree is perfect if all its levels are completely filled.
        """
        for level, nodes in enumerate(self.get_nodes()):
            if 2**level != len(nodes):
                return False
        return True


    ############################## STRICT ##############################
    def __is_subtree_strict(self, start_node):
        left_node = start_node.get_left()
        right_node = start_node.get_right()

        if left_node is None and right_node is None:
            return True
        elif left_node is not None and right_node is None:
            return False
        elif left_node is None and right_node is not None:
            return False
        else:
            return self.__is_subtree_strict(start_node.get_left()) and \
                    self.__is_subtree_strict(start_node.get_right())

    def is_strict(self):
        """
        BinaryTree is strict if all its non-leaf nodes has left and right
        children.
        """
        return self.__is_subtree_strict(self.root)


    ############################## LENGTH ##############################
    def __count_nodes(self, start_node):
        total_nodes = 0
        if start_node != None:
            total_nodes += 1
            if start_node.get_left():
                total_nodes += self.__count_nodes(start_node.get_left())
            if start_node.get_right():
                total_nodes += self.__count_nodes(start_node.get_right())
        return total_nodes

    def __len__(self):
        return self.__count_nodes(self.root)


    ########################### LEAF NODES ###########################
    def __count_leaf_nodes(self, start_node):
        total_nodes = 0
        if start_node != None:
            if start_node.is_leaf():
                total_nodes += 1
            if start_node.get_left():
                total_nodes += self.__count_leaf_nodes(start_node.get_left())
            if start_node.get_right():
                total_nodes += self.__count_leaf_nodes(start_node.get_right())
        return total_nodes

    def count_leaf_nodes(self):
        return self.__count_leaf_nodes(self.root)


    ############################## NODES ##############################
    def __iter__(self):
        current_nodes = [self.root]
        while len(current_nodes) > 0:
            next_nodes = []
            for node in current_nodes:
                yield node
                if node.get_left() != None:
                    next_nodes.append(node.get_left())
                if node.get_right() != None:
                    next_nodes.append(node.get_right())
            current_nodes = next_nodes


    ######################### Pre-Order TRAVERSE #########################
    def __preorder_traverse(self, start_node):
        nodes = []
        if start_node != None:
            nodes.append(start_node.get_data())
            if start_node.get_left():
                nodes.extend(self.__preorder_traverse(start_node.get_left()))
            if start_node.get_right():
                nodes.extend(self.__preorder_traverse(start_node.get_right()))
        return nodes

    def preorder_traverse(self):
        return self.__preorder_traverse(self.root)

    def depth_first_traverse(self):
        return self.__preorder_traverse(self.root)


    ######################### Post-Order TRAVERSE #########################
    def __postorder_traverse(self, start_node):
        nodes = []
        if start_node != None:
            if start_node.get_left():
                nodes.extend(self.__postorder_traverse(start_node.get_left()))
            if start_node.get_right():
                nodes.extend(self.__postorder_traverse(start_node.get_right()))
            nodes.append(start_node.get_data())
        return nodes

    def postorder_traverse(self):
        return self.__postorder_traverse(self.root)


    ######################### In-Order TRAVERSE #########################
    def __inorder_traverse(self, start_node):
        nodes = []
        if start_node != None:
            if start_node.get_left():
                nodes.extend(self.__inorder_traverse(start_node.get_left()))
            nodes.append(start_node.get_data())
            if start_node.get_right():
                nodes.extend(self.__inorder_traverse(start_node.get_right()))
        return nodes

    def inorder_traverse(self):
        return self.__inorder_traverse(self.root)


    #################### breadth-first TRAVERSE ####################
    def breadth_first_traverse(self):
        return [tree_node.get_data() for tree_node in self]


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

    ############################## NODES ##############################
    def __get_nodes_per_level(self, start_node, level, level_nodes):
        if start_node != None:
            if level == len(level_nodes):
                level_nodes.append([])
            level_nodes[level].append(start_node)
            if start_node.get_left():
                self.__get_nodes_per_level(start_node.get_left(),
                                           level+1,
                                           level_nodes)
            if start_node.get_right():
                self.__get_nodes_per_level(start_node.get_right(),
                                           level+1,
                                           level_nodes)
        return level_nodes

    def get_nodes(self):
        return self.__get_nodes_per_level(self.root, 0, [])

    ############################## PARSE ##############################
    def __create_subtree(self, lst):
        if type(lst) == list:
            if len(lst) == 1:
                parent = TreeNode(lst[0])
            elif len(lst) == 2:
                parent = TreeNode(lst[0])
                parent.set_left( self.__create_subtree(lst[1]) )
            elif len(lst) == 3:
                parent = TreeNode(lst[0])
                parent.set_left( self.__create_subtree(lst[1]) )
                parent.set_right( self.__create_subtree(lst[2]) )
            else:
                raise AssertionError("Given list can not be parsed!")
            return parent
        else:
            return TreeNode(lst)










if __name__ == "__main__":
    # create tree using TreeNode
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(1)
    root.right = TreeNode(20)
    btree = BinaryTree(root)
    print(btree)
    print('='*50)
    ##############################
    btree = BinaryTree(1)
    btree.root.left = TreeNode(2)
    btree.root.right = TreeNode(3)
    btree.root.right.left = TreeNode(6)
    btree.root.right.right = TreeNode(7)
    btree.root.left.left = TreeNode(4)
    btree.root.left.right = TreeNode(5)
    # btree.root.left.left.left = TreeNode(100)
    print(btree)
    #################################
    print("Tree Nodes:", len(btree))
    print("Tree Height:", btree.get_height())
    print("Left-tree Node:", btree.root.left)
    print("Left-node Depth:", btree._get_depth(btree.root.left))
    print("Nodes per level:", btree.get_nodes())
    print("Iterate over given tree:")
    for node in btree:
        print('\t', node)
    print("Total Leaf Nodes:", btree.count_leaf_nodes())
    print("Balanced Tree:", btree.is_balanced())
    print("Perfect Tree:", btree.is_perfect())
    print("Strict Tree:", btree.is_strict())
    print("PreOrder Traverse:")
    print(btree.preorder_traverse())
    print("\npostOrder Traverse:")
    print(btree.postorder_traverse())
    print("\ninOrder Traverse:")
    print(btree.inorder_traverse())
    print("\nbreadth-first Traverse:")
    print(btree.breadth_first_traverse())
    print("\nTraverse:")
    print(btree.traverse())
    #####################################
    # lst = ["S", ["NP", ["DET", "There"]], ["S", ["VP", ["VERB", "is"], ["VP", ["NP", ["DET", "no"], ["NOUN", "asbestos"]], ["VP", ["PP", ["ADP","in"], ["NP", ["PRON", "our"]]], ["ADVP", ["ADV","now"]]]]]]]
    # btree = BinaryTree(lst)
    # print(btree)
