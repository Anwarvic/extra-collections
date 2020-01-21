import operator



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
        assert data != None
        self.data = data
    

    def get_next(self):
        return self.next
    

    def set_next(self, next_node):
        assert (isinstance(next_node, Node) and next_node.get_data() != None)\
            or next_node == None
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
            raise TypeError("Given object has no `iter` attribute!!")
        ll = LinkedList()
        prev_node = None
        for item in iterable:
            ll._validate_inserted_item(item)
            if isinstance(item, Node):
                prev_node = ll._insert_node(prev_node, item)
            else:
                prev_node = ll._insert_value(prev_node, item)
        return ll


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

    
    ############################# OPERATOR #############################
    def __iter__(self):
        counter = 0
        curr_node = self.head
        while(counter < self.length):
            yield curr_node
            counter += 1
            curr_node = curr_node.get_next()


    def _compare(self, other, op):
        """
        Returns the last two nodes that don't match the given operator. They
        could be the end of both LinkedList or just some random nodes in the
        middle.
        """
        assert type(self) == type(other)
        assert op.__name__ in dir(operator)
        # start_comparing
        pointer1 = self.head if not self.is_empty() else None
        pointer2 = other.head if not other.is_empty() else None
        while(pointer1 != None and pointer2 != None):
            try:
                if pointer1.get_data() == pointer2.get_data():
                    pass
                elif not op(pointer1.get_data(), pointer2.get_data()):
                    return pointer1, pointer2
            except TypeError:
                raise TypeError(
                    "Inconsists data-types within the two LinkedLists!!")
            pointer1 = pointer1.get_next()
            pointer2 = pointer2.get_next()
        return pointer1, pointer2


    def __eq__(self, other):
        if type(self) != type(other):
            raise TypeError(f"Can't compare a Linked List to {type(other)}")
        # check length
        if self.length != other.length:
            return False
        pointer1, pointer2 = self._compare(other, operator.eq)
        return True if pointer1 == pointer2 == None else False
    

    def __ne__(self, other):
        if type(self) != type(other):
            raise TypeError(f"Can't compare a Linked List to {type(other)}")
        if self.length != other.length:
            return True
        pointer1, pointer2 = self._compare(other, operator.ne)
        return False if pointer1 == pointer2 == None else True
    

    def __lt__(self, other):
        if type(self) != type(other):
            raise TypeError(f"Can't compare a Linked List to {type(other)}")
        pointer1, _ = self._compare(other, operator.lt)
        return True if pointer1 == None else False
    

    def __lte__(self, other):
        if type(self) != type(other):
            raise TypeError(f"Can't compare a Linked List to {type(other)}")
        pointer1, _ = self._compare(other, operator.le)
        return True if pointer1 == None else False
    

    def __gt__(self, other):
        if type(self) != type(other):
            raise TypeError(f"Can't compare a Linked List to {type(other)}")
        _, pointer2 = self._compare(other, operator.le)
        return True if pointer2 == None else False
    

    def __ge__(self, other):
        if type(self) != type(other):
            raise TypeError(f"Can't compare a Linked List to {type(other)}")
        _, pointer2 = self._compare(other, operator.le)
        return True if pointer2 == None else False


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
        if isinstance(value, Node):
            value = value.get_data()
        found_node = self._search(value, self.head)
        if found_node == None or found_node.get_data() != value:
            return False
        return True


    def _get_node(self, idx):
        assert 0 <= idx or idx < self.length
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
        if item == None:
            raise TypeError("Can't set a `None` into Linked List!")
        elif isinstance(item, Node) and item.get_data() == None:
            raise TypeError("Can't set a Node with `None` into Linked List!")
        

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
        assert prev_node == None or isinstance(prev_node, Node)
        assert value != None and not isinstance(value, Node)
        new_node = Node(value)
        return self._insert_node(prev_node, new_node)
    

    def _insert(self, idx, item):
        assert 0 <= idx or idx <= self.length
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
        assert 0 <= idx or idx <= self.length
        assert isinstance(new_node, Node)
        _, old_node = self._get_node(idx)
        old_node.set_data(new_node.get_data())
    

    def __setitem__(self, idx, item):
        #TODO: handle -ve indexing
        #TODO: handle slice objects
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
                self.head.data = None #NOTE: don't use set_data() here
            else:
                self.head = next_node
        else:
            prev_node.set_next(next_node)
        self.length -= 1


    def _remove_idx(self, idx):
        assert 0 <= idx or idx < self.length
        prev_node, node = self._get_node(idx)
        self._remove_node(prev_node, node)


    def __delitem__(self, idx):
        """Removes a node at index=idx from the linked list"""
        #TODO: handle -ve indexing
        #TODO: handle slice objects
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
        assert not isinstance(value, Node) and value != None
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
        if type(all) != bool:
            raise TypeError("`all` is a boolean flag (True by default)!")
        self._validate_inserted_item(value)
        self._remove_value(value, stop_node=None, all=all)


    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        self.__init__()
    

    ############################## ROTATION #############################
    def _rotate(self, distance, direction):
        if type(distance) != int:
            raise TypeError("Rotation distance has to be an `int`!!")
        if distance < 0:
            raise ValueError("Rotation distance has to be >= zero!!")
        distance = distance % self.length if self.length > 0 else 0
        if direction == "RIGHT": distance = self.length - distance
        left_list, right_list = self.split(distance)
        # perform rotation
        if len(right_list) == 0:
            return left_list
        elif len(left_list) == 0:
            return right_list
        else:
            # get last_right_node
            last_right_node, _ = right_list._get_node(len(right_list))
            last_right_node.set_next(left_list.head)
            return right_list


    def rotate_left(self, distance):
        return self._rotate(distance, "LEFT")
    

    def rotate_right(self, distance):
        return self._rotate(distance, "RIGHT")

    
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
        if isinstance(value, Node):
            value = value.get_data()
        for node in self:
            if node.get_data() == value:
                total_count += 1
        return total_count


    def copy(self):
        copied_list = LinkedList()
        if not self.is_empty():
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
        

    def sort(self):
        #TODO: use comparators with sorted()
        #Raises: TypeError if LinkedList has more than one type
        pass


if __name__ == "__main__":
    llist1 = LinkedList.from_iterable([1, '2', 3.14])
    llist2 = LinkedList.from_iterable([1, '2', 5.14])
    assert llist1 == llist1
    assert llist2 == llist2
    assert llist1 != llist2
    assert llist1 < llist2
    assert llist1 <= llist2
    assert llist2 > llist2
    assert llist2 >= llist2