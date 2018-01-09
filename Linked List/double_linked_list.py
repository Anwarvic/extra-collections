class Node():
    """Basic object for the Node used for double linked lists"""
    def __init__(self, value=None):
        self.data = value
        self.prev = None
        self.next = None

    def __repr__(self):
        data = self.data
        nxt = self.next.data if self.next else None
        prv = self.prev.data if self.prev else None
        return "Node: (value: {}, previous: {}, next: {})".format(data, prv, nxt)


class DoubleLinkedList():
    """Basic object for the double linked list"""
    def __init__(self, value=None):
        self.head = self.tail = Node(value)
        self.length = 1 if value else 0

    
    def __repr__(self):
        """Represents the double linked list as a string"""
        pointer = self.head
        # handle edge case
        if pointer.data == None:
            return "[]"
        # general case
        output = "["
        while(pointer.next != None):
            output += "({}) <-> ".format(pointer.data)
            pointer = pointer.next
        output += "({})".format(pointer.data)
        return output+"]"


    def __len__(self):
        """Gets the length of the double linked list"""
        return self.length


    def __getitem__(self, idx):
        """Retrieves the element at the given index with complexity of O(n/2).
        It supports negative indexing."""
        # caliberate idx if -ve
        if idx <= -1:
            idx += self.length
        # sanity check over given index
        if idx >= self.length:
            raise IndexError("max index for this list is "+str(self.length-1))
        # handle edge case
        if idx == 0:
            return self.head
        elif idx == self.length-1:
            return self.tail
        elif idx < self.length//2:
            # iterate over the double linked list (forwards)
            pointer = self.head
            counter = 0
            while(pointer.next != None):
                counter += 1
                pointer = pointer.next
                if counter == idx:
                    return pointer
        else:
            # iterate over the double linked list (backwards)
            pointer = self.tail
            counter = self.length-1
            while(pointer.prev != None):
                counter -= 1
                pointer = pointer.prev
                if counter == idx:
                    return pointer


    def is_empty(self):
        """Checks if double linked list is empty"""
        return self.length == 0


    def add_front(self, value):
        """Adds node at the head of the linked list with complexity of O(1)"""
        if self.length == 0:
            self.head = self.tail = Node(value)
        elif self.length == 1:
            self.head = Node(value)
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            new_node = self.head
            # update head
            self.head = Node(value)
            self.head.next = new_node
            new_node.prev = self.head
        self.length += 1


    def add_end(self, value):
        """Adds node at the tail of the linked list with complexity of O(1)"""
        if self.head.data == None:
            self.head = self.tail = Node(value)
        elif self.length == 1:
            self.tail = Node(value)
            self.tail.prev = self.head
            self.head.next = self.tail
        else:
            new_node = self.tail
            self.tail = Node(value)
            self.tail.prev = new_node
            new_node.next = self.tail
        self.length += 1


    def remove_front(self):
        """Removes the linked list head with complexity of O(1)"""
        if len(self)>0:
            tmp = self.head.next
            tmp.prev = None
            self.head = tmp


    def remove_end(self):
        """Removes the linked list tail with complexity of O(n)"""
        if len(self)>0:
            tmp = self.head
            while(tmp.next.next != None):
                tmp = tmp.next
            tmp.next = None


    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        self.head = Node()


    def reverse(self):
        """Reverses the whole linked list with complexity of O(n)"""
        output = DoubleLinkedList()
        if self.head.data == None:
            return DoubleLinkedList()
        tmp = self.head.next
        while(tmp.next != None):
            output.add_front(tmp.prev.data)
            tmp = tmp.next
        output.add_front(tmp.prev.data)
        output.add_front(tmp.data)
        return output






if __name__ == "__main__":
    # l = DoubleLinkedList()
    # l.add_front(1) #1
    # l.add_front(0) #0 1
    # l.add_front(7) #7 0 1
    # l.add_front(20) #20 7 0 1
    # l.add_front(100) #100 20 7 0 1
    # print(l)
    # print(l[0])
    # print(l[1])
    # print(l[2])
    # print(l[3])
    # print(l[4])
    l = DoubleLinkedList()
    l.add_end(1) #1
    l.add_end(0) #1 0
    l.add_end(7) #1 0 7
    l.add_end(20) #1 0 7 20
    l.add_end(100) #1 0 7 20 100
    print(l)
    # print(l[0])
    # print(l[1])
    # print(l[2])
    # print(l[3])
    # print(l[4])
    # iterate over l backwards
    print("===== Backward Iteration =====")
    pointer = l.tail
    while(pointer != None):
        print(pointer)
        pointer = pointer.prev
    # iterate over l forward
    print("===== Forward Iteration =====")
    pointer = l.head
    while(pointer != None):
        print(pointer)
        pointer = pointer.next
    # print(l.reverse())
    # l.add_front(0) #0 1 0 7
    # l.add_front(2) #2 0 1 0 7
    # l.add_front(9) #9 2 0 1 0 7
    # print(l)
    # print(l[4].prev)
    # l.remove_end() #9 2 0 1 0
    # l.remove_front() #2 0 1 0
    # print(l)
    # print(l[0].prev)
    # print(l[0].next)
    # rev = l.reverse()
    # print(rev)
    # l.clear()
    # print(len(l))

