"""
Suffix trees store information about a single string and exports a huge amount
of structural information about that string.
"""
from abc import abstractmethod
from extra.interface import Extra
from extra.trees.radix_trie import RadixTrie



class SuffixTrie(Extra):
    def __name__(self):
        return "extra.SuffixTrie"

    
    def __init__(self, word):
        super()._validate_item(word)
        if type(word) != str:
            raise TypeError(f"Can't insert {type(word)} into {self.__name__()}")
        elif len(word) == 0:
            raise ValueError(\
                f"An empty string can't be inserted to {self.__name__()}!!")
        # Ukkonen's algorithm
        self._word = word
        self._rt = RadixTrie()
        for idx in range(len(word)):
            self._rt.insert(word[idx:])


    def __repr__(self):
        return str(self._rt)


    def __len__(self):
        return len(self._rt)


    def has_suffix(self, suffix):
        return self._rt.has_prefix(suffix)


    # def has_substr(self, substr):
    #     return self._rt.has_prefix(substr)


    ##############################       LCS      ##############################
    def __get_deepest_nodes(self):
        if self._rt.is_empty():
            return self._rt._root
        level_nodes = \
            self._rt._get_nodes_per_level(self._rt._root, 0, [], False)
        return level_nodes[-1]


    def get_lcs(self):
        #NOTE:stands for "Longest Common Substring"
        if self._rt.is_empty():
            return []
        lcs_set = set()
        longest_length = 0
        for node in self.__get_deepest_nodes():
            lcs = []
            parent = node.get_parent()
            while(parent is not self._rt._root):
                parent_data = parent.get_data()
                lcs.append(parent_data)
                longest_length = max(longest_length, len(parent_data))
                parent = parent.get_parent()
            lcs_set.add("".join(lcs[::-1]))
        # return the longest ones
        return [substr for substr in lcs_set if len(substr) == longest_length]


    def get_lrs(self):
        """TODO
        LRS stands for "Longest Repeated Substring". lrs is the longest
        substring that occurs at least twice.
        """
        pass


    def get_longest_palindrome(self):
        #TODO
        pass


    def get_lowest_common_ancestor(self):
        #TODO
        pass
    

    def to_suffix_array(self):
        #TODO
        pass








if __name__ == "__main__":
    # st = SuffixTrie("banana")
    # print(st)
    # print(st.has_substr('nan'))
    
    # st = SuffixTrie("ATCGATCGA")
    # print(st)
    # # print(st.get_longest_repeated_substr())
    # print("Total Nodes:", len(st))


    # st = SuffixTrie("minimize")
    # print(st)
    # print("Total Nodes:", len(st))
    # print(st.has_suffix('ize'))    

    # st = SuffixTrie("nonsense")
    # print(st)
    # print("Total Nodes:", len(st))
    # print(st.get_lcs())


    st = SuffixTrie("abcpqrabpqpq")
    print(st)
    print(st.get_lcs())  #ABABA

