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
        super()._validate_item(key)
        super().__init__(key)
        self._priority = \
            random.randint(0, 100) if priority is None else priority
    

    def get_priority(self):
        return self._priority


    def set_priority(self, new_priority):
        assert type(new_priority) in {int, float}
        self._priority = new_priority


    def __repr__(self):
        """Represents Node object as a string"""
        return f"PriorityNode(data: {self.data}, Priority: {self._priority})"

    
    def _represent(self):
        if PriorityQueue.SHOW_PRIORITY:
            return f"{self.data}|P:{self._priority}"
        else:
            return f"{self.data}"




class PriorityQueue(Queue):
    """Basic object for the Priority Queue data structure where highest priority
    is zero."""
    SHOW_PRIORITY = False


    def __name__(self):
        return "extra.PriorityQueue()"


    def __init__(self, max_capacity=float("inf")):
        super().__init__(max_capacity)
        self._min_priority = float("inf")
        self._max_priority = float("-inf")
    

    ##############################     ENQUEUE    ##############################
    def __validate_priority(self, new_priority):
        if new_priority is not None and type(new_priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
    

    def enqueue(self, item, priority=None):
        """Insert value into the Priority Queue"""
        super()._validate_item(item)
        self.__validate_priority(priority)
        node = PriorityNode(item, priority)
        self._min_priority = min(self._min_priority, node.get_priority())
        self._max_priority = max(self._max_priority, node.get_priority())
        super()._enqueue(node)
    

    ##############################     DEQUEUE    ##############################
    def _update_min_priority(self):
        self._min_priority = float("inf")
        if not self.is_empty():
            curr_node = self._container._head
            while(curr_node is not None):
                self._min_priority = \
                    min(curr_node.get_priority(), self._min_priority)
                curr_node = curr_node.get_next()
    

    def _update_max_priority(self):
        self._max_priority = float("-inf")
        if not self.is_empty():
            curr_node = self._container._head
            while(curr_node is not None):
                self._max_priority = \
                    max(curr_node.get_priority(), self._max_priority)
                curr_node = curr_node.get_next()


    def dequeue(self, lowest_priority=False):
        """Removes the highest-priority value from the PriorityQueue"""
        if self.is_empty():
            warnings.warn(f"Dequeuing from an empty {self.__name__()}!!")
            return None
        else:
            curr_node = self._container._head
            while(curr_node is not None):
                if lowest_priority:
                    if curr_node.get_priority() == self._min_priority:
                        node_data = curr_node.get_data()
                        self._container._remove_node(curr_node.get_prev(),
                                                    curr_node)
                        self._update_min_priority()
                        break
                else:
                    if curr_node.get_priority() == self._max_priority:
                        node_data = curr_node.get_data()
                        self._container._remove_node(curr_node.get_prev(),
                                                    curr_node)
                        self._update_max_priority()
                        break
                curr_node = curr_node.get_next()
        return node_data


