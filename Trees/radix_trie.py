from trie import TrieNode, Trie

#helper function
def find_last_common_idx(word1, word2):
    idx = 0
    while(idx < len(word1)):
        if idx < len(word2) and word1[idx] == word2[idx]:
            idx += 1
        else:
            break
    return idx



class RadixTrie(Trie):
   
    ############################## INSERTION ##############################
    def __insert(self, start_node, word):
        while(word):
            ch = word[0]
            child = start_node.get_child(ch)
            if not child:
                new_node = TrieNode(word)
                new_node.is_word = True
                start_node.set_child(word[0], new_node)
                return
            else:
                child_data = child.get_data()
                # child has exactly the given word
                if child_data == word:
                    if not child.is_word:
                        child.is_word = True
                    return
                idx = find_last_common_idx(child_data, word)
                # child has part of the given word as a prefix
                if idx <= len(word) and idx != len(child_data):
                    # split child
                    new_node = TrieNode(child_data[:idx])
                    child.data = child_data[idx:]
                    new_node.set_child(child_data[idx], child)
                    # connect new_node to start_node
                    start_node.set_child(child_data[0], new_node)
                    child = new_node
                start_node = child
                word = word[idx:]
                if word == "":
                    start_node.is_word = True


    def insert(self, word):
        assert type(word) == str, "You can insert String objects only!!"
        assert len(word) > 0, "You can't insert any empty String!!"

        if self.root.children == {}:
            new_node = TrieNode(word)
            new_node.is_word = True
            self.root.set_child(word[0], new_node)
        else:
            start_node = self.root
            self.__insert(start_node, word)


    ############################## FIND ##############################
    def find(self, word):
        start_node = self.root
        ch = word[0]
        child = start_node.get_child(ch)
        if child is None:
            return False
        else:
            while(word):
                child_data = child.get_data()
                if child_data == word[:len(child_data)]:
                    start_node = child
                    word = word[:len(child_data)]
                else:
                    return False
            return True


    ######################### AUTO-COMPLETION #########################
    def get_candidates(self, prefix=''):
        pass






if __name__ == "__main__":
    # rt = RadixTrie()
    # rt.insert("shear")
    # rt.insert("she")
    # rt.insert("shepard")
    # rt.insert("shepard")
    # rt.insert("she")
    # rt.insert('s')
    # rt.insert("ahly")
    # print(rt)
    
    # # src: https://en.wikipedia.org/wiki/Radix_tree?oldformat=true
    # rt = RadixTrie()
    # rt.insert("romane")
    # rt.insert("romanus")
    # rt.insert("romulus")
    # rt.insert("rubens")
    # rt.insert("ruber")
    # rt.insert("rubicon")
    # rt.insert("rubicundus")
    # print(rt)

    rt = RadixTrie()
    rt.insert('test')
    rt.insert('toaster')
    rt.insert('toasting')
    rt.insert('slow')
    rt.insert('slowly')
    rt.insert('slowlier')
    rt.insert('toast')
    rt.insert('slower')
    print(rt)


