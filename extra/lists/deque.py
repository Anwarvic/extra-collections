"""
A deque, which is usually pronounced "deck", is a queue-like data structure that
supports insertion and deletion at both the front and the back of the queue.
Deque is a short for "double-ended queue". The deque is more general than both
the stack and the queue.

[image]

The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **m** is the number of elements in the *other* container.
- **k** is the value of a parameter.

+----------------+---------------------------------------------------+-------------+-------------+
| Method         | Description                                       | Worst-case  | Optimal     |
+================+===================================================+=============+=============+
| __len__()      | Returns the number of values in the deque.        | O(1)        | O(1)        |
+----------------+---------------------------------------------------+-------------+-------------+
| append_left()  | Adds new value to the left-side of the deque.     | O(1)        | O(1)        |
+----------------+---------------------------------------------------+-------------+-------------+
| append_right() | Adds new value to the right-side of the deque.    | O(1)        | O(1)        |
+----------------+---------------------------------------------------+-------------+-------------+
| pop_left()     | Removes value from the left-side of the deque.    | O(1)        | O(1)        |
+----------------+---------------------------------------------------+-------------+-------------+
| pop_right()    | Removes value from the right-side of the deque.   | O(1)        | O(1)        |
+----------------+---------------------------------------------------+-------------+-------------+
| get_left()     | Returns the value at the left-side of the deque.  | O(1)        | O(1)        |
+----------------+---------------------------------------------------+-------------+-------------+
| get_right()    | Returns the value at the right-side of the deque. | O(1)        | O(1)        |
+----------------+---------------------------------------------------+-------------+-------------+
| clear()        | Clears the deque.                                 | O(1)        | O(1)        |
+----------------+---------------------------------------------------+-------------+-------------+
| is_empty()     | Checks if the deque is empty.                     | O(1)        | O(1)        |
+----------------+---------------------------------------------------+-------------+-------------+
| is_full()      | Checks if the deque is full.                      | O(1)        | O(1)        |
+----------------+---------------------------------------------------+-------------+-------------+
"""
import warnings
from extra.lists.queue import Queue




class Deque(Queue):
    """Basic object for the Deque data structure"""
    __name__ = "extra.Deque()"

    def __init__(self, max_capacity=float("inf")):
        super().__init__(max_capacity)
    

    ##############################      PRINT     ##############################
    def __repr__(self):
        return super()._print_queue('⟷')
    

    ##############################     LENGTH     ##############################
    def __len__(self):
        return super().__len__()


    def is_empty(self):
        return super().is_empty()


    def is_full(self):
        return super().is_full()

    
    ##############################     APPEND     ##############################
    def append_left(self, item):
        super().enqueue(item)


    def append_right(self, item):
        super()._validate_item(item)
        if self.is_full():
            warnings.warn(
                f"Enqueuing to a full `{self.__name__}` "+\
                    "could lead to missing values!!",
                UserWarning
            )
            self._container.remove_front()
        self._container._insert(len(self), item)



    #############################       GET       ##############################
    def get_left(self):
        if self.is_empty():
            raise IndexError(
                f"Can't retrieve from an empty `{self.__name__}`!!"
            )
        return self._container._head.get_data()
    

    def get_right(self):
        return super().top()




    ##############################       POP      ##############################
    def pop_left(self):
        if self.is_empty():
            warnings.warn(f"Dequeuing from an empty `{self.__name__}`!!")
            return
        else:
            return self._container.remove_front().get_data()


    def pop_right(self):
        return super().dequeue()


    def clear(self):
        super().clear()


