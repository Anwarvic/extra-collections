class Item:
    """Basic object for item inside Priority Queue"""
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __repr__(self):
        return "Item: {}, priority: {}".format(self.data, self.priority)



class PriorityQueue:
    """Basic object for the Priority Queue data structure"""
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

    def enqueue(self, item):
        """Insert value into the Priority Queue"""
        for i, num in enumerate(self.container):
            if item >= num:
                self.container.insert(i, item)
                return
        self.container.append(item)

    def dequeue(self):
        """Removes value from the Priority Queue (Queue's head)"""
        return self.container.pop(0)

    def head(self):
        """Returns the Priority Qeueu head (first element to be enqueued) """
        return self.container[0]

    def tail(self):
        """Returns the Priority Qeueu tail (last element to be enqueued) """
        return self.container[-1]

    def is_empty(self):
        """Checks if the Priority Queue is empty"""
        return self.container == 0

    def clear(self):
        """Clears the whole Priority Queue"""
        self.container = []




if __name__ == "__main__":
    q = PriorityQueue()
    q.enqueue(1)
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(-1)
    print(q)
    q.dequeue()
    print(q)
    q.clear()
    print(q)