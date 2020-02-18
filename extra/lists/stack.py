import warnings




class Stack:
    """Basic object for the Stack data structure"""
    def __name__(self):
        return "extra.Stack()"

    
    def __init__(self, max_capacity=float("inf")):
        if type(max_capacity) not in {int, float}:
            raise TypeError("Max Capacity has to be a number!!")
        elif max_capacity < 0:
            raise ValueError(f"Max capacity of {self.__name__()} must be >= 0!")
        self.container = []
        self.max_capacity = max_capacity


    ############################## PRINT ##############################
    def __repr__(self):
        """Represents the stack as a string."""
        top_border    = '┌'
        middle_border = '│'
        down_border   = '└'
        for item in self.container:
            width = len(str(item))+2 #2: for a space before & after item
            top_border += ('─'*width) + '┬'
            middle_border += " {} │".format(item)
            down_border += ('─'*width) + '┴'
        # add extension
        top_border += '─'
        middle_border += ' '
        down_border += '─'
        return "{}\n{}\n{}".format(top_border, middle_border, down_border)


    ############################## LENGTH ##############################
    def __len__(self):
        """Gets the length of the stack with complexity of O(1)"""
        return len(self.container)


    ############################## PUSH ###############################
    def __validate_item(self, item):
        if item is None:
            raise TypeError(f"Can't push `None` into {self.__name__()}!!")
        elif type(item) == str and item == '':
            raise ValueError(\
                f"Can't push empty-string into {self.__name__()}!!")


    def push(self, item):
        """Pushs item to the stack"""
        if self.is_full():
            raise OverflowError("Stackoverflow! Can't push into a full stack!")
        self.__validate_item(item)
        self.container.append(item)


    ############################## PEEK ###############################
    def peek(self):
        """Returns the top item from the stack"""
        if self.is_empty():
            raise IndexError("Can't peek from an empty Stack!!")
        return self.container[-1]


    ############################# REMOVE #############################
    def pop(self):
        """Pops item from the stack"""
        if self.is_empty():
            warnings.warn("Popping from empty Stack!!", UserWarning)
            return None
        else:
            return self.container.pop()


    def clear(self):
        """Clears the stack"""
        self.__init__(max_capacity=self.max_capacity)


    ############################# STATUS #############################
    def is_empty(self):
        """Checks if the stack is empty"""
        return len(self.container) == 0
    

    def is_full(self):
        """Checks if the stack is at full capacity"""
        return len(self) == self.max_capacity


