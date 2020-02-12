from extra.lists.doubly_linked_list import DoublyLinkedList




class Queue():
    """Basic object for the Queue data structure"""
    def __init__(self, max_capacity=float("inf")):
        assert type(max_capacity) in {int, float}, "Max Capacity is a number!!"
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


    ############################## PEEK ################################
    def get_first(self):
        """Returns the Qeueu head (first element to be inserted) """
        if self.is_empty():
            raise IndexError("Can't retrieve from an empty Queue!!")
        return self.container.head.get_data()


    ############################# ENQUEUE ##############################
    def enqueue(self, item):
        """Insert value into the Queue"""
        if len(self.container) >= self.max_capacity:
            # raise OverflowError("Can't push into a full queue!")
            self.container.remove_end()
        self.container.add_front(item)


    ############################# DEQUEUE ##############################
    def dequeue(self):
        """Removes value from the Queue (Queue's head)"""
        return self.container.remove_end()


    def is_empty(self):
        """Checks if the Queue is empty"""
        return self.container.is_empty()


    def clear(self):
        """Clears the whole Queue"""
        self.__init__(max_capacity=self.max_capacity)




if __name__ == "__main__":
    q = Queue(max_capacity=3)
    q.enqueue(2)  #2
    print(q)
    q.enqueue(40) #40 2
    print(q)
    q.enqueue(800)#800 42 2
    q.enqueue('hello') #hello 800 40 (replaces most right item)
    print(q)
    
    print('='*20)
    print(q.get_left()) #hello
    print(q.get_right()) #'40
    q.dequeue()
    print(q) #hello 800

    print('='*20)
    print(q.is_empty()) #False
    q.clear()
    print(q)
    print(q.is_empty()) #True
    print(q.max_capacity)