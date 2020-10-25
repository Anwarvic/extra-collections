.. _red_black_tree:

Red-Black Tree
==============

.. automodule:: extra.trees.red_black_tree
    :noindex:
    :members:
    :special-members:
    :exclude-members: RedBlackNode, RedBlackTree, Color


.. image:: ../../img/trees/red_black_tree.gif
    :align: center
    :height: 800


⏱ Time-Complexity
-------------------
The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of nodes currently in the red-black tree.
- **h** is the height of the red-black tree which equals to **log(n)**.

.. csv-table::
   :file: ../../_files/trees/red_black_tree.csv
   :header-rows: 1
   :widths: 10, 70, 10, 10


☕️ API
-------
Here are all of the public methods that can be used with `RedBlackTree()`
objects:

.. autoclass:: extra.trees.red_black_tree.RedBlackTree
    :members:
    :special-members:
    :exclude-members:
