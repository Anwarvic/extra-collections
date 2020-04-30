import warnings
from extra.interface import Extra




class Stack(Extra):
    """Basic object for the Stack data structure"""
    def __name__(self):
        return "extra.Stack()"

    
    def __init__(self, max_capacity=float("inf")):
        if type(max_capacity) not in {int, float}:
            raise TypeError(\
                f"Max Capacity {self.__name__()} has to be a number!!")
        elif max_capacity < 0:
            raise ValueError(\
                f"Max capacity of {self.__name__()} must be >= 0")
        self._container = []
        self._max_capacity = max_capacity


    ############################## PRINT ##############################
    def __repr__(self):
        """Represents the stack as a string."""
        top_border    = '┌'
        middle_border = '│'
        down_border   = '└'
        for item in self._container:
            #NOTE: +2 for a space before & after `item`
            width = len(str(item))+2
            top_border += ('─'*width) + '┬'
            middle_border += " {} │".format(item)
            down_border += ('─'*width) + '┴'
        # add extension
        top_border += '─'
        middle_border += ' '
        down_border += '─'
        return "{}\n{}\n{}".format(top_border, middle_border, down_border)


    ##############################     LENGTH     ##############################
    def __len__(self):
        """Gets the length of the stack with complexity of O(1)"""
        return len(self._container)


    ##############################      PUSH     ###############################
    def push(self, item):
        """Pushs item to the stack"""
        if self.is_full():
            raise OverflowError(\
                f"Stackoverflow! Can't push into a full {self.__name__()}!")
        super()._validate_item(item)
        self._container.append(item)


    ############################## PEEK ###############################
    def peek(self):
        """Returns the top item from the stack"""
        if self.is_empty():
            raise IndexError(f"Can't peek from an empty {self.__name__()}!!")
        return self._container[-1]


    ############################# REMOVE #############################
    def pop(self):
        """Pops item from the stack"""
        if self.is_empty():
            warnings.warn(f"Popping from empty {self.__name__()}!!", UserWarning)
            return
        else:
            return self._container.pop()


    def clear(self):
        """Clears the stack"""
        self.__init__(max_capacity=self._max_capacity)


    ############################# STATUS #############################
    def is_empty(self):
        """Checks if the stack is empty"""
        return len(self._container) == 0
    

    def is_full(self):
        """Checks if the stack is at full capacity"""
        return len(self) >= self._max_capacity


