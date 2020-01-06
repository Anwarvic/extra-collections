from queue import Queue




class Deque(Queue):
    """Basic object for the Deque data structure"""

    def __repr__(self):
        """Represents the deque as a string."""
        return super()._print_queue('⟷')


    def append_left(self, item):
        """Insert value into the front of the Deque"""
        if self.max_capacity and len(self) == self.max_capacity:
            self.remove_right()
        self.container.insert(0, item)


    def append_right(self, item):
        """Insert value into the end of the Deque"""
        if self.max_capacity and len(self) == self.max_capacity:
            self.remove_left()
        self.container.append(item)


    def remove_left(self):
        """Removes value from the Deque (first-inserted item)"""
        return self.container.pop(0)


    def remove_right(self):
        """Removes value from the Deque (most recent)"""
        return self.container.pop()


    def peek(self):
        """Returns the Deque recent item"""
        return self.container[-1]




if __name__ == "__main__":
    q = Deque(max_capacity=3)
    q.append_left(0) #0
    q.append_right(1)   #0 1
    q.append_right(8)   #0 1 8
    q.append_left(9) #9 0 1
    print(q)
    