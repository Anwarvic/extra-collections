.. _avl:

AVL Tree
========

.. automodule:: extra.trees.avl
    :noindex:
    :members:
    :special-members:
    :exclude-members: AVLNode, AVL


⏱ Time-Complexity
-------------------
The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the AVL tree.
- **h** is the AVL tree's height which approximatley equals to **log(n)**.

.. csv-table::
   :file: ../../_files/trees/avl.csv
   :header-rows: 1
   :widths: 10, 70, 10, 10


☕️ API
-------
Here are all of the public methods that can be used with `AVL()` objects:

.. autoclass:: extra.trees.avl.AVL
    :members:
    :special-members:
    :exclude-members:

