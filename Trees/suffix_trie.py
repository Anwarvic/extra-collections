from radix_trie import RadixTrie



class SuffixTrie(RadixTrie):
    
    ############################## INSERTION ##############################
    def insert(self, word):
        assert type(word) == str, "You can insert String objects only!!"
        assert len(word) > 0, "You can't insert any empty String!!"
        
        # Ukkonen's algorithm
        for idx in range(len(word)):
            # create new node using given word
            sub_word = word[idx:]
            super().insert(sub_word)

    ############################## remove ##############################
    def remove(self):
        raise NotImplementedError("Can't remove from SuffixTries!!")




if __name__ == "__main__":
    # st = SuffixTrie()
    # st.insert("banana")
    # print(st)
    # print(st.find('nan'))

    st = SuffixTrie()
    st.insert("minimize")
    print(st)