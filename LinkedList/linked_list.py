

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
        if not isinstance(next_item, Node) and next_item != None:
            raise TypeError("Linked List elements have to be of type `Node`")
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
        curr_node = self.head
        while(curr_node != None):
            item = curr_node.get_data()
            if item:
                width = len(str(item))+2 #2: for a space before & after an item
                top_border += (['─']*width) + ['┬']
                middle += [" {} →".format(item)]
                down_border += (['─']*width) + ['┴']
            curr_node = curr_node.get_next()
        top_border += ['─']
        middle += [' ']
        down_border += ['─']
        return "{}\n{}\n{}".format(\
            "".join(top_border), "".join(middle), "".join(down_border))


    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return self.length
    

    def __iter__(self):
        curr_node = self.head
        while(curr_node != None):
            yield curr_node
            curr_node = curr_node.get_next()


    def __getitem__(self, idx):
        """Retrieves the element at the given index. It allows -ve indexing"""
        # sanity check over given index
        if type(idx) != int:
            msg = "Indices must be an integer!"
            raise TypeError(msg)
        elif idx < -self.length or idx >= self.length:
            msg = "Can't find any element at the given index!!"
            raise IndexError(msg)
        else:
            # convert idx to positive if -ve
            if idx <= -1:
                idx += self.length
            # iterate over the linked list
            counter = 0
            curr_node = self.head
            while(counter != idx):
                counter += 1
                curr_node = curr_node.get_next()
            return curr_node


    def __setitem__(self, idx, item):
        self.insert(idx, item)


    def __delitem__(self, idx):
        """Removes a node at index=idx from the linked list"""
        if type(idx) != int:
            msg = "Indices must be an integer!!"
            raise TypeError(msg)
        elif idx <= -1:
            msg = "Linked List doesn't support -ve indexing with removal!!"
            raise IndexError(msg)
        elif idx >= self.length:
            msg = "Can't find any element at the given index!!"
            raise IndexError(msg)
        # handle edge case
        if idx == 0:
            self.remove_front()
        # handle general case
        else:
            counter = 0
            curr_node = self.head
            while(counter != idx-1):  
                curr_node = curr_node.get_next()
                counter += 1
            # curr_node is now at (idx-1)
            curr_node.set_next(curr_node.get_next().get_next())
            self.length -= 1


    def is_empty(self):
        """Checks if linked list is empty"""
        return self.length == 0


    def add_front(self, item):
        """Adds node at the head of the linked list with complexity of O(1)"""
        if self.is_empty():
            self.head = Node(item)
        else:
            new_node = Node(self.head.get_data())
            new_node.set_next(self.head.get_next())
            self.head = Node(item)
            self.head.set_next(new_node)
        self.length += 1


    def add_end(self, item):
        """Adds node at the tail of the linked list with complexity of O(n)"""
        if self.is_empty():
            self.head = Node(item)
        else:
            curr_node = self.head
            while(curr_node.get_next() != None):
                curr_node = curr_node.get_next()
            # now curr_node is the last node
            curr_node.set_next(Node(item))
        self.length += 1


    def insert(self, idx, item):
        """Inserts a certain item at a given index into the linked list"""
        if type(idx) != int:
            msg = "Indices must be an integer!"
            raise TypeError(msg)
        elif idx <= -1:
            msg = "Linked List doesn't support -ve indexing with insertion!!"
            raise IndexError(msg)
        elif idx == 0:
            self.add_front(item)
        else:
            counter = 0
            curr_node = self.head
            while(counter != idx-1):  
                curr_node = curr_node.get_next()
                counter += 1
            # curr_node is now at (idx-1)
            new_node = Node(item)
            new_node.set_next(curr_node.get_next())
            curr_node.set_next(new_node)
            self.length += 1


    def _remove_node(self, prev, node):
        assert node != None, "Can't remove `None` node"
        # if node to be removed is the first
        if prev == None:
            self.head = node.get_next() if node else None
        else:
            prev.set_next(node.get_next())
        self.length -= 1
    

    def remove_front(self):
        """Removes the linked list head with complexity of O(1)"""
        if not self.is_empty():
            self._remove_node(prev=None, node=self.head)


    def remove_end(self):
        """Removes the linked list tail with complexity of O(n)"""
        if not self.is_empty():
            if self.length == 1:
                self.remove_front()
            else:
                curr_node = self.head
                while(curr_node.get_next().get_next() != None):
                    curr_node = curr_node.get_next()
                self._remove_node(prev=curr_node, node=curr_node.get_next())


    def remove(self, value, all=True):
        #removes all occurrences (when all==True) of `value` if found.
        if not self.is_empty():
            prev = None
            curr_node = self.head
            FOUND_FIRST = False #True: when the first occurrence is found
            while(curr_node.get_next() != None):
                if FOUND_FIRST and all==False:
                    return
                if curr_node.get_data() == value:
                    self._remove_node(prev, curr_node)
                    FOUND_FIRST = True
                prev = curr_node
                curr_node = curr_node.get_next()


    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        if not self.is_empty():
            self.head = Node()
            self.length = 0


    def reverse(self):
        """Reverses the whole linked list with complexity of O(n)"""
        rev = LinkedList()
        curr_node = self.head
        while(curr_node.get_next() != None):
            rev.add_front(curr_node.get_data())
            curr_node = curr_node.get_next()
        rev.add_front(curr_node.get_data())
        return rev




if __name__ == "__main__":
    l = LinkedList()
    # test removing from empty list:
    l.remove_front() #Nothing
    l.remove_end()   #Nothing
    l.remove(10)     #Nothing
    del l[0]         #throughs IndexError

    # addinng
    l.add_front(6)   #6
    l.add_end(20)    #6 20
    print(l)
    l.insert(1, 10)   #6 10 20
    l.insert(2, 77)   #6 10 77 20
    l.insert(4, 43)   #6 10 77 20 43
    l.insert(0, 2)    #2 6 10 77 20 43
    print(l)
    del l[1]
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



