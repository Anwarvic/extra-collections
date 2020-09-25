"""
A heap is a binary tree that stores a collection of nodes. Each node must
satisfy two additional properties:

1. Heap-Order Property: It is a relational property defined in terms of the 
value stored at the node. So, for every node other than the root, the value
stored at the node is less than or equal to the value stored at the
node's parent. 



"""
from extra.trees._heap import Heap




class MaxHeap(Heap):
    __name__ = "extra.MinHeap()"


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
    


