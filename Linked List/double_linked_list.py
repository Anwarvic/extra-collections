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
        """Adds node at the tail of the double linked list with O(1) complexity """
        if self.length == 0:
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
        """Removes the double linked list head with complexity of O(1)"""
        if self.length > 0:
            if self.length == 1:
                self.head = self.tail = Node()
            else:
                self.head = self.head.next
                self.head.prev = None
            self.length -= 1


    def remove_end(self):
        """Removes the double linked list tail with complexity of O(1)"""
        if self.length > 0:
            if self.length == 1:
                self.tail = self.head = Node()
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.length -= 1


    def insert(self, idx, value):
        """Inserts a certain value at a given index into the double linked list"""
        # handle edge cases
        if idx > self.length:
            msg = "idx cannot be bigger than the size of the double linked list"
            raise IndexError(msg)
        elif idx == 0:
            self.add_front(value)
        elif idx == self.length:
            self.add_end(value)
        # handle general case
        else:
            counter = 0
            pointer = self.head
            while(counter != idx-1):  
                pointer = pointer.next
                counter += 1
            # pointer is now at (idx-1)
            new_node = Node(value)
            new_node.next = pointer.next
            pointer.next.prev = new_node
            new_node.prev = pointer
            pointer.next = new_node
            self.length += 1


    def remove(self, idx):
        """Removes a node at index=idx from the double linked list"""
        if idx > self.length:
            msg = "idx cannot be bigger than the size of the double linked list"
            raise IndexError(msg)
        elif idx == 0:
            self.remove_front()
        elif idx == self.length-1:
            self.remove_end()
        # handle general case
        else:
            counter = 0
            pointer = self.head
            while(counter != idx-1):  
                pointer = pointer.next
                counter += 1
            # pointer is now at (idx-1)
            next_pointer = pointer.next.next
            next_pointer.prev = pointer
            pointer.next = next_pointer
            self.length -= 1


    def insert_multiple(self, idx, lst):
        """Inserts multiple values into the linked list at once"""
        # handle edge cases
        if idx > self.length:
            msg = "idx cannot be bigger than the size of the double linked list"
            raise IndexError(msg)
        elif idx == 0:
            # iterate over given list in reverse-order
            for i in range(len(lst)-1, -1, -1):
                value = lst[i]
                self.add_front(value)
        # handle general case
        elif idx < self.length//2:
            # iterate over the double linked list (forwards)
            counter = 0
            pointer = self.head
            while(counter != idx-1):  
                pointer = pointer.next
                counter += 1
            # pointer is now at (idx-1)
            # iterate over given list in reverse-order
            for i in range(0, len(lst)):
                # define main nodes
                new_node = Node(lst[i])
                next_pointer = pointer.next
                # adjuct connections
                new_node.next = next_pointer
                next_pointer.prev = new_node
                new_node.prev = pointer
                pointer.next = new_node
                # update pointer
                pointer = pointer.next
                self.length += 1
        else:
            # iterate over the double linked list (backwords)
            pointer = self.tail
            counter = self.length-1
            while(counter != idx-1):
                pointer = pointer.next
                counter -= 1
            # pointer is now at (idx-1)
            # iterate over given list in reverse-order
            for i in range(0, len(lst)):
                # define main nodes
                new_node = Node(lst[i])
                prev_pointer = pointer.prev
                # adjuct connections
                new_node.prev = prev_pointer
                prev_pointer.next = new_node
                new_node.next = pointer
                pointer.prev = new_node
                # update pointer
                pointer = pointer.prev
                self.length += 1


    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        self.head = self.tail = Node()
        self.length = 0


    def reverse(self):
        """Reverses the whole double linked list with complexity of O(n)"""
        rev = DoubleLinkedList()
        if self.length == 0:
            return DoubleLinkedList()
        # iterate over original double linked list in (forward)
        pointer = self.head
        while(pointer != None):
            rev.add_front(pointer.data)
            pointer = pointer.next
        return rev






if __name__ == "__main__":
    l = DoubleLinkedList()
    l.add_front(6)   #6
    l.add_end(20)    #6 20
    l.insert(1, 10)  #6 10 20
    l.insert_multiple(2, [1, 2, 3, 4])  #6 10 1 2 3 4 20
    print(l, "LENGTH:", len(l), "\n")

    # l.remove_front() #10 1 2 3 4 20
    # l.remove_end()   #10 1 2 3 4
    # print(l, "LENGTH:", len(l), "\n")
    # l.remove(0)      #1 2 3 4
    # print(l, "LENGTH:", len(l), "\n")

    # print(l[0], l[3], "\n")

    # rev = l.reverse()#4 3 2 1
    # print(rev, "REV LENGTH:", len(rev), "\n")
    # print(rev[1], rev[2], "\n")

    # print("Linked List is empty?", l.is_empty())
    # print(l, "LENGTH:", len(l), "\n")
    # l.clear()
    # print("Linked List is empty?", l.is_empty())
    # print(l, "LENGTH:", len(l), "\n")



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
