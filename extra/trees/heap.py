from extra.trees._heap import Heap




class MinHeap(Heap):
    def __name__(self):
        return "extra.MinHeap()"
    

    def __init__(self, value=None):
        super().__init__(value)
    

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




class MaxHeap(Heap):
    def __name__(self):
        return "extra.MinHeap()"


    def __init__(self, value=None):
        super().__init__(value)


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
    







if __name__ == "__main__":
    # # test MinHeap
    heap = MinHeap.heapify([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190])
    # heap.remove(102)
    # heap.remove(4)
    heap.remove(1)
    print(heap)
    print(heap.to_list())
    print("Min value:", heap.get_min())
    print("Max value:", heap.get_max())
    print("Heap length:", len(heap))
    print('='*50)

    # # #####################################################
    # # test MaxHeap
    # heap = MaxHeap.heapify([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190])
    # heap.remove(102)
    # heap.remove(100)
    # heap.remove(190)
    # print(heap)
    # print("Min value:", heap.get_min())
    # print("Max value:", heap.get_max())
    # print("Heap length:", len(heap))
    # print('='*50)

    # # #####################################################
    # # test insert
    # heap = MinHeap(35)
    # heap.insert(33)
    # heap.insert(42)
    # heap.insert(10)
    # heap.insert(14)
    # heap.insert(19)
    # heap.insert(27)
    # heap.insert(44)
    # heap.insert(26)
    # heap.insert(31)
    # print(heap)
    # print('='*50)

    # heap = MaxHeap(35)
    # heap.insert(33)
    # heap.insert(42)
    # heap.insert(10)
    # heap.insert(14)
    # heap.insert(19)
    # heap.insert(27)
    # heap.insert(44)
    # heap.insert(26)
    # heap.insert(31)
    # print(heap)
    