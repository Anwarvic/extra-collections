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
        try:
            return self._children[ch]
        except KeyError:
            return None


    def get_parent(self):
        return self._parent


    def set_child(self, ch, new_node):
        self._children[ch] = new_node
        new_node._parent = self


    def has_no_children(self):
        return self._children == {}


    def __repr__(self):
        return f"TrieNode({self._data})"


    def __str__(self):
        if self._is_word:
            return self._data + ' ✓'
        else:
            return self._data




class Trie(Tree):
    def __name__(self):
        return "extra.Trie()"
    

    def __init__(self):
        self._root = TrieNode("ROOT")
        self._nodes_count = 1


    ##############################     LENGTH     ##############################
    def __len__(self):
        return self._nodes_count


    def is_empty(self):
        return self._nodes_count == 1
    

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
                f"{self.__name__()} contains only characters!!")
        if not accept_empty_string and len(word.strip()) == 0:
            raise ValueError(\
                f"White-spaces can't be used with {self.__name__()}!!")
    

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
            warnings.warn(f"`{word}` doesn't exist in {self.__name__()}",
                UserWarning
            )
            return
        elif word == "":
            return
        last_node, remaining_word = self._follow_path(word)
        if remaining_word == "": #found the whole word
            curr_node = last_node
            curr_node._is_word = False
            while(not curr_node._is_word and curr_node.has_no_children()):
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


