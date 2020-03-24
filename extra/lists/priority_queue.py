"""
PriorityQueue is a data structure which where every node has two values.
    - Key: Contains any value as the standard Queue
    - Priority: value that represents the priority

A priority node is represented like the following 0|P:45 where 0 is the key and 
45 is the priority. The higher the number is, the more priority it has.
"""
import random
import warnings
from extra.lists.doubly_linked_list import DoublyNode
from extra.lists.queue import Queue




class PriorityNode(DoublyNode):
    """Basic object for item inside Priority Queue"""
    def __init__(self, key, priority=None):
        if priority is not None and type(priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
        assert key is not None
        super().__init__(key)
        self.priority = \
            random.randint(-100, 100) if priority is None else priority
    

    def get_priority(self):
        return self.priority


    def set_priority(self, new_priority):
        assert type(new_priority) in {int, float}
        self.priority = new_priority


    def __repr__(self):
        """Represents Node object as a string"""
        return f"PriorityNode(data: {self.data}, Priority: {self.priority})"

    
    def _represent(self):
        if PriorityQueue.SHOW_PRIORITY:
            return f"{self.data}|P:{self.priority}"
        else:
            return f"{self.data}"




class PriorityQueue(Queue):
    """Basic object for the Priority Queue data structure where highest priority
    is zero."""
    SHOW_PRIORITY = False


    def __name__(self):
        return "extra.PriorityQueue()"

    
    ############################# ENQUEUE ##############################
    def __validate_priority(self, new_priority):
        if new_priority is not None and type(new_priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
    

    def enqueue(self, item, priority=None):
        """Insert value into the Priority Queue"""
        super()._validate_item(item)
        self.__validate_priority(priority)
        node = PriorityNode(item, priority)
        super()._enqueue(node)
    
    ##############################    DEQUEUE    ##############################





if __name__ == "__main__":
    q = PriorityQueue()
    q.enqueue(10)
    print(type(q.container[0]))
    print(q)