from abc import ABC, abstractmethod
from extra.trees.binary_tree import BinaryTreeNode, BinaryTree




class HeapNode(BinaryTreeNode):
    def __name__(self):
        return "extra.HeapNode()"
    

    def __init__(self, value):
        if type(value) not in {int, float}:
            raise TypeError(f"{self.__name__()} contains only numbers!!")
        super().__init__(value)




class Heap(ABC):
    _basic_node = HeapNode


    def __name__(self):
        return "extra.Heap()"
    

    @abstractmethod
    def __init__(self):
        self._heap = []


    def __len__(self):
        return len(self._heap)


    def __iter__(self):
        for node in self._heap:
            yield node


    def __repr__(self):
        root = self._transform(self._heap)
        btree = BinaryTree(root)
        return str( btree )


    def _validate_item(self, item):
        if isinstance(item, self._basic_node): item = item.get_data()
        if type(item) not in {int, float}:
            raise TypeError(f"{self.__name__()} accepts only numbers!!")
        

    ############################## HEAPIFY ##############################
    @classmethod
    def _transform(cls, lst):
        root = BinaryTreeNode(lst[0])
        q = [root]
        idx = 1
        length = len(lst)
        while (idx < length):
            parent_node = q.pop(0)
            parent_node.left = cls._basic_node(lst[idx])
            q.append(parent_node.left)
            idx += 1
            if idx < length:
                parent_node.right = cls._basic_node(lst[idx])
                q.append(parent_node.right)
                idx += 1
        return BinaryTree(root)
    
    
    ############################## INSERTION ##############################
    def insert(self, value, is_min_heap):
        # add the new value
        self._heap.append(value)
        # swap between parents when needed
        idx = len(self._heap)-1
        while(idx != 0):
            parent_idx = (idx-1)//2
            current = self._heap[idx]
            parent = self._heap[parent_idx]
            if (is_min_heap and parent>current) or \
                                    (not is_min_heap and parent<current):
                self._heap[parent_idx], self._heap[idx] = \
                                        self._heap[idx], self._heap[parent_idx]
                idx = parent_idx
            else:
                break


    ############################## REMOVAL ##############################
    def __rebalance(self, parent_idx, is_min_heap):
        last_idx = len(self._heap)-1
        while(parent_idx < last_idx):
            parent = self._heap[parent_idx]
            left_child_idx, right_child_idx = (parent_idx*2)+1, (parent_idx*2)+2
            # get which child is smaller
            if right_child_idx >= last_idx:
                if left_child_idx >= last_idx:
                    break
                else:
                    child_idx = left_child_idx
            else:
                if is_min_heap:
                    if self._heap[left_child_idx] < self._heap[right_child_idx]:
                        child_idx = left_child_idx
                    else:
                        child_idx = right_child_idx
                else:
                    if self._heap[left_child_idx] > self._heap[right_child_idx]:
                        child_idx = left_child_idx
                    else:
                        child_idx = right_child_idx
            child = self._heap[child_idx]
            if (is_min_heap and parent>child) or \
                                        (not is_min_heap and parent<child):
                self._heap[parent_idx], self._heap[child_idx] = \
                                self._heap[child_idx], self._heap[parent_idx]
                parent_idx = child_idx
            else:
                break


    def remove(self, del_val, is_min_heap):
        """Removes first utterence of given value"""
        del_idx = self._heap.index(del_val)
        last_idx = len(self._heap)-1
        # swap between removed item and last item
        self._heap[last_idx], self._heap[del_idx] = \
                                self._heap[del_idx], self._heap[last_idx]
        if is_min_heap:
            # set last item to -inf
            self._heap[last_idx] = float('-inf')
        else:
            # set last item to inf
            self._heap[last_idx] = float('inf')
        # start swapping when needed
        self.__rebalance(del_idx, is_min_heap)
        # remove the (+/-)inf
        self._heap.pop()




class MinHeap(Heap):
    def __init__(self, value):
        if hasattr(value, '__iter__'):
            self._heap = sorted(value)
        elif type(value) in {int, float}:
            self._heap = [value]
        else:
            raise ValueError("Unsupported datatype!!")

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
    def __init__(self, value):
        if hasattr(value, '__iter__'):
            self._heap = sorted(value, reverse=True)
        elif type(value) in {int, float}:
            self._heap = [value]
        else:
            raise ValueError("Unsupported datatype!!")

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
    