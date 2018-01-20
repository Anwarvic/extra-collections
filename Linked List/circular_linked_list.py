class Node():
    def __init__(self, value=None):
        self.data = value
        self.next = None

    def __repr__(self):
        """Represents Node object as a string"""
        data = self.data
        nxt = self.next.data if self.next else None
        return "Node: (value: {}, next: {})".format(data, nxt)


class CircularLinkedList():
    """Basic object for the Circular Linked List"""
    def __init__(self, value=None):
        self.head = Node(value)
        self.head.next = self.head
        self.length = 1 if value else 0


    def __repr__(self):
        """Represents the Circular linked list as a string"""
        pointer = self.head
        # handle edge case
        if pointer.data == None:
            return "[]"
        # handle general case
        top_line = ""
        while(pointer.next != self.head):
            top_line += "({}) -> ".format(pointer.data)
            pointer = pointer.next
        top_line += "({}) -> ".format(pointer.data)
        # backtrace representation
        left_offset = (len(str(self.head.data))+1)//2
        remaining = len(top_line) - left_offset
        top_line += '┐'
        middle_line = (' '*left_offset) + '^' + (' '*(remaining-1)) + '│'
        bottom_line = (' '*left_offset) + '└' + ('─'*(remaining-1)) + '┘'
        return "{}\n{}\n{}".format(top_line, middle_line, bottom_line)


    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return self.length


    def __getitem__(self, num):
        """Retrieves the element at the given index."""
        #TODO: handle It allows -ve indexing
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
        """Checks if circular linked list is empty"""
        if len(self) == 0:
            return True
        return False


    def add_front(self, item):
        """Adds node at the head of the circular linked list in O(1)"""
        if self.head.data == None:
            self.head.data = item
        else:
            new = Node()
            new.data = self.head.data
            new.next = self.head.next
            self.head.data = item
            self.head.next = new
        self.length += 1


    def add_end(self, item):
        """Adds node at the head of the circular linked list"""
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
        self.length += 1


    def remove_front(self):
        """Removes the circular linked list head with complexity of O(1)"""
        if len(self)>0:
            last = self.head
            while(last.next != self.head ):
                last = last.next
            tmp = self.head.next
            self.head = tmp
            last.next = self.head
            self.length -= 1            
            


    def remove_end(self):
        """Removes the circular linked list tail with complexity of O(n)"""
        if len(self)>0:
            tmp = self.head
            while(tmp.next.next != self.head):
                tmp = tmp.next
            tmp.next = self.head
            self.length -= 1


    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        self.head = Node()
        self.head.next = self.head
        self.length = 0


    def reverse(self):
        """Reverses the whole linked list with complexity of O(n)"""
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
    print(len(l))
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




