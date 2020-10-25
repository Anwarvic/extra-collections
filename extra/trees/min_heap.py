"""
A heap is a binary tree that stores a collection of nodes. Each node must
satisfy two additional properties:

1. **Heap-Order Property**: It is a relational property defined in terms of the
value stored at the node. So, for every node, other than the root, the value
stored at the node is greater than or equal to the value stored at the node's
parent. As a consequence of the heap-order property, the value encountered on a
path from the root to a leaf node are in nondecreasing order. Also, the minimum
value is always stored at the root of the `MinHeap()`. This makes it easy to
locate such a node when `get_min()` or `remove_min()` is called, as it is
informally said to be at the top of the heap. Hence, the name "Min Heap"

2. **Perfect Binary Tree Property**: It is a structural property defined in
terms of the shape of heap itself. A binary tree is perfect if all its levels
are completely filled. So, given an **n** inserted items, the height of the
heap should be **log(n)** at most.
"""
from extra.trees._heap import Heap


class MinHeap(Heap):
    """
    A Min heap is a perfect binary tree that stores a collection of nodes. Each
    node stores a value greater than or equal to the value strored at the
    node's parent.
    """

    __name__ = "extra.MinHeap()"

    def __init__(self):
        """
        Creates an empty `MinHeap()` object!!

        Example
        -------
        >>> min_heap = MinHeap()
        >>> type(min_heap)
        <class 'extra.trees.min_heap.MinHeap'>
        >>> min_heap
        / \\
        """
        super().__init__()

    @classmethod
    def heapify(cls, iterable):
        """
        A class method which creates a `MinHeap()` instance using an iterable
        object in time-complexity of O(n) where **n** is the number of elements
        inside the given `iterable`.

        Parameters
        ----------
        iterable: iterable
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.

        Returns
        -------
        MinHeap()
            It returns a `MinHeap()` instance with input values being inserted.

        Raises
        ------
        TypeError:
            It can be raised in two cases
                1. In case the given object isn't iterable.
                2. If one of the elements in the iterable is NOT a number.
        ValueError:
            If one of the iterable elements is `None`.

        Examples
        --------
        >>> MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2

        Using an iterable object with `None` as one of its elements will raise
        `ValueError`

        >>> MinHeap.heapify([2, None])
        ValueError: Can't use `None` as an element within `extra.MinHeap()`!!

        Using a non-iterable object will raise `TypeError`

        >>> MinHeap.heapify(2)
        TypeError: The given object isn't iterable!!

        Using nested `MinHeap()` objects will raise `TypeError` as well

        >>> min_heap_1 = MinHeap.heapify([1])
        >>> min_heap_2 = MinHeap.heapify([1, min_heap_1])
        TypeError: Can't create `extra.MinHeap()` using `extra.MinHeap()`!!
        """
        return super().heapify(iterable)

    # =============================    LENGTH    ==============================
    def __len__(self):
        """
        Gets the length of the `MinHeap()` instance in constant time.

        Returns
        -------
        int:
            The length of the `MinHeap()` instance. Length is the number of
            tree nodes in the instance.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2
        >>> len(min_heap)
        7
        """
        return super().__len__()

    def is_empty(self):
        """
        Checks if the `MinHeap()` instance is empty or not in constant time.

        Returns
        -------
        bool:
            A boolean flag showing if the `MinHeap()` instance is empty or not.
            `True` shows that this instance is empty and `False` shows it's
            not empty.

        Example
        --------
        >>> min_heap = MinHeap()
        >>> min_heap.is_empty()
        True
        >>> min_heap.insert(10)
        >>> min_heap.is_empty()
        False
        """
        return super().is_empty()

    # =============================     PRINT    ==============================
    def __repr__(self):
        """
        Represents the `MinHeap()` instance as a string.

        Returns
        -------
        str:
            The string-representation of the `MinHeap()` instance.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2
        """
        return super().__repr__()

    # =============================    MIN/MAX   ==============================
    def get_min(self):
        """
        Gets the minimum value in the `MinHeap()` instance in constant time.
        The minimum value can be found at the root of the `MinHeap()` instance.

        Returns
        -------
        int or float:
            The minimum numeric value in the `MinHeap()` instance.

        Raises
        ------
        IndexError:
            In case the `MinHeap()` instance is empty.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2
        >>> min_heap.get_min()
        0
        """
        if self.is_empty():
            raise IndexError("Can't get the minimum out of an empty Heap!!")
        return self._heap[0]

    def get_max(self):
        """
        Gets the maximum value in the `MinHeap()` instance in linear time.
        The maximum value can be found at the deepest level of the `MinHeap()`
        instance.

        Returns
        -------
        int or float:
            The masximum numeric value in the `MinHeap()` instance.

        Raises
        ------
        IndexError:
            In case the `MinHeap()` instance is empty.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2
        >>> min_heap.get_max()
        9
        """
        if self.is_empty():
            raise IndexError("Can't get the maximum out of an empty Heap!!")
        last_half = self._heap[len(self) // 2:]
        return max(last_half)

    # =============================    SEARCH    ==============================
    def __contains__(self, num):
        """
        Searches the `MinHeap()` for the given value and returns `True` if the
        value exists and `False` if not in linear time.

        Parameters
        ----------
        find_val: int or float
            The value to be searched for in the `MinHeap()` instance.

        Returns
        -------
        bool:
            Returns `True` if the value exists in the `MinHeap()` instance and
            `False` if not.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2
        >>> 9 in min_heap
        True
        >>> 5 in min_heap
        False
        >>> 50 in min_heap
        False
        """
        return super().__contains__(num)

    # =============================    INSERT    ==============================
    def insert(self, value):
        """
        Inserts a numeric value in the `MinHeap()` instance.

        Parameters
        ----------
        value: int or float
            The new numeric value that will be inserted.

        Raises
        ------
        ValueError:
            If the given `value` is `None`.
        TypeError:
            If the given `value` is not a numeric value.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2
        >>> min_heap.insert(15)
        >>> min_heap.insert(-1)
        >>> min_heap
                 __-1__
                /      \\
             __0        1
            /   \\     / \\
          _4     9    3   2
         /  \\
        15   7
        """
        super().insert(value, is_min_heap=True)

    # =============================    REMOVE    ==============================
    def remove(self, del_value):
        """
        Removes the `del_value` from the `MinHeap()` instance.

        Parameters
        ----------
        del_value: int or float
            The value to be deleted from the subtree.

        Raises
        ------
        UserWarning:
            If the `MinHeap()` instance is empty of if the value wasn't found
            in the instance.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2
        >>> min_heap.remove(0)
        >>> min_heap
            __1__
           /     \\
          4       2
         / \\    /
        7   9   3
        >>> min_heap.remove(50)
        UserWarning: Couldn't find `50` in `extra.MinHeap()`!!
        """
        super().remove(del_value, is_min_heap=True)

    def remove_min(self):
        """
        Removes the minimum value from the `MinHeap()` instance which is the
        root.

        Raises
        ------
        UserWarning:
            If the `MinHeap()` instance is empty of if the value wasn't found
            in the instance.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2
        >>> min_heap.remove_min()
        >>> min_heap
            __1__
           /     \\
          4       2
         / \\    /
        7   9   3
        """
        self.remove(self.get_min())

    def remove_max(self):
        """
        Removes the maximum value from the `MinHeap()` instance which is one of
        the nodes at the deepest level of the instance.

        Raises
        ------
        UserWarning:
            If the `MinHeap()` instance is empty of if the value wasn't found
            in the instance.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\    / \\
        7   9   3   2
        >>> min_heap.remove_max()
        >>> min_heap
            __0__
           /     \\
          4       1
         /       / \\
        7       3   2
        """
        self.remove(self.get_max())

    # =============================     ITER     ==============================
    def __iter__(self):
        """
        Iterates over the `MinHeap()` instance and returns a generator of the
        heap node values in breadth-first manner.

        Yields
        ------
        int or float:
            The number stored at each node in the instance.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2
        >>> for value in min_heap:
        ...     print(value, end=',')
        0,4,1,7,9,3,2,
        """
        return super().__iter__()

    def to_list(self):
        """
        Converts the `MinHeap()` instance to a `list` where values will be
        inserted in breadth-first manner.

        Returns
        -------
        list:
            A `list` object containing the same elements as the `MinHeap()`
            instance.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2
        >>> min_heap.to_list()
        [0, 4, 1, 7, 9, 3, 2]
        """
        return super().to_list()

    # =============================     CLEAR    ==============================
    def clear(self):
        """
        Removes all nodes within the `MinHeap()` instance in constant time.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> min_heap
            __0__
           /     \\
          4       1
         / \\     / \\
        7   9    3   2
        >>> min_heap.clear()
        >>> min_heap
        / \\
        >>> min_heap.is_empty()
        True
        """
        super().__init__()
