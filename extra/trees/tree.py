import os


class TreeNode:
    def __init__(self, value):
        if value is None:
            raise TypeError("TreeNode's value can't be `None`!!")
        elif type(value) == str and value.strip() == '':
            raise ValueError("TreeNode's value can't be an empty string!!")
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
        

    def __repr__(self):
        return f"TreeNode({self.data})"
    

    def __str__(self):
        return str(self.data)




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


    ############################ LENGTH ############################
    def __get_length(self, curr_node):
        length = 1
        for child in curr_node.get_children():
            length += self.__get_length(child)
        return length


    def __len__(self):
        return self.__get_length(self.root)


    ############################ PRINT ############################
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
        line.append(str(start_node))
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
            return str(self.root)








    