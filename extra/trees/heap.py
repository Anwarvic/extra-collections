from abc import ABC, abstractmethod
from extra.trees._heap import Heap




class MinHeap(Heap):
    def __name__(self):
        return "extra.MinHeap()"
    

    def get_min(self):
        return self._heap[0]


    def get_max(self):
        # TODO: optimize as you don't have to iterate over the whole list
        return max(self._heap)


    def insert(self, value):
        super().insert(value, is_min_heap=True)


    def remove(self, del_value):
        super().remove(del_value, is_min_heap=True)




class MaxHeap(Heap):
    def __name__(self):
        return "extra.MinHeap()"


    def get_min(self):
        # TODO: optimize as you don't have to iterate over the whole list
        return min(self._heap)


    def get_max(self):
        return self._heap[0]


    def insert(self, value):
        super().insert(value, is_min_heap=False)


    def remove(self, del_value):
        super().remove(del_value, is_min_heap=False)
    







if __name__ == "__main__":
    # h = Heap()

    # test iteration
    heap = MinHeap([6, 2, 7, 1])
    print(heap, '\n')
    for node in heap:
        print(node)
    print('='*50)

    #####################################################
    # test MinHeap
    heap = MinHeap([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190])
    heap.remove(102)
    heap.remove(4)
    heap.remove(1)
    print(heap)
    print("Min value:", heap.get_min())
    print("Max value:", heap.get_max())
    print("Heap length:", len(heap))
    print('='*50)

    #####################################################
    # test MaxHeap
    heap = MaxHeap([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190])
    heap.remove(102)
    heap.remove(100)
    heap.remove(190)
    print(heap)
    print("Min value:", heap.get_min())
    print("Max value:", heap.get_max())
    print("Heap length:", len(heap))
    print('='*50)

    #####################################################
    # test insert
    heap = MinHeap(35)
    heap.insert(33)
    heap.insert(42)
    heap.insert(10)
    heap.insert(14)
    heap.insert(19)
    heap.insert(27)
    heap.insert(44)
    heap.insert(26)
    heap.insert(31)
    print(heap)
    print('='*50)

    heap = MaxHeap(35)
    heap.insert(33)
    heap.insert(42)
    heap.insert(10)
    heap.insert(14)
    heap.insert(19)
    heap.insert(27)
    heap.insert(44)
    heap.insert(26)
    heap.insert(31)
    print(heap)
    