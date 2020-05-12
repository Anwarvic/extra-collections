"""
Suffix trees store information about a single string and exports a huge amount
of structural information about that string.
"""
from abc import abstractmethod
from extra.interface import Extra
from extra.trees.radix_trie import TrieNode, RadixTrie




def get_lcp(word1, word2):
    # NOTE: LCP stands for Longest Common Prefix
    assert type(word1)==str and type(word2)==str
    assert len(word1)>0 and len(word2)>0

    for i in range(min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            return word1[:i]
    return word1 if len(word1) < len(word2) else word2


def create_suffix_array(word):
    assert type(word)==str and len(word)>0

    suffix_array = [ (idx, word[idx:]) for idx in range(len(word)) ]
    # sort suffix array alphabetically
    suffix_array = sorted(suffix_array, key=lambda  x: x[1])
    return suffix_array


def create_lcp_array(suffix_array):
    assert type(suffix_array)==list and len(suffix_array)>0

    lcp_array = [0]
    for i in range(len(suffix_array)-1):
        _, first_suffix = suffix_array[i]
        _, second_suffix = suffix_array[i+1]
        lcp = get_lcp(first_suffix, second_suffix)
        lcp_array.append(len(lcp))
    return lcp_array




class SuffixTrie(Extra):
    def __name__(self):
        return "extra.SuffixTrie"

    
    def __init__(self, word):
        # Ukkonen's algorithm
        super()._validate_item(word)
        if type(word) != str:
            raise TypeError(f"Can't insert {type(word)} into {self.__name__()}")
        elif len(word) == 0:
            raise ValueError(\
                f"An empty string can't be inserted to {self.__name__()}!!")
        
        self._word = word.replace('$', '')
        # dictionary containing suffix-index as key and leaf nodes as values 
        self._leaf_nodes = {}
        # SuffixTrie is basically a RadixTrie
        self._rt = RadixTrie()
        # suffix_array
        self._suffix_array = []
        for idx in range(len(self._word)):
            self._leaf_nodes[idx] = \
                self._rt._insert(self._word[idx:] + "$ ⟶ " + str(idx))
            self._suffix_array.append( (idx, self._word[idx:]) )
        
        # edge case
        self._leaf_nodes[len(self._word)] = \
            self._rt._insert("$ ⟶ " + str(len(self._word)))
        self._suffix_array.append((len(self._word), '$'))

        # sort suffix array alphabetically
        self._suffix_array = \
            [k for k, v in sorted(self._suffix_array, key=lambda  x: x[1])]


    def __repr__(self):
        return str(self._rt)


    def __len__(self):
        return len(self._rt)


    def has_substr(self, substr):
        return self._rt.has_prefix(substr)


    def to_suffix_array(self):
        return self._suffix_array


    ##############################     LCS/LRS    ##############################
    def __get_deepest_nodes(self):
        if self._rt.is_empty():
            return self._rt._root
        level_nodes = \
            self._rt._get_nodes_per_level(self._rt._root, 0, [], False)
        if len(level_nodes) > 2:
            return level_nodes[-1] + level_nodes[-2]
        return level_nodes[-1]


    def _get_ancestors_data(self, node):
        assert type(node) is TrieNode

        ancestors_data = []
        parent = node.get_parent()
        while(parent is not self._rt._root):
            parent_data = parent.get_data()
            ancestors_data.append(parent_data)
            parent = parent.get_parent()
        return "".join(ancestors_data[::-1])


    def get_longest_common_substring(self):
        if self._rt.is_empty():
            return []
        lcs_set = set()
        longest_length = 0
        for node in self.__get_deepest_nodes():
            lcs = self._get_ancestors_data(node)            
            longest_length = max(longest_length, len(lcs))
            lcs_set.add(lcs)
        # return the longest ones
        return [substr for substr in lcs_set if len(substr) == longest_length]


    def get_longest_repeated_substring(self):
        # LRS is the longest substring that occurs at least twice.
        return self.get_longest_common_substring()


    def get_lowest_common_ancestor(self, i, j):
        if type(i) != int or type(j) != int:
            raise TypeError("`i` and `j` should be integer values!!")
        elif i < 0 or j < 0 :
            raise ValueError("`i` and `j` should be postive integer values!!")
        elif i >= len(self._word) or j >= len(self._word):
            raise ValueError(\
                f"`i` and `j` values can't exceed {len(self._word)} " + 
                f"since it is the length of given word `{self._word}`!!"
            )
        ith_ancestors_data = self._get_ancestors_data(self._leaf_nodes[i])
        jth_ancestors_data = self._get_ancestors_data(self._leaf_nodes[j])
        return get_lcp(ith_ancestors_data, jth_ancestors_data)
    
    
    ##############################   PALINDROME   ##############################
    def get_longest_palindrome(self):
        # NOTE A palindrome is a string that reads the same if reversed
        # like "madam" or "".
        word = self._word + '$' + self._word[::-1]
        suffix_arr = create_suffix_array(word)
        lcp_arr = create_lcp_array(suffix_arr)
        # start searching
        position = 0
        longest_length = 0
        length = len(self._word)
        for i in range(1, len(word)):
            if lcp_arr[i] > longest_length:
                if ((suffix_arr[i-1][0] < length and suffix_arr[i][0] > length)
                    or
                    (suffix_arr[i][0]< length and suffix_arr[i-1][0] > length)):
                    longest_length = lcp_arr[i]
                    position = suffix_arr[i][0]
        return word[position : position+longest_length]
        
        
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
    st.get_longest_palindrome ()
    # print(st.get_longest_common_substring())
    # print(st.get_lowest_common_ancestor(2, 4))
    # print(st.to_suffix_array())
    # print(st)