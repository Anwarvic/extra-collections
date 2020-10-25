.. _skip_list:

Skip List
=========

.. automodule:: extra.lists.skip_list
    :noindex:
    :members:
    :special-members:
    :exclude-members: flip_coin, search_sorted, SkipNode, SkipList


.. image:: ../../img/lists/skip_list.gif
    :align: center
    :height: 800


⏱ Time-Complexity
-------------------
The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the skip list.
- **k** is the value of a parameter.
- **h** is the height of the skip list.

.. csv-table::
   :file: ../../_files/lists/skip_list.csv
   :header-rows: 1
   :widths: 10, 70, 10, 10


☕️ API
-------
Here are all of the public methods that can be used with `SkipList()` objects:

.. autoclass:: extra.lists.skip_list.SkipList
    :members:
    :special-members:
    :exclude-members:
