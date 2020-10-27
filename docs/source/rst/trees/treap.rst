.. _treap:

Treap
=====

.. automodule:: extra.trees.treap
    :noindex:
    :members:
    :special-members:
    :exclude-members: TreapNode, Treap


.. image:: ../../_images/trees/treap.gif
    :align: center
    :height: 650


⏱ Time-Complexity
-------------------
The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of nodes currently in the treap.
- **h** is the height of the treap which approximatley equals to **log(n)**
    when the tree is balanced.

.. csv-table::
   :file: ../../_files/trees/treap.csv
   :header-rows: 1
   :widths: 10, 70, 10, 10


☕️ API
-------
Here are all of the public methods that can be used with `Treap()` objects:

.. autoclass:: extra.trees.treap.Treap
    :members:
    :special-members:
    :exclude-members:
