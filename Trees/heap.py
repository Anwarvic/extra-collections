from math import log2
from abc import ABC, abstractmethod

from binary_tree import TreeNode, BinaryTree


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
    return lst


class Heap(ABC):
    @abstractmethod
    def __init__(self):
        self._heap = []
        pass

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
    
    def insert(self, value, is_swap_needed):
        # add the new value
        self._heap.append(value)
        # swap between parents when needed
        idx = len(self._heap)-1
        while(idx != 0):
            parent_idx = (idx-1)//2
            current = self._heap[idx]
            parent = self._heap[parent_idx]
            if is_swap_needed(parent, current):
                self._heap[parent_idx], self._heap[idx] = \
                                        self._heap[idx], self._heap[parent_idx]
                idx = parent_idx
            else:
                break


    def get_level(self, idx):
        """returns heap-level given item index"""
        return int( log2(idx+1) )

    def remove(self, del_val, is_swap_needed):
        """Removes first utterence of given value"""
        del_idx = self._heap.index(del_val)
        last_idx = len(self._heap)-1
        if del_idx != last_idx:
            self._heap[last_idx], self._heap[del_idx] = \
                                    self._heap[del_idx], self._heap[last_idx]
        # remove this item
        self._heap.pop()
        idx = del_idx
        while(idx != 0):
            parent_idx = (idx-1)//2
            current = self._heap[idx]
            parent = self._heap[parent_idx]
            if is_swap_needed(parent, current):
                self._heap[parent_idx], self._heap[idx] = \
                                        self._heap[idx], self._heap[parent_idx]
                idx = parent_idx
            else:
                break







class MinHeap(Heap):

    def __init__(self, value):
        if type(value) in {list, set, frozenset}:
            self._heap = sort_heap(value, min_heap=True)
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


    ############################## MIN/MAX ##############################
    def get_min(self):
        return self._heap[0]

    def get_max(self):
        return max(self._heap)


    ############################## INSERTION ##############################
    def __is_parent_bigger(self, parent, child):
        return parent > child

    def insert(self, value):
        super().insert(value, self.__is_parent_bigger)


    ############################## REMOVAL ##############################







if __name__ == "__main__":
    # h = Heap()

    heap = MinHeap([1, 3, 6, 5, 9, 8])
    heap.insert(-2)
    print(heap)
    print("Min value:", heap.get_min())
    print("Max value:", heap.get_max())
    print("Heap length:", len(heap))
    print('='*50)

    #####################################################
    # heap = MinHeap([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190])
    # heap.insert(0)
    # print(heap)
