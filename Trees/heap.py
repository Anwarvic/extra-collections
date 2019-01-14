from math import log2
from abc import ABC, abstractmethod

from binary_tree import TreeNode, BinaryTree


def sort_heap(lst, min_heap=True):
    """Sort given list to the parent node will be bigger than children if
    min_heap=False or smaller than children if min_heap=True (default)"""
    idx = len(lst)-1
    for idx in range(len(lst)-1, -1, -1):
        parent_idx = (idx-1)//2
        if (min_heap and lst[parent_idx] > lst[idx]) or \
            (not min_heap and lst[parent_idx] < lst[idx]):
            # sift up
            lst[parent_idx], lst[idx] = lst[idx], lst[parent_idx]
    return lst


class Heap(ABC):
    @abstractmethod
    def __init__(self):
        self.heap = []
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
        self.heap.append(value)
        # swap between parents when needed
        idx = len(self.heap)-1
        while(idx != 0):
            parent_idx = (idx-1)//2
            current = self.heap[idx]
            parent = self.heap[parent_idx]
            if is_swap_needed(parent, current):
                self.heap[parent_idx], self.heap[idx] = \
                                        self.heap[idx], self.heap[parent_idx]
                idx = parent_idx
            else:
                break


    def get_level(self, idx):
        """returns heap-level given item index"""
        return int( log2(idx+1) )

    def remove(self, del_val, is_swap_needed):
        """Removes first utterence of given value"""
        del_idx = self.heap.index(del_val)
        last_idx = len(self.heap)-1
        if del_idx != last_idx:
            self.heap[last_idx], self.heap[del_idx] = \
                                    self.heap[del_idx], self.heap[last_idx]
        # remove this item
        self.heap.pop()
        idx = del_idx
        while(idx != 0):
            parent_idx = (idx-1)//2
            current = self.heap[idx]
            parent = self.heap[parent_idx]
            if is_swap_needed(parent, current):
                self.heap[parent_idx], self.heap[idx] = \
                                        self.heap[idx], self.heap[parent_idx]
                idx = parent_idx
            else:
                break







class MinHeap(Heap):

    def __init__(self, value):
        if type(value) in {list, set, frozenset}:
            self.heap = sort_heap(value, min_heap=True)
        elif type(value) in {int, float}:
            self.heap = [value]
        else:
            raise ValueError("Unsupported datatype!!")

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        root = super().heapify(self.heap)
        btree = BinaryTree(root)
        return str( btree )


    ############################## MIN/MAX ##############################
    def get_min(self):
        return self.heap[0]

    def get_max(self):
        return max(self.heap)


    ############################## INSERTION ##############################
    def __is_parent_bigger(self, parent, child):
        return parent > child

    def insert(self, value):
        super().insert(value, self.__is_parent_bigger)


    ############################## REMOVAL ##############################







if __name__ == "__main__":
    # h = Heap()
    # heap = MinHeap([1,2,3,4])
    # heap.insert(1)
    # heap.insert(2)
    # heap.insert(20)
    # heap.insert(500)
    # heap.insert(200)
    # heap.insert(15)
    # heap.insert(40)
    # heap.insert(11)
    # heap.insert(5)
    # heap.insert(8)
    # heap.insert(0)
    # print(heap)
    # print(heap.heap)
    # print("Min value:", heap.get_min())
    # print("Max value:", heap.get_max())
    # print("Heap length:", len(heap))
    # print('='*50)

    # #####################################################
    # heap = MinHeap([1,2,3,4])
    # heap.insert(1)
    # heap.insert(2)
    # heap.insert(20)
    # heap.insert(500)
    # heap.insert(200)
    # heap.insert(0)
    # print(heap)
    # print(heap.heap)
    # print("Min value:", heap.get_min())
    # print("Max value:", heap.get_max())
    # print("Heap length:", len(heap))

    #####################################################
    heap = MinHeap([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190])
    print(heap)
