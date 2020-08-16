"""
A trie, pronounced "try", is a tree-based data structure for storing strings in
order to support fast pattern matching. Indeed, the name "trie" comes from the
word "retrieval". The primary query operations that tries support is "prefix
matching" which involves being given a string and looking for all the sequences
that contain the given string as a prefix.

[image]

The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.

+--------------------+------------------------------------------+------------+---------+
| Method             | Description                              | Worst-case | Optimal |
+====================+==========================================+============+=========+
| __len__()          | Returns the number of nodes.             | O(n)       | O(1)    |
+--------------------+------------------------------------------+------------+---------+
| is_empty()         | Checks if trie is empty.                 | O(1)       | O(1)    |
+--------------------+------------------------------------------+------------+---------+
| __repr__()         | Represents the trie.                     | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| __iter__()         | Iterates over the trie.                  | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| __contains__()     | Checks the existence of the given item   | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| get_height()       | Gets the trie's height                   | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| get_depth()        | Gets the trie's depth                    | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| get_nodes()        | Returns a list of all nodes per level    | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| count_leaf_nodes() | Counts all leaf nodss in the trie        | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| clear()            | Clears the whole trie instance           | O(1)       | O(1)    |
+--------------------+------------------------------------------+------------+---------+
| to_list()          | Converts the trie instance to  list.     | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+


Class Documentation
===================
Here are all of the public methods that can be used with `Trie()` objects:
"""
import warnings
from extra.trees.tree import TreeNode, Tree




class TrieNode(TreeNode):
    """
    A trie node is the basic unit for building tries. A tree node must contain
    a value and this value has to be a `str`. Each trie node has zero or more
    trie nodes as children.
    """
    __name__ = "extra.TrieNode()"


    def __init__(self, value):
        """
        Creates a `TrieNode()` object which is the basic unit for building 
        Trie() objects!!

        Parameters
        ----------
        value: str
            The value to be saved within the `TrieNode()` instance

        Raises
        ------
        TypeError: If the given item is not a `str` object.
        """
        if type(value) != str:
            raise TypeError("Trienodes accept characters only!!")
        
        self._parent = None
        self._data = value
        self._children = {}
        self._is_word = False


    def get_characters(self):
        """
        Returns a list of all the character children following the current 
        `TrieNode()` instance.

        Returns
        -------
        list:
            A list of all the characters obtained by the children.
        """
        return self._children.keys()


    def get_children(self):
        """
        Returns a list of all the children nodes of the current `TrieNode()`
        instance.

        Returns
        -------
        list:
            A list of all the children nodes of the current `TrieNode()`.
        """
        return list(self._children.values())


    def get_child(self, ch):
        """
        Gets the child that has the given character (`ch`) as a key.

        Parameters
        ----------
        ch: str
            A character that represents the child's key.
        
        Returns
        -------
        TrieNode() or None:
            If the key belongs to a certain `TrieNode()` child, this child is
            returned. If the key wasn't found, `None` is returned.
        """
        try:
            return self._children[ch]
        except KeyError:
            return None


    def get_parent(self):
        """
        Returns the parent of the current `TrieNode()` instance.

        Returns
        -------
        TrieNode() or None:
            A reference to the parent of the current `TrieNode()` which could be
            a `TrieNode() object or `None` in case the current `TrieNode()` is
            the root of the `Trie()` instance.
        """
        return self._parent


    def set_child(self, ch, new_node):
        """
        Sets the given `new_node` as a child for the current `TrieNode()` using
        the given `ch` as a new key.

        Parameters
        ----------
        ch: str
            The character that will be used as a key for the new node.
        
        new_node: TrieNode()
            The `TrieNode()` that will be a child for the current one.

        Raises
        ------
        TypeError: This can be raised due to the following reasons:
            1. The given key is not a `str`.
            2. If the given item is not an `TrieNode()` object.
        """
        if type(ch) != str:
            raise TypeError(
                f"Given key is `{type(ch)}` and it should be a `str`!!"
            )
        elif not isinstance(new_node, TrieNode):
            raise TypeError(
                f"You can't set a child unless it's an `{self.__name__}` " + 
                "object!!"
            )
        self._children[ch] = new_node
        new_node._parent = self


    def is_leaf(self):
        """
        Checks if the current `TrieNode()` instance is a leaf node. A leaf node
        is a tree node that has no children.

        Returns
        -------
        bool:
            `True` if the current `TrieNode()` has no children and `False`
            otherwise.
        """
        return self._children == {}


    def __repr__(self):
        """
        Represents `TrieNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `TrieNode()` instance.
        
        Example
        -------
        >>> x = TrieNode("x")
        >>> x
        >>> TrieNode("x")
        """
        return f"TrieNode({self._data})"


    def _represent(self):
        """
        
        Note
        ----
        The following character: '✓' is appended to a the `TrieNode()` object if
        it's the last child in representing a whole word.
        """
        if self._is_word:
            return self._data + ' ✓'
        else:
            return self._data




class Trie(Tree):
    """
    A trie is a tree-based data structure that can be defined recursively using
    a collection of `TrieNode()` instances, where each node contains string 
    value and each node has a list of references to the children `TrieNode()`
    instances.
    """
    __name__ = "extra.Trie()"
    

    def __init__(self):
        """
        Creates an empty `Trie()` object!!
        
        Example
        -------
        >>> t = Trie()
        >>> type(t)
        <class 'extra.trees.trie.Trie'>
        """
        self._root = TrieNode("ROOT")
        self._nodes_count = 1


    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the `Trie()` instance. Length is the number of nodes
        in the instance.

        
        Returns
        -------
        int:
            The length of the `Tie()` instance. Length is the number of tree
            nodes in the instance.
        
        Examples
        --------
        >>> t = Trie()
        >>> len(t)
        0
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
        >>> len(t)
        7
        """
        return self._nodes_count


    def is_empty(self):
        """
        Checks if the `Trie()` instance is empty or not in time-complexity of
        O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the `Trie()` instance is empty or not.
            `True` shows that this instance is empty and `False` shows it's
            not empty.
        
        Example
        --------
        >>> t = Trie()
        >>> t.is_empty()
        True
        >>> t.insert("apple")
        >>> t.is_empty()
        False
        """
        return self._nodes_count == 1
    

    ##############################     PRINT      ##############################
    def __repr__(self):
        """
        Represents the `Trie()` instance as a string.
        
        Returns
        -------
        str:
            The string-representation of the `Trie()` instance.

        Example
        -------
        >>> t = Tree()
        >>> t
        --
        >>> t.insert("car")
        >>> t.insert("cart")
        >>> t.insert("cast")
        ROOT
        └─┬ c
          └─┬ a
            ├─┬ r ✓
            │ └── t ✓
            └─┬ s
              └── t ✓
        """
        return super().__repr__()


    ##############################  HEIGHT/DEPTH  ##############################
    def get_height(self):
        """
        Gets the height of the `Tree()` instance. The tree's height is the 
        number of edges between the root and the furthest leaf node.

        Returns
        -------
        int:
            A positive integer representing the height of the instance.
        
        Example
        -------
        >>> t.insert("car")
        >>> t.insert("cart")
        >>> t.insert("cast")
        ROOT
        └─┬ c
          └─┬ a
            ├─┬ r ✓
            │ └── t ✓
            └─┬ s
              └── t ✓
        >>> t.get_height()
        4
        """
        return super().get_height()
    

    def get_depth(self):
        """
        Gets the depth of the `Trie()` instance.

        Returns
        -------
        int:
            A positive integer representing the depth of the given `Trie()`.
        
        Example
        -------
        >>> t.insert("car")
        >>> t.insert("cart")
        >>> t.insert("cast")
        ROOT
        └─┬ c
          └─┬ a
            ├─┬ r ✓
            │ └── t ✓
            └─┬ s
              └── t ✓
        >>> t.get_depth()
        0
        """
        if self.is_empty():
            return 0
        return self._get_depth(self._root)
    
    

    ##############################      FIND      ##############################
    def _follow_path(self, word):
        """
        This method parses the Trie and returns the last accessed node and
        the part of the word that can't be parsed.
        """
        assert type(word) == str

        curr_node = self._root
        while(word):
            ch = word[0]
            child = curr_node.get_child(ch)
            child_data = child.get_data() if child else "}"
            #'}' is used to break the following if-condition
            if child_data == word[:len(child_data)]:
                word = word[len(child_data):]
                curr_node = child
            else:
                break
        return curr_node, word


    def _validate_item(self, word, accept_empty_string=True):
        super()._validate_item(word)
        if type(word) != str:
            raise TypeError(f"Can't deal with {type(word)} object since " + \
                f"`{self.__name__}` contains only characters!!")
        if not accept_empty_string and len(word.strip()) == 0:
            raise ValueError(\
                f"White-spaces can't be used with `{self.__name__}`!!")
    

    def __contains__(self, word):
        if type(word) != str:
            return False
        last_node, remaining_word = self._follow_path(word)
        return remaining_word == "" and last_node._is_word


    def has_prefix(self, prefix):
        if type(prefix) != str:
            return False
        last_node, remaining = self._follow_path(prefix)
        if remaining:
            child = last_node.get_child(remaining[0])
            child_data = child.get_data() if child else ''
            return child_data[:len(remaining)] == remaining
        return True


    ##############################   INSERTION    ##############################
    def insert(self, word):
        self._validate_item(word, accept_empty_string=False)
        last_node, remaining_word = self._follow_path(word)
        curr_node = last_node
        for ch in remaining_word:
            child = TrieNode(ch)
            curr_node.set_child(ch, child)
            self._nodes_count += 1
            curr_node = child
        curr_node._is_word = True


    ##############################     REMOVE     ##############################
    def remove(self, word):
        if type(word) != str:
            warnings.warn(f"`{word}` doesn't exist in `{self.__name__}`",
                UserWarning
            )
            return
        elif word == "":
            return
        last_node, remaining_word = self._follow_path(word)
        if remaining_word == "": #found the whole word
            curr_node = last_node
            curr_node._is_word = False
            while(not curr_node._is_word and curr_node.is_leaf()):
                ch = curr_node.get_data()[0]
                parent = curr_node.get_parent()
                del parent._children[ch]
                self._nodes_count -= 1
                curr_node = parent


    ############################## AUTOCOMPLETION ##############################
    def _get_candidates(self, start_node, prev_prefixes):
        assert isinstance(start_node, TrieNode)
        assert type(prev_prefixes) == list

        output = []
        prefixes = prev_prefixes + [start_node.get_data()]
        if start_node._is_word:
            output.append("".join(prefixes))
        # iterate over children
        for child in start_node.get_children():
            output.extend( self._get_candidates(child, prefixes) )
        return output


    def auto_complete(self, prefix=''):
        self._validate_item(prefix)
        last_node, remaining = self._follow_path(prefix)
        candidates = []
        if remaining == "":
            curr_node = last_node
            # get candidates starting from given prefix
            if curr_node._is_word:
                candidates.append(prefix)
            for child in curr_node.get_children():
                candidates.extend(self._get_candidates(child, [prefix]))
        return candidates


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    print(t)