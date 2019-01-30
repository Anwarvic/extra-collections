class TreeNode:
    def __init__(self, value=None):
        assert value != None, "You can't use None as a value!!"
        self.data = value
        self.children = []

    def __repr__(self):
        return "TreeNode({})".format(self.data)



class Tree:
    def __init__(self, value=None):
        if isinstance(value, TreeNode):
            self.root = value
        else:
            self.root = TreeNode(value)


    ############################ PRINT ############################
    def __print_subtree(self, start_node, level, lines,
                        is_last_child, is_right_most_child):
        line = []
        if level != 0:
            line.append((level-1)*'│ ') if not is_right_most_child \
                                        else line.append((level-1)*'  ')
            line.append('└─') if is_last_child else line.append('├─')
            line.append('┬ ') if start_node.children else line.append('─ ')
        line.append(start_node.data)
        lines.append("".join(line))
        for idx, child in enumerate(start_node.children):
            if idx == len(start_node.children) -1:
                self.__print_subtree(child, level+1, lines, 
                                    True, is_right_most_child)
            else:
                self.__print_subtree(child, level+1, lines,
                                    False, is_right_most_child)
        return lines

    def __repr__(self):
        lines = [self.root.data]
        for idx, child in enumerate(self.root.children):
            if idx == len(self.root.children)-1:
                self.__print_subtree(child, 1, lines, True, True)
            else:
                self.__print_subtree(child, 1, lines, False, False)
        return "\n".join(lines)









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
    h.children = [i]
    b.children = [e, h, f]
    d.children = [g]
    t = Tree(a)
    t.root.children = [b, c ,d]
    print(t)
