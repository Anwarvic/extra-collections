import warnings

from extra.lists.queue import Queue




class Deque(Queue):
    """Basic object for the Deque data structure"""
    def __name__(self):
        return "extra.Deque()"
    

    ############################## PRINT ##############################
    def __repr__(self):
        """Represents the deque as a string."""
        return super()._print_queue('⟷')

    
    ############################## GET ################################
    def get_last(self):
        """Returns the Qeueu tail (last element to be enqueued) """
        if self.is_empty():
            raise IndexError(\
                f"Can't retrieve from an empty {self.__name__()}!!")
        return self.container.tail.get_data()


    ############################# APPEND ##############################
    def append_left(self, item):
        """Insert value into the front of the Deque"""
        super().enqueue(item)


    def append_right(self, item):
        """Insert value into the end of the Deque"""
        if len(self.container) >= self.max_capacity:
            self.container.remove_end()
        self.container.add_end(item)


    ############################## POP ###############################
    def pop_left(self):
        """Removes value from the Deque (first-inserted item)"""
        return self.container.remove_front()


    def pop_right(self):
        """Removes value from the Deque (most recent)"""
        return super().dequeue()




if __name__ == "__main__":
    q = Deque(max_capacity=3)
    q.append_left(0)    #0
    q.append_right(1)   #0 1
    q.append_right(8)   #0 1 8
    q.append_left(9)    #9 0 1
    print(q)
    