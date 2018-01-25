class Node():
    """Basic object for the Node used for Circular linked lists"""
    def __init__(self, item=None):
        self.data = item
        self.next = None

    def __repr__(self):
        """Represents Node object as a string"""
        data = self.data
        nxt = self.next.data if self.next else None
        return "Node: (item: {}, next: {})".format(data, nxt)



class CircularLinkedList():
    """Basic object for the Circular Linked List"""
    def __init__(self, item=None):
        self.head = Node(item)
        self.head.next = self.head
        self.length = 1 if item else 0


    def __repr__(self):
        """Represents the Circular linked list as a string"""
        # NOTE: complexity of + operator is O(1) in lists and O(n) in string
        first_line = ['┌']
        second_line = ['│']
        third_line = ['└']
        fourth_line = ''
        fifth_line = ''
        pointer = self.head
        while(pointer.next != self.head):
            item = pointer.data
            width = len(str(item))+2 #2: for a space before & after an item
            first_line += (['─']*width) + ['┬']
            second_line += [" {} →".format(item)]
            third_line += (['─']*width) + ['┴']
            pointer = pointer.next
        # add last item
        item = pointer.data
        width = len(str(item))+2 #2: for a space before & after an item
        first_line += (['─']*width) + ['┬']
        second_line += [" {} →".format(item)]
        third_line += (['─']*width) + ['┴']
        # backtrace representation
        second_line += [' ┐']
        third_line += [' │']
        left_offset = (len(str(self.head.data))+3)//2
        remaining = len(first_line) - left_offset
        fourth_line = (' '*left_offset) + '^' + (' '*(remaining)) + '│'
        fifth_line = (' '*left_offset) + '└' + ('─'*(remaining)) + '┘'
        return "{}\n{}\n{}\n{}\n{}".format(\
            "".join(first_line), "".join(second_line), "".join(third_line),\
            fourth_line, fifth_line)


    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return self.length


    def __fix_index(self, idx):
        """
        private method to return the appropriate index for the circular linked
        list. If the given index is negative, then it converts it to a positive one.
        It raises a TypeError if the index isn't integer.
        """
        if type(idx) != int:
            msg = "idx must be an integer!"
            raise TypeError(msg)
        if self.length == 0:
            return 0
        else:
            idx = idx % (self.length)
            return idx


    def __getitem__(self, idx):
        """Retrieves the element at the given index."""
        # sanity check over given index
        idx = self.__fix_index(idx)
        pointer = self.head
        # handle edge case
        if idx == 0:
            return self.head
        # iterate over the linked list
        counter = 0
        pointer = self.head
        while(pointer.next != self.head):
            counter += 1
            pointer = pointer.next
            if counter == idx:
                return pointer


    def is_empty(self):
        """Checks if circular linked list is empty"""
        return self.length == 0


    def add_front(self, item):
        """Adds node at the head of the circular linked list in O(1)"""
        if self.head.data == None:
            self.head.data = item
        else:
            old_head = Node()
            old_head.data = self.head.data
            old_head.next = self.head.next
            self.head.data = item
            self.head.next = old_head
        self.length += 1


    def add_end(self, item):
        """Adds node at the head of the circular linked list"""
        if self.length == 0:
            self.head.data = item
        else:
            pointer = self.head
            while(pointer.next != self.head):
                pointer = pointer.next
            new_node = Node(item)
            new_node.next = self.head
            pointer.next = new_node
        self.length += 1


    def remove_front(self):
        """Removes the circular linked list head with complexity of O(1)"""
        if self.length == 1:
            self.head.data = None
            self.length -= 1
        elif self.length > 1:
            pointer = self.head
            while(pointer.next != self.head ):
                pointer = pointer.next
            #pointer is the last item in the circular linked list
            self.head = self.head.next
            pointer.next = self.head
            self.length -= 1
    

    def remove_end(self):
        """Removes the circular linked list tail with complexity of O(n)"""
        if self.length == 1:
            self.head.data = None
            self.length -= 1
        elif self.length > 0:
            pointer = self.head
            while(pointer.next.next != self.head):
                pointer = pointer.next
            #pointer is now at the second last item
            pointer.next = self.head
            self.length -= 1


    def insert(self, idx, item):
        """Inserts an item at a given index into the circular linked list"""
        idx = self.__fix_index(idx)
        if idx == 0:
            self.add_front(item)
        else:
            pointer = self.head
            counter = 0
            while(counter != idx-1):
                counter += 1
                pointer = pointer.next
            new_node = Node(item)
            new_node.next = pointer.next
            pointer.next = new_node
            self.length += 1


    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        self.head = Node()
        self.head.next = self.head
        self.length = 0


    def reverse(self):
        """Reverses the whole linked list with complexity of O(n)"""
        rev = CircularLinkedList()
        pointer = self.head
        while(pointer.next != self.head):
            rev.add_front(pointer.data)
            pointer = pointer.next
        rev.add_front(pointer.data)
        return rev




if __name__ == "__main__":
    l = CircularLinkedList()
    l.insert(100, 'item')
    print(l)
    # l.add_front(100)
    # l.add_front(700)
    # l.add_end(90)
    # l.add_front("B")
    # print(l)
    # print(l[-10])

    # l.insert(10, 'item')
    # print(l)

    # rev = l.reverse()
    # rev.remove_end()
    # print(rev)
    # print(rev[-1])
    # print(rev.is_empty())
    
    # rev.remove_front()
    # print(rev.is_empty())
