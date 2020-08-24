"""
A suffix trie is a radix trie that stores information about a single string and
exports a huge amount of structural information about that string. It is able
to perform these stuctural operations by storing all the possible suffixes of
the given text, hence the name "Suffix Trie".

[image]


"""
from extra.interface import Extra
from extra.trees.radix_trie import get_lcp, TrieNode, RadixTrie




def is_palindrome(word):
    """
    Checks if the given word is a palindrome or not. A palindrome is  string
    that reads the same if reversed like "madam" or "anna".

    Parameters
    ----------
    word: str
        The word to be checked if it's a palindrome or not.
    
    Returns
    -------
    bool:
        A boolean verifying if the given word is a palindrome. `True` indicates
        the given word is a palindrome. `False` indicates it's not.

    Raises
    ------
    AssertionError: If the given word isn't a `str` object.

    Example
    -------
    >>> is_palindrome("madam")
    True
    >>> is_palindrome("anna")
    True
    >>> is_palindrome("apple")
    False
    >>> is_palindrome("")
    True
    """
    assert type(word) == str

    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return False
    return True




class SuffixTrie(Extra):
    """
    A suffix trie is a radix trie that stores information about a single string
    and exports a huge amount of structural information about that string. It is
    able to perform these stuctural operations by storing all the possible
    suffixes of the given text, hence the name "Suffix Trie".
    """
    __name__ = "extra.SuffixTrie"

    
    def __init__(self, word):
        """
        Creates a `SuffixTrie()` object using the given `word` in quadratic
        time-complexity!!

        Parameters
        ----------
        word: str
            The string that we want to create our `SuffixTrie()` from its
            suffixes.
        
        Raises
        ------
        ValueError: It can be raised due to one of these cases:
            1. If given `word` is `None`.
            2. If the given `word` is an empty string.
        TypeError: It can be raised due to one of these cases:
            1. If `word` is an `Extra` object.
            2. If the type of the given `word` isn't a string.

        Example
        -------
        >>> st = SuffixTrie("banana")
        >>> type(st)
        <class 'extra.trees.suffix_trie.SuffixTrie'>
        >>> st
        ROOT
        ├── banana$ ⟶ 0
        ├─┬ a
        │ ├─┬ na
        │ │ ├── na$ ⟶ 1
        │ │ └── $ ⟶ 3
        │ └── $ ⟶ 5
        ├─┬ na
        │ ├── na$ ⟶ 2
        │ └── $ ⟶ 4
        └── $ ⟶ 6
        """
        # Ukkonen's algorithm
        super()._validate_item(word)
        if type(word) != str:
            raise TypeError(
                f"Can't insert {type(word)} into `{self.__name__}`!!"
            )
        elif len(word) == 0:
            raise ValueError(
                f"An empty string can't be inserted to `{self.__name__}`!!"
            )
        
        self._word = word.replace('$', '')
        # dictionary containing suffix-index as key and leaf nodes as values 
        self._leaf_nodes = {}
        # SuffixTrie is basically a RadixTrie
        self._rt = RadixTrie()
        # suffix array is a tuple of (index, suffix) entries.
        self._suffix_array = []
        for idx in range(len(self._word)):
            node = self._rt._insert(self._word[idx:] + "$ ⟶ " + str(idx))
            node._is_word = False
            self._leaf_nodes[idx] = node
            self._suffix_array.append( (idx, self._word[idx:]) )
        
        # edge case
        node = self._rt._insert("$ ⟶ " + str(len(self._word)))
        node._is_word = False
        self._leaf_nodes[len(self._word)] = node
        self._suffix_array.append((len(self._word), '$'))
        # NOTE
        # The `self._suffix_array` isn't the actually suffix array. To obtain
        # the suffix array, you will need to sort the suffixes alphabetically
        # and obtain the indices only. And that's what happens in
        # `to_suffix_array` method.



    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the number of nodes within the `SuffixTrie()` instance.
        
        Returns
        -------
        int:
            The length of the `SuffixTrie()` instance. Length is the number of
            nodes in the instance.
        
        Examples
        --------
        >>> st = SuffixTrie("banana")
        >>> st
        ROOT
        ├── banana$ ⟶ 0
        ├─┬ a
        │ ├─┬ na
        │ │ ├── na$ ⟶ 1
        │ │ └── $ ⟶ 3
        │ └── $ ⟶ 5
        ├─┬ na
        │ ├── na$ ⟶ 2
        │ └── $ ⟶ 4
        └── $ ⟶ 6
        >>> len(t)
        11
        """
        return len(self._rt)


    ##############################     PRINT      ##############################
    def __repr__(self):
        """
        Represents the `SuffixTrie()` instance as a string.
        
        Returns
        -------
        str:
            The string-representation of the `SuffixTrie()` instance.
        
        Examples
        --------
        >>> st = SuffixTrie("banana")
        >>> st
        ROOT
        ├── banana$ ⟶ 0
        ├─┬ a
        │ ├─┬ na
        │ │ ├── na$ ⟶ 1
        │ │ └── $ ⟶ 3
        │ └── $ ⟶ 5
        ├─┬ na
        │ ├── na$ ⟶ 2
        │ └── $ ⟶ 4
        └── $ ⟶ 6
        """
        return str(self._rt)


    ##############################  HEIGHT/DEPTH  ##############################
    def get_height(self):
        """
        Gets the height of the `SuffixTrie()` instance. The trie's height is the 
        number of edges between the root and the furthest leaf node.

        Returns
        -------
        int:
            A positive integer representing the height of the instance.
        
        Example
        -------
        >>> st = SuffixTrie("banana")
        >>> st
        ROOT
        ├── banana$ ⟶ 0
        ├─┬ a
        │ ├─┬ na
        │ │ ├── na$ ⟶ 1
        │ │ └── $ ⟶ 3
        │ └── $ ⟶ 5
        ├─┬ na
        │ ├── na$ ⟶ 2
        │ └── $ ⟶ 4
        └── $ ⟶ 6
        >>> st.get_height()
        3
        """
        return self._rt.get_height()
    

    def get_depth(self):
        """
        Gets the depth of the `SuffixTrie()` instance.

        Returns
        -------
        int:
            A positive integer representing the depth of the given
            `SuffixTrie()`.
        
        Example
        -------
        >>> st = SuffixTrie("banana")
        >>> st
        ROOT
        ├── banana$ ⟶ 0
        ├─┬ a
        │ ├─┬ na
        │ │ ├── na$ ⟶ 1
        │ │ └── $ ⟶ 3
        │ └── $ ⟶ 5
        ├─┬ na
        │ ├── na$ ⟶ 2
        │ └── $ ⟶ 4
        └── $ ⟶ 6
        >>> st.get_depth()
        0
        """
        return self._rt.get_depth()
        

    ##############################   LEAF NODES   ##############################
    def count_leaf_nodes(self):
        """
        Counts the number of leaf nodes in the `SuffixTrie()` instance. Leaf
        nodes are the trie nodes that have no children.

        Returns
        -------
        int:
            A positive integer representing the number of leaf nodes in the 
            `SuffixTrie()`.
                
        Example
        -------
        >>> st = SuffixTrie("banana")
        >>> st
        ROOT
        ├── banana$ ⟶ 0
        ├─┬ a
        │ ├─┬ na
        │ │ ├── na$ ⟶ 1
        │ │ └── $ ⟶ 3
        │ └── $ ⟶ 5
        ├─┬ na
        │ ├── na$ ⟶ 2
        │ └── $ ⟶ 4
        └── $ ⟶ 6
        >>> st.count_leaf_nodes()
        2
        """
        return self._rt.count_leaf_nodes()


    ##############################      ITER      ##############################
    def __iter__(self):
        """
        Iterates over the `SuffixTrie()` instance and returns a generator of the 
        `TrieNode()` values in breadth-first manner.

        Returns
        -------
        generator:
            The value of each node in the instance.
        
        Example
        -------
        >>> st = SuffixTrie("banana")
        >>> st
        ROOT
        ├── banana$ ⟶ 0
        ├─┬ a
        │ ├─┬ na
        │ │ ├── na$ ⟶ 1
        │ │ └── $ ⟶ 3
        │ └── $ ⟶ 5
        ├─┬ na
        │ ├── na$ ⟶ 2
        │ └── $ ⟶ 4
        └── $ ⟶ 6
        >>> for value in st:
        ...     print(value, end=',')
        banana$,a,na,$,na,$,na$,$,na$,$,
        """
        for node in self._rt.__iter__():
            yield node.split(' ⟶ ')[0]
    

    def to_list(self):
        """
        Converts the `SuffixTrie()` instance to a `list` where values will be
        inserted in breadth-first manner.

        Returns
        -------
        list:
            A `list` object containing the same elements as the `SuffixTrie()`
            instance.
        
        Example
        -------
        >>> st = SuffixTrie("banana")
        >>> st
        ROOT
        ├── banana$ ⟶ 0
        ├─┬ a
        │ ├─┬ na
        │ │ ├── na$ ⟶ 1
        │ │ └── $ ⟶ 3
        │ └── $ ⟶ 5
        ├─┬ na
        │ ├── na$ ⟶ 2
        │ └── $ ⟶ 4
        └── $ ⟶ 6
        >>> st.to_list()
        ['banana$', 'a', 'na', '$', 'na', '$', 'na$', '$', 'na$', '$']
        """
        return [node for node in self]

    
    ##############################      FIND      ##############################
    def has_substr(self, substr):
        """
        Searches the `SuffixTrie()` for the given substring and returns `True`
        if the whole substring exists and `False` if not.

        Parameters
        ----------
        substr: str
            The substring to be searched for in the `SuffixTrie()` instance.
        
        Returns
        -------
        bool:
            Returns `True` if the substring exists in the `SuffixTrie()`
            instance and `False` if not.
        
        Example
        -------
        >>> st = SuffixTrie("banana")
        >>> st
        ROOT
        ├── banana$ ⟶ 0
        ├─┬ a
        │ ├─┬ na
        │ │ ├── na$ ⟶ 1
        │ │ └── $ ⟶ 3
        │ └── $ ⟶ 5
        ├─┬ na
        │ ├── na$ ⟶ 2
        │ └── $ ⟶ 4
        └── $ ⟶ 6
        >>> t.has_substr("ban")
        True
        >>> t.has_substr("ab")
        False
        """
        return self._rt.has_prefix(substr)


    def to_suffix_array(self):
        """
        Converts the `SuffixTrie()` to a suffix array. A suffix array is an
        array that stores the starting indices of all suffix in the given
        string sorted alphabetically.

        Returns
        -------
        list:
            The suffix array.
        
        Example
        -------
        >>> st = SuffixTrie("banana")
        >>> st
        ROOT
        ├── banana$ ⟶ 0
        ├─┬ a
        │ ├─┬ na
        │ │ ├── na$ ⟶ 1
        │ │ └── $ ⟶ 3
        │ └── $ ⟶ 5
        ├─┬ na
        │ ├── na$ ⟶ 2
        │ └── $ ⟶ 4
        └── $ ⟶ 6
        >>> st.to_suffix_array()
        [6, 5, 3, 1, 0, 4, 2]
        >>> # indices associated with the following suffixes:
        >>> # ['$', 'a', 'ana', 'anana', 'banana', 'na', 'nana']
        """
        # sort suffixes alphabetically and obtain only the indices
        print(sorted(self._suffix_array, key=lambda  x: x[1]))
        return [k for k, v in sorted(self._suffix_array, key=lambda  x: x[1])]


    ##############################     LCS/LRS    ##############################
    def __get_deepest_nodes(self):
        """
        Returns a list of the trie nodes found in the deepest one or two levels
        of the `SuffixTrie()` instance. It returns a list of the deepest two
        level only if the height of the SuffixTrie exceeds 2. Other than that,
        it returns a list of the deepest level.

        Returns
        -------
        list:
            A list of the deepest `TrieNode()` objects found in the 
            `SuffixTrie()` instanece.
        """
        if self._rt.is_empty():
            return self._rt._root
        level_nodes = \
            self._rt._get_nodes_per_level(self._rt._root, 0, [], False)
        if len(level_nodes) > 2:
            return level_nodes[-1] + level_nodes[-2]
        return level_nodes[-1]


    def _get_ancestors_data(self, node):
        """
        Gets all the data in the ancestors (parent, then grand-parent, then 
        great grand-parent, ...etc.) of the given `node` inorder where the first
        value belongs to the shallowest ancestor.

        Parameters
        ----------
        node: TrieNode()
            The `TrieNode()` whose ansestors data should be obtained.
        
        Returns
        -------
        list:
            A list of all the data stores at the ancestors of the given `node`
            in order where the first value belongs to the shallowest ancestor.
        
        Raises
        ------
        AssertionError: If the given `node` is not a `TrieNode()`.
        
        Example
        -------
        >>> st = SuffixTrie("banana")
        >>> st
        ROOT
        ├── banana$ ⟶ 0
        ├─┬ a
        │ ├─┬ na
        │ │ ├── na$ ⟶ 1
        │ │ └── $ ⟶ 3
        │ └── $ ⟶ 5
        ├─┬ na
        │ ├── na$ ⟶ 2
        │ └── $ ⟶ 4
        └── $ ⟶ 6
        >>> st._get_ancestors_data(st._root)
        
        >>> node = st._rt._root.get_child('a').get_child("n").get_child("n")
        >>> node
        TrieNode(na$ ⟶ 1)
        >>> st._get_ancestors_data(node)
        ana
        """
        assert isinstance(node, TrieNode)

        ancestors_data = []
        if node is not self._rt._root:
            parent = node.get_parent()
            while(parent is not self._rt._root):
                parent_data = parent.get_data()
                ancestors_data.append(parent_data)
                parent = parent.get_parent()
        return "".join(ancestors_data[::-1])


    def get_longest_common_substring(self):
        """
        Gets the longest common substring in the `SuffixTrie()`.

        Returns
        -------
        list:
            A list of longest commong substring(s) found in the `SuffixTrie()`
        
        Example
        >>> st = SuffixTrie("banana")
        >>> st.get_longest_common_substring()
        ['ana']
        >>> st = SuffixTrie("abcpqrabpqpq")
        >>> st.get_longest_common_substring()
        ["pq", "ab"]
        """
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
    def __get_longest_palindrome(self):
        """
        IT'S NOT READY YET!!
        """
        rev = self._word[::-1]
        longest_palindrome = ''
        for i in range(len(rev)):
            suffix = rev[i:]
            node, remaining = self._rt._follow_path(suffix)
            if not remaining: remaining = '$'
            child = node.get_child(remaining[0])
            if child is not None and child.is_leaf():
                child_data = child.get_data() if child else ''
                position = int(child_data.split(" ⟶ ")[1])
                lcp = get_lcp(child_data, remaining)
                remaining = remaining[len(lcp):]
                end_position = len(suffix)-len(remaining)
                if position == len(self._word)-i-end_position:
                    palindrome = suffix[:end_position]
                    if is_palindrome(palindrome) and \
                        len(palindrome) > len(longest_palindrome):
                        longest_palindrome = palindrome
        return longest_palindrome
               
        
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


    st = SuffixTrie("PAPERSFORPAPERS")
    print(st)
    print(st.get_longest_common_substring())
    # print(st.count_pattern_occurrences('P'))



    # st = SuffixTrie("banana")
    # print(st.to_suffix_array())
    # st = SuffixTrie("nonsense")
    # st = SuffixTrie("1234aba4321")
    # st = SuffixTrie("abacdfgdcaba")
    # print(st)
    # print(st.__get_longest_palindrome())
    # print(st.get_longest_common_substring())
    # print(st.get_lowest_common_ancestor(2, 4))
    # print(st.to_suffix_array())
    # print(st)