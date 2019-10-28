

class Node:
    """Basic object for the Node used for linked lists"""
    def __init__(self, item=None):
        self.data = item
        self.next = None


    def __repr__(self):
        """Represents Node object as a string"""
        data = self.data
        nxt = self.next.data if self.next else None
        return "Node: (item: {}, next: {})".format(data, nxt)


    def get_data(self):
        return self.data
    

    def get_next(self):
        return self.next
    

    def set_next(self, next_item):
        if not isinstance(next_item, Node):
            raise TypeError("Linked List elemnts have to be Node()")
        self.next = next_item
    



class LinkedList:
    """Basic object for the linked list"""
    def __init__(self, item=None):
        self.head = Node(item)
        self.length = 1 if item != None else 0


    def __repr__(self):
        """Represents the linked list as a string."""
        # NOTE: complexity of + operator is O(1) in lists and O(n) in string
        top_border = ['┌']
        middle = ['│']
        down_border = ['└']
        pointer = self.head
        while(pointer != None):
            item = pointer.data
            if item:
                width = len(str(item))+2 #2: for a space before & after an item
                top_border += (['─']*width) + ['┬']
                middle += [" {} →".format(item)]
                down_border += (['─']*width) + ['┴']
            pointer = pointer.next
        top_border += ['─']
        middle += [' ']
        down_border += ['─']
        return "{}\n{}\n{}".format(\
            "".join(top_border), "".join(middle), "".join(down_border))


    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return self.length


    def __validate_index(self, idx):
        if type(idx) != int:
            msg = "idx must be an integer!"
            raise TypeError(msg)
        elif idx < -self.length or idx >= self.length:
            msg = "max index for this linked list is " + str(self.length-1)
            raise IndexError(msg)
          

    def __getitem__(self, idx):
        """Retrieves the element at the given index. It allows -ve indexing"""
        # sanity check over given index
        self.__validate_index(idx)
        # convert idx to positive if -ve
        if idx <= -1:
            idx += self.length
        # handle edge case
        if idx == 0:
            return self.head
        # iterate over the linked list
        counter = 0
        curr_node = self.head
        while(curr_node.next != None):
            counter += 1
            curr_node = curr_node.next
            if curr_node == idx:
                return curr_node


    def is_empty(self):
        """Checks if linked list is empty"""
        return self.length == 0


    def add_front(self, item):
        """Adds node at the head of the linked list with complexity of O(1)"""
        if self.is_empty():
            self.head = Node(item)
        else:
            new_node = Node(self.head.data)
            new_node.set_next(self.head.next)
            self.head = Node(item)
            self.head.next = new_node
        self.length += 1


    def add_end(self, item):
        """Adds node at the tail of the linked list with complexity of O(n)"""
        if self.length == 0:
            self.head = Node(item)
        else:
            pointer = self.head
            while(pointer.next != None):
                pointer = pointer.next
            # now pointer is the last node
            pointer.next = Node(item)
        self.length += 1


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


    def insert(self, idx, item):
        """Inserts a certain item at a given index into the linked list"""
        if idx <= -1 and abs(idx) <= self.length+1:
            idx += self.length+1
        else:
            idx = self.__fix_index(idx)
        # handle edge case
        if idx == 0:
            self.add_front(item)
        # handle general case
        else:
            counter = 0
            pointer = self.head
            while(counter != idx-1):  
                pointer = pointer.next
                counter += 1
            # pointer is now at (idx-1)
            new_node = Node(item)
            new_node.next = pointer.next
            pointer.next = new_node
            self.length += 1


    def __setitem__(self, idx, item):
        self.insert(idx, item)


    def remove(self, idx):
        """Removes a node at index=idx from the linked list"""
        idx = self.__fix_index(idx)
        # handle edge case
        if idx == 0:
            self.remove_front()
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
    print(l)
    l.add_front(6)   #6
    l.add_end(20)    #6 20
    print(l)
    l.insert(1, 10)  #6 10 20
    l.insert(-2, 999)#6 10 999 20
    l.insert(-9, -555)#-555 6 10 1 2 3 4 999 20
    print(l)
    print("LENGTH:", len(l))


    l.remove(-9)     #6 10 1 2 3 4 999 20
    l.remove(-2)     #6 10 1 2 3 4 20
    l.remove_front() #10 1 2 3 4 20
    l.remove_end()   #10 1 2 3 4
    l.remove(0)      #1 2 3 4
    print(l)
    print("LENGTH:", len(l))
    
    print(l[0], l[3], "\n")

    rev = l.reverse()#4 3 2 1
    print(rev)
    print("REV LENGTH:", len(rev))
    print(rev[1], rev[2])

    l.clear()
    print("Linked List is empty?", l.is_empty())
    print("Reversed Linked List is empty?", rev.is_empty())



