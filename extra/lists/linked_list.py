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


    @staticmethod
    def from_iterable(iterable):
        if not hasattr(iterable, "__iter__"):
            raise TypeError("Given object has no `iter` attribute")
        l = LinkedList()
        curr_node = l.head
        for item in iterable:
            if l.is_empty():
                l.head.set_data(item)
            else:
                curr_node.set_next(Node(item))
                curr_node = curr_node.get_next()
            l.length += 1
        return l


    ############################## PRINT ##############################
    def _print_node(self, node):
        assert isinstance(node, Node)
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
        assert isinstance(start_node, Node)
        assert stop_node == None or isinstance(stop_node, Node)
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


    ############################## LENGTH ##############################
    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return self.length
    

    def is_empty(self):
        """Checks if linked list is empty"""
        return self.length == 0

    
    ############################# ITERATOR #############################
    def __iter__(self):
        counter = 0
        curr_node = self.head
        while(counter < self.length):
            yield curr_node
            counter += 1
            curr_node = curr_node.get_next()


    ############################## SEARCH ##############################
    def _search(self, value, start_node, stop_node=None):
        """
        Search the Linked List for a given `value` and returns the first node
        containing that value if found. If not found, it returns the last node
        in the Linked List.
        """
        assert not isinstance(value, Node)
        assert isinstance(start_node, Node)
        assert stop_node == None or isinstance(stop_node, None)
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
        assert 0 <= idx < self.length
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
        if isinstance(idx, slice):
            indices = range(*idx.indices(self.length))
            max_idx = indices[-1]
            indices = set(indices)
            # start getting wanted nodes
            counter = 0
            prev_node = None
            curr_node = self.head
            out_llist = LinkedList()
            while(counter <= max_idx):
                if counter in indices:
                    prev_node = out_llist._insert_value(prev_node,
                                                        curr_node.get_data())
                curr_node = curr_node.get_next()
                counter += 1
            return out_llist
        else:
            self._validate_index(idx, accept_negative=True)
            # sanity check over given index
            if idx == self.length:
                raise IndexError("Can't find any element at the given index!!")
            # convert idx to positive if -ve
            if idx <= -1: idx += self.length
            # get the item
            _, node = self._get_node(idx)
            return node


    ############################## INSERT ##############################
    def _validate_inserted_item(self, item):
        if not isinstance(item, Node):
            if item == None:
                raise TypeError("Can't set a `None` into Linked List!")
            item = Node(item)
        else:
            if item.get_data() == None:
                raise TypeError(\
                    "Can't set a Node whose value is `None` into Linked List!")
        

    def _insert_node(self, prev_node, new_node):
        assert isinstance(new_node, Node)
        assert new_node.get_data() != None
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
        return new_node


    def _insert_value(self, prev_node, value):
        assert value != None
        assert not isinstance(value, Node)
        new_node = Node(value)
        return self._insert_node(prev_node, new_node)
    

    def _insert(self, idx, item):
        assert 0 <= idx <= self.length
        prev_node, _ = self._get_node(idx)
        if isinstance(item, Node):
            assert item.get_data() != None
            return self._insert_node(prev_node, item)
        else:
            assert item != None
            return self._insert_value(prev_node, item)


    def add_front(self, item):
        """Adds node at the head of the linked list with complexity of O(1)"""
        self._validate_inserted_item(item)
        return self._insert(0, item)


    def add_end(self, item):
        """Adds node at the tail of the linked list with complexity of O(n)"""
        self._validate_inserted_item(item)
        return self._insert(len(self), item)
    
    
    def insert(self, idx, item):
        """Inserts a certain item at a given index into the linked list"""
        self._validate_index(idx)
        self._validate_inserted_item(item)
        return self._insert(idx, item)


    ############################### SET ################################
    def _replace_node(self, idx, new_node):
        assert 0 <= idx <= self.length
        assert isinstance(new_node, Node)
        _, old_node = self._get_node(idx)
        old_node.set_data(new_node.get_data())
    

    def __setitem__(self, idx, item):
        self._validate_index(idx)
        if idx == self.length:
            raise IndexError("Can't find any element at the given index!!")
        self._validate_inserted_item(item)
        self._replace_node(idx, item)
        

    ############################## REMOVE ##############################
    def _remove_node(self, prev_node, node_to_be_removed):
        assert prev_node == None or isinstance(prev_node, Node)
        assert isinstance(node_to_be_removed, Node)
        next_node = node_to_be_removed.get_next()
        # if node to be removed is the first
        if prev_node == None:
            if self.length == 1:
                self.head.set_data(None)
            else:
                self.head = next_node
        else:
            prev_node.set_next(next_node)
        self.length -= 1


    def _remove_idx(self, idx):
        assert 0 <= idx < self.length
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
        if not self.is_empty():
            self.__delitem__(0)


    def remove_end(self):
        """Removes the linked list tail with complexity of O(n)"""
        if not self.is_empty():
            self.__delitem__( self.length-1 )


    def _remove_value(self, value, stop_node, all):
        # removes all occurrences (when all==True) of `value` if found.
        assert not isinstance(value, Node)
        assert stop_node == None or isinstance(stop_node, Node)
        assert type(all) == bool
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


    def count(self, value):
        total_count = 0
        for node in self:
            if node.get_data() == value:
                total_count += 1
        return total_count


    def copy(self):
        copied_list = LinkedList()
        copied_node = None
        curr_node = self.head
        while(curr_node != None):
            copied_node = copied_list._insert_value(copied_node,
                                                    curr_node.get_data())
            curr_node = curr_node.get_next()
        return copied_list


    def split(self, idx):
        """
        idx is the start index of the second list after splitting.
        So, idx=0, then the left_list will be empty while the right_list will be
        the rest. And the opposite when idx=self.length
        """
        self._validate_index(idx)
        left_list, right_list = LinkedList(), LinkedList()
        if not self.is_empty():
            counter = 0
            prev_node = None
            curr_node = self.head
            # left list
            while(counter < idx):
                prev_node = left_list._insert_value(prev_node,
                                                    curr_node.get_data())
                curr_node = curr_node.get_next()
                counter += 1
            # right list
            while(curr_node != None):
                prev_node = right_list._insert_value(prev_node,
                                                    curr_node.get_data())
                curr_node = curr_node.get_next()
        return left_list, right_list
        

    def _rotate(self, distance, direction):
        if type(distance) != int or distance < 0:
            raise ValueError("Rotation distance has to be an `int` >= zero!!")
        distance = distance % self.length if self.length > 0 else 0
        if direction == "RIGHT": distance = self.length - distance
        left_list, right_list = self.split(distance)
        last_right_node, _ = right_list._get_node(len(right_list))
        if len(left_list) > 0:
            last_right_node.set_next(left_list.head)
        return right_list


    def rotate_left(self, distance):
        return self._rotate(distance, "LEFT")
    

    def rotate_right(self, distance):
        return self._rotate(distance, "RIGHT")




if __name__ == "__main__":
    ll = LinkedList()
    left_list, right_list = ll.split(0)
    print(left_list)
    print(right_list)
    # l = LinkedList()
    # # test removing from empty list:
    # l.remove_front() #Nothing
    # l.remove_end()   #Nothing
    # l.remove(10)     #Nothing
    # # del l[0]       #throughs IndexError

    # l.add_front(10)  #10 
    # l.add_front(5)   #5 10
    # print(l)
    # l.remove(20)     #nothing
    # l.remove_front() #10
    # print(l)
    # l.remove_end()   #[]
    # print(l)
    # l.insert(0, 100) #100
    # l.insert(1, 200) #100 200
    # l.insert(1, 100) #100 100 200
    # print(l)
    # l.remove(100)    #200
    # print(l)
    # l.clear()        #[]

    # # test remove() alone
    # l.add_end(0)     #0
    # l.remove(0)      #[]
    # print(l)

    # # addinng
    # l.add_front(6)   #6
    # l.add_end(20)    #6 20
    # print(l)
    # l.insert(1, 10)   #6 10 20
    # l.insert(2, 77)   #6 10 77 20
    # l.insert(4, 43)   #6 10 77 20 43
    # l.insert(0, 2)    #2 6 10 77 20 43
    # print(43 in l)    #true
    # print(l)
    # del l[len(l)-1]   #2 6 10 77 20
    # print(l)
    # print("LENGTH:", len(l)) #5
    # print(l.to_list())#[2, 6, 10, 77, 20]

    # print(l[0], l[3], "\n") #2 77

    # rev = l.reverse() #20 77 10 6 2
    # print(rev)
    # print("REV LENGTH:", len(rev))
    # print(rev[1], rev[2]) #77 10

    # l.clear()
    # print("Linked List is empty?", l.is_empty())
    # print("Reversed Linked List is empty?", rev.is_empty())
    # print(l)

    # print('='*50)
    # l = LinkedList.from_iterable([1, 2, 3, 4, 5, 6])
    # clone = l.copy()
    # clone.add_front(0)
    # print(clone)
    # print(l)

    # print('='*50)
    # l = LinkedList.from_iterable([1, 2, 3, 4, 5, 6])
    # left_list, right_list = l.split(5)
    # print("Left list:")
    # print(left_list)
    # print("Right list:")
    # print(right_list)
    # print("Original List:")
    # l.add_end("200")
    # print(l)

    # print('='*50)
    # l = LinkedList.from_iterable([1, 2, 3, 4, 5, 6])
    # print(l.right_rotate(1))

    # print('='*50)
    # l = LinkedList.from_iterable([1, 2, 3, 4, 5, 6])
    # print(l[1:4])