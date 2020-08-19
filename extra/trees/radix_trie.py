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

[image]

Searching in a radix trie is not necessarily faster than in a standard tree,
since there is still need to compare every character of the desired pattern with
the potentially multi-character labels while traversing paths in the trie.

"""
from extra.trees.trie import TrieNode, Trie




#helper function
def find_last_common_idx(word1, word2):
    idx = 0
    while(idx < len(word1)):
        if idx < len(word2) and word1[idx] == word2[idx]:
            idx += 1
        else:
            break
    return idx




class RadixTrie(Trie):
    def __name__(self):
        return "extra.RadixTrie()"
    

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


