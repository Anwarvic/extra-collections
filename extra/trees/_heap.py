from extra.trees.binary_tree import BinaryTreeNode, BinaryTree




class HeapNode(BinaryTreeNode):
    def __name__(self):
        return "extra.HeapNode()"
    

    def __init__(self, value):
        if type(value) not in {int, float}:
            raise TypeError(f"{self.__name__()} contains only numbers!!")
        super().__init__(value)




class Heap(ABC):
    ############################ INIT ############################
    _basic_node = HeapNode


    def __name__(self):
        return "extra.Heap()"
    

    def _validate_item(self, item):
        if isinstance(item, self._basic_node): item = item.get_data()
        if type(item) not in {int, float}:
            raise TypeError(f"{self.__name__()} accepts only numbers!!")
        

    @abstractmethod
    def __init__(self, value=None):
        if value is None:
            self._heap = []
        else:
            self._validate_item(value)
            self._heap = [value]


    def __len__(self):
        return len(self._heap)


    def __iter__(self):
        for node in self._heap:
            yield node


    @staticmethod
    def heapify(self, obj, is_min_heap):
        #TODO: there is a better way.
        if not hasattr(obj, '__iter__'):
            raise TypeError("Given object isn't iterable!!")
        self._heap = sorted(value, reverse=not is_min_heap)


    ############################## PRINT ##############################
    @classmethod
    def __transform(cls, lst):
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
    

    def __repr__(self):
        root = self.__transform(self._heap)
        btree = BinaryTree(root)
        return str( btree )
    

    ############################## INSERT ##############################
    def insert(self, value, is_min_heap):
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
        assert type(parent_idx) == int and parent_idx >= 0:
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


    def remove(self, del_val, is_min_heap):
        """Removes first utterence of given value"""
        #TODO: try to handle more than just the first utterence
        self._validate_item(del_val)
        assert type(is_min_heap) == bool

        del_idx = self._heap.index(del_val)
        last_idx = len(self._heap)-1
        # swap between removed item and last item
        self._heap[last_idx], self._heap[del_idx] = \
                                self._heap[del_idx], self._heap[last_idx]
        # set last item to -inf or inf based on heap type
        self._heap[last_idx] = float('-inf') if is_min_heap else float('inf')
        # start swapping when needed
        self.__rebalance(del_idx, is_min_heap)
        # remove the (+/-)inf
        self._heap.pop()
    

    def clear(self):
        self.__init__()
