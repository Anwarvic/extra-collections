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
    

