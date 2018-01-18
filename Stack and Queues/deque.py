class Deque():
    def __init__(self):
        self.container = []

    def __repr__(self):
        output = "["
        for item in self.container:
            output += str(item)
            if item != self.container[-1]:
                output += ", "
        return output+"]"

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
 