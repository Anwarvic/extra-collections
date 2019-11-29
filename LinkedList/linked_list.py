

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
    

    def set_data(self, data):
        self.data = data
    

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


    ############################## PRINT ##############################
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
    
        
    def _print_linked_list(self, start_node, stop_node=None):
        # NOTE: complexity of + operator is O(1) in lists and O(n) in string
        top_border = []
        middle = []
        lower_border = []
        if self.is_empty():
            top_border += ['┌─']
            middle += ['│']
            lower_border += ['└─']
        else:
            curr_node = start_node
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
        top_border, middle, lower_border = self._print_linked_list(self.head)
        return "{}\n{}\n{}".format(\
            ''.join(top_border), ''.join(middle), ''.join(lower_border))


    # def __repr__(self): #TODO: comment this operator
    #     output = [str(item) for item in self]
    #     return '[' + ", ".join(output) + ']'


    ############################## LENGTH ##############################
    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return self.length
    

    def is_empty(self):
        """Checks if linked list is empty"""
        return self.length == 0

    
    ############################# ITERATOR #############################
    def __iter__(self):
        curr_node = self.head
        while(curr_node != None):
            yield curr_node
            curr_node = curr_node.get_next()


    ############################## SEARCH ##############################
    def _search(self, value, start_node, stop_node=None):
        """
        Search the Linked List for a given `value` and returns the first node
        containing that value if found. If not found, it returns the last node
        in the Linked List.
        """
        # returns `None` if Linked List is empty
        if self.is_empty(): return start_node
        curr_node = start_node
        while(curr_node.get_next() != stop_node):
            if curr_node.get_data() == value:
                return curr_node
            curr_node = curr_node.get_next()
        return curr_node


    def __contains__(self, value):
        found_node = self._search(value, self.head)
        if found_node == None or found_node.get_data() != value:
            return False
        return True


    def _get_node(self, idx):
        # iterate over the linked list
        counter = 0
        prev_node = None
        curr_node = self.head
        while(counter != idx):  
            counter += 1
            prev_node = curr_node
            curr_node = curr_node.get_next()
        return prev_node, curr_node


    def _validate_index(self, idx, accept_negative=False):
        if type(idx) != int:
            raise TypeError("Indices must be an integer!")
        elif idx <= -1 and accept_negative==False:
            raise IndexError(\
                "Negative indexing isn't supported with this functinoality!!")
        elif idx < -self.length or idx > self.length:
            raise IndexError("Can't find any element at the given index!!")


    def __getitem__(self, idx):
        """Retrieves the element at the given index. It allows -ve indexing"""
        # sanity check over given index
        self._validate_index(idx, accept_negative=True)
        if idx == self.length:
            raise IndexError("Can't find any element at the given index!!")
        # convert idx to positive if -ve
        if idx <= -1: idx += self.length
        # get the item
        _, node = self._get_node(idx)
        return node


    ############################## INSERT ##############################
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
            new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        self.length += 1


    def _insert(self, idx, item):
        counter = 0
        prev_node = None
        curr_node = self.head
        # iterate over the double linked list (forwards)
        while(counter != idx):
            counter += 1
            prev_node = curr_node
            curr_node = curr_node.get_next()
        self._insert_node(prev_node, item)


    def add_front(self, item):
        """Adds node at the head of the linked list with complexity of O(1)"""
        self._insert(0, item)


    def add_end(self, item):
        """Adds node at the tail of the linked list with complexity of O(n)"""
        self._insert(len(self), item)
    
    
    def insert(self, idx, item):
        """Inserts a certain item at a given index into the linked list"""
        self._validate_index(idx)
        self._insert(idx, item)


    ############################### SET ################################
    def __setitem__(self, idx, item):
        assert isinstance(item, Node), \
            f"Can't set an {type(item)}, it needs to be a `Node` object!"
        _, node = self._get_node(idx)
        node.set_data(item.get_data())


    ############################## REMOVE ##############################
    def _remove_node(self, prev_node, node_to_be_removed):
        assert node_to_be_removed != None, "Can't remove `None` node!!"
        # if node to be removed is the first
        if prev_node == None:
            if self.length == 1:
                self.head.set_data(None)
            else:
                self.head = node_to_be_removed.get_next()
        else:
            prev_node.set_next(node_to_be_removed.get_next())
        self.length -= 1


    def _remove_idx(self, idx):
        prev_node, node = self._get_node(idx)
        self._remove_node(prev_node, node)


    def __delitem__(self, idx):
        """Removes a node at index=idx from the linked list"""
        self._validate_index(idx)
        if idx == self.length:
            raise IndexError("Can't find any element at the given index!!")
        self._remove_idx(idx)
    

    def remove_front(self):
        """Removes the linked list head with complexity of O(1)"""
        #NOTE: I check the length 'cause I don't wanna throw an IndexError
        if not self.is_empty():
            self.__delitem__(0)


    def remove_end(self):
        """Removes the linked list tail with complexity of O(n)"""
        #NOTE: I check the length 'cause I don't wanna throw an IndexError
        if not self.is_empty():
            self.__delitem__( self.length-1 )


    def _remove_value(self, value, stop_node, all):
        # removes all occurrences (when all==True) of `value` if found.
        prev = None
        curr_node = self.head
        FOUND_FIRST = False #True when the first occurrence is found
        while(curr_node != stop_node):
            if all==False and FOUND_FIRST:
                return
            if curr_node.get_data() == value:
                FOUND_FIRST = True
                self._remove_node(prev, curr_node)
                curr_node = prev.get_next() if prev != None else self.head
            else:
                prev = curr_node
                curr_node = curr_node.get_next()

    
    def remove(self, value, all=True):
        self._remove_value(value, stop_node=None, all=all)


    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        self.__init__()
    
    
    ############################## MISC ##############################
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
