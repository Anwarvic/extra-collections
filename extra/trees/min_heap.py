"""
A heap is a binary tree that stores a collection of nodes. Each node must
satisfy two additional properties:

1. Heap-Order Property: It is a relational property defined in terms of the 
value stored at the node. So, for every node other than the root, the value
stored at the node is greater than or equal to the value stored at the node's
parent. As a consequence of the heap-order property, the value encountered on a
path from the root to a leaf node are in nondecreasing order. Also, the minimum
value is always stored at the root of the `MinHeap()`. This makes it easy to
locate such a node when `get_min()` or `remove_min()` is called, as it is
informally said to be at the top of the heap. Hence, the name "Min Heap"

2. Perfect Binary Tree Property: It is a structural property defined in terms of
the shape of heap itself. A binary tree is perfect if all its levels are
completely filled. So, given an **n** inserted items, the height of the heap 
should be **log(n)** at most.
"""
from extra.trees._heap import Heap




class MinHeap(Heap):
    """
    A Min heap is a perfect binary tree that stores a collection of nodes. Each
    node other than stores a value greater than or equal to the value strored at
    the node's parent.
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
        TypeError: It can be raised in two cases
            1. In case the given object isn't iterable.
            2. If one of the elements in the iterable is NOT a number.

        ValueError: If one of the iterable elements is `None`.

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
    

    ##############################     MIN/MAX    ##############################
    def get_min(self):
        """
        Gets the minimum value in the `MinHeap()` instance in a constant time.
        The minimum value can be at the root of the `MinHeap()` instance.

        Returns
        -------
        int or float:
            The minimum numeric value in the `MinHeap()` instance.
        
        Raises
        ------
        IndexError: In case the `MinHeap()` instance is empty.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
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
        Gets the maximum value in the `MinHeap()` instance in a linear time.
        The maximum value can be at the deepest level of the `MinHeap()`
        instance.

        Returns
        -------
        int or float:
            The masximum numeric value in the `MinHeap()` instance.
        
        Raises
        ------
        IndexError: In case the `MinHeap()` instance is empty.

        Example
        -------
        >>> min_heap = MinHeap.heapify([2, 4, 3, 7, 9, 0, 1])
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
        last_half = self._heap[len(self)//2:]
        return max(last_half)


    ##############################     INSERT     ##############################
    def insert(self, value):
        super().insert(value, is_min_heap=True)


    def remove(self, del_value):
        super().remove(del_value, is_min_heap=True)


