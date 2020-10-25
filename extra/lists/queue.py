"""
A queue is a close cousin of the stack, as a queue is a collection of objects
that are inserted and removed according to the first-in, first-out (FIFO)
principle. That is, elements can be inserted at any time,
but only the element that has been in the queue the longest can be next
removed. We usually say that elements enter a queue at the back and are removed
from the front.
"""
import warnings
from extra.interface import Extra
from extra.lists.doubly_linked_list import DoublyLinkedList


class Queue(Extra):
    """
    A queue is a close cousin of the stack, as a queue is a collection of
    objects that are inserted and removed according to the first-in, first-out
    (FIFO) principle. That is, elements can be inserted at any time, but only
    the element that has been in the queue the longest can be next removed. We
    usually say that elements enter a queue at the back and are removed from
    the front.
    """

    __name__ = "extra.Queue()"

    def __init__(self, max_capacity=float("inf")):
        """
        Creates a `Queue()` object!!

        Parameters
        ----------
        max_capacity: int
            It's a positive integer representing the maximum number of elements
            a `Queue()` should contain (Default: inf).

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
        self._max_capacity = (
          round(max_capacity) if max_capacity != float("inf") else max_capacity
        )

    # =============================     PRINT    ==============================
    def _print_queue(self, direction_char=" "):
        """
        Represents the `Queue()` instance as a string.

        Parameters
        ----------
        direction_char: str
            A character that shows the direction when needed. A space character
            shows that there's no direction. (Default: ' ')

        Returns
        -------
        str:
            A string representing the content of the `Queue()` instance.

        Example
        -------
        >>> q = Queue()
        >>> q.enqueue(10)
        >>> print(q._print_queue())
        ─┬────┬─
         │ 10 │
        ─┴────┴─
        >>> print(q._print_queue('x'))
        ─┬────┬─
        x│ 10 │x
        ─┴────┴─
        >>> print(q._print_queue('⟶'))
        ─┬────┬─
        ⟶│ 10 │⟶
        ─┴────┴─
        """
        top_border = "─┬"
        middle_border = direction_char + "│"
        down_border = "─┴"
        curr_node = self._container._head
        while curr_node is not None:
            # NOTE: +2 for a space before & after `curr_node`
            width = len(curr_node._represent()) + 2
            top_border += ("─" * width) + "┬"
            middle_border += f" {curr_node._represent()} │"
            down_border += ("─" * width) + "┴"
            curr_node = curr_node.get_next()
        # add extension
        if not self.is_empty():
            top_border += "─"
            middle_border += direction_char
            down_border += "─"
        return "{}\n{}\n{}".format(top_border, middle_border, down_border)

    def __repr__(self):
        """
        Represents the `Queue()` instance as a string.

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
        return self._print_queue(direction_char="⟶")

    # =============================    LENGTH    ==============================
    def __len__(self):
        """
        Gets the length of the `Queue()` instance in constant time.

        Returns
        -------
        int:
            The length of the `Queue()` instance. By Length, I mean the number
            of nodes of in the instance.

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
        Checks if `Queue()` instance is empty or not in constant time.

        Returns
        -------
        bool:
            A boolean flag showing if the `Queue()` instance is empty or not.
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
        Checks if `Queue()` instance is at full-capacity in constant time.

        Returns
        -------
        bool:
            A boolean flag showing if the `Queue()` instance is full or not.
            `True` shows that this instance is full and `False` shows it's not
            full.

        Example
        --------
        >>> q = Queue(max_capacity=2)
        >>> q.is_full()
        False
        >>> q.enqueue(5)
        >>> q.is_full()
        False
        >>> q.enqueue(10)
        >>> q.is_full()
        True
        """
        return len(self) == self._max_capacity

    # =============================    ENQUEUE   ==============================
    def _enqueue(self, item):
        """
        Inserts the given `item` to end of the `Queue()`, it does that in
        constant time.

        Parameters
        ----------
        item: object
            The python object to be pushed to the `Queue()`.

        Raises
        ------
        UserWarning:
            If the `Queue()` instance was full!! By "full", I mean the number
            of items in the `Queue()` equals to the assigned maximum capacity.
        AssertionError:
            If the given `item` is `None`

        Example
        -------
        >>> q = Queue(max_capacity=2)
        >>> q
        ─┬
        ⟶│
        ─┴
        >>> q._enqueue(1)
        >>> q._enqueue(2)
        >>> q
        ─┬───┬───┬─
        ⟶│ 2 │ 1 │⟶
        ─┴───┴───┴─
        >>> q._enqueue(3)
        UserWarning: Enqueuing to a full `extra.Queue()` could lead to \
            missing values!!
        >>> q
        ─┬───┬───┬─
        ⟶│ 3 │ 2 │⟶
        ─┴───┴───┴─
        """
        assert item is not None
        if self.is_full():
            warnings.warn(
                f"Enqueuing to a full `{self.__name__}` "
                + "could lead to missing values!!",
                UserWarning,
            )
            self._container.remove_end()
        if self._max_capacity > 0:
            self._container._insert(0, item)

    def enqueue(self, item):
        """
        Inserts the given `item` to end of the `Queue()`, it does that in
        constant time.

        Parameters
        ----------
        item: object
            The python object to be pushed to the `Queue()`.

        Raises
        ------
        UserWarning:
            If the Queue() instance was full!! By "full", I mean the number of
            items in the Queue() equals to the assigned maximum capacity.
        ValueError:
            If the given `item` is `None`.
        TypeError:
            If the given `item` is an instance of `Extra`.

        Example
        -------
        >>> q = Queue(max_capacity=2)
        >>> q
        ─┬
        ⟶│
        ─┴
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q
        ─┬───┬───┬─
        ⟶│ 2 │ 1 │⟶
        ─┴───┴───┴─
        >>> q.enqueue(3)
        UserWarning: Enqueuing to a full `extra.Queue()` could lead to \
            missing values!!
        >>> q
        ─┬───┬───┬─
        ⟶│ 3 │ 2 │⟶
        ─┴───┴───┴─
        """
        super()._validate_item(item)
        self._enqueue(item)

    # =============================      TOP     ==============================
    def top(self):
        """
        Returns the first item inserted to the `Queue()` instance in constant
        time.

        Returns
        -------
        object:
            The `Queue()` instance's first inserted item.

        Raises
        ------
        IndexError:
            If the `Queue()` instance is empty!!

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

    # =============================    DEQUEUE   ==============================
    def dequeue(self):
        """
        Pops the first inserted item from the `Queue()` in constant time.

        Returns
        -------
        object:
            The `Queue()` instance's first item.

        Raises
        ------
        UserWarning:
            If the `Queue()` instance is empty!!

        Example
        -------
        >>> q = Queue()
        >>> q.dequeue()
        UserWarning: Dequeuing from empty `extra.Queue()`!!
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
                f"Dequeuing from an empty `{self.__name__}`!!", UserWarning
            )
            return
        else:
            tail_value = self._container._tail.get_data()
            self._container.remove_end()
            return tail_value

    def clear(self):
        """
        Removes all objects within the `Queue()` instance in constant time.

        Example
        -------
        >>> q = Queue()
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.enqueue(3)
        >>> q
        ─┬───┬───┬───┬─
        ⟶│ 3 │ 2 │ 1 │⟶
        ─┴───┴───┴───┴─
        >>> len(q)
        3
        >>> q.clear()
        >>> q
        ─┬
        ⟶│
        ─┴
        >>> len(q)
        0

        Note
        ----
        When you clear the `Queue()` instance, the `max_capacity` of the
        cleared instance remains the same as the one before.
        """
        self.__init__(max_capacity=self._max_capacity)
