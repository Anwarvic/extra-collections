"""
A queue is a close cousin of the queue, as a queue is a collection of objects
that are inserted and removed according to the first-in, first-out (FIFO)
principle. That is, elements can be inserted at any time,
but only the element that has been in the queue the longest can be next removed.
We usually say that elements enter a queue at the back and are removed from
the front.

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
| __len__()  | Returns the number of values in the queue. | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| enqueue()  | Adds new value to the top of the queue.    | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| dequeue()  | Adds the value from the top of the queue.  | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| top()      | Returns the value at the top of the queue. | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| clear()    | Clears the queue.                          | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| is_empty() | Checks if the queue is empty.              | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| is_full()  | Checks if the queue is full.               | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
"""
import warnings
from extra.interface import Extra
from extra.lists.doubly_linked_list import DoublyLinkedList




class Queue(Extra):
    """Basic object for the Queue data structure"""
    __name__ = "extra.Queue()"
    
    
    def __init__(self, max_capacity=float("inf")):
        """
        Creates a Queue() object!!
        
        Parameters
        ----------
        max_capacity: int
            It'q a positive integer representing the maximum number of elements
            a Queue() should contain (Default: inf).
        
        Raises
        ------
        TypeError: If the type of `max_capacity` isn't `int` or `float`.
        ValueError: If the given value of `max_capacity` is less than zero.

        Example
        -------
        >>> q = Queue()
        >>> type(q)
        <class 'extra.lists.queue.Queue'>
        >>> q._max_capacity
        inf

        You can define the maximum capacity for your own instance:

        >>> q = Queue(10)
        >>> q._max_capacity
        10

        Note
        ----
        If you passed a `float` number as the maximum capacity, then the value
        that get assigned is the rounding of that number:

        >>> q = Queue(10.6)
        >>> q._max_capacity
        11
        """
        if type(max_capacity) not in {int, float}:
            raise TypeError(
                f"Max Capacity of `{self.__name__}` has to be a number!!"
            )
        elif max_capacity < 0:
            raise ValueError(
                f"Max capacity of `{self.__name__}` has to be >= 0"
            )
        self._container = DoublyLinkedList()
        self._max_capacity = round(max_capacity) \
            if max_capacity != float("inf") \
            else max_capacity


    ##############################      PRINT     ##############################
    def _print_queue(self, direction_char=' '):
        """
        Represents the Queue() instance as a string.

        Parameters
        ----------
        direction_char: str
            A character that shows the direction when needed. A space character
            shows that there'q no direction. (Default: ' ')
        
        Returns
        -------
        str:
            A string representing the content of the Queue() instance.
        
        Example
        -------
        >>> q = Queue()
        >>> q.enqueue(10)
        >>> q._print_queue()
        ─┬────┬─
         │ 10 │ 
        ─┴────┴─
        >>> q._print_queue('x')
        ─┬────┬─
        x│ 10 │x
        ─┴────┴─
        >>> q._print_queue('⟶')
        ─┬────┬─
        ⟶│ 10 │⟶
        ─┴────┴─
        """
        top_border = '─┬'
        middle_border = direction_char+'│'
        down_border = '─┴'
        curr_node = self._container._head
        while curr_node is not None:
            #NOTE: +2 for a space before & after `curr_node`
            width = len(curr_node._represent())+2
            top_border += ('─'*width) + '┬'
            middle_border += f" {curr_node._represent()} │"
            down_border += ('─'*width) + '┴'
            curr_node = curr_node.get_next()
        # add extension
        if not self.is_empty():
            top_border += '─'
            middle_border += direction_char
            down_border += '─'
        return "{}\n{}\n{}".format(top_border, middle_border, down_border)


    def __repr__(self):
        """
        Represents the Queue() instance as a string.

        Returns
        -------
        str:
            The string-representation of the `Queue()` instance.
        
        Example
        -------
        >>> q = Queue()
        >>> q.enqueue(10)
        >>> q.enqueue(20)
        >>> q
        ─┬────┬────┬─
        ⟶│ 20 │ 10 │⟶
        ─┴────┴────┴─
        """
        return self._print_queue(direction_char='⟶')


    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the Queue() instance in time-complexity of O(1).

        Returns
        -------
        int:
            The length of the Queue() instance. By Length, I mean the
            number of nodes of in the instance.
        
        Examples
        --------
        >>> q = Queue()
        >>> len(q)
        0
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.enqueue(3)
        >>> len(q)
        3
        """
        return len(self._container)


    def is_empty(self):
        """
        Checks if Queue() instance is empty or not in time-complexity of O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the Queue() instance is empty or not.
            `True` shows that this instance is empty and `False` shows it's not
            empty.
        
        Example
        --------
        >>> q = Queue()
        >>> q.is_empty()
        True
        >>> q.enqueue(5)
        >>> q.is_empty()
        False
        """
        return self._container.is_empty()


    def is_full(self):
        """
        Checks if Queue() instance is at full-capacity in time-complexity of
        O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the Queue() instance is full or not.
            `True` shows that this instance is full and `False` shows it'q not
            full.
        
        Example
        --------
        >>> q = Queue(max_capacity=2)
        >>> q.is_full()
        False
        >>> q.enqueue(5)
        >>> q.is_full()
        True
        >>> q.enqueue(10)
        >>> q.is_full()
        True
        """
        return len(self) == self._max_capacity
    

    ##############################     ENQUEUE    ##############################
    def _enqueue(self, item):
        """
        Inserts the given `item` to end of the Queue(), it does that in time-
        complexity of O(1). 

        Parameters
        ----------
        item: object
            The python object to be pushed to the Queue().
        
        Raises
        ------
        UserWarning: If the Queue() instance was full!! By "full", I mean \
            the number of items in the Queue() equals to the assigned maximum
            capacity.
        AssertionError: If the given `item` is `None` or an instance of `Extra`

        Example
        -------
        >>> q = Queue(max_capactity=2)
        >>> q
        ┌─
        │ 
        └─
        >>> q._enqueue(1)
        >>> q._enqueue(2)
        >>> q
        ─┬───┬───┬─
        ⟶│ 2 │ 1 │⟶
        ─┴───┴───┴─
        >>> q._enqueue(3)
        UserWarning: Enqueuing to a full `extra.Queue()` could lead to missing values!!
        >>> q
        ─┬───┬───┬─
        ⟶│ 3 │ 2 │⟶
        ─┴───┴───┴─
        """
        assert item is not None and not isinstance (item, Extra)
        if self.is_full():
            warnings.warn(
                f"Enqueuing to a full `{self.__name__}` " +
                "could lead to missing values!!",
                UserWarning
            )
            self._container.remove_end()
        return self._container._insert(0, item)


    def enqueue(self, item):
        """
        Inserts the given `item` to end of the Queue(), it does that in time-
        complexity of O(1). 

        Parameters
        ----------
        item: object
            The python object to be pushed to the Queue().
        
        Raises
        ------
        UserWarning: If the Queue() instance was full!! By "full", I mean \
            the number of items in the Queue() equals to the assigned maximum
            capacity.
        AssertionError: If the given `item` is `None` or an instance of `Extra`

        Example
        -------
        >>> q = Queue(max_capactity=2)
        >>> q
        ┌─
        │ 
        └─
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q
        ─┬───┬───┬─
        ⟶│ 2 │ 1 │⟶
        ─┴───┴───┴─
        >>> q.enqueue(3)
        UserWarning: Enqueuing to a full `extra.Queue()` could lead to missing values!!
        >>> q
        ─┬───┬───┬─
        ⟶│ 3 │ 2 │⟶
        ─┴───┴───┴─
        """
        super()._validate_item(item)
        self._enqueue(item)


    ##############################      TOP     ################################
    def top(self):
        """
        Returns the first item inserted to the Queue() instance in time-
        complexity of O(1).

        Returns
        -------
        object:
            The Queue() instance's first inserted item.
        
        Raises
        ------
        IndexError: If the Queue() instance is empty!!

        Example
        -------
        >>> q = Queue()
        >>> q.top()
        IndexError: Can't retrieve from an empty `extra.Queue()`!!
        >>> q.enqueue(10)
        >>> q.enqueue(20)
        >>> q
        ─┬────┬────┬─
        ⟶│ 20 │ 10 │⟶
        ─┴────┴────┴─
        >>> q.top()
        10
        """
        if self.is_empty():
            raise IndexError(
                f"Can't retrieve from an empty `{self.__name__}`!!"
            )
        return self._container._tail.get_data()



    ##############################    DEQUEUE     ##############################
    def dequeue(self):
        """
        Pops the first inserted item from the Queue() in time-complexity of
        O(1).
        
        Returns
        -------
        object:
            The Queue() instance's first item.
        
        Raises
        ------
        UserWarning: If the Queue() instance is empty!!

        Example
        -------
        >>> q = Queue()
        >>> q.dequeue()
        UserWarning: Popping from empty `extra.Queue()`!!
        >>> q.enqueue(10)
        >>> q.enqueue(20)
        >>> q
        ─┬────┬────┬─
        ⟶│ 20 │ 10 │⟶
        ─┴────┴────┴─
        >>> q.dequeue()
        10
        >>> q
        ─┬────┬─
        ⟶│ 20 │⟶
        ─┴────┴─
        """
        if self.is_empty():
            warnings.warn(
                f"Dequeuing from an empty `{self.__name__}`!!",
                UserWarning
            )
            return
        else:
            tail_value = self._container._tail.get_data()
            self._container.remove_end()
            return tail_value


    def clear(self):
        self.__init__(max_capacity=self._max_capacity)


