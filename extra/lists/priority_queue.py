import random
from extra.lists.doubly_linked_list import DoublyNode
from extra.lists.queue import Queue




class DoublyPriorityNode(DoublyNode):
    """Basic object for item inside Priority Queue"""
    def __init__(self, key, priority=None):
        if priority is not None and type(priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
        assert key is not None
        super().__init__(key)
        self.priority = \
            random.randint(0, 100) if priority is None else priority
    

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


    def enqueue(self, item):
        """Insert value into the Priority Queue"""
        if len(self) == 0:
            self.container.append(item)
        else:
            new_data, new_priority = item.data, item.priority
            for i, _item in enumerate(self.container):
                curr_data, curr_priority = _item.data, _item.priority
                if new_priority <= curr_priority:
                    self.container = self.container[:i] + [item]\
                                         + self.container[i:]
                    break





if __name__ == "__main__":
    q = PriorityQueue()
    q.enqueue(10)
    print(type(q.container[0]))