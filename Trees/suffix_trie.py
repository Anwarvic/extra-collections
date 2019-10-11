from radix_trie import TrieNode, RadixTrie



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

    ############################## FIND ##############################
    def find(self, word):
        assert type(word) == str, \
        "Can't find {} since tries contain only characters!!".format(type(word))
        
        start_node = self.root
        word += '$'
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




if __name__ == "__main__":
    st = SuffixTrie()
    st.insert("banana")
    print(st)
    print(st.find('nan'))

    # st = SuffixTrie()
    # st.insert("m")