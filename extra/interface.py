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
* :ref:`linked_list`
* :ref:`doubly_linked_list`
* :ref:`circular_linked_list`
* :ref:`stack`
* :ref:`queue`
* :ref:`deque`
* :ref:`priority_queue`
* :ref:`skip_list`

2. Tree-based Data Structures:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* :ref:`tree`
* :ref:`binary_tree`
* :ref:`bst`
* :ref:`avl`
* :ref:`splay_tree`
* :ref:`red_black_tree`
* :ref:`min_heap`
* :ref:`max_heap`
* :ref:`treap`
* :ref:`trie`
* :ref:`radix_trie`
* :ref:`suffix_trie`



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
    __name__ = "extra.Extra()"


    def _validate_item(self, item):
        """
        Makes sure the input variable type can be processed. The main use for 
        this method is to make sure we can't create nested objects from the 
        package.
        
        Parameters
        ----------
        item: object
            The input object of any type.
        
        Raises
        -------
        ValueError: If `item` is `None`
        TypeError: If `item` is an `Extra` object.
        """
        if item is None:
            raise ValueError(
                f"Can't use `None` as an element within `{self.__name__}`!!"
            )
        elif isinstance(item, Extra):
            raise TypeError(
                f"Can't use `{self.__name__}` with `{item.__name__}`!!"
              )
