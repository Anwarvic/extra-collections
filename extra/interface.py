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

# List-based Data Structures:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Linked List
* Doubly Linked List
* Circular Linked List
* Stack
* Queue
* PriorityQueue
* Deque
* SkipList

# Tree-based Data Structures:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and a loose standing reference guide, available from
`the NumPy homepage <https://www.scipy.org>`_.

"""

class Extra:
    """An example docstring for a class definition."""
    
    def __name__(self):
        """
        Blah blah blah.
        Parameters
        ---------
        name
            A string to assign to the `name` instance attribute.
        """
        return "extra.Extra()"
    

    def _validate_item(self, item):
        """
        Return information about an instance created from ExampleClass.
        """
        if item is None:
            raise ValueError(\
                f"Can't use `None` as an initial value for {self.__name__()}!!")
        elif isinstance(item, Extra):
            raise TypeError(\
            f"Can't create {self.__name__()} object using {item.__name__()}!!")
