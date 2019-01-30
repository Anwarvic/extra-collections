from tree import TreeNode, Tree


class TrieNode(TreeNode):
    def __init__(self, value):
        assert type(value)==str and len(value)==1, \
                    "Trie nodes accept characters only!!"
        self.data = value
        self.children = []

    def __repr__(self):
        return "TrieNode({})".format(self.data)


class Trie(Tree):
    def __init__(self):
        self.root = TrieNode(' ')
        self.root.data = "root"

    ############################## INSERTION ##############################
    def __insert(self, start_node):
        pass


    def insert(self, word):
        pass

if __name__ == "__main__":
    t = Trie()
    print(t)