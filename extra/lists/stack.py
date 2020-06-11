"""
A stack is the simplest linear data structure where objects that are inserted
and removed according to the last-in, first-out (LIFO) principle. A user may
insert objects into a stack at any time, but may only access or remove the most
recently inserted object that remains at, the so-called, **top** of the stack.

[image]

The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **m** is the number of elements in the *other* container.
- **k** is the value of a parameter.

+------------+--------------------------------------------+-------------+-------------+
| Method     | Description                                | Worst-case  | Optimal     |
+============+============================================+=============+=============+
| __len__()  | Returns the number of values in the stack. | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| push()     | Adds new value to the top of the stack.    | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| pop()      | Adds the value from the top of the stack.  | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| peek()     | Returns the value at the top of the stack. | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| clear()    | Clears the stack.                          | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| is_empty() | Checks if the stack is empty.              | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| is_full()  | Checks if the stack is full.               | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
"""
import warnings
from extra.interface import Extra




class Stack(Extra):
    """Basic object for the Stack data structure"""
    __name__ = "extra.Stack()"

    
    def __init__(self, max_capacity=float("inf")):
        """
        Creates a Stack() object!!
        
        Parameters
        ----------
        max_capacity: int
            It's a positive integer representing the maximum number of elements
            a Stack() should contain (Default: inf).
        
        Raises
        ------
        TypeError: If the type of `max_capacity` isn't `int` or `float`.
        ValueError: If the given value of `max_capacity` is less than zero.

        Example
        -------
        >>> s = Stack()
        >>> type(s)
        <class 'extra.lists.stack.Stack'>
        >>> s._max_capacity
        inf

        You can define the maximum capacity for your own instance:

        >>> s = Stack(10)
        >>> s._max_capacity
        10

        Note
        ----
        If you passed a `float` number as the maximum capacity, then the value
        that get assigned is the rounding of that number:

        >>> s = Stack(10.6)
        >>> s._max_capacity
        11
        """
        if type(max_capacity) not in {int, float}:
            raise TypeError(
                f"Max Capacity `{self.__name__}` has to be a number!!"
            )
        elif max_capacity < 0:
            raise ValueError(
                f"Max capacity of `{self.__name__}` has to be >= 0"
            )
        self._container = []
        
        self._max_capacity = round(max_capacity) \
            if max_capacity != float("inf") \
            else max_capacity


    ############################## PRINT ##############################
    def __repr__(self):
        """
        Represents the Stack() instance as a string.

        Returns
        -------
        str:
            The string-representation of the `Stack()` instance.
        
        Example
        -------
        >>> s = Stack()
        >>> s.push(10)
        >>> s.push(20)
        >>> s
        ┌────┬────┬─
        │ 10 │ 20 │ 
        └────┴────┴─
        """
        top_border    = '┌'
        middle_border = '│'
        down_border   = '└'
        for item in self._container:
            #NOTE: +2 for a space before & after `item`
            width = len(str(item))+2
            top_border += ('─'*width) + '┬'
            middle_border += " {} │".format(item)
            down_border += ('─'*width) + '┴'
        # add extension
        top_border += '─'
        middle_border += ' '
        down_border += '─'
        return "{}\n{}\n{}".format(top_border, middle_border, down_border)


    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the Stack() instance in time-complexity of O(1).

        Returns
        -------
        int:
            The length of the Stack() instance. By Length, I mean the
            number of nodes of in the instance.
        
        Examples
        --------
        >>> s = Stack()
        >>> len(s)
        0
        >>> s.puah(1)
        >>> s.push(2)
        >>> s.push(3)
        >>> len(s)
        3
        """
        return len(self._container)


    ##############################      PUSH     ###############################
    def push(self, item):
        """Pushs item to the stack"""
        if self.is_full():
            raise OverflowError(\
                f"Stackoverflow! Can't push into a full `{self.__name__}`!!")
        super()._validate_item(item)
        self._container.append(item)


    ############################## PEEK ###############################
    def peek(self):
        """Returns the top item from the stack"""
        if self.is_empty():
            raise IndexError(f"Can't peek from an empty `{self.__name__}`!!")
        return self._container[-1]


    ############################# REMOVE #############################
    def pop(self):
        """Pops item from the stack"""
        if self.is_empty():
            warnings.warn(
                f"Popping from empty `{self.__name__}`!!",
                UserWarning
            )
            return
        else:
            return self._container.pop()


    def clear(self):
        """Clears the stack"""
        self.__init__(max_capacity=self._max_capacity)


    ############################# STATUS #############################
    def is_empty(self):
        """Checks if the stack is empty"""
        return len(self._container) == 0
    

    def is_full(self):
        """Checks if the stack is at full capacity"""
        return len(self) == self._max_capacity


