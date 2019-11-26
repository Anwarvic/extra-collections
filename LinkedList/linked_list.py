

class Node:
    """Basic object for the Node used for linked lists"""
    def __init__(self, item=None):
        self.data = item
        self.next = None


    def __str__(self):
        return str(self.data)

    
    def __repr__(self):
        """Represents Node object as a string"""
        data = self.data
        nxt = self.next.data if self.next else None
        return "Node: (data: {}, next: {})".format(data, nxt)


    def get_data(self):
        return self.data
    

    def get_next(self):
        return self.next
    

    def set_next(self, next_node):
        if not isinstance(next_node, Node) and next_node != None:
            raise TypeError("Linked List elements have to be of type `Node`")
        self.next = next_node




class LinkedList:
    """Basic object for the linked list"""
    def __init__(self, item=None):
        if isinstance(item, Node):
            self.head = item
            self.length = 1 if item.get_data() != None else 0
        else:
            self.head = Node(item)
            self.length = 1 if item != None else 0


    def _print_node(self, node):
        top_border = ['┌']
        middle = ['│']
        lower_border = ['└']
        item = str(node)
        width = len(item)+2 #2: for a space before & after an item
        top_border += (['─']*width) + ['┐ ']
        middle += [f" {item} │⟶"]
        lower_border += (['─']*width) + ['┘ ']
        return top_border, middle, lower_border
    
        
    def _print_linked_list(self, stop_node=None):
        # NOTE: complexity of + operator is O(1) in lists and O(n) in string
        top_border = []
        middle = []
        lower_border = []
        if self.is_empty():
            top_border += ['┌─']
            middle += ['│']
            lower_border += ['└─']
        else:
            curr_node = self.head
            while(curr_node != stop_node):
                top_part, middle_part, lower_part = self._print_node(curr_node)
                top_border += top_part
                middle += middle_part
                lower_border += lower_part
                # update curr_node
                curr_node = curr_node.get_next()
        return top_border, middle, lower_border

    
    def __repr__(self):
        """Represents the linked list as a string like so:
        ┌────┐ ┌────┐ ┌────┐ ┌───┐ ┌───┐ 
        │ 20 │⟶│ 77 │⟶│ 10 │⟶│ 6 │⟶│ 2 │⟶ 
        └────┘ └────┘ └────┘ └───┘ └───┘ 
        """
        top_border, middle, lower_border = self._print_linked_list()
        return "{}\n{}\n{}".format(\
            ''.join(top_border), ''.join(middle), ''.join(lower_border))


    # def __repr__(self): #TODO: comment this operator
    #     output = [str(item) for item in self]
    #     return '[' + ", ".join(output) + ']'


    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return self.length
    

    def __iter__(self):
        curr_node = self.head
        while(curr_node != None):
            yield curr_node
            curr_node = curr_node.get_next()


    def _search(self, value):
        """
        Search the Linked List for a given `value` and returns the first node
        containing that value if found. If not found, it returns the last node
        in the Linked List.
        """
        curr_node = self.head
        # returns `None` if Linked List is empty
        if self.is_empty(): return curr_node
        while(curr_node.get_next() != None):
            if curr_node.get_data() == value:
                return curr_node
            curr_node = curr_node.get_next()
        return curr_node


    def __contains__(self, value):
        found_node = self._search(value)
        if found_node == None or found_node.get_data() != value:
            return False
        return True


    def __getitem__(self, idx):
        """Retrieves the element at the given index. It allows -ve indexing"""
        # sanity check over given index
        if type(idx) != int:
            raise TypeError("Indices must be an integer!")
        elif idx < -self.length or idx >= self.length:
            raise IndexError("Can't find any element at the given index!!")
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


    def is_empty(self):
        """Checks if linked list is empty"""
        return self.length == 0


    def _insert_node(self, prev_node, item):
        # handle different types of `item`
        if isinstance(item, Node):
            assert item.get_data() != None, \
                "Can't insert `None` value as a node!!"
            new_node = item
        else:
            assert item != None, "Can't insert `None` value as a node!!"
            new_node = Node(item)
        
        # start inserting the node
        if self.length == 0:
            self.head = new_node
        elif prev_node == None:
            if not self.is_empty(): new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        self.length += 1
        return new_node


    def add_front(self, item):
        """Adds node at the head of the linked list with complexity of O(1)"""
        self._insert_node(prev_node=None, item=item)


    def add_end(self, item):
        """Adds node at the tail of the linked list with complexity of O(n)"""
        if self.is_empty():
            self.add_front(item)
        else:
            prev_node = None
            curr_node = self.head
            while(curr_node != None):
                prev_node = curr_node
                curr_node = curr_node.get_next()
            self._insert_node(prev_node, item)


    def _validate_index(self, idx):
        if type(idx) != int:
            raise TypeError("Indices must be an integer!")
        elif idx <= -1:
            raise IndexError(\
                "Negative indexing isn't allowed with insertion/removal!!")
        elif idx > self.length:
            raise IndexError("Can't find any element at the given index!!")


    def insert(self, idx, item):
        """Inserts a certain item at a given index into the linked list"""
        self._validate_index(idx)
        counter = 0
        prev_node = None
        curr_node = self.head
        # iterate over the double linked list (forwards)
        while(counter != idx):
            counter += 1
            prev_node = curr_node
            curr_node = curr_node.get_next()
        self._insert_node(prev_node, item)


    def __setitem__(self, idx, item):
        self.insert(idx, item)


    def _remove_node(self, prev_node, node_to_be_removed):
        assert node_to_be_removed != None, "Can't remove `None` node!!"
        # if node to be removed is the first
        if prev_node == None:
            self.head = node_to_be_removed.get_next()
        else:
            prev_node.set_next(node_to_be_removed.get_next())
        self.length -= 1
    

    def remove_front(self):
        """Removes the linked list head with complexity of O(1)"""
        if not self.is_empty():
            self._remove_node(prev_node=None, node_to_be_removed=self.head)


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


    def __delitem__(self, idx):
        """Removes a node at index=idx from the linked list"""
        self._validate_index(idx)
        if idx == self.length:
            raise IndexError("Can't find any element at the given index!!")
        counter = 0
        prev_node = None
        curr_node = self.head
        while(counter != idx):  
            counter += 1
            prev_node = curr_node
            curr_node = curr_node.get_next()
        self._remove_node(prev_node, curr_node)


    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        self.__init__()
    

    def to_list(self):
        return [item.get_data() for item in self]


    def reverse(self):
        """Reverses the whole linked list with complexity of O(n)"""
        rev = LinkedList()
        if not self.is_empty():
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
    l.clear()        #[]

    # test remove() alone
    l.add_end(0)     #0
    l.remove(0)      #[]
    print(l)

    # addinng
    l.add_front(6)   #6
    l.add_end(20)    #6 20
    print(l)
    l.insert(1, 10)   #6 10 20
    l.insert(2, 77)   #6 10 77 20
    l.insert(4, 43)   #6 10 77 20 43
    l.insert(0, 2)    #2 6 10 77 20 43
    print(43 in l)    #true
    print(l)
    del l[len(l)-1]   #2 6 10 77 20
    print(l)
    print("LENGTH:", len(l)) #5
    print(l.to_list())#[2, 6, 10, 77, 20]

    print(l[0], l[3], "\n")

    rev = l.reverse() #20 77 10 6 2
    print(rev)
    print("REV LENGTH:", len(rev))
    print(rev[1], rev[2])

    l.clear()
    print("Linked List is empty?", l.is_empty())
    print("Reversed Linked List is empty?", rev.is_empty())
    print(l)
