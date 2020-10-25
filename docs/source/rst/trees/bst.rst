.. _bst:

Binary Search Tree (BST)
========================

.. automodule:: extra.trees.bst
    :noindex:
    :members:
    :special-members:
    :exclude-members: BSTNode, BST


.. image:: ../../img/trees/bst.gif
    :align: center
    :height: 800


⏱ Time-Complexity
-------------------
The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of nodes currently in the BST.
- **h** is the BST height which is **log(n)** when the tree is balanced.

.. csv-table::
   :file: ../../_files/trees/bst.csv
   :header-rows: 1
   :widths: 10, 70, 10, 10


☕️ API
-------
Here are all of the public methods that can be used with `BST()` objects:

.. autoclass:: extra.trees.bst.BST
    :members:
    :special-members:
    :exclude-members:
