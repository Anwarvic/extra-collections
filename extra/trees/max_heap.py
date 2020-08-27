"""
A heap is a binary tree that stores a collection of nodes. Each node must
satisfy two additional properties:

1. Heap-Order Property: It is a relational property defined in terms of the 
value stored at the node. So, for every node other than the root, the value
stored at the node is less than or equal to the value stored at the node's
parent. As a consequence of the heap-order property, the value encountered on a
path from the root to a leaf node are in nonincreasing order. Also, the maximum
value is always stored at the root of the `MaxHeap()`. This makes it easy to
locate such a node when `get_max()` or `remove_max()` is called, as it is
informally said to be at the top of the heap. Hence, the name "Max Heap"

2. Perfect Binary Tree Property: It is a structural property defined in terms of
the shape of heap itself. A binary tree is perfect if all its levels are
completely filled. So, given an **n** inserted items, the height of the heap 
should be **log(n)** at most.

The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **h** is the height of the BST which approximatley equals to **log(n)**.

+--------------------------+----------------------------------------------------+------------+---------+
| Method                   | Description                                        | Worst-case | Optimal |
+==========================+====================================================+============+=========+
| __len__()                | Returns the number of nodes in the max heap.       | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_empty()               | Checks if max heap is empty.                       | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __repr__()               | Represents the max heap as a string.               | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __iter__()               | Iterates over the max heap.                        | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __contains__()           | Checks the existence of the given item.            | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| clear()                  | Clears the whole max heap instance.                | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| to_list()                | Converts the max heap instance to list.            | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_min()                | Gets the minimum number in the max heap.           | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_max()                | Gets the maximum number in the max heap.           | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| insert()                 | Inserts a certain value to the max heap.           | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| remove()                 | Removes a certain value from the max heap.         | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| remove_min()             | Removes the minimum value from the max heap.       | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| remove_max()             | Removes a certain value from the max heap.         | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+



Class Documentation
===================
Here are all of the public methods that can be used with `MaxHeap()` objects:
"""
from extra.trees._heap import Heap




class MaxHeap(Heap):
    """
    A Max heap is a perfect binary tree that stores a collection of nodes. Each
    node other than stores a value less than or equal to the value strored at
    the node's parent.
    """
    __name__ = "extra.MaxHeap()"


    def __init__(self):
        """
        Creates an empty `MaxHeap()` object!!
        
        Example
        -------
        >>> max_heap = MaxHeap()
        >>> type(max_heap)
        <class 'extra.trees.max_heap.MaxHeap'>
        """
        super().__init__()


    @classmethod
    def heapify(cls, iterable):
        """
        A class method which creates a `MaxHeap()` instance using an iterable
        object in time-complexity of O(n) where **n** is the number of elements
        inside the given `iterable`.

        Parameters
        ----------
        iterable: iterable
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
        
        Returns
        -------
        MaxHeap()
            It returns a `MaxHeap()` instance with input values being inserted.
        
        Raises
        ------
        TypeError: It can be raised in two cases
            1. In case the given object isn't iterable.
            2. If one of the elements in the iterable is NOT a number.

        ValueError: If one of the iterable elements is `None`.

        Examples
        --------
        >>> MaxHeap.heapify([2, 4, 3, 7, 9, 0, 1])
            __9__
           /     \\
          7       3
         / \\    / \\
        2   4   0   1


        Using an iterable object with `None` as one of its elements will raise
        `ValueError`

        >>> MaxHeap.heapify([2, None])
        ValueError: Can't use `None` as an element within `extra.MaxHeap()`!!
        
        Using a non-iterable object will raise `TypeError`

        >>> MaxHeap.heapify(2)
        TypeError: The given object isn't iterable!!
        
        Using nested `MaxHeap()` objects will raise `TypeError` as well

        >>> max_heap_1 = MaxHeap.heapify([1])
        >>> max_heap_2 = MaxHeap.heapify([1, max_heap_1])
        TypeError: Can't create `extra.MaxHeap()` using `extra.MaxHeap()`!!
        """
        return super().heapify(iterable)
    

    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the `MaxHeap()` instance in time-complexity of O(1).
        
        Returns
        -------
        int:
            The length of the `MaxHeap()` instance. Length is the number of tree 
            nodes in the instance.
        
        Example
        -------
        >>> max_heap = MaxHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> max_heap
            __9__
           /     \\
          7       3
         / \\    / \\
        2   4   0   1
        >>> len(max_heap)
        7
        """
        return super().__len__()

    
    def is_empty(self):
        """
        Checks if the `MaxHeap()` instance is empty or not in time-complexity of
        O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the `MaxHeap()` instance is empty or not.
            `True` shows that this instance is empty and `False` shows it's
            not empty.
        
        Example
        --------
        >>> max_heap = MaxHeap()
        >>> max_heap.is_empty()
        True
        >>> max_heap.insert(10)
        >>> max_heap.is_empty()
        False
        """
        return super().is_empty()
    
    
    ##############################     PRINT      ##############################
    def __repr__(self):
        """
        Represents the `MaxHeap()` instance as a string.
        
        Returns
        -------
        str:
            The string-representation of the `MaxHeap()` instance.

        Example
        -------
        >>> max_heap = MaxHeap.heapify([2, 4, 3, 7, 9, 0, 1])
        >>> max_heap
            __9__
           /     \\
          7       3
         / \\    / \\
        2   4   0   1
        """
        return super().__repr__()


    