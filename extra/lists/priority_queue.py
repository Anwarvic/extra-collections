"""
A priority queue is a collection of prioritized elements that allows arbitrary
element insertion, and allows the removal of the element that has the highest
priority. When an element is added to a priority queue, the user designates its
priority by providing an associated priority. The element with the minimum 
priority will be the next to be removed from the queue.

In other words, a piority queue is data structure where each node contains two
values:

- **data**: The value inserted to the queue.
- **priority**: A numeric value that indicates how important this object is. \
    The bigger this numeric value is, the higher its priority in the queue is.

Note
----
The priority values are always hidden. If you want to see the priorty for each
item in the PriorityQueue(), you can set the static variable `SHOW_PRIORITY` to
`True` just like so:

>>> PriorityQueue.SHOW_PRIORITY = True

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
| dequeue()  | Adds the value from the top of the queue.  | O(n)        | O(n)        |
+------------+--------------------------------------------+-------------+-------------+
| top()      | Returns the value at the top of the queue. | O(n)        | O(n)        |
+------------+--------------------------------------------+-------------+-------------+
| clear()    | Clears the queue.                          | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| is_empty() | Checks if the queue is empty.              | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+
| is_full()  | Checks if the queue is full.               | O(1)        | O(1)        |
+------------+--------------------------------------------+-------------+-------------+



Class Documentation
===================
Here are all of the public methods that can be used with `PriorityQueue()` objects:
"""
import random
import warnings
from extra.lists.doubly_linked_list import DoublyNode
from extra.lists.queue import Queue




class PriorityNode(DoublyNode):
    """Basic object for item inside Priority PriorityQueue"""
    __name__ = "extra.DoublyNode()"


    def __init__(self, item, priority=None):
        """
        Creates a `PriorityNode()` object used mainly with PriorityQueue()
        objects!!

        Parameters
        ----------
        item: object
            The value to be saved within the `DoublyNode()` instance.
        priority: int or float
            It is a numeric value that indicates how important this object is.
            The bigger this numeric value is, the higher its priority in the
            queue is. If `priority=None`, then a random integer number will be
            assigned.

        Raises
        ------
        ValueError: If the given item is `None`.
        TypeError: If the given item is an `Extra` object.
        """
        if priority is not None and type(priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
        super()._validate_item(item)
        super().__init__(item)
        self._priority = \
            random.randint(0, 100) if priority is None else priority
    

    def get_priority(self):
        """
        Returns the priority of the current node.

        Returns
        -------
        int or float:
            The priority of the current node.
        """
        return self._priority


    def set_priority(self, new_priority):
        """
        Sets the priority of the current node with the new value.

        Parameters
        ----------
        new_priority: int or float
            The new priority of the node.

        Raises
        ------
        TypeError: If the given priority isn't a number.
        """
        if type(new_priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
        self._priority = new_priority


    def __repr__(self):
        """Represents Node object as a string"""
        return f"PriorityNode(data: {self._data}, Priority: {self._priority})"

    
    def _represent(self):
        if PriorityQueue.SHOW_PRIORITY:
            return f"{self._data}|P:{self._priority}"
        else:
            return f"{self._data}"




class PriorityQueue(Queue):
    """Basic object for the Priority PriorityQueue data structure."""
    SHOW_PRIORITY = False
    __name__ = "extra.PriorityQueue()"


    def __init__(self, max_capacity=float("inf")):
        """
        Creates a PriorityQueue() object!!
        
        Parameters
        ----------
        max_capacity: int
            It's a positive integer representing the maximum number of elements
            a PriorityQueue() should contain (Default: inf).
        
        Raises
        ------
        TypeError: If the type of `max_capacity` isn't `int` or `float`.
        ValueError: If the given value of `max_capacity` is less than zero.

        Example
        -------
        >>> pq = PriorityQueue()
        >>> type(pq)
        <class 'extra.lists.priority_queue.PriorityQueue'>
        >>> pq._max_capacity
        inf

        You can define the maximum capacity for your own instance:

        >>> pq = PriorityQueue(10)
        >>> pq._max_capacity
        10

        Note
        ----
        If you passed a `float` number as the maximum capacity, then the value
        that get assigned is the rounding of that number:

        >>> pq = PriorityQueue(10.6)
        >>> pq._max_capacity
        11
        """
        super().__init__(max_capacity)
        self._min_priority = float("inf")
        self._max_priority = float("-inf")
    

    ##############################      PRINT     ##############################
    def __repr__(self):
        """
        Represents the PriorityQueue() instance as a string.

        Returns
        -------
        str:
            The string-representation of the `PriorityQueue()` instance.
        
        Example
        -------
        >>> pq = PriorityQueue()
        >>> pq.enqueue(10, priority=1)
        >>> pq.enqueue(20, priority=5)
        >>> pq
        ─┬────┬────┬─
        ⟶│ 20 │ 10 │⟶
        ─┴────┴────┴─

        You can show the priority of these items by enabling `SHOW_PRIOIRYT`
        static variable:

        >>> PriorityQueue.SHOW_PRIORITY = True
        >>> pq
        ─┬────────┬────────┬─
        ⟶│ 20|P:5 │ 10|P:1 │⟶
        ─┴────────┴────────┴─
        """
        return super().__repr__()
    

    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the PriorityQueue() instance in time-complexity of
        O(1).

        Returns
        -------
        int:
            The length of the PriorityQueue() instance. By Length, I mean the
            number of elements of in the instance.
        
        Examples
        --------
        >>> pq = PriorityQueue()
        >>> len(pq)
        0
        >>> pq.enqueue(1)
        >>> pq.enqueue(2)
        >>> pq.enqueue(3)
        >>> len(pq)
        3
        """
        return super().__len__()


    def is_empty(self):
        """
        Checks if PriorityQueue() instance is empty or not in time-complexity of
        O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the PriorityQueue() instance is empty or
            not. `True` shows that this instance is empty and `False` shows it's
            not empty.
        
        Example
        --------
        >>> pq = PriorityQueue()
        >>> pq.is_empty()
        True
        >>> pq.enqueue(5)
        >>> pq.is_empty()
        False
        """
        return super().is_empty()


    def is_full(self):
        """
        Checks if PriorityQueue() instance is at full-capacity in time-
        complexity of O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the PriorityQueue() instance is full or
            not. `True` shows that this instance is full and `False` shows it's
            not full.
        
        Example
        --------
        >>> pq = PriorityQueue(max_capacity=2)
        >>> pq.is_full()
        False
        >>> pq.enqueue(5)
        >>> pq.is_full()
        False
        >>> pq.enqueue(10)
        >>> pq.is_full()
        True
        """
        return super().is_full()
    

    ##############################     ENQUEUE    ##############################
    def __validate_priority(self, new_priority):
        """
        Checks the validity of the given priority. It raises the appropriate
        error when the priority value isn't valid and it returns nothing if the
        priority value is valid.

        Parameters
        ----------
        idx: int
            The priority value.
        
        Raises
        ------
        TypeError: If the given priority value isn't a number.
        
        Examples
        --------
        >>> pq = PriorityQueue()
        >>> pq.__validate_priority("10")
        TypeError: Given priority has to be a number!!
        
        And it would return nothing if the given index if valid:

        >>> pq.__validate_priority(10)
        >>> pq.__validate_priority(-2)
        >>> pq.__validate_priority(2.3)
        """
        if new_priority is not None and type(new_priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
    

    def enqueue(self, item, priority=None):
        """
        Inserts the given `item` to the end of the PriorityQueue(), it does that
        in time-complexity of O(1). 

        Parameters
        ----------
        item: object
            The python object to be pushed to the PriorityQueue().
        priority: int or float
            The priority is a numeric value that indicates how important this
            object is. The bigger this numeric value is, the higher its priority
            in the queue is. If `priority=None`, then a random integer number
            will be assigned.
        
        Raises
        ------
        UserWarning: If the PriorityQueue() instance was full!! By "full", I \
            mean the number of items in the PriorityQueue() equals to the \
            assigned maximum capacity.
        ValueError: If the given `item` is `None`.
        TypeError: It can be raised due to one of the following reasons:
            1. If the given `item` is an instance of `Extra`.
            2. If the given `priority` isn't a number.

        Example
        -------
        >>> pq = PriorityQueue(max_capactity=2)
        >>> pq
        ─┬
        ⟶│
        ─┴
        >>> pq.enqueue(1)
        >>> pq.enqueue(2)
        >>> pq
        ─┬───┬───┬─
        ⟶│ 2 │ 1 │⟶
        ─┴───┴───┴─
        >>> pq.enqueue(3)
        UserWarning: Enqueuing to a full `extra.PriorityQueue()` could lead to missing values!!
        >>> pq
        ─┬───┬───┬─
        ⟶│ 3 │ 2 │⟶
        ─┴───┴───┴─
        """
        super()._validate_item(item)
        self.__validate_priority(priority)
        node = PriorityNode(item, priority)
        self._min_priority = min(self._min_priority, node.get_priority())
        self._max_priority = max(self._max_priority, node.get_priority())
        super()._enqueue(node)
    

    ##############################      TOP     ################################
    def top(self):
        """
        Returns the first item inserted to the PriorityQueue() instance in time-
        complexity of O(1).

        Returns
        -------
        object:
            The PriorityQueue() instance's first inserted item.
        
        Raises
        ------
        IndexError: If the PriorityQueue() instance is empty!!

        Example
        -------
        >>> pq = PriorityQueue()
        >>> pq.top()
        IndexError: Can't retrieve from an empty `extra.PriorityQueue()`!!
        >>> pq.enqueue(10)
        >>> pq.enqueue(20)
        >>> pq
        ─┬────┬────┬─
        ⟶│ 20 │ 10 │⟶
        ─┴────┴────┴─
        >>> pq.top()
        10
        """
        return super().top()
    

    ##############################     DEQUEUE    ##############################
    def _update_min_priority(self):
        """
        Updates the value of `_min_priority` member variable by iterating over
        the PriorityQueue() instance and assigns it to the lowest priority. If
        the PriorityQueue() is empty, then the value of `_min_priority` will be
        `inf`.
        """
        self._min_priority = float("inf")
        if not self.is_empty():
            curr_node = self._container._head
            while(curr_node is not None):
                self._min_priority = \
                    min(curr_node.get_priority(), self._min_priority)
                curr_node = curr_node.get_next()
    

    def _update_max_priority(self):
        """
        Updates the value of `_max_priority` member variable by iterating over
        the PriorityQueue() instance and assigns it to the highest priority. If
        the PriorityQueue() is empty, then the value of `_max_priority` will be
        `-inf`.
        """
        self._max_priority = float("-inf")
        if not self.is_empty():
            curr_node = self._container._head
            while(curr_node is not None):
                self._max_priority = \
                    max(curr_node.get_priority(), self._max_priority)
                curr_node = curr_node.get_next()


    def dequeue(self, lowest_priority=False):
        """
        Pops the item that has the highest priority from the PriorityQueue()
        instance in time-complexity of O(1).
        
        Returns
        -------
        object:
            The item that has the highest priority in the PriorityQueue().
        
        Raises
        ------
        UserWarning: If the PriorityQueue() instance is empty!!

        Example
        -------
        >>> pq = PriorityQueue()
        >>> PriorityQueue.SHOW_PRIORITY = True
        >>> pq.dequeue()
        UserWarning: Dequeuing from empty `extra.PriorityQueue()`!!
        >>> pq.enqueue(10, priority=0)
        >>> pq.enqueue(20, prioirty=2)
        >>> pq
        ─┬────────┬────────┬─
        ⟶│ 20|P:2 │ 10|P:0 │⟶
        ─┴────────┴────────┴─
        >>> pq.dequeue()
        20
        >>> pq
        ─┬────────┬─
        ⟶│ 10|P:0 │⟶
        ─┴────────┴─
        """
        if self.is_empty():
            warnings.warn(
                f"Dequeuing from an empty `{self.__name__}`!!",
                UserWarning
            )
            return
        else:
            curr_node = self._container._head
            while(curr_node is not None):
                if lowest_priority:
                    if curr_node.get_priority() == self._min_priority:
                        node_data = curr_node.get_data()
                        self._container._remove_node(curr_node.get_prev(),
                                                    curr_node)
                        self._update_min_priority()
                        break
                else:
                    if curr_node.get_priority() == self._max_priority:
                        node_data = curr_node.get_data()
                        self._container._remove_node(curr_node.get_prev(),
                                                    curr_node)
                        self._update_max_priority()
                        break
                curr_node = curr_node.get_next()
        return node_data


    def clear(self):
        """
        Removes all objects within the PriorityQueue() instance in time-
        complexity of O(1).

        Example
        -------
        >>> pq = PriorityQueue()
        >>> pq.enqueue(1)
        >>> pq.enqueue(2)
        >>> pq.enqueue(3)
        ─┬───┬───┬───┬─
        ⟶│ 3 │ 2 │ 1 │⟶
        ─┴───┴───┴───┴─
        >>> len(pq)
        3
        >>> pq.clear()
        >>> pq
        ─┬
        ⟶│
        ─┴
        >>> len(pq)
        0

        Note
        ----
        When you clear the PriorityQueue() instance, the max capacity remains
        the same as before.
        """
        super().clear()


