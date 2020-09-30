"""
A radix trie, or compressed trie, is similar to a standard trie but it ensures
that each internal node in the trie has at least two children. It enforces this 
rule by compressing chains of single-child nodes into individual edges. So, the
following is a simple trie formed by inserting these three words: "car", "cart",
and "cast".

.. code-block:: text

    ROOT
    └─┬ c
      └─┬ a
        ├─┬ r ✓
        │ └── t ✓
        └─┬ s
          └── t ✓

And the following is a radix trie, or compressed trie, created using the same
three words:

.. code-block:: text

    ROOT
    └─┬ ca
      ├─┬ r ✓
      │ └── t ✓
      └── st ✓

The advantage of a radix trie over a standard trie is that the number of nodes
of the compressed trie is less than the latter. Also, the number of nodes is 
proportional to the number of strings and not to their total length. This
additional compression scheme reduces the total space for the trie itself from
**O(n)** for the standard trie to **O(s)** for the radix trie, where **n** is
the total length of the strings and **s** is the number of strings.

Searching in a radix trie is not necessarily faster than in a standard tree,
since there is still need to compare every character of the desired pattern with
the potentially multi-character labels while traversing paths in the trie.

.. image:: ../../img/trees/radix_trie.gif

The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **m** is the number of elements in the *other* container.

+-----------------------+----------------------------------------------------------------+------------+---------+
| Method                | Description                                                    | Worst-case | Optimal |
+=======================+================================================================+============+=========+
| __len__()             | Returns the number of nodes.                                   | O(n)       | O(1)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| is_empty()            | Checks if radix trie is empty.                                 | O(1)       | O(1)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| __repr__()            | Represents the radix trie.                                     | O(n)       | O(n)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| __iter__()            | Iterates over the radix trie.                                  | O(n)       | O(n)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| __contains__()        | Checks the existence of the given item in the radix trie.      | O(m)       | O(1)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| get_height()          | Gets the radix trie's height                                   | O(n)       | O(n)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| get_depth()           | Gets the radix trie's depth                                    | O(1)       | O(1)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| get_nodes_per_level() | Returns a list of all nodes per level found in the radix trie. | O(n)       | O(n)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| count_leaf_nodes()    | Counts all leaf nodss in the radix trie.                       | O(n)       | O(n)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| clear()               | Clears the whole radix trie instance.                          | O(1)       | O(1)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| to_list()             | Converts the radix trie instance to list.                      | O(n)       | O(n)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| auto_complete()       | Auto-completes given index from the radix trie.                | O(m)       | O(m)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| insert()              | Inserts a new word to the radix trie.                          | O(m)       | O(m)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
| remove()              | Removes a word from the radix trie.                            | O(m)       | O(m)    |
+-----------------------+----------------------------------------------------------------+------------+---------+
"""
from extra.trees.trie import TrieNode, Trie




def get_lcp(word1, word2):
    """
    Gets the LCP, Longest Common Prefix, between the two given words.
    
    Parameters
    ----------
    word1: str
        The first word to consider when getting LCP.
    word2: str
        The second word to considerwhen getting LCP.
    
    Returns
    -------
    str:
        The longest common prefix between the given two words.
    
    Raises
    ------
    AssertionError: If either of the two given words isn't a string.
    
    Example
    -------
    >>> get_lcp("apple", "append")
    app
    >>> get_lcp("apple", "abnormal")
    a
    >>> get_lcp("apple", "xapple")
    
    """
    assert type(word1)==str and type(word2)==str

    for i in range(min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            return word1[:i]
    return word1 if len(word1) < len(word2) else word2




class RadixTrie(Trie):
    """
    A radix trie is a compressed trie that ensures that each internal node has
    at least two children. It enforces this rule by compressing chains of
    single-child nodes into individual edges. It is defined using a collection
    of `TrieNode()` instances, where each node contains string value and each
    node has a list of references to the children `TrieNode()` instances.
    """
    __name__ = "extra.RadixTrie()"
    
    def __init__(self):
        """
        Creates an empty `RadixTrie()` object!!
        
        Example
        -------
        >>> rt = RadixTrie()
        >>> type(rt)
        <class 'extra.trees.radix_trie.RadixTrie'>
        """
        super().__init__()
    

    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the `RadixTrie()` instance. Length is the number of
        nodes in the instance.

        
        Returns
        -------
        int:
            The length of the `RadixTrie()` instance. Length is the number of
            nodes in the instance.
        
        Examples
        --------
        >>> rt = RadixTrie()
        >>> len(t)
        0
        >>> t.insert("car")
        >>> t.insert("cart")
        >>> t.insert("cast")
        >>> t
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> len(t)
        5
        """
        return super().__len__()
    

    def is_empty(self):
        """
        Checks if the `RadixTrie()` instance is empty or not in time-complexity
        of O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the `RadixTrie()` instance is empty or
            not. `True` shows that this instance is empty and `False` shows it's
            not empty.
        
        Example
        --------
        >>> rt = RadixTrie()
        >>> rt.is_empty()
        True
        >>> rt.insert("apple")
        >>> rt.is_empty()
        False
        """
        return super().is_empty()
    

    ##############################     PRINT      ##############################
    def __repr__(self):
        """
        Represents the `RadixTrie()` instance as a string.
        
        Returns
        -------
        str:
            The string-representation of the `RadixTrie()` instance.

        Example
        -------
        >>> rt = RadixTree()
        >>> rt
        --
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        """
        return super().__repr__()


    ##############################  HEIGHT/DEPTH  ##############################
    def get_height(self):
        """
        Gets the height of the `RadixTrie()` instance. The trie's height is the 
        number of edges between the root and the furthest leaf node.

        Returns
        -------
        int:
            A positive integer representing the height of the instance.
        
        Example
        -------
        >>> rt = RadixTrie()
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> rt.get_height()
        3
        """
        return super().get_height()
    

    def get_depth(self):
        """
        Gets the depth of the `RadixTrie()` instance.

        Returns
        -------
        int:
            A positive integer representing the depth of the given `RadixTrie()`.
        
        Example
        -------
        >>> rt = RadixTrie()
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> rt.get_depth()
        0
        """
        return super().get_depth()
    
    
    ##############################   LEAF NODES   ##############################
    def count_leaf_nodes(self):
        """
        Counts the number of leaf nodes in the `RadixTrie()` instance. Leaf
        nodes are the trie nodes that have no children.

        Returns
        -------
        int:
            A positive integer representing the number of leaf nodes in the 
            `RadixTrie()`.
                
        Example
        -------
        >>> rt = RadixTrie()
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> rt.count_leaf_nodes()
        2
        """
        return super().count_leaf_nodes()


    ##############################      ITER      ##############################
    def __iter__(self):
        """
        Iterates over the `RadixTrie()` instance and returns a generator of the 
        `TrieNode()` values in breadth-first manner.

        Returns
        -------
        generator:
            The value of each node in the instance.
        
        Example
        -------
        >>> rt = RadixTrie()
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> for value in rt:
        ...     print(value, end=',')
        ca,r,st,t,
        """
        return super().__iter__()
    

    def to_list(self):
        """
        Converts the `RadixTrie()` instance to a `list` where values will be
        inserted in breadth-first manner.

        Returns
        -------
        list:
            A `list` object containing the same elements as the `RadixTrie()`
            instance.
        
        Example
        -------
        >>> rt = RadixTrie()
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> rt.to_list()
        ['ca', 'r', 'st', 't']
        """
        return super().to_list()


    ##############################      FIND      ##############################
    def __contains__(self, word):
        """
        Searches the `RadixTrie()` for the given `word` and returns `True` if
        the whole word exists and `False` if not.

        Parameters
        ----------
        word: str
            The word to be searched for in the `RadixTrie()` instance.
        
        Returns
        -------
        bool:
            Returns `True` if the value exists in the `RadixTrie()` instance and
            `False` if not.
        
        Example
        -------
        >>> rt = RadixTrie()
        >>> t.insert("car")
        >>> t.insert("cart")
        >>> t.insert("cast")
        >>> t
        ROOT
        └─┬ c
          └─┬ a
            ├─┬ r ✓
            │ └── t ✓
            └─┬ s
              └── t ✓
        >>> "car" in t
        True
        >>> "cas" in t
        False
        >>> "care" in t
        False
        """
        return super().__contains__(word)


    def has_prefix(self, prefix):
        """
        Searches the `RadixTrie()` for the given `prefix` and returns `True` if
        the whole prefix exists and `False` if not.

        Parameters
        ----------
        prefix: str
            The prefix to be searched for in the `RadixTrie()` instance.
        
        Returns
        -------
        bool:
            Returns `True` if the prefix exists in the `RadixTrie()` instance
            and `False` if not.
        
        Example
        -------
        >>> rt = RadixTrie()
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> t.has_prefix("car")
        True
        >>> "cas" in t
        False
        >>> t.has_prefix("cas")
        True
        """
        return super().has_prefix(prefix)


    ##############################     INSERT     ##############################
    def _insert(self, word):
        """
        Inserts a word to the `RadixTrie()` instance.

        Parameters
        ----------
        word: str
            The new word to be inserted.
        
        Returns
        -------
        TrieNode():
            A reference to the last accessed node after inserting the given
            `word`.
            
        Raises
        ------
        AssertionError: If the given `word` is either empty or its type isn't 
        a `str`.
        """
        assert type(word) == str and len(word) > 0

        last_node, remaining_word = super()._follow_path(word)
        curr_node = last_node
        while(remaining_word):
            ch = remaining_word[0]
            child = curr_node.get_child(ch)
            child_data = child.get_data() if child else ''
            idx = len(get_lcp(child_data, remaining_word))
            # couldn't find the remaining_word
            if idx == 0:
                new_node = TrieNode(remaining_word)
                curr_node.set_child(ch, new_node)
                remaining_word = ''
                self._nodes_count += 1
            # child is prefix of the remaining_word
            elif idx <= len(remaining_word) and idx != len(child_data):
                # split child
                new_node = TrieNode(child_data[:idx])
                child._data = child_data[idx:]
                new_node.set_child(child_data[idx], child)
                # connect new_node to curr_node
                curr_node.set_child(child_data[0], new_node)
                remaining_word = remaining_word[idx:]
                self._nodes_count += 1
            curr_node = new_node
        # mark current node as a word
        curr_node._is_word = True
        # return the newest created node after insertion
        return curr_node
    

    def insert(self, word):
        """
        Inserts a `word` in the `RadixTrie()` instance.

        Parameters
        ----------
        word: str
            The new word that will be inserted.
        
        Raises
        ------
        ValueError: If the given `word` is empty.
        TypeError: If the type of the given `word` is not `str`.

        Example
        -------
        >>> rt = RadixTrie()
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        """
        super()._validate_item(word, accept_empty_string=False)
        self._insert(word)


    ##############################     REMOVE     ##############################
    def remove(self, word):
        """
        Removes the given `word` from the `RadixTrie()` instance. 

        Parameters
        ----------
        word: str
            The word to be deleted from the `RadixTrie()`.
        
        Raises
        ------
        UserWarning: If the `RadixTrie()` instance is empty of if the value \
            wasn't found in the instance.
        
        Example
        -------
        >>> t = Trie()
        >>> t.insert("car")
        >>> t.insert("cart")
        >>> t.insert("cast")
        >>> t
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> t.remove("cart")
        ROOT
        └─┬ ca
          ├── r ✓
          └── st ✓
        """
        super().remove(word)


    def clear(self):
        """
        Removes all nodes within the `RadixTrie()` instance in constant time.

        Example
        -------
        >>> rt = RadixTrie()
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> rt.clear()
        >>> rt
        --
        >>> rt.is_empty()
        True
        """
        super().clear()


    ############################## AUTOCOMPLETION ##############################
    def auto_complete(self, prefix=''):
        """
        Parses the `RadixTrie()` instance and retrieves all the words that has
        the given `prefix`. In other words, auto-compeletes a given prefix using
        all saved words found in the `RadixTrie()` instance.

        Parameters
        ----------
        prefix: str (default '')
            A prefix to auto-complete.
        
        Returns
        -------
        list:
            A list of all found words that have the given `prefix`.
        
        Example
        -------
        >>> rt = Trie()
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> rt.auto_complete("ca")
        ["car", "cart"]
        >>> rt.auto_complete("cas")
        ["cast"]
        >>> rt.auto_complete()
        ['car', 'cart', 'cast']

        Note
        ----
        Using an empty prefix as an input will return all saved words in the 
        `Trie()` instance.
        """

        super()._validate_item(prefix)
        candidates = []
        last_node, remaining = super()._follow_path(prefix)
        # update prefix
        curr_node = last_node
        prefix = prefix[:-len(remaining)] if remaining else prefix
        if remaining:
            ch = remaining[0]
            child = curr_node.get_child(ch)
            child_data = child.get_data() if child else ''
            # couldn't find the remaining prefix
            if len(remaining) > len(child_data) or \
                child_data[:len(remaining)] != remaining:
                return candidates
            else:
                remaining = ''
                prefix += child_data
                curr_node = child
       
        # check the current node
        if curr_node._is_word:
            candidates.append(prefix)
        # get candidates starting from given prefix
        for child in curr_node.get_children():
            candidates.extend(super()._get_candidates(child, [prefix]))
        return candidates


    ##############################      NODES     ##############################
    def get_nodes_per_level(self):
        """
        Retrieves all trie nodes within the `RadixTrie()` instance so that all
        trie nodes in a certain level will be concatenated into a separate list.

        Returns
        -------
        list:
            A nested list where the first inner-list has all the trie nodes in 
            the first level, the second inner-list has all the trie nodes in the 
            second level, ... so on.
        
        Example
        -------
        >>> rt = RadixTrie()
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> t.get_nodes_per_level()
        [['ca'], ['r', 'st'], ['t']]
        """
        return super().get_nodes_per_level()[1:]
    

    