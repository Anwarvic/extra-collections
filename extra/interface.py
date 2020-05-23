"""
Extra Collections
==================
"extra-collections" ("extra" for short) is a python library that provides an
intuitive pythonic implementation of the most common data structures used in 
in most of the software projects in the market. Some of these data structures
are simple such as `Stack` or `Queue`; and some are much more complicated such
as `SkipList` or `RedBlackTree`.

The name of this pacakge was inspired by a built-in python library called
`collections <https://docs.python.org/3.8/library/collections.html>`_
which provides a pythonic implementation for some basic data structures. "Extra"
provides an extra group of data structures, hence the name "extra-collections".
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
