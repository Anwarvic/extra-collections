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
        for idx in range(len(self._word)):
            self._rt.insert(self._word[idx:] + "$ ⟶ " + str(idx))
        self._rt.insert("$ ⟶ " + str(len(self._word)))


    def __repr__(self):
        return str(self._rt)


    def __len__(self):
        return len(self._rt)


    def has_substr(self, substr):
        return self._rt.has_prefix(substr)


    ##############################     LCS/LRS    ##############################
    def __get_deepest_nodes(self):
        if self._rt.is_empty():
            return self._rt._root
        level_nodes = \
            self._rt._get_nodes_per_level(self._rt._root, 0, [], False)
        if len(level_nodes) > 2:
            return level_nodes[-1] + level_nodes[-2]
        return level_nodes[-1]


    def get_longest_common_substring(self):
        # NOTE:stands for "Longest Common Substring"
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
                parent = parent.get_parent()
            lcs = "".join(lcs[::-1])
            longest_length = max(longest_length, len(lcs))
            lcs_set.add(lcs)
        # return the longest ones
        return [substr for substr in lcs_set if len(substr) == longest_length]


    def get_longest_repeated_substring(self):
        # NOTE: stands for "Longest Repeated Substring". 
        # lrs is the longest substring that occurs at least twice.
        return self.get_longest_common_substring()

    
    ##############################    MATCHING    ##############################
    def count_pattern_occurrences(self, pattern):
        if type(pattern) != str:
            return 0
        last_node, remaining = self._rt._follow_path(pattern)
        if remaining:
            child = last_node.get_child(remaining[0])
            child_data = child.get_data() if child else ''
            if child_data[:len(remaining)] == remaining:
                last_node = child
            else:
                return 0
        if last_node == self._rt._root:
            return 0
        return self._rt._count_leaf_nodes(last_node)


    def get_longest_palindrome(self):
        #TODO
        pass


    def get_lca(self):
        #NOTE: stands for "Lowest Common Ancestor"
        pass
       

    def to_suffix_array(self):
        #TODO
        pass








if __name__ == "__main__":
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


    # st = SuffixTrie("PAPERSFORPAPERS")
    # print(st)
    # print(st.get_longest_common_substring())
    # print(st.count_pattern_occurrences('P'))



    st = SuffixTrie("banana")
    print(st.get_longest_common_substring())
    print(st)