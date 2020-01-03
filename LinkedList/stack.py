
class Stack:
    """Basic object for the Stack data structure"""
    def __init__(self, max_capacity=float("inf")):
        assert type(max_capacity) in {int, float}, "Max Capacity is a number!!"
        self.container = []
        self.max_capacity = max_capacity


    ############################## PRINT ##############################
    def __repr__(self):
        """Represents the stack as a string."""
        top_border = '┌'
        middle = '│'
        down_border = '└'
        for item in self.container:
            width = len(str(item))+2 #2: for a space before & after item
            top_border += ('─'*width) + '┬'
            middle += " {} │".format(item)
            down_border += ('─'*width) + '┴'
        # add extension
        top_border += '─'
        middle += ' '
        down_border += '─'
        return "{}\n{}\n{}".format(top_border, middle, down_border)


    ############################## LENGTH ##############################
    def __len__(self):
        """Gets the length of the stack with complexity of O(1)"""
        return len(self.container)


    ############################## PUSH ###############################
    def push(self, item):
        """Pushs item to the stack"""
        if len(self.container) >= self.max_capacity:
            raise OverflowError("Stackoverflow! Can't push into a full stack!")
        self.container.append(item)


    ############################## PEEK ###############################
    def peek(self):
        """Returns the top item from the stack"""
        return self.container[-1]


    ############################# REMOVE #############################
    def pop(self):
        """Pops item from the stack"""
        return self.container.pop()


    def is_empty(self):
        """Checks if the stack is empty"""
        return len(self) == 0


    def clear(self):
        """Clears the stack"""
        self.__init__()




if __name__ == "__main__":
    s = Stack(max_capacity=3)
    s.push(2) #2
    print(s)
    s.push(40) #2 40
    print(s)
    s.push(800) #2 40 800
    s.push(1000000) #2 40 800 (won't push)
    print(s)

    print('='*20)
    print(s.peek()) #800
    print(s)
    print(s.pop())  #800
    print(s) #2 40
    
    print('='*20)
    print(s.is_empty()) #False
    s.clear()
    print(s)
    print(s.is_empty()) #True


 