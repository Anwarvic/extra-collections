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
    def insert(self, word):
        assert type(word) == str, "You can insert String objects only!!"
        assert len(word) > 0, "You can't insert any empty String!!"

        if self.root.children == {}:
            self.root.set_child(word[0], TrieNode(word))
        else:
            start_node = self.root
            while(word):
                ch = word[0]
                child = start_node.get_child(ch)
                if not child:
                    start_node.set_child(word[0], TrieNode(word))
                    return
                else:
                    child_data = child.get_data()
                    idx = find_last_common_idx(child_data, word)
                    # whole word is found
                    if idx == len(word):
                        return
                    # child has the given word as prefix
                    elif idx > len(word):
                        child.data = word
                        word = child_data
                    # child has prefix of the word
                    else:
                        start_node = child
                        word = word[idx:]

            
            


    ############################## FIND ##############################
    def find(self, word):
        pass


    ######################### AUTO-COMPLETION #########################
    def get_candidates(self, prefix=''):
        pass






if __name__ == "__main__":
    t = RadixTrie()
    t.insert("shear")
    t.insert("she")
    t.insert("shepard")
    print(t)
    # print(t.root.children)