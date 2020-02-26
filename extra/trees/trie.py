from extra.trees.tree import TreeNode, Tree




class TrieNode(TreeNode):
    def __init__(self, value):
        if type(value) != str:
            raise TypeError("Trienodes accept characters only!!")
        # assert len(value) == 1
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
            return None


    def get_parent(self):
        return self.parent


    def set_child(self, ch, new_node):
        self.children[ch] = new_node
        new_node.parent = self


    def has_no_children(self):
        return self.children == {}


    def __repr__(self):
        return f"TrieNode({self.data})"


    def __str__(self):
        if self.is_word:
            return self.data + ' ✓'
        else:
            return self.data




class Trie(Tree):
    def __name__(self):
        return "extra.Trie()"
    

    def __init__(self):
        self.root = TrieNode('x') #dummy data
        self.root.data = "ROOT"
        self.nodes_count = 1


    ############################## LENGTH ##############################
    def __len__(self):
        return self.nodes_count


    def is_empty(self):
        return self.nodes_count == 1
    

    ############################## FIND ##############################
    def _follow_path(self, word):
        """
        This method parses the Trie and returns the last accessed node and
        the part of the word that can't be parsed.
        """
        assert type(word) == str
        curr_node = self.root
        while(word):
            ch = word[0]
            child = curr_node.get_child(ch)
            #'}' is used to break the following if-condition
            child_data = child.get_data() if child else "}"
            if child_data == word[:len(child_data)]:
                word = word[len(child_data):]
                curr_node = child
            else:
                break
        return curr_node, word


    def _validate_item(self, word, accept_empty_string=True):
        if type(word) != str:
            raise TypeError(f"Can't deal with {type(word)} object since " + \
                f"{self.__name__()} contains only characters!!")
        if not accept_empty_string and len(word.strip()) == 0:
            raise ValueError(\
                f"An empty string can't be here with {self.__name__()}!!")
    

    def __contains__(self, word):
        self._validate_item(word)    
        last_node, remaining_word = self._follow_path(word)
        return remaining_word == "" and last_node.is_word


    def has_prefix(self, prefix):
        self._validate_item(prefix)
        last_node, remaining = self._follow_path(prefix)
        if remaining:
            child = last_node.get_child(remaining[0])
            child_data = child.get_data() if child else ''
            return child_data[:len(remaining)] == remaining
        return True


    ############################## INSERTION ##############################
    def insert(self, word):
        self._validate_item(word, accept_empty_string=False)
        last_node, remaining_word = self._follow_path(word)
        curr_node = last_node
        for ch in remaining_word:
            child = TrieNode(ch)
            curr_node.set_child(ch, child)
            self.nodes_count += 1
            curr_node = child
        curr_node.is_word = True


    ############################## REMOVE ##############################
    def remove(self, word):
        self._validate_item(word, accept_empty_string=False)
        last_node, remaining_word = self._follow_path(word)
        if remaining_word == "": #found the whole word
            curr_node = last_node
            curr_node.is_word = False
            while(not curr_node.is_word and curr_node.has_no_children()):
                ch = curr_node.get_data()[0]
                parent = curr_node.get_parent()
                del parent.children[ch]
                self.nodes_count -= 1
                curr_node = parent


    def clear(self):
        self.__init__()
    

    ######################### AUTO-COMPLETION #########################
    def _get_candidates(self, start_node, prev_prefixes):
        assert isinstance(start_node, TrieNode)
        assert type(prev_prefixes) == list
        output = []
        prefixes = prev_prefixes + [start_node.get_data()]
        if start_node.is_word:
            output.append("".join(prefixes))
        # iterate over children
        for child in start_node.get_children():
            output.extend( self._get_candidates(child, prefixes) )
        return output


    def auto_complete(self, prefix=''):
        self._validate_item(prefix)
        last_node, remaining = self._follow_path(prefix)
        candidates = []
        if remaining == "":
            curr_node = last_node
            # get candidates starting from given prefix
            if curr_node.is_word:
                candidates.append(prefix)
            for child in curr_node.get_children():
                candidates.extend(self._get_candidates(child, [prefix]))
        return candidates


