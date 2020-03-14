from tree import TreeNode, Tree


class TrieNode(TreeNode):
    def __init__(self, value):
        assert type(value)==str, "Trie nodes accept characters only!!"
        self.parent = None
        self.data = value
        self.children = {}
        self.is_word = False

    def get_characters(self):
        return self.children.keys()

    def get_children(self):
        return list(self.children.values())

    def get_child(self, ch):
        try:
            return self.children[ch]
        except KeyError:
            return ""

    def get_parent(self):
        return self.parent

    def set_child(self, ch, new_node):
        self.children[ch] = new_node
        new_node.parent = self
    
    def has_no_children(self):
        return self.children == {}

    def __repr__(self):
        return "TrieNode({})".format(self.data)

    def represent_data(self):
        if self.is_word:
            return self.data + ' ✓'
        else:
            return self.data



class Trie(Tree):
    def __init__(self):
        self.root = TrieNode('')
        self.root.data = "ROOT"


    ############################## INSERTION ##############################
    def insert(self, word):
        assert type(word) == str, "You can insert String objects only!!"
        assert len(word) > 0, "You can't insert any empty String!!"

        start_node = self.root
        for ch in word:
            if ch not in start_node.get_characters():
                start_node.set_child(ch, TrieNode(ch))
            start_node = start_node.get_child(ch)
        start_node.is_word = True


    ############################## REMOVE ##############################
    def remove(self, word):
        assert type(word) == str, "You can remove String objects only!!"
        start_node = self.root
        for ch in word:
            if ch not in start_node.children:
                return
            start_node = start_node.get_child(ch)
        
        # if word is found, clear it
        if start_node.is_word:
            start_node.is_word = False
        while(not start_node.is_word and start_node.has_no_children()):
            ch = start_node.get_data()
            parent = start_node.get_parent()
            del parent.children[ch]
            start_node = parent


    ############################## FIND ##############################
    def __contains__(self, word):
        assert type(word) == str, \
        "Can't find {} since tries contain only characters!!".format(type(word))
        
        start_node = self.root
        while(word):
            ch = word[0]
            child = start_node.get_child(ch)
            if not child:
                return False
            else:
                child_data = child.get_data()
                if child_data == word[:len(child_data)]:
                    start_node = child
                    word = word[len(child_data):]
                else:
                    return False
        return start_node.is_word


    def has_substring(self, substr):
        curr_node = self.root
        for ch in substr:
            if ch not in curr_node.get_characters():
                return False
            curr_node = curr_node.get_child(ch)
        return True


    ######################### AUTO-COMPLETION #########################
    def __get_candidates(self, start_node, prefix):
        output = []
        new_prefix = prefix.copy()
        new_prefix += start_node.get_data()
        if start_node.is_word:
            output.append("".join(new_prefix))
        # iterate over children
        for child in start_node.get_children():
            output.extend( self.__get_candidates(child, new_prefix) )
        return output

    def auto_complete(self, prefix=''):
        assert type(prefix) == str, "A character-sequence is expected!!"
        start_node = self.root
        # parse the prefix
        for ch in prefix:
            if ch not in start_node.get_characters():
                return []
            start_node = start_node.get_child(ch)
        # get candidates starting from given prefix
        candidates = []
        if start_node.is_word:
            candidates.append(prefix)
        for child in start_node.get_children():
            candidates.extend(self.__get_candidates(child, [prefix]))
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
    print(t.has_substring('carr'))

    # explort Trie
    print(t.root)
    print(t.root.get_child('t').data)
    print(t.root.get_child('c').children)
    
    # test find() and get_cadidates()
    print('cards' in t)
    print('c' in t)
    print(t.auto_complete())
    print(t.auto_complete('c'))
    print(t.auto_complete('tri'))
    print('='*50)
    
    # test remove()
    t = Trie()
    t.insert("tre")
    t.insert("trees")
    t.insert("treed")
    t.remove("trees")
    t.remove("tre")
    print(t)
    print(t.auto_complete("t"))

    # sanity checks
    t = Trie()
    t.insert('a')
    t.insert('A')
    t.remove('AA')
    print(t)
