from abc import ABC, abstractmethod

from binary_tree import TreeNode, BinaryTree


class Heap(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def heapify(lst):
        length = len(lst)
        if length == 1:
            node = TreeNode(lst[0])
        elif length == 2:
            node = TreeNode(lst[0])
            node.left = TreeNode(lst[1])
        else:
            node = TreeNode(lst[0])
            node.left = Heap.heapify(lst[1::2])
            node.right = Heap.heapify(lst[2::2])
        return node

    def insert(self, value, swap_needed):
        # add the new value
        self.heap.append(value)
        # swap between parents when needed
        idx = len(self.heap)-1
        while(idx != 0):
            parent_idx = (idx-1)//2
            current = self.heap[idx]
            parent = self.heap[parent_idx]
            if swap_needed(parent, current):
                self.heap[parent_idx], self.heap[idx] = \
                                        self.heap[idx], self.heap[parent_idx]
                idx = parent_idx
            else:
                break






class MinHeap(Heap):

    def __init__(self, value):
        if type(value) in {list, set, frozenset}:
            lst = sorted(value)
            self.heap = lst
        elif type(value) in {int, float}:
            self.heap = [value]
        else:
            raise ValueError("Unsupported datatype!!")

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        root = Heap.heapify(self.heap)
        btree = BinaryTree(root)
        return str( btree )


    ############################## INSERTION ##############################
    def __is_parent_bigger(self, parent, child):
        return parent > child

    def insert(self, value):
        super().insert(value, self.__is_parent_bigger)

    def get_min(self):
        return self.heap[0]

    def get_max(self):
        return max(self.heap)







if __name__ == "__main__":
    # h = Heap()
    heap = MinHeap([1,2,3,4])
    heap.insert(1)
    heap.insert(2)
    heap.insert(20)
    heap.insert(500)
    heap.insert(200)
    heap.insert(0)
    print(heap)
    print("Min value:", heap.get_min())
    print("Max value:", heap.get_max())
    print("Heap length:", len(heap))