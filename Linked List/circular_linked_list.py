class Node():
    def __init__(self, value=None):
        self.data = value
        self.next = None

    def __repr__(self):
        data = self.data
        nxt = self.next.data if self.next else None
        return "Node: (value: {}, next: {})".format(data, nxt)


class CircularLinkedList():
    def __init__(self, value=None):
        self.head = Node(value)
        self.head.next = self.head
        self.length = 1 if value else 0


    def __repr__(self):
        pointer = self.head
        # handle edge case
        if pointer.data == None:
            return "[]"
        # handle general case
        output = ""
        while(pointer.next != self.head):
            output += "({}) -> ".format(pointer.data)
            pointer = pointer.next
        output += "({}) -> ".format(pointer.data)
        # backtrace representation
        offset = (len(str(self.head.data))+1)//2
        remaining = len(output) - offset
        middle = (' '*offset) + '^' + (' '*(remaining-1)) + '│'
        bottom = (' '*offset) + '└' + ('─'*(remaining-1)) + '┘'
        return "{}┐\n{}\n{}".format(output, middle, bottom)


    def __len__(self):
        length = 0
        tmp = self.head
        if tmp.data == None:
            return length
        while(tmp.next != self.head):
            length += 1
            tmp = tmp.next
        return length+1


    def __getitem__(self, num):
        if len(self) <= num or num <= -1:
            raise IndexError
        counter = 0
        tmp = self.head
        if num == 0:
            return tmp
        while(tmp.next != self.head):
            tmp = tmp.next
            counter += 1
            if counter == num:
                return tmp


    def is_empty(self):
        if len(self) == 0:
            return True
        return False


    def add_front(self, item):
        if self.head.data == None:
            self.head.data = item
        else:
            new = Node()
            new.data = self.head.data
            new.next = self.head.next
            self.head.data = item
            self.head.next = new


    def add_end(self, item):
        if self.head.data == None:
            self.head.data = item
        else:
            tmp = self.head
            while(tmp.next != self.head):
                tmp = tmp.next
            new = Node()
            new.data = item
            new.next = self.head
            tmp.next = new


    def remove_front(self):
        if len(self)>0:
            last = self.head
            while(last.next != self.head ):
                last = last.next
            tmp = self.head.next
            self.head = tmp
            last.next = self.head
            # print "length", len(self)
            


    def remove_end(self):
        if len(self)>0:
            tmp = self.head
            while(tmp.next.next != self.head):
                tmp = tmp.next
            tmp.next = self.head


    def clear(self):
        self.head = Node()
        self.head.next = self.head


    def reverse(self):
        output = CircularLinkedList()
        tmp = self.head
        while(tmp.next != self.head):
            output.add_front(tmp.data)
            tmp = tmp.next
        output.add_front(tmp.data)
        return output




if __name__ == "__main__":
    l = CircularLinkedList()
    # print l
    # print len(l)
    l.add_end(10000000000000) #1
    l.add_end(0) #1 0
    l.add_end(7) #1 0 7
    print(l)
    # print l
    # print l[2].next
    l.add_front(0) #0 1 0 7
    l.add_front(2) #2 0 1 0 7
    l.add_front(9) #9 2 0 1 0 7
    # print l
    # rev = l.reverse()
    # print rev
    # print l[5].next
    l.remove_end() #9 2 0 1 0
    l.remove_front() #2 0 1 0
    print(l[3].next)
    # print l.is_empty()
    print(l)
    l.clear()
    print(l.is_empty())




