.. _min_heap:

Min Heap
========

.. automodule:: extra.trees.min_heap
    :noindex:
    :members:
    :special-members:
    :exclude-members: MinHeap


⏱ Time-Complexity
-------------------
The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of nodes currently in the min heap.
- **h** is the height of the heap which approximatley equals to **log(n)**.

.. csv-table::
   :file: ../../_files/trees/min_heap.csv
   :header-rows: 1
   :widths: 10, 70, 10, 10


☕️ API
-------
Here are all of the public methods that can be used with `MinHeap()` objects:

.. autoclass:: extra.trees.min_heap.MinHeap
    :members:
    :special-members:
    :exclude-members:
