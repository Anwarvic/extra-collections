import os


class TreeNode:
    def __name__(self):
        return "extra.TreeNode()"
    

    def __init__(self, value):
        if value is None:
            raise ValueError(\
                f"Can't use `None` as an initial value for {self.__name__()}!!")
        elif type(value) == str and value.strip() == '':
            raise ValueError("Can't use an empty string as an initial "+\
                f"value for {self.__name__()}!!")
        elif isinstance(value, TreeNode):
            raise ValueError("Can't create nested TreeNodes!!")
        self.data = value
        self.children = []


    def get_data(self):
        return self.data


    def get_children(self):
        return self.children
    

    def set_child(self, child):
        assert isinstance(child, TreeNode)
        self.children.append(child)
    
    
    def set_children(self, lst):
        self.children = [item if isinstance(item, TreeNode) else TreeNode(item)\
            for item in lst]
    

    def is_leaf(self):
        return self.get_children() == []
        

    def __repr__(self):
        return f"TreeNode({self.data})"


    @staticmethod
    def swap(node1, node2):
        assert isinstance(node1, TreeNode)
        assert isinstance(node1, TreeNode)
        node1.data, node2.data = node2.data, node1.data




class Tree:
    def __name__(self):
        return "extra.Tree()"
    

    def __init__(self, value):
        if isinstance(value, TreeNode):
            self.root = value
        else:
            self.root = TreeNode(value)
    

    @staticmethod
    def __form_tree_from_path(parent_abs_path, curr_folder):
        node = TreeNode(curr_folder)
        abs_path = os.path.join(parent_abs_path, curr_folder)
        if os.path.isdir(abs_path):
            for child in sorted( os.listdir(abs_path) ):
                node.set_child(Tree.__form_tree_from_path(abs_path, child))
        return node


    @staticmethod
    def from_path(path):
        abs_path = os.path.abspath(path)
        parent, folder = os.path.split(abs_path)
        root = Tree.__form_tree_from_path(parent, folder)
        return Tree(root)


    ##############################     LENGTH     ##############################
    def __count_nodes(self, start_node):
        assert start_node is None or isinstance(start_node, TreeNode)
        total_nodes = 0
        if start_node != None:
            total_nodes += 1
            for child in start_node.get_children():
                total_nodes += self.__count_nodes(child)
        return total_nodes


    def __len__(self):
        return self.__count_nodes(self.root)


    ##############################     PRINT      ##############################
    def __print_subtree(self, start_node, lines, is_last_child, seq=[]):
        """
        seq (list): is a boolean list containing values
        """
        line = []
        if seq:
            for is_parent_last_child in seq[1:]:
                line.append('  ') if is_parent_last_child else line.append('│ ')
            line.append('└─') if is_last_child else line.append('├─')
            line.append('┬ ')if start_node.get_children() else line.append('─ ')
        line.append(str(start_node.get_data()))
        lines.append("".join(line))
        # append node status
        my_seq = seq.copy()
        my_seq.append(is_last_child)
        # iterate over children
        children = start_node.get_children()
        num_children = len(children)
        for idx in range(num_children):
            child = children[idx]
            is_last_child = True if idx == num_children-1 else False
            self.__print_subtree(child, lines, is_last_child, my_seq)
        return lines


    def __repr__(self):
        if self.root.get_children():
            return "\n".join(self.__print_subtree(self.root, [], False))
        else:
            return str(self.root.get_data())


    ##############################  HEIGHT/DEPTH  ##############################
    def _get_depth(self, start_node):
        assert start_node is None or isinstance(start_node, TreeNode)
        depth = 0
        for child in start_node.get_children():
            depth = max(depth, 1 + self._get_depth(child))
        return depth


    def get_depth(self):
        return self._get_depth(self.root)
    

    def get_height(self):
        return self._get_depth(self.root)
    

    ##############################   LEAF NODES   ##############################
    def __count_leaf_nodes(self, start_node):
        assert start_node is None or isinstance(start_node, TreeNode)
        total_nodes = 0
        if start_node != None:
            if start_node.is_leaf():
                total_nodes += 1
            for child in start_node.get_children():
                total_nodes += self.__count_leaf_nodes(child)
        return total_nodes


    def count_leaf_nodes(self):
        return self.__count_leaf_nodes(self.root)


    ##############################      ITER      ##############################
    def __iter__(self):
        current_nodes = [self.root]
        while len(current_nodes) > 0:
            next_nodes = []
            for node in current_nodes:
                yield node
                next_nodes.extend(node.get_children())
            current_nodes = next_nodes


    def to_list(self):
        return [node.get_data() for node in self]





if __name__ == "__main__":
    t = Tree.from_path("./extra/trees/")
    print(t)
    print(t.get_depth())
    print(len(t))
    print(t.count_leaf_nodes())
    for i in t:
        print(i)