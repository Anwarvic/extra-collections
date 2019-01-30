class TreeNode:
    def __init__(self, value=None):
        assert value != None, "You can't use None as a value!!"
        self.data = value
        self.children = []

    def __repr__(self):
        return "TreeNode({})".format(self.data)

    def get_children(self):
        return self.children



class Tree:
    def __init__(self, value=None):
        if isinstance(value, TreeNode):
            self.root = value
        else:
            self.root = TreeNode(value)


    ############################ PRINT ############################
    def __print_subtree(self, start_node, level, lines, is_last_child):
        line = []
        if level != 0:
            line.append((level-1)*'│ ')
            line.append('└─') if is_last_child else line.append('├─')
            line.append('┬ ') if start_node.children else line.append('─ ')
        line.append(start_node.data)
        lines.append("".join(line))
        # iterate over children
        children = start_node.get_children()
        num_children = len(children)
        for idx in range(num_children):
            child = children[idx]
            is_last_child = True if idx == num_children-1 else False
            self.__print_subtree(child, level+1, lines, is_last_child)
        return lines


    def __repr__(self):
        if self.root.children:
            return "\n".join(self.__print_subtree(self.root, 0, [], False))
        else:
            return self.root.data







if __name__ == "__main__":
    # create simple tree
    a = TreeNode('A')
    b = TreeNode('B')
    c = TreeNode('C')
    d = TreeNode('D')
    e = TreeNode('E')
    f = TreeNode('F')
    g = TreeNode('G')
    h = TreeNode('H')
    i = TreeNode('I')
    j = TreeNode('J')
    z = TreeNode('Z')
    x = TreeNode('X')
    y = TreeNode('Y')
    a.children = [b, c, d]
    d.children = [g]
    g.children = [z]
    t = Tree(a)
    print(t)

    #  # create simple tree
    # a = TreeNode('A')
    # b = TreeNode('B')
    # c = TreeNode('C')
    # d = TreeNode('D')
    # e = TreeNode('E')
    # f = TreeNode('F')
    # g = TreeNode('G')
    # h = TreeNode('H')
    # i = TreeNode('I')
    # j = TreeNode('J')
    # h.children = [i, j]
    # b.children = [e, h, f]
    # d.children = [g]
    # a.children = [b, c ,d]

    # z = TreeNode('Z')
    # z.children = [TreeNode('X'), TreeNode('Y')]
    # c.children = [z]
    # g.children = [z]
    # t = Tree(a)
    # print(t)