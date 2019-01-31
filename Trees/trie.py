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

    ############################## INSERTION ##############################
    def insert(self, word):
        assert type(word) == str, "You can insert String objects only!!"
        start_node = self.root
        for ch in word:
            if ch not in start_node.children:
                start_node.children[ch] = TrieNode(ch)
            start_node = start_node.children[ch]
        start_node.is_word = True


    ############################## FIND ##############################
    def find(self, word):
        start_node = self.root
        for ch in word:
            if ch not in start_node.children:
                return False
            start_node = start_node.children[ch]
        return start_node.is_word


    ######################### AUTO-COMPLETION #########################
    def __parse(self, start_node, prefix):
        output = []
        new_prefix = prefix.copy()
        new_prefix += start_node.data
        if start_node.is_word:
            output.append("".join(new_prefix))
        # iterate over children
        for child in start_node.get_children():
            output.extend( self.__parse(child, new_prefix) )
        return output


    def get_candidates(self, prefix=''):
        assert type(prefix) == str, "A character-sequence is expected!!"
        start_node = self.root
        # parse the prefix
        for ch in prefix:
            if ch not in start_node.children:
                return []
            start_node = start_node.children[ch]
        # get candidates starting from given prefix
        candidates = []
        if start_node.is_word:
            candidates.append(prefix)
        for child in start_node.get_children():
            candidates.extend(self.__parse(child, [prefix]))
        return candidates






if __name__ == "__main__":
    t = Trie()
    t.insert('car')
    t.insert('card')
    t.insert('cards')
    t.insert('cot')
    t.insert('cots')
    t.insert('trie')
    t.insert('tried')
    t.insert('tries')
    t.insert('try')

    print(t)
    print(t.find('cards'))
    print(t.find('c'))
    print(t.get_candidates())
    print(t.get_candidates('c'))
    print(t.get_candidates('tri'))

