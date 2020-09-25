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
should be **log(n)**.
"""
from extra.trees._heap import Heap




class MinHeap(Heap):
    __name__ = "extra.MinHeap()"
    

    def __init__(self):
        super().__init__()
    

    @classmethod
    def heapify(cls, iterable):
        return super().heapify(iterable)
    

    def get_min(self):
        if self.is_empty():
            raise IndexError("Can't get the minimum out of an empty Heap!!")
        return self._heap[0]


    def get_max(self):
        if self.is_empty():
            raise IndexError("Can't get the maximum out of an empty Heap!!")
        last_half = self._heap[len(self)//2:]
        return max(last_half)


    def insert(self, value):
        super().insert(value, is_min_heap=True)


    def remove(self, del_value):
        super().remove(del_value, is_min_heap=True)


