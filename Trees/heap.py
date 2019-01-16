from math import log2
from abc import ABC, abstractmethod

from binary_tree import TreeNode, BinaryTree

# deprecated
def sort_heap(lst, min_heap=True):
    """Sort given list to the parent node will be bigger than children if
    min_heap=False or smaller than children if min_heap=True (default)"""
    idx = len(lst)-1
    while(idx != 0):
        parent_idx = (idx-1)//2
        if (min_heap and lst[parent_idx] > lst[idx]) or \
            (not min_heap and lst[parent_idx] < lst[idx]):
            # sift up
            lst[parent_idx], lst[idx] = \
                            lst[idx], lst[parent_idx]
        idx -= 1


class Heap(ABC):
    @abstractmethod
    def __init__(self):
        self._heap = []
        pass

    ############################## HEAPIFY ##############################
    def heapify(self, lst):
        root = TreeNode(lst[0])
        q = [root]
        idx = 1
        length = len(lst)
        while (idx < length):
            parent_node = q.pop(0)
            parent_node.left = TreeNode(lst[idx])
            q.append(parent_node.left)
            idx += 1
            if idx < length:
                parent_node.right = TreeNode(lst[idx])
                q.append(parent_node.right)
                idx += 1
        return BinaryTree(root)
    
    
    ############################## INSERTION ##############################
    def insert(self, value, min_heap):
        # add the new value
        self._heap.append(value)
        # swap between parents when needed
        idx = len(self._heap)-1
        while(idx != 0):
            parent_idx = (idx-1)//2
            current = self._heap[idx]
            parent = self._heap[parent_idx]
            if (min_heap and parent>current) or (not min_heap and parent<current):
                self._heap[parent_idx], self._heap[idx] = \
                                        self._heap[idx], self._heap[parent_idx]
                idx = parent_idx
            else:
                break


    ############################## REMOVAL ##############################
    def remove(self, del_val, min_heap):
        """Removes first utterence of given value"""
        del_idx = self._heap.index(del_val)
        last_idx = len(self._heap)-1
        # swap between removed item and last item
        self._heap[last_idx], self._heap[del_idx] = \
                                self._heap[del_idx], self._heap[last_idx]
        if min_heap:
            # set last item to -inf
            self._heap[last_idx] = float('-inf')
        else:
            # set last item to inf
            self._heap[last_idx] = float('inf')
        # start swapping when needed
        parent_idx = del_idx
        while(parent_idx < last_idx):
            parent = self._heap[parent_idx]
            left_child_idx = (parent_idx*2)+1
            right_child_idx = (parent_idx*2)+2
            # get which child is smaller
            if right_child_idx >= last_idx:
                if left_child_idx >= last_idx:
                    break
                else:
                    child_idx = left_child_idx
            else:
                child_idx = left_child_idx
                if self._heap[left_child_idx] > self._heap[right_child_idx]:
                    child_idx = right_child_idx
            child = self._heap[child_idx]
            if (min_heap and parent>child) or (not min_heap and parent<child):
                self._heap[parent_idx], self._heap[child_idx] = \
                                self._heap[child_idx], self._heap[parent_idx]
                parent_idx = child_idx
            else:
                break
        # remove the (+/-)inf
        self._heap.pop()







class MinHeap(Heap):

    def __init__(self, value):
        if type(value) in {list, set, frozenset}:
            self._heap = sorted(value)
        elif type(value) in {int, float}:
            self._heap = [value]
        else:
            raise ValueError("Unsupported datatype!!")

    def __len__(self):
        return len(self._heap)

    def __repr__(self):
        root = super().heapify(self._heap)
        btree = BinaryTree(root)
        return str( btree )

    def get_min(self):
        return self._heap[0]

    def get_max(self):
        return max(self._heap)

    def insert(self, value):
        super().insert(value, min_heap=True)

    def remove(self, del_value):
        super().remove(del_value, min_heap=True)


    







if __name__ == "__main__":
    # h = Heap()

    # heap = MinHeap([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190])
    # heap.insert(0)
    # print(heap)
    # print("Min value:", heap.get_min())
    # print("Max value:", heap.get_max())
    # print("Heap length:", len(heap))
    # print('='*50)

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
    
    # heap.remove(31)
    print(heap)