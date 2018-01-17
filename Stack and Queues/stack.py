class Stack():
    """Basic object for the Stack data structure"""
    def __init__(self):
        self.container = []

    def __repr__(self):
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

    def __len__(self):
        return len(self.container)

    def push(self, item):
        """Pushs item to the stack"""
        self.container.append(item)

    def pop(self):
        """Pops item from the stack"""
        return self.container.pop()

    def peek(self):
        """Returns the top item from the stack"""
        return self.container[-1]

    def is_empty(self):
        """Checks if the stack is empty"""
        return len(self) == 0

    def clear(self):
        """Clears the stack"""
        self.container = []



if __name__ == "__main__":
    s = Stack()
    s.push(2) #2
    print(s)
    s.push(40) #2 40
    print(s)
    s.push(800) #2 40 800
    print(s)

    print('='*20)
    print(s.peek())
    print(s)
    print(s.pop())
    print(s)
    
    print('='*20)
    print(s.is_empty())
    s.clear()
    print(s)
    print(s.is_empty())


 