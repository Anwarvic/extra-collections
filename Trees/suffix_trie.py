"""
Suffix trees store information about a single string and exports a huge amount
of structural information about that string.
"""
from radix_trie import RadixTrie
from trie import Trie



class SuffixTrie:

    def __init__(self, word):
        assert type(word) == str, "The initial value must be a string!!"
        assert len(word) > 0, "An empty string can't be used!!"
        # Ukkonen's algorithm
        self.rt = RadixTrie()
        for idx in range(len(word)):
            self.rt.insert(word[idx:])


    def __repr__(self):
        return str(self.rt)


    def __len__(self):
        return len(self.rt)


    def has_suffix(self, suffix):
        return self.rt.has_prefix(suffix)


    def has_substr(self, substr):
        return substr in self.rt


    def get_lcs(self):
        #TODO:stands for "longest Common Substring"
        pass


    def get_lrs(self):
        """TODO
        LRS stands for "longest Repeated Substring". lrs is the longest
        substring that occurs at least twice.
        """
        pass


    def get_longest_palindrome(self):
        #TODO
        pass


    def get_lowest_common_ancestor(self):
        #TODO
        pass


    def 






if __name__ == "__main__":
    # st = SuffixTrie("banana")
    # print(st)
    # print(st.find('nan'))
    
    st = SuffixTrie("ATCGATCGA")
    print(st)
    print(st.get_longest_repeated_substr())
    print("Total Nodes:", len(st))


    # st = SuffixTrie("minimize")
    # print(st)
    # print("Total Nodes:", len(st))
    # print(st.has_suffix('ize'))    

    # st = SuffixTrie("nonsense")
    # print(st)
    # print("Total Nodes:", len(st))
    # print(st.has_substr("se"))
    # print(st.get_longest_repeated_substr())


    # st = SuffixTrie("ABABABA")
    # print(st)
    # print(st.get_longest_repeated_substr())    

