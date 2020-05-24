"""
Extra Collections
==================

"extra-collections" ("extra" for short) is a python library that provides an
intuitive pythonic implementation of the most common data structures used in 
most of the software projects in the market. Some of these data structures are
simple such as `Stack` or `Queue`; and some are much more complicated such as
`SkipList` or `RedBlackTree`.

The name of this pacakge was inspired by the 
`collections <https://docs.python.org/3.8/library/collections.html>`_ python
library which provides a pythonic implementation for some basic data structures.
"extra" provides an additional set of data structures, hence the name...
"extra-collections".


Available Data Structures
-------------------------
In this release, you can find +20 data structures that can be categorized into
two categories:

1. List-based Data Structures:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* :ref:`linked_list_label`
* Doubly Linked List
* Circular Linked List
* Stack
* Queue
* PriorityQueue
* Deque
* SkipList

2. Tree-based Data Structures:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Tree
* BinaryTree
* BST (Binary Search Tree)
* AVL (Adel'son-Vel'skii and Landis)
* SplayTree
* RedBlackTree
* MinHeap
* MaxHeap
* Treap
* Trie
* RadixTrie
* SuffixTrie



How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and a loose standing reference guide, available from
`the NumPy homepage <https://www.scipy.org>`_.

"""
from numpy import sort
class Extra:
    """Extra is the package interface which means that all objects inherits from
    this class. So, each object in this pacakge is an Extra object in the fisrt
    place."""
    
    def _validate_item(self, item):
        """
        Makes sure the input variable type can be processed. The main use for 
        this method is to make sure we can't create nested objects from the 
        package.
        
        :param item: the input object of any type.
        
        :raises [ValueError]: if `item` is `None`
        :raises [TypeError]: if `item` is an `Extra` object. 
        """
        if item is None:
            raise ValueError(\
                f"Can't use `None` as an initial value for {self.__module__}!!")
        elif isinstance(item, Extra):
            raise TypeError(\
            f"Can't create {self.__module__} object using {item.__module__}!!")
