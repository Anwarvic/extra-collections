from radix_trie import TrieNode, RadixTrie



class TrieNode(TrieNode):
    def __init__(self, value):
        super().__init__(value)
        delattr(self, 'is_word')

    def represent_data(self):
        return self.data




class SuffixTrie(RadixTrie):
    
    ############################## INSERTION ##############################
    def insert(self, word):
        assert type(word) == str, "You can insert String objects only!!"
        assert len(word) > 0, "You can't insert any empty String!!"
        
        # Ukkonen's algorithm
        for idx in range(len(word)+1):
            # create new node using given word
            sub_word = word[idx:]+'$' #'$': string termination symbol
            super()._insert(sub_word)





if __name__ == "__main__":
    st = SuffixTrie()
    st.insert("banana")
    print(st)

    # st = SuffixTrie()
    # st.insert("m")