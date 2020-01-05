from doubly_linked_list import DoublyLinkedList


class Queue():
    """Basic object for the Queue data structure"""
    def __init__(self, max_capacity=float("inf")):
        assert type(max_capacity) in {int, float}, "Max Capacity is a number!!"
        self.container = DoublyLinkedList()
        self.max_capacity = max_capacity


    ############################## PRINT ##############################
    def __repr__(self):
        """Represents the queue as a string."""
        top_border = '─┬'
        middle = '⟶│'
        down_border = '─┴'
        for item in self.container:
            width = len(str(item))+2 #2: for a space before & after item
            top_border += ('─'*width) + '┬'
            middle += " {} │".format(item)
            down_border += ('─'*width) + '┴'
        # add extension
        if not self.is_empty():
            top_border += '─'
            middle += '⟶'
            down_border += '─'
        return "{}\n{}\n{}".format(top_border, middle, down_border)


    ############################## LENGTH ##############################
    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return len(self.container)


    def enqueue(self, item):
        """Insert value into the Queue"""
        if len(self.container) >= self.max_capacity:
            # raise OverflowError("Can't push into a full queue!")
            self.container.remove_end()
        self.container.add_front(item)


    def dequeue(self):
        """Removes value from the Queue (Queue's head)"""
        return self.container.remove_end()


    def get_left(self):
        """Returns the Qeueu head (first element to be enqueued) """
        return self.container.head.get_data()


    def get_right(self):
        """Returns the Qeueu tail (last element to be enqueued) """
        return self.container.tail.get_data()


    def is_empty(self):
        """Checks if the Queue is empty"""
        return len(self.container) == 0


    def clear(self):
        """Clears the whole Queue"""
        self.__init__(max_capacity=self.max_capacity)




if __name__ == "__main__":
    q = Queue(max_capacity=3)
    q.enqueue(2)  #2
    print(q)
    q.enqueue(40) #2 40
    print(q)
    q.enqueue(800)#2 40 800
    q.enqueue('hello') #40 800 'hello' (replaces most left item)
    print(q)
    
    print('='*20)
    print(q.get_left()) #40
    print(q.get_right()) #'hello'
    q.dequeue()
    print(q) #800 'hello'

    print('='*20)
    print(q.is_empty()) #False
    q.clear()
    print(q)
    print(q.is_empty()) #True
    print(q.max_capacity)