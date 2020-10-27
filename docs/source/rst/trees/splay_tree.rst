.. _splay_tree:

Splay Tree
==========

.. automodule:: extra.trees.splay_tree
    :noindex:
    :members:
    :special-members:
    :exclude-members: SplayTree


.. image:: ../../_images/trees/splay_tree.gif
    :align: center
    :height: 650


⏱ Time-Complexity
-------------------
The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of nodes currently in the splay tree.
- **h** is the splay tree's height which approximatley equals to **log(n)**.

.. csv-table::
   :file: ../../_files/trees/splay_tree.csv
   :header-rows: 1
   :widths: 10, 70, 10, 10


☕️ API
-------
Here are all of the public methods that can be used with `SplayTree()` objects:

.. autoclass:: extra.trees.splay_tree.SplayTree
    :members:
    :special-members:
    :exclude-members:

