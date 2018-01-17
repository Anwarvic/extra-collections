class Queue():
    def __init__(self):
        self.container = []

    def __repr__(self):
        top_border = '' if self.container else '┬'
        middle = '' if self.container else '│'
        down_border = '' if self.container else '┴'
        for item in self.container:
            width = len(str(item))+2 #2: for a space before & after item
            top_border += ('─'*width) + '┬'
            middle += " {} │".format(item)
            down_border += ('─'*width) + '┴'
        # add extension
        top_border += '─'
        down_border += '─'
        return "{}\n{}\n{}".format(top_border, middle, down_border)

    def __len__(self):
        return len(self.container)

    def enqueue(self, item):
        self.container.append(item)

    def dequeue(self):
        return self.container.pop(0)

    def get_head(self):
        return self.container[0]

    def get_tail(self):
        return self.container[-1]

    def is_empty(self):
        return self.container == 0

    def clear(self):
        self.container = []



if __name__ == "__main__":
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(8)
    q.enqueue(9)
    print(q.get_head())
    q.dequeue()
    print(q)
    q.clear()
    print(q)