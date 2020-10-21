.. _binary_tree:

Binary Tree
===========

.. automodule:: extra.trees.binary_tree
    :noindex:
    :members:
    :special-members:
    :exclude-members: BinaryTreeNode, BinaryTree


⏱ Time-Complexity
-------------------
The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of nodes currently in the binary tree.

.. csv-table::
   :file: ../../_files/trees/binary_tree.csv
   :header-rows: 1
   :widths: 10, 70, 10, 10


☕️ API
-------

BinaryTreeNode()
^^^^^^^^^^^^^^^^
Here are all of the public methods that can be used with `BinaryTreeNode()`
objects:

.. autoclass:: extra.trees.binary_tree.BinaryTreeNode
    :members:
    :special-members:
    :exclude-members: set_children

--------------------------------------------------------------------------------

BinaryTree()
^^^^^^^^^^^^
Here are all of the public methods that can be used with `BinaryTree()` objects:

.. autoclass:: extra.trees.binary_tree.BinaryTree
    :members:
    :special-members:
    :exclude-members:
