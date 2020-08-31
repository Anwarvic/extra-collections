import warnings
from abc import ABC, abstractmethod
from extra.interface import Extra
from extra.trees.binary_tree import BinaryTreeNode, BinaryTree




class HeapNode(BinaryTreeNode):
    """
    A heap node is the basic unit for building Heaps with its two types: MinHeap
    and MaxHeap. A heap node must contain a number. Each heap node has either
    zero, one or two children heap nodes.
    """
    __name__ = "extra.HeapNode()"
    

    def __init__(self, value):
        """
        Creates a `HeapNode()` object which is the basic unit for building 
        Heap() objects!!

        Parameters
        ----------
        value: int or float
            The value to be saved within the `BSTNode()` instance

        Raises
        ------
        ValueError: If the given item is `None`.
        TypeError: If the given item isn't a number.
        """
        if type(value) not in {int, float}:
            raise TypeError(f"`{self.__name__}` contains only numbers!!")
        super().__init__(value)
    

    def __repr__(self):
        """
        Represents `HeapNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `HeapNode()` instance.
        
        Example
        -------
        >>> x = HeapNode(10)
        >>> x
        >>> HeapNode(10)
        """
        return f"HeapNode({self._data})"




class Heap(ABC, Extra):
    _basic_node = HeapNode
    __name__ = "extra.Heap()"
    

    @abstractmethod
    def __init__(self):
        """
        An abstract method that initializes the `Heap()` abstract class.
        """
        self._heap = []


    def _validate_item(self, item):
        """
        Makes sure the input variable type can be processed. The main use for 
        this method is to make sure we can't create nested objects from the 
        package.
        
        Parameters
        ----------
        item: object
            The input object of any type.
        
        Raises
        -------
        ValueError: If `item` is `None`
        TypeError: If `item` is not a numeric value.
        """
        super()._validate_item(item)
        if type(item) not in {int, float}:
            raise TypeError(f"`{self.__name__}` accepts only numbers!!")
        

    @classmethod
    def heapify(cls, iterable):
        """
        A class method which converts an iterable object to a heap object in
        time-complexity of O(n) where **n** is the number of elements inside
        the given `iterable`.

        Parameters
        ----------
        iterable: iterable
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
        
        Returns
        -------
        MinHeap() or MaxHeap()
            It returns a heap instance with input values being inserted.
        
        Raises
        ------
        TypeError: It can be raised in two cases
            1. In case the given object isn't iterable.
            2. If one of the elements in the iterable is NOT a number.

        ValueError: If one of the iterable elements is `None`.
        """
        if not hasattr(iterable, '__iter__'):
            raise TypeError("The given object isn't iterable!!")
        heap = cls()
        for item in iterable:
            heap.insert(item)
        return heap


    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the heap instance in time-complexity of O(1).
        
        Returns
        -------
        int:
            The length of the heap instance. Length is the number of tree 
            nodes in the instance.
        """
        return len(self._heap)


    def is_empty(self):
        """
        Checks if the heap instance is empty or not in time-complexity of
        O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the heap instance is empty or not.
            `True` shows that this instance is empty and `False` shows it's
            not empty.
        """
        return self._heap == []


    ##############################     PRINT      ##############################
    def _transform(self):
        """
        Converts a list-shaped heap to a binary-tree shaped in linear time.

        Returns
        -------
        BinaryTree():
            The binary-tree shaped of the heap.
        """
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
        """
        Represents the heap instance as a string.
        
        Returns
        -------
        str:
            The string-representation of the `MinHeap()` instance.
        """
        if self.is_empty():
            return "/ \\"
        btree = self._transform()
        return str( btree )

    
    ##############################     SEARCH     ##############################
    def __contains__(self, num):
        """
        Searches the heap instance for the given value and returns `True` if the 
        value exists and `False` if not.

        Parameters
        ----------
        find_val: int or float
            The value to be searched for in the heap instance.
        
        Returns
        -------
        bool:
            Returns `True` if the value exists in the heap instance and `False`
            if not.
        """
        if self.is_empty() or type(num) not in {int, float}:
            return False
        return num in self._heap


    ##############################     INSERT     ##############################
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


    ##############################     REMOVE     ##############################
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
            warnings.warn(f"`{self.__name__}` is empty!!", UserWarning)
            return
        elif type(del_value) not in {int, float}:
            warnings.warn(f"Couldn't find `{del_value}` in `{self.__name__}`",
                UserWarning
            )
            return
        try:
            del_idx = self._heap.index(del_value)
        except ValueError:
            # del_value wasn't found in the heap
            warnings.warn(f"Couldn't find `{del_value}` in `{self.__name__}`",
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
    

    ##############################      ITER      ##############################
    def __iter__(self):
        btree = self._transform()
        for node in btree:
            yield node
    

    def to_list(self):
        return self._heap
    

    ##############################      CLEAR     ##############################
    def clear(self):
        self.__init__()
    


