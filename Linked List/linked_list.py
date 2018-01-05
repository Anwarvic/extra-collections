class Node():
    """Basic object for the Node used for linked lists"""
    def __init__(self, value=None):
        self.data = value
        self.next = None

    def __repr__(self):
        if self.next:
            return "Node: (value: {}, next: {})".format(self.data, self.next.data)
        else:
            return "Node: (value: {}, next: {})".format(self.data, self.next)
    


class LinkedList():
    """Basic object for the linked list"""
    def __init__(self, value=None):
        self.head = Node(value)
        self.length = 1 if value else 0


    def __repr__(self):
        """Represents the linked list as a string"""
        pointer = self.head
        # handle edge case
        if pointer.data == None:
            return "[]"
        # general case
        output = "["
        while(pointer.next != None):
            output += str(pointer.data) + ", "
            pointer = pointer.next
        output += str(pointer.data)
        return output+"]"


    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return self.length


    def __getitem__(self, idx):
        """Retrieves the value at the given index. It allows -ve indexing"""
        # caliberate idx if -ve
        if idx <= -1:
            idx += self.length
        # sanity check over given index
        if idx >= self.length:
            raise IndexError("max index for this list is "+str(self.length-1))
        pointer = self.head
        # handle edge case
        if idx == 0: return pointer.data
        # iterate over the linked list
        counter = 0
        while(pointer.next != None):
            counter += 1
            pointer = pointer.next
            if counter == idx:
                return pointer.data


    def is_empty(self):
        """Checks if linked list is empty"""
        return self.length == 0


    def add_front(self, value):
        """Adds node at the head of the linked list with complexity of O(1)"""
        self.length += 1
        if self.head.data == None:
            self.head = Node(value)
        else:
            new_node = Node(self.head.data)
            new_node.next = self.head.next
            self.head = Node(value)
            self.head.next = new_node


    def add_end(self, value):
        """Adds node at the tail of the linked list with complexity of O(n)"""
        self.length += 1
        if self.head.data == None:
            self.head = Node(value)
        else:
            pointer = self.head
            while(pointer.next != None):
                pointer = pointer.next
            # now pointer is the last node
            pointer.next = Node(value)


    def remove_front(self):
        """Removes the linked list head with complexity of O(1)"""
        if self.length > 0:
            self.head = self.head.next
            self.length -= 1


    def remove_end(self):
        """Removes the linked list tail with complexity of O(n)"""
        if self.length > 0:
            pointer = self.head
            while(pointer.next.next != None):
                pointer = pointer.next
            # now the pointer is the second last node
            pointer.next = None
            self.length -= 1


    def insert(self, idx, value):
        """Inserts a certain value at a given index into the linked list"""
        # handle edge cases
        if idx > self.length:
            msg = "Index cannot be bigger than the size of the linked list"
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
            pointer.next = new_node
            self.length += 1


    def remove(self, idx):
        """Removes a node at index=idx from the linked list"""
        # handle edge cases
        if idx > self.length:
            msg = "Index cannot be bigger than the size of the linked list"
            raise IndexError(msg)
        elif idx == 0:
            self.remove_front(value)
        elif idx == self.length:
            self.remove_end(value)
        # handle general case
        else:
            counter = 0
            pointer = self.head
            while(counter != idx-1):  
                pointer = pointer.next
                counter += 1
            # pointer is now at (idx-1)
            pointer.next = pointer.next.next
            self.length -= 1


    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        self.head = Node()
        self.length = 0


    def reverse(self):
        """Reverses the whole linked list with complexity of O(n)"""
        rev = LinkedList()
        pointer = self.head
        while(pointer.next != None):
            rev.add_front(pointer.data)
            pointer = pointer.next
        rev.add_front(pointer.data)
        return rev




if __name__ == "__main__":
    l = LinkedList()
    rev = l.reverse()
    l.insert(idx=0, value=1) #1
    l.add_end(7) #1 7
    l.insert(idx=1, value=0) #1 0 7
    l.insert(idx=1, value=[100]) #1 [100] 0 7
    l.remove(idx=1) #1 0 7
    print(l[2])
    print(l)
    l.add_front(0) #0 1 0 7
    l.add_front(2) #2 0 1 0 7
    l.add_front(9) #9 2 0 1 0 7
    rev = l.reverse()
    print(l)
    print(rev)
    l.remove_end() #9 2 0 1 0
    l.remove_front() #2 0 1 0
    print(l.is_empty()) #False
    print(l) #2 0 1 0
    l.clear()
    print(l.is_empty()) #True
    print(len(l)) #0
