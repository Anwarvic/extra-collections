

class TreeNode:
    def __init__(self, value):
        assert value != '',   "TreeNode's value can't be empty string!!"
        assert value != None, "TreeNode's value can't be None!!"
        self.data = value
        self.children = []

    def get_data(self):
        return self.data

    def get_children(self):
        return self.children

    def __repr__(self):
        return "TreeNode({})".format(self.data)
    
    def __str__(self):
        return str(self.data)




class Tree:
    def __init__(self, value):
        if isinstance(value, TreeNode):
            self.root = value
        else:
            self.root = TreeNode(value)


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






if __name__ == "__main__":
    # create Simpsons tree
    root = TreeNode('TheSimpsons')
    # homer-side
    abraham = TreeNode('Abraham + Mona')
    herb = TreeNode('Herb')
    homer = TreeNode('Homer')
    abraham.children = [herb, homer]
    
    # marge-side
    jackie = TreeNode('Clancy + Jackie')
    marge = TreeNode('Marge')
    patty = TreeNode('Patty')
    selma = TreeNode('Selma')
    ling = TreeNode('Ling')
    selma.children = [ling]
    jackie.children = [marge, patty, selma]

    # homer-marge children
    bart = TreeNode('Bart')
    lisa = TreeNode('Lisa')
    maggie = TreeNode('Maggie')
    homer.children = [bart, lisa, maggie]
    marge.children = homer.children
    # set root
    root.children = [abraham, jackie]
    t = Tree(root)
    print(t)
    print(len(t))