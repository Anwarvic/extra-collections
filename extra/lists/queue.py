import warnings
from extra.interface import Extra
from extra.lists.doubly_linked_list import DoublyLinkedList




class Queue(Extra):
    """Basic object for the Queue data structure"""
    def __name__(self):
        return "extra.Queue()"
    
    
    def __init__(self, max_capacity=float("inf")):
        if type(max_capacity) not in {int, float}:
            raise TypeError(
                f"Max Capacity of {self.__name__()} has to be a number!!")
        elif max_capacity < 0:
            raise ValueError(f"Max capacity of {self.__name__()} must be >= 0")
        self._container = DoublyLinkedList()
        self._max_capacity = max_capacity


    ##############################      PRINT     ##############################
    def _print_queue(self, direction_char=' '):
        top_border = '─┬'
        middle_border = direction_char+'│'
        down_border = '─┴'
        counter = 0
        curr_node = self._container._head
        while counter < len(self._container):
            #NOTE: +2 for a space before & after `curr_node`
            width = len(curr_node._represent())+2
            top_border += ('─'*width) + '┬'
            middle_border += f" {curr_node._represent()} │"
            down_border += ('─'*width) + '┴'
            curr_node = curr_node.get_next()
        # add extension
        if not self.is_empty():
            top_border += '─'
            middle_border += direction_char
            down_border += '─'
        return "{}\n{}\n{}".format(top_border, middle_border, down_border)


    def __repr__(self):
        """Represents the queue as a string."""
        return self._print_queue(direction_char='⟶')


    ##############################     LENGTH     ##############################
    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return len(self._container)


    ##############################      GET     ################################
    def top(self):
        """Returns the Qeueu head (first element to be inserted) """
        if self.is_empty():
            raise IndexError(\
                f"Can't retrieve from an empty {self.__name__()}!!")
        return self._container._tail.get_data()


    ##############################     ENQUEUE    ##############################
    def _enqueue(self, item):
        assert item is not None
        if self.is_full():
            warnings.warn(f"Enqueuing to a full {self.__name__()} "+\
                "could lead to missing values!!", UserWarning)
            self._container.remove_end()
        return self._container._insert(0, item)


    def enqueue(self, item):
        """Insert value into the Queue"""
        super()._validate_item(item)
        self._enqueue(item)


    ##############################    DEQUEUE     ##############################
    def dequeue(self):
        """Removes value from the Queue (Queue's head)"""
        if self.is_empty():
            warnings.warn(f"Dequeuing from an empty {self.__name__()}!!")
            return
        else:
            return self._container.remove_end().get_data()


    def clear(self):
        """Clears the whole Queue"""
        self.__init__(max_capacity=self._max_capacity)


    ##############################     STATUS     ##############################
    def is_empty(self):
        """Checks if the Queue is empty"""
        return self._container.is_empty()


    def is_full(self):
        return len(self) >= self._max_capacity


