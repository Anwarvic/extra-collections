import warnings
from abc import ABC, abstractmethod
from extra.interface import Extra
from extra.trees.binary_tree import BinaryTreeNode, BinaryTree




class HeapNode(BinaryTreeNode):
    def __name__(self):
        return "extra.HeapNode()"
    

    def __init__(self, value):
        if type(value) not in {int, float}:
            raise TypeError(f"{self.__name__()} contains only numbers!!")
        super().__init__(value)
    

    def __repr__(self):
        return f"HeapNode({self._data})"




class Heap(ABC, Extra):
    ############################ INIT ############################
    _basic_node = HeapNode


    def __name__(self):
        return "extra.Heap()"
    

    def _validate_item(self, item):
        super()._validate_item(item)
        if type(item) not in {int, float}:
            raise TypeError(f"{self.__name__()} accepts only numbers!!")
        

    @abstractmethod
    def __init__(self):
        self._heap = []


    @classmethod
    def heapify(cls, iterable):
        if not hasattr(iterable, '__iter__'):
            raise TypeError("Given object isn't iterable!!")
        # heap = cls._create_instance(cls)
        heap = cls()
        for item in iterable:
            heap.insert(item)
        return heap


    ############################## LENGTH ##############################
    def __len__(self):
        return len(self._heap)


    def is_empty(self):
        return self._heap == []


    ############################## PRINT ##############################
    def _transform(self):
        # transform the list-shaped heap to a tree-shaped
        assert not self.is_empty()

        root = self._basic_node(self._heap[0])
        q = [root]
        idx = 1
        while (idx < len(self)):
            parent_node = q.pop(0)
            parent_node.set_left( self._basic_node(self._heap[idx]) )
            q.append(parent_node.get_left())
            idx += 1
            if idx < len(self):
                parent_node.set_right( self._basic_node(self._heap[idx]) )
                q.append(parent_node.get_right())
                idx += 1
        btree = BinaryTree()
        btree._root = root
        return btree
    

    def __repr__(self):
        if self.is_empty():
            return "/ \\"
        btree = self._transform()
        return str( btree )

    
    ############################## ITER ##############################
    def __iter__(self):
        btree = self._transform()
        for node in btree:
            yield node
    

    def to_list(self):
        return self._heap
    
    
    ############################## SEARCH ##############################
    def __contains__(self, num):
        if self.is_empty() or type(num) not in {int, float}:
            return False
        return num in self._heap


    ############################## INSERT ##############################
    def insert(self, value, is_min_heap=True):
        self._validate_item(value)
        assert type(is_min_heap) == bool

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
        assert type(parent_idx) == int and parent_idx >= 0
        assert type(is_min_heap) == bool

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


    def remove(self, del_value, is_min_heap=True):
        """Removes first utterence of given value"""
        #TODO: try to handle more than just the first utterence
        assert type(is_min_heap) == bool

        if self.is_empty():
            warnings.warn(f"{self.__name__()} is empty!!", UserWarning)
            return
        elif type(del_value) not in {int, float}:
            warnings.warn(f"Couldn't find `{del_value}` in {self.__name__()}",
                UserWarning
            )
            return
        try:
            del_idx = self._heap.index(del_value)
        except ValueError:
            # del_value wasn't found in the heap
            warnings.warn(f"Couldn't find `{del_value}` in {self.__name__()}",
                UserWarning
            )
            return
        last_idx = len(self._heap) - 1
        # swap between removed item and last item
        self._heap[last_idx], self._heap[del_idx] = \
                                self._heap[del_idx], self._heap[last_idx]
        # set last item to -inf or inf based on heap type
        self._heap[last_idx]=float('-inf') if is_min_heap else float('inf')
        # start swapping when needed
        self.__rebalance(del_idx, is_min_heap)
        # remove the (+/-)inf
        self._heap.pop()
    

    def clear(self):
        self.__init__()
    

