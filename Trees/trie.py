from tree import TreeNode, Tree


class TrieNode(TreeNode):
    def __init__(self, value):
        assert type(value)==str and len(value)==1, \
                    "Trie nodes accept characters only!!"
        self.data = value
        self.children = {}
        self.is_word = False

    def __repr__(self):
        return "TrieNode({})".format(self.data)

    def get_children(self):
        return list(self.children.values())




class Trie(Tree):
    def __init__(self):
        self.root = TrieNode(' ')
        self.root.data = "root"

    def insert(self, word):
        assert type(word) == str, "You can insert String objects only!!"
        start_node = self.root
        for ch in word:
            if ch not in start_node.children:
                start_node.children[ch] = TrieNode(ch)
            start_node = start_node.children[ch]
        start_node.is_word = True


    def find(self, word):
        start_node = self.root
        for ch in word:
            if ch not in start_node.children:
                return False
            start_node = start_node.children[ch]
        return start_node.is_word




if __name__ == "__main__":
    t = Trie()
    t.insert('abcd')
    t.insert('axyz')
    print(t)
    print(t.find('ad'))
