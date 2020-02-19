import warnings
from extra.lists.doubly_linked_list import DoublyLinkedList




class Queue():
    """Basic object for the Queue data structure"""
    def __name__(self):
        return "extra.Queue()"
    
    
    def __init__(self, max_capacity=float("inf")):
        if type(max_capacity) not in {int, float}:
            raise TypeError("Max Capacity has to be a number!!")
        elif max_capacity < 0:
            raise ValueError(f"Max capacity of {self.__name__()} must be >= 0!")
        self.container = DoublyLinkedList()
        self.max_capacity = max_capacity


    ############################## PRINT ##############################
    def _print_queue(self, direction_char=' '):
        top_border = '─┬'
        middle_border = direction_char+'│'
        down_border = '─┴'
        for item in self.container:
            width = len(str(item))+2 #2: for a space before & after item
            top_border += ('─'*width) + '┬'
            middle_border += " {} │".format(item)
            down_border += ('─'*width) + '┴'
        # add extension
        if not self.is_empty():
            top_border += '─'
            middle_border += direction_char
            down_border += '─'
        return "{}\n{}\n{}".format(top_border, middle_border, down_border)


    def __repr__(self):
        """Represents the queue as a string."""
        return self._print_queue(direction_char='⟶')


    ############################## LENGTH ##############################
    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return len(self.container)


    ############################## GET ################################
    def get_first(self):
        """Returns the Qeueu head (first element to be inserted) """
        if self.is_empty():
            raise IndexError(\
                f"Can't retrieve from an empty {self.__name__()}!!")
        return self.container.head.get_data()


    ############################# ENQUEUE ##############################
    def _validate_item(self, item):
        if item is None:
            raise TypeError(f"Can't push `None` into {self.__name__()}!!")
        elif type(item) == str and item.strip() == '':
            raise ValueError(\
                f"Can't push an empty-string into {self.__name__()}!!")
    

    def enqueue(self, item):
        """Insert value into the Queue"""
        self._validate_item(item)
        if self.is_full():
            warnings.warn(f"Enqueuing to a full {self.__name__()} "+\
                "could lead to missing values!!", UserWarning)
            self.container.remove_front()
        self.container.add_end(item)


    ##############################    DEQUEUE    ##############################
    def dequeue(self):
        """Removes value from the Queue (Queue's head)"""
        if self.is_empty():
            warnings.warn(f"Dequeuing from an empty {self.__name__()}!!")
            return None
        else:
            return self.container.remove_front().get_data()


    def clear(self):
        """Clears the whole Queue"""
        self.__init__(max_capacity=self.max_capacity)


    ##############################     STATUS     ##############################
    def is_empty(self):
        """Checks if the Queue is empty"""
        return self.container.is_empty()


    def is_full(self):
        return len(self) == self.max_capacity


