import warnings

from extra.lists.queue import Queue




class Deque(Queue):
    """Basic object for the Deque data structure"""
    def __name__(self):
        return "extra.Deque()"
    

    ##############################      PRINT     ##############################
    def __repr__(self):
        """Represents the deque as a string."""
        return super()._print_queue('⟷')

    
    ##############################       GET      ##############################
    def get_left(self):
        if self.is_empty():
            raise IndexError(\
                f"Can't retrieve from an empty {self.__name__()}!!")
        return self._container._head.get_data()
    

    def get_right(self):
        return super().top()


    ##############################     APPEND     ##############################
    def append_left(self, item):
        """Insert value into the left-side of the Deque"""
        super().enqueue(item)


    def append_right(self, item):
        """Insert value into the right-side of the Deque"""
        super()._validate_item(item)
        if self.is_full():
            warnings.warn(f"Enqueuing to a full {self.__name__()} "+\
                "could lead to missing values!!", UserWarning)
            self._container.remove_front()
        self._container._insert(len(self), item)


    ##############################       POP      ##############################
    def pop_left(self):
        """Removes value from the left-side of the Deque"""
        if self.is_empty():
            warnings.warn(f"Dequeuing from an empty {self.__name__()}!!")
            return
        else:
            return self._container.remove_front().get_data()


    def pop_right(self):
        """Removes value from the right-side of the Deque"""
        return super().dequeue()


