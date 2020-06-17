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
    The bigger this numeric value is, the higher its priority in thq queue is.

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
    def __init__(self, key, priority=None):
        if priority is not None and type(priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
        super()._validate_item(key)
        super().__init__(key)
        self._priority = \
            random.randint(0, 100) if priority is None else priority
    

    def get_priority(self):
        return self._priority


    def set_priority(self, new_priority):
        assert type(new_priority) in {int, float}
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
        return super().__len__()


    def is_empty(self):
        return super().is_empty()


    def is_full(self):
        return super().is_full()
    

    ##############################     ENQUEUE    ##############################
    def __validate_priority(self, new_priority):
        if new_priority is not None and type(new_priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
    

    def enqueue(self, item, priority=None):
        super()._validate_item(item)
        self.__validate_priority(priority)
        node = PriorityNode(item, priority)
        self._min_priority = min(self._min_priority, node.get_priority())
        self._max_priority = max(self._max_priority, node.get_priority())
        super()._enqueue(node)
    

    ##############################      TOP     ################################
    def top(self):
        return super().top()
    

    ##############################     DEQUEUE    ##############################
    def _update_min_priority(self):
        self._min_priority = float("inf")
        if not self.is_empty():
            curr_node = self._container._head
            while(curr_node is not None):
                self._min_priority = \
                    min(curr_node.get_priority(), self._min_priority)
                curr_node = curr_node.get_next()
    

    def _update_max_priority(self):
        self._max_priority = float("-inf")
        if not self.is_empty():
            curr_node = self._container._head
            while(curr_node is not None):
                self._max_priority = \
                    max(curr_node.get_priority(), self._max_priority)
                curr_node = curr_node.get_next()


    def dequeue(self, lowest_priority=False):
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
        super().clear()


