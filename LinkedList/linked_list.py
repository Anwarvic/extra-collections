

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


    def __contains__(self, value):
        found_node = self._search(value)
        if found_node == None or found_node.get_data() != value:
            return False
        return True


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


    def _insert_node(self, prev_node, new_node):
        assert new_node != None, "Can't insert `None` value as a node!!"
        if prev_node == None:
            if not self.is_empty(): new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        self.length += 1
        return new_node


    def add_front(self, item):
        """Adds node at the head of the linked list with complexity of O(1)"""
        self._insert_node(prev_node=None, new_node=Node(item))


    def add_end(self, item):
        """Adds node at the tail of the linked list with complexity of O(n)"""
        prev_node = None
        curr_node = self.head
        while(curr_node != None):
            prev_node = curr_node
            curr_node = curr_node.get_next()
        self._insert_node(prev_node, Node(item))


    def insert(self, idx, item):
        """Inserts a certain item at a given index into the linked list"""
        if type(idx) != int:
            msg = "Indices must be an integer!"
            raise TypeError(msg)
        elif idx <= -1:
            msg = "Linked List doesn't support -ve indexing with insertion!!"
            raise IndexError(msg)
        else:
            counter = 0
            prev_node = None
            curr_node = self.head
            while(counter != idx):
                counter += 1
                prev_node = curr_node
                curr_node = curr_node.get_next()
            self._insert_node(prev_node, Node(item))


    def _remove_node(self, prev_node, node):
        assert node != None, "Can't remove `None`!!"
        # if node to be removed is the first
        if prev_node == None:
            self.head = node.get_next()
        else:
            prev_node.set_next(node.get_next())
        self.length -= 1
    

    def remove_front(self):
        """Removes the linked list head with complexity of O(1)"""
        if not self.is_empty():
            self._remove_node(prev_node=None, node=self.head)


    def remove_end(self):
        """Removes the linked list tail with complexity of O(n)"""
        if not self.is_empty():
            prev_node = None
            curr_node = self.head
            while(curr_node.get_next() != None):
                prev_node = curr_node
                curr_node = curr_node.get_next()
            self._remove_node(prev_node, curr_node)


    def remove(self, value, all=True):
        #removes all occurrences (when all==True) of `value` if found.
        prev = None
        curr_node = self.head
        FOUND_FIRST = False #True when the first occurrence is found
        while(curr_node != None):
            if all==False and FOUND_FIRST:
                return
            if curr_node.get_data() == value:
                FOUND_FIRST = True
                self._remove_node(prev, curr_node)
                curr_node = prev.get_next() if prev != None else self.head
            else:
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


    def _search(self, value):
        # Search the Linked List for a given `value` and returns the first node
        # containing that value if found. If not found, it returns the last node
        # in the Linked List.
        curr_node = self.head
        # returns `None` if Linked List is empty
        if self.is_empty(): return curr_node
        while(curr_node.get_next() != None):
            if curr_node.get_data() == value:
                return curr_node
            curr_node = curr_node.get_next()
        return curr_node




if __name__ == "__main__":
    l = LinkedList()
    # test removing from empty list:
    l.remove_front() #Nothing
    l.remove_end()   #Nothing
    l.remove(10)     #Nothing
    # del l[0]       #throughs IndexError

    l.add_front(10)  #10 
    l.add_front(5)   #5 10
    print(l)
    l.remove(20)     #nothing
    l.remove_front() #10
    print(l)
    l.remove_end()   #[]
    print(l)
    l.insert(0, 100) #100
    l.insert(1, 200) #100 200
    l.insert(1, 100) #100 100 200
    print(l)
    l.remove(100)    #200
    print(l)
    l.clear()

    # test remove() alone
    l.add_end(0)
    l.remove(0)
    print(l)

    # addinng
    l.add_front(6)   #6
    l.add_end(20)    #6 20
    print(l)
    l.insert(1, 10)   #6 10 20
    l.insert(2, 77)   #6 10 77 20
    l.insert(4, 43)   #6 10 77 20 43
    l.insert(0, 2)    #2 6 10 77 20 43
    print(43 in l)
    print(l)
    del l[1]
    print(l)
    print("LENGTH:", len(l))

    print(l[0], l[3], "\n")

    rev = l.reverse()#43 20 77 10 2
    print(rev)
    print("REV LENGTH:", len(rev))
    print(rev[1], rev[2])

    l.clear()
    print("Linked List is empty?", l.is_empty())
    print("Reversed Linked List is empty?", rev.is_empty())
