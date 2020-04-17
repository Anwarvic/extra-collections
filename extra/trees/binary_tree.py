import warnings
from extra.trees.tree import TreeNode, Tree




class BinaryTreeNode(TreeNode):
    def __name__(self):
        return "extra.BinaryTreeNode()"
    
    
    def __init__(self, value):
        super().__init__(value)
        self._left = self._right = None
        del self._children


    def get_left(self):
        return self._left


    def get_right(self):
        return self._right


    def get_children(self):
        children = []
        if self._left is not None: children.append(self._left)
        if self._right is not None: children.append(self._right)
        return children


    def set_children(self, lst):
        raise NotImplementedError(\
            "You can use set_left() or set_right() methods instead!!")


    def set_left(self, new_node):
        if not isinstance(new_node, BinaryTreeNode):
            raise TypeError(\
            f"You can't set a child unless it's an {self.__name__()} object!!")
        self._left = new_node


    def set_right(self, new_node):
        if not isinstance(new_node, BinaryTreeNode):
            raise TypeError(\
            f"You can't set a child unless it's an {self.__name__()} object!!")
        self._right = new_node
        

    def has_one_child(self):
        return not super().is_leaf() \
                and (self._left is None or self._right is None)


    def __repr__(self):
        return f"BinaryTreeNode({self._data})"


    def _represent(self):
        #represents BinaryTreeNode when being printed within a tree
        return str(self._data)




class BinaryTree(Tree):
    def __name__(self):
        return "extra.BinaryTree()"
    

    @staticmethod
    def __create_subtree(lst):
        if type(lst) not in {list, tuple}: lst = [lst]
        if len(lst) == 0 or len(lst) >= 4:
            raise ValueError(f"Given {type(lst)} can not be parsed!!")
        try:
            parent = BinaryTreeNode(lst[0])
            parent.set_left( BinaryTree.__create_subtree(lst[1]) )
            parent.set_right( BinaryTree.__create_subtree(lst[2]) )
        except IndexError:
            pass
        return parent


    @staticmethod
    def parse(lst):
        if type(lst) not in {list, tuple}:
            raise TypeError("Given object must be a `list` or `tuple`!!")
        bt = BinaryTree()
        bt._root = BinaryTree.__create_subtree(lst)
        return bt


    ##############################     PRINT      ##############################
    def __print_subtree(self, root, curr_index):
        """
        src: https://github.com/joowani/binarytree/blob/master/binarytree
        """
        if root is None:
            return [], 0, 0, 0
        else:
            line1 = []
            line2 = []
            node_repr = root._represent()
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


    def _print_empty_tree(self):
        return "/ \\"


    def __repr__(self):
        if self.is_empty():
            return self._print_empty_tree()
        lines, _, _, _ = self.__print_subtree(self._root, 0)
        return '\n'.join((line.rstrip() for line in lines[:-1]))


    ##############################    BALANCED    ##############################
    def is_balanced(self):
        """
        BinaryTree is balanced if the difference between the depth of any
        two leaf nodes is less than or equal one.
        """
        if self.is_empty():
            warnings.warn(\
                f"You are checking the balance of an empty {self.__name__()}",
                UserWarning)
            return True
        left_depth = 0 if self._root.get_left() is None \
                        else 1 + super()._get_depth(self._root.get_left()) 
        right_depth = 0 if self._root.get_right() is None \
                        else 1 + super()._get_depth(self._root.get_right()) 
        return abs(left_depth - right_depth) <= 1


    ##############################    PERFECT     ##############################
    def is_perfect(self):
        """
        BinaryTree is perfect if all its levels are completely filled.
        """
        if self.is_empty():
            warnings.warn(\
                f"You are checking the perfection of an empty {self.__name__()}",
                UserWarning)
            return True
        for level, nodes in enumerate(self.get_nodes()):
            if 2**level != len(nodes):
                return False
        return True


    ##############################     STRICT     ##############################
    def __is_subtree_strict(self, start_node):
        assert start_node is None or isinstance(start_node, BinaryTreeNode)
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
        if self.is_empty():
            warnings.warn(\
                f"You are checking the strictness of an empty {self.__name__()}",
                UserWarning)
            return True
        return self.__is_subtree_strict(self._root)


    ##############################   Pre-Order    ##############################
    def __preorder_traverse(self, start_node):
        assert start_node is None or isinstance(start_node, BinaryTreeNode)
        nodes = []
        if start_node != None:
            nodes.append(start_node.get_data())
            if start_node.get_left():
                nodes.extend(self.__preorder_traverse(start_node.get_left()))
            if start_node.get_right():
                nodes.extend(self.__preorder_traverse(start_node.get_right()))
        return nodes


    def preorder_traverse(self):
        return self.__preorder_traverse(self._root)


    def depth_first_traverse(self):
        return self.__preorder_traverse(self._root)


    ##############################   Post-Order   ##############################
    def __postorder_traverse(self, start_node):
        assert start_node is None or isinstance(start_node, BinaryTreeNode)
        nodes = []
        if start_node != None:
            if start_node.get_left():
                nodes.extend(self.__postorder_traverse(start_node.get_left()))
            if start_node.get_right():
                nodes.extend(self.__postorder_traverse(start_node.get_right()))
            nodes.append(start_node.get_data())
        return nodes


    def postorder_traverse(self):
        return self.__postorder_traverse(self._root)


    ##############################    In-Order    ##############################
    def __inorder_traverse(self, start_node):
        assert start_node is None or isinstance(start_node, BinaryTreeNode)
        nodes = []
        if start_node != None:
            if start_node.get_left():
                nodes.extend(self.__inorder_traverse(start_node.get_left()))
            nodes.append(start_node.get_data())
            if start_node.get_right():
                nodes.extend(self.__inorder_traverse(start_node.get_right()))
        return nodes


    def inorder_traverse(self):
        return self.__inorder_traverse(self._root)


    ##############################  BREADTH-FIRST ##############################
    def breadth_first_traverse(self):
        return super().to_list()


    ##############################    TRAVERSE    ##############################
    def traverse(self, method='inorder'):
        trav_methods = {"inorder", "postorder", "preorder", "depth-first",
                        "breadth-first"}
        if type(method) != str:
            raise TypeError("Given traverse method has to be one of these:\n"+\
                        str(trav_methods))
        # traverse based on given method
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
            raise ValueError("Given traverse method has to be one of these:\n"+\
                        str(trav_methods))


