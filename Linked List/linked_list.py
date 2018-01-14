class Node():
    """Basic object for the Node used for linked lists"""
    def __init__(self, value=None):
        self.data = value
        self.next = None

    def __repr__(self):
        data = self.data
        nxt = self.next.data if self.next else None
        return "Node: (value: {}, next: {})".format(data, nxt)
    


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
            output += "({}) -> ".format(pointer.data)
            pointer = pointer.next
        output += "({})".format(pointer.data)
        return output+"]"


    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return self.length


    def __fix_index(self, idx):
        """
        private method to make a sanity-check over the given index and fix it
        if it was -ve. It should return the index if it's valid. If the index is
        negative, then it converts it to positive index if possible.
        If the index has any error of any kind, it raises an appropriate error.
        """
        if type(idx) != int:
            msg = "idx must be an integer!"
            raise TypeError(msg)
        # handle negative index
        if idx <=-1 and abs(idx) <= self.length+1:
            idx += self.length + 1
        elif abs(idx) > self.length:
            msg = "max index for this linked list is " + str(self.length)
            raise IndexError(msg)
        else:
            pass #direct
        return idx
            

    def __getitem__(self, idx):
        """Retrieves the element at the given index. It allows -ve indexing"""
        # sanity check over given index
        idx = self.__fix_index(idx)
        # handle edge cases
        if idx == 0:
            return self.head
        elif idx == self.length:
            msg = "max index for this linked list is " + str(self.length-1)
            raise IndexError(msg)
        # iterate over the linked list
        counter = 0
        pointer = self.head
        while(pointer.next != None):
            counter += 1
            pointer = pointer.next
            if counter == idx:
                return pointer


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
        idx = self.__fix_index(idx)
        # handle edge case
        if idx == 0:
            self.add_front(value)
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
        idx = self.__fix_index(idx)
        # handle edge cases
        if idx == 0:
            self.remove_front()
        elif idx == self.length:
            msg = "max index for this linked list is " + str(self.length-1)
            raise IndexError(msg)
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


    def insert_multiple(self, idx, lst):
        """Inserts multiple values into the linked list at once"""
        idx = self.__fix_index(idx)
        # handle edge case
        if idx == 0:
            # NOTE: iterate over given list in reverse-order as add_front() is
            # faster than add_end()
            for i in range(len(lst)-1, -1, -1):
                self.add_front(lst[i])
        # handle general case
        else:
            counter = 0
            pointer = self.head
            while(counter != idx-1):  
                pointer = pointer.next
                counter += 1
            # pointer is now at (idx-1)
            # iterate over given list in reverse-order
            for value in lst:
                new_node = Node(value)
                new_node.next = pointer.next
                pointer.next = new_node
                # update pointer
                pointer = pointer.next
                self.length += 1


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
    l.add_front(6)   #6
    l.add_end(20)    #6 20
    l.insert(1, 10)  #6 10 20
    l.insert(-2, 999)#6 10 999 20
    l.insert_multiple(2, [1, 2, 3, 4])  #6 10 1 2 3 4 999 20
    print(l, "LENGTH:", len(l), "\n")

    l.remove_front() #10 1 2 3 4 20
    l.remove_end()   #10 1 2 3 4
    l.remove(0)      #1 2 3 4
    print(l, "LENGTH:", len(l), "\n")

    # print(l[0], l[3], "\n")

    # rev = l.reverse()#4 3 2 1
    # print(rev, "REV LENGTH:", len(rev), "\n")
    # print(rev[1], rev[2], "\n")

    # print("Linked List is empty?", l.is_empty())
    # print(l, "LENGTH:", len(l), "\n")
    # l.clear()
    # print("Linked List is empty?", l.is_empty())
    # print(l, "LENGTH:", len(l), "\n")

