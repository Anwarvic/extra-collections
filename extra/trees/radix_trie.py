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

[image]

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




def find_last_common_idx(word1, word2):
    """
    A helper function which returns the index of the last common prefix between
    the given two words
    """
    idx = 0
    while(idx < len(word1)):
        if idx < len(word2) and word1[idx] == word2[idx]:
            idx += 1
        else:
            break
    return idx




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
        >>> rt.insert("car")
        >>> rt.insert("cart")
        >>> rt.insert("cast")
        >>> rt
        ROOT
        └─┬ ca
          ├─┬ r ✓
          │ └── t ✓
          └── st ✓
        >>> t.get_height()
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
        Counts the number of leaf nodes in the `Trie()` instance. Leaf nodes are
        the trie nodes that have no children.

        Returns
        -------
        int:
            A positive integer representing the number of leaf nodes in the 
            `Trie()`.
                
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
        >>> t.count_leaf_nodes()
        2
        """
        return super().count_leaf_nodes()


    ##############################   INSERTION    ##############################
    def _insert(self, word):
        assert type(word) == str and len(word) > 0
        last_node, remaining_word = super()._follow_path(word)
        curr_node = last_node
        while(remaining_word):
            ch = remaining_word[0]
            child = curr_node.get_child(ch)
            child_data = child.get_data() if child else ''
            idx = find_last_common_idx(child_data, remaining_word)
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
        super()._validate_item(word, accept_empty_string=False)
        self._insert(word)


    ############################## AUTOCOMPLETION ##############################
    def auto_complete(self, prefix=''):
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


