class Deque():
    def __init__(self):
        self.container = []

    def __repr__(self):
        top_border = '─┬'
        middle = ' │'
        down_border = '─┴'
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

    def add_front(self, item):
        self.container.insert(0, item)

    def add_end(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def eject(self):
        return self.container.pop(0)

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return self.container == 0

    def clear(self):
        self.container = []




if __name__ == "__main__":
    q = Deque()
    q.add_front(0)
    q.add_end(1)
    q.add_end(8)
    q.add_front(9)
    print(q)
    