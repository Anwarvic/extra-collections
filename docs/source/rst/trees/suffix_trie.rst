.. _suffix_trie:

Suffix Trie
===========

.. automodule:: extra.trees.suffix_trie
    :noindex:
    :members:
    :special-members:
    :exclude-members: is_palindrome, SuffixTrie


.. image:: ../../_images/trees/suffix_trie.gif
    :align: center
    :height: 650


⏱ Time-Complexity
-------------------
The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of nodes currently in the suffix trie.
- **m** is the length of the passed string.

.. csv-table::
   :file: ../../_files/trees/suffix_trie.csv
   :header-rows: 1
   :widths: 10, 70, 10, 10


☕️ API
-------
Here are all of the public methods that can be used with `SuffixTrie()` objects:

.. autoclass:: extra.trees.suffix_trie.SuffixTrie
    :members:
    :special-members:
    :exclude-members:
