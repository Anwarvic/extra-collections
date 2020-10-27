.. _radix_trie:

Radix Trie
==========

.. automodule:: extra.trees.radix_trie
    :noindex:
    :members:
    :special-members:
    :exclude-members: get_lcp, RadixTrie


.. image:: ../../_images/trees/radix_trie.gif
    :align: center
    :height: 650


⏱ Time-Complexity
-------------------
The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of nodes currently in the radix trie.
- **m** is the length of the passed string.

.. csv-table::
   :file: ../../_files/trees/radix_trie.csv
   :header-rows: 1
   :widths: 10, 70, 10, 10


☕️ API
-------
Here are all of the public methods that can be used with `RadixTrie()` objects:

.. autoclass:: extra.trees.radix_trie.RadixTrie
    :members:
    :special-members:
    :exclude-members:
