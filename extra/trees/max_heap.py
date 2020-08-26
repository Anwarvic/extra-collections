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
        super().__init__()


    @classmethod
    def heapify(cls, iterable):
        return super().heapify(iterable)
    

    def get_min(self):
        if self.is_empty():
            raise IndexError("Can't get the minimum out of an empty Heap!!")
        last_half = self._heap[len(self)//2:]
        return min(last_half)


    def get_max(self):
        if self.is_empty():
            raise IndexError("Can't get the maximum out of an empty Heap!!")
        return self._heap[0]


    def insert(self, value):
        super().insert(value, is_min_heap=False)


    def remove(self, del_value):
        super().remove(del_value, is_min_heap=False)
    


