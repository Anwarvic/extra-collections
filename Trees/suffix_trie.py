from radix_trie import RadixTrie



class SuffixTrie:

    def __init__(self, word):
        assert type(word) == str, "The initial value must be a string!!"
        assert len(word) > 0, "An empty string can't be used!!"
        self.rt = RadixTrie()
        # Ukkonen's algorithm
        for idx in range(len(word)):
            self.rt.insert(word[idx:])


    def __repr__(self):
        return str(self.rt)


    def __len__(self):
        return len(self.rt)
    
    ############################## PATTERN ##############################        
    def hasSuffix(self, s):
        """ Return  true    iff s   is  a   suffix  of  t   """
        node    = self.followPath(s)
        return  node    is not None and '$' in  node




if __name__ == "__main__":
    # st = SuffixTrie("banana")
    # print(st)
    # print(st.find('nan'))

    st = SuffixTrie("minimize")
    print(st)
    print("Total Nodes:", len(st))
