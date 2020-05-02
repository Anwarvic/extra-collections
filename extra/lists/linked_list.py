import warnings, operator
from extra.interface import Extra




class Node(Extra):
    """Basic object for the Node used for linked lists"""
    def __name__(self):
        return "extra.Node()"
    

    def __init__(self, item):
        super()._validate_item(item)
        if type(item) == str:
            item = item.replace('\n', '\\n')
        self._data = item
        self._next = None


    def __repr__(self):
        """Represents Node object as a string"""
        nxt = self._next.get_data() if self._next is not None else None
        return f"Node(data: {self._data}, next: {nxt})"


    def get_data(self):
        return self._data
    

    def set_data(self, data):
        super()._validate_item(data)
        if type(data) == str:
            data = data.replace('\n', '\\n')
        self._data = data
    

    def get_next(self):
        return self._next
    

    def set_next(self, next_node):
        if next_node is None:
            self._next = None
        elif not isinstance(next_node, Node):
            raise TypeError(
                f"Can't set {type(next_node)} as a {self.__name__()}!!")
        elif next_node.get_data() is None:
            raise ValueError(f"{self.__name__()} data can't be `None`!!")
        else:
            self._next = next_node


    def _represent(self):
        return str(self._data)




class LinkedList(Extra):
    """Basic object for the linked list"""
    _basic_node = Node
    
    def __init__(self):
        self._head = None
        self._length = 0


    def __name__(self):
        return "extra.LinkedList()"


    def _create_instance(self):
        return LinkedList()


    @classmethod
    def from_iterable(cls, iterable):
        if not hasattr(iterable, "__iter__"):
            raise TypeError("The given object isn't iterable!!")
        elif isinstance(iterable, cls):
            return iterable
        else:
            ll = cls()  #cls._create_instance(cls)
            prev_node = None
            for item in iterable:
                ll._validate_item(item)
                if isinstance(item, Node): #Node here is generic
                    item = item.get_data()
                prev_node = ll._insert_value(prev_node, item)
            return ll


    ##############################     PRINT      ##############################
    def _print_node(self, node):
        assert isinstance(node, self._basic_node)

        top_border = ['┌']
        middle = ['│']
        lower_border = ['└']
        item = node._represent()
        width = len(item)+2 #2: for a space before & after an item
        top_border += (['─']*width) + ['┐ ']
        middle += [f" {item} │⟶"]
        lower_border += (['─']*width) + ['┘ ']
        return top_border, middle, lower_border
    

    def _print_empty_linked_list(self):
        assert self._length == 0

        top_border    = ['┌─']
        middle_border = ['│']
        lower_border  = ['└─']
        return "{}\n{}\n{}".format(\
            ''.join(top_border), ''.join(middle_border), ''.join(lower_border))

        
    def _print_linked_list(self, start_node):
        assert isinstance(start_node, self._basic_node)

        # NOTE: complexity of + operator is O(1) in lists and O(n) in string
        top_border = []
        middle_border = []
        lower_border = []
        counter = 0
        curr_node = start_node
        while(counter < self._length):
            top_part, middle_part, lower_part = self._print_node(curr_node)
            top_border += top_part
            middle_border += middle_part
            lower_border += lower_part
            # update curr_node
            curr_node = curr_node.get_next()
            counter += 1
        return top_border, middle_border, lower_border

    
    def __repr__(self):
        """Represents the linked list as a string like so:
        ┌────┐ ┌────┐ ┌────┐ ┌───┐ ┌───┐ 
        │ 20 │⟶│ 77 │⟶│ 10 │⟶│ 6 │⟶│ 2 │⟶
        └────┘ └────┘ └────┘ └───┘ └───┘ 
        """
        if self.is_empty():
            return self._print_empty_linked_list()
        top_border, middle, lower_border = self._print_linked_list(self._head)
        return "{}\n{}\n{}".format(\
            ''.join(top_border), ''.join(middle), ''.join(lower_border))


    ##############################     LENGTH     ##############################
    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return self._length
    

    def is_empty(self):
        """Checks if linked list is empty"""
        return self._length == 0

    
    ##############################    OPERATOR    ##############################
    def __iter__(self):
        counter = 0
        curr_node = self._head
        while(counter < self._length):
            yield curr_node.get_data()
            counter += 1
            curr_node = curr_node.get_next()


    def _compare(self, other, op):
        """
        Returns the last two nodes that don't match the given operator. They
        could be the end of both LinkedList or just some random nodes in the
        middle.
        """
        assert isinstance(other, self.__class__)
        assert op.__name__ in dir(operator)

        # start_comparing
        counter = 0
        pointer1 = self._head
        pointer2 = other._head
        while(counter < min(self._length, other._length)):
            try:
                #NOTE: Don't remove the following if-condition
                if pointer1.get_data() == pointer2.get_data():
                    pass 
                elif not op(pointer1.get_data(), pointer2.get_data()):
                    return counter
            except TypeError:
                raise TypeError(
                    "Inconsists data-types within the two LinkedLists!!")
            pointer1 = pointer1.get_next()
            pointer2 = pointer2.get_next()
            counter += 1
        return counter


    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can't compare {self.__name__()} to {type(other)}")
        # check length
        if self._length != other._length:
            return False
        idx = self._compare(other, operator.eq)
        return True if idx == self._length == other._length else False
    

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can't compare {self.__name__()} to {type(other)}")
        if self._length != other._length:
            return True
        idx = self._compare(other, operator.eq)
        return False if idx == self._length == other._length else True
    

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can't compare {self.__name__()} to {type(other)}")
        idx = self._compare(other, operator.lt)
        return True if idx == self._length else False
    

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can't compare {self.__name__()} to {type(other)}")
        idx = self._compare(other, operator.le)
        return True if idx == self._length else False
    

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can't compare {self.__name__()} to {type(other)}")
        idx = self._compare(other, operator.le)
        return True if idx is other._length else False
    

    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can't compare {self.__name__()} to {type(other)}")
        idx = self._compare(other, operator.le)
        return True if idx == other._length else False


    ##############################     SEARCH     ##############################
    def _search(self, value, start_node):
        """
        Search the Linked List for a given `value` and returns the first node
        containing that value if found. If not found, it returns the last node
        in the Linked List.
        """
        assert not isinstance(value, Node) #Node here is generic
        assert isinstance(start_node, self._basic_node)

        counter = 0
        curr_node = start_node
        while(counter < self._length):
            if curr_node.get_data() == value:
                return curr_node
            curr_node = curr_node.get_next()
            counter += 1
        return curr_node


    def __contains__(self, value):
        #NOTE: DON'T validate the given value
        if value is None or self.is_empty():
            return False
        found_node = self._search(value, self._head)
        if found_node.get_data() != value:
            return False
        return True


    def _get_node(self, idx):
        assert 0 <= idx or idx < self._length
        # iterate over the linked list
        counter = 0
        prev_node = None
        curr_node = self._head
        while(counter != idx):  
            counter += 1
            prev_node = curr_node
            curr_node = curr_node.get_next()
        return prev_node, curr_node


    def _validate_index(self, idx, accept_negative=False, accept_slice=False):
        if isinstance(idx, slice):
            if not accept_slice:
                raise IndexError(\
                    "Slice indexing isn't supported with this functinoality!!")
        elif type(idx) != int:
            raise TypeError("Given index must be an integer!!")
        elif idx <= -1 and not accept_negative:
            raise IndexError(\
                "Negative indexing isn't supported with this functinoality!!")
        elif idx < -self._length or idx > self._length:
            raise IndexError("Can't find any element at the given index!!")


    def __getitem__(self, idx):
        """Retrieves the element at the given index. It allows -ve indexing"""
        # sanity check over given index
        self._validate_index(idx, accept_negative=True, accept_slice=True)
        if isinstance(idx, slice):
            indices = range(*idx.indices(self._length))
            max_idx = indices[-1] if indices else -1
            indices = set(indices)
            # start getting wanted nodes
            counter = 0
            prev_node = None
            curr_node = self._head
            out_llist = self._create_instance()
            while(counter <= max_idx):
                if counter in indices:
                    prev_node = out_llist._insert_value(prev_node,
                                                        curr_node.get_data())
                curr_node = curr_node.get_next()
                counter += 1
            return out_llist
        else:
            if idx == self._length:
                raise IndexError("Can't find any element at the given index!!")
            # convert idx to positive if -ve
            if idx <= -1: idx += self._length
            # get the item
            _, node = self._get_node(idx)
            return node


    ##############################     INSERT     ##############################
    def _insert_node(self, prev_node, new_node):
        assert prev_node is None or isinstance(prev_node, self._basic_node)
        assert isinstance(new_node, self._basic_node)
        assert new_node.get_data() is not None

        # start inserting the node
        if self._length == 0:
            new_node.set_next(None)
            self._head = new_node
        elif prev_node is None:
            new_node.set_next(self._head)
            self._head = new_node
        else:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        self._length += 1
        return new_node


    def _insert_value(self, prev_node, value):
        assert prev_node is None or isinstance(prev_node, self._basic_node)
        assert value is not None and not isinstance(value, self._basic_node)
        
        new_node = self._basic_node(value)
        return self._insert_node(prev_node, new_node)
    

    def _insert(self, idx, item):
        assert 0 <= idx or idx <= self._length
        prev_node, _ = self._get_node(idx)
        if isinstance(item, Node):  #Keep it generic
            assert item.get_data() is not None
            return self._insert_node(prev_node, item)
        else:
            assert item is not None
            return self._insert_value(prev_node, item)


    def add_front(self, item):
        """Adds node at the head of the linked list with complexity of O(1)"""
        super()._validate_item(item)
        self._insert(0, item)


    def add_end(self, item):
        """Adds node at the tail of the linked list with complexity of O(n)"""
        super()._validate_item(item)
        self._insert(len(self), item)
    
    
    def insert(self, idx, item):
        """Inserts a certain item at a given index into the linked list"""
        self._validate_index(idx)
        super()._validate_item(item)
        self._insert(idx, item)


    ##############################       SET      ##############################
    def _replace_node(self, idx, new_node):
        assert 0 <= idx or idx <= self._length
        assert new_node is not None

        _, old_node = self._get_node(idx)
        if isinstance(new_node, self._basic_node):
            old_node.set_data(new_node.get_data())
        else:
            old_node.set_data(new_node)
    

    def __setitem__(self, idx, item):
        #TODO: handle -ve indexing
        #TODO: handle slice objects
        self._validate_index(idx)
        if idx == self._length:
            raise IndexError("Can't find any element at the given index!!")
        super()._validate_item(item)
        self._replace_node(idx, item)
        

    ##############################     REMOVE     ##############################
    def _remove_node(self, prev_node, node_to_be_removed):
        assert prev_node is None or isinstance(prev_node, self._basic_node)
        assert isinstance(node_to_be_removed, self._basic_node)

        next_node = node_to_be_removed.get_next()
        # if node to be removed is the first
        if prev_node is None:
            if self._length == 1:
                #NOTE: don't use set_data() here
                self._head.data = None
            else:
                self._head.set_next(next_node.get_next())
                self._head.set_data(next_node.get_data())
        else:
            prev_node.set_next(next_node)
        self._length -= 1


    def _remove_idx(self, idx):
        assert 0 <= idx or idx < self._length

        prev_node, node = self._get_node(idx)
        node_data = node.get_data()
        self._remove_node(prev_node, node)
        return self._basic_node(node_data)


    def __delitem__(self, idx):
        """Removes a node at index=idx from the linked list"""
        #TODO: handle -ve indexing
        #TODO: handle slice objects
        self._validate_index(idx)
        if idx == self._length:
            raise IndexError("Can't find any element at the given index!!")
        return self._remove_idx(idx)
    

    def remove_front(self):
        """Removes the linked list head with complexity of O(1)"""
        if not self.is_empty():
            return self.__delitem__(0)


    def remove_end(self):
        """Removes the linked list tail with complexity of O(n)"""
        if not self.is_empty():
            return self.__delitem__( self._length-1 )


    def _remove_value(self, value, all):
        # removes all occurrences (when all==True) of `value` if found.
        assert not isinstance(value, self._basic_node) and value is not None
        assert type(all) == bool

        counter = 0
        prev = None
        curr_node = self._head
        FOUND_FIRST = False #True when the first occurrence is found
        total_length = self._length
        while(counter < total_length):
            if all==False and FOUND_FIRST:
                return
            if curr_node.get_data() == value:
                FOUND_FIRST = True
                self._remove_node(prev, curr_node)
                curr_node = prev.get_next() if prev is not None else self._head
            else:
                prev = curr_node
                curr_node = curr_node.get_next()
            counter += 1

    
    def remove(self, value, all=True):
        if type(all) != bool:
            raise TypeError("`all` is a boolean flag (True by default)!!")
        super()._validate_item(value)
        self._remove_value(value, all=all)


    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        self.__init__()
    

    ##############################   SPLIT/JOIN   ##############################
    def _split(self, idx):
        assert type(idx) == int

        left_list = self._create_instance()
        right_list = self._create_instance()
        if not self.is_empty():
            counter = 0
            prev_node = None
            curr_node = self._head
            # left list
            while(counter < idx):
                prev_node = left_list._insert_value(prev_node,
                                                    curr_node.get_data())
                curr_node = curr_node.get_next()
                counter += 1
            # right list
            while(counter < self._length):
                prev_node = right_list._insert_value(prev_node,
                                                    curr_node.get_data())
                curr_node = curr_node.get_next()
                counter += 1
        return left_list, right_list
    

    def split(self, idx):
        """
        idx is the start index of the second list after splitting.
        So, idx=0, then the left_list will be empty while the right_list will be
        the rest. And the opposite when idx=self._length
        """
        self._validate_index(idx)
        return self._split(idx)
        

    def join(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(\
            f"Type Mismatch! Can't join {self.__name__()} with f{type(other)}.")
        if other.is_empty():
            pass # do nothing
        elif self.is_empty():
            self._head = other._head
            self._length = other._length
        else:
            last_node, _ = self._get_node(self._length)
            last_node.set_next(other._head)
            self._length += other._length


    ##############################    ROTATION    ##############################
    def _validate_distance(self, distance):
        # It doesn't happen inplace
        if type(distance) != int:
            raise TypeError("Rotation distance has to be an `int`!!")
        if distance < 0:
            raise ValueError("Rotation distance has to be >= zero!!")
    
    
    def __calibrate_distance(self, distance, direction):
        assert type(distance) == int
        assert direction in {"RIGHT", "LEFT"}

        distance = distance % self._length if self._length > 0 else 0
        if direction == "RIGHT":
            distance = self._length - distance
        return distance


    def _rotate(self, distance, direction):
        #TODO: when distance is -ve, rotate right
        distance = self.__calibrate_distance(distance, direction)
        # split based on distance
        left_list, right_list = self.split(distance)
        # join them to mimic rotation effect
        right_list.join(left_list)
        # return rotated
        return right_list


    def rotate_left(self, distance, inplace=True):
        if type(inplace) != bool:
            raise TypeError("`inplace` is a boolean flag (True by default)!!")
        self._validate_distance(distance)
        rotated = self._rotate(distance, "LEFT")
        if not inplace: return rotated
        self._head = rotated._head
        
    
    def rotate_right(self, distance, inplace=True):
        self._validate_distance(distance)
        rotated = self._rotate(distance, "RIGHT")
        if not inplace: return rotated
        self._head = rotated._head

    
    ##############################      MISC      ##############################
    def reverse(self):
        """Reverses the whole linked list with complexity of O(n)"""
        rev = self._create_instance()
        counter = 0
        curr_node = self._head
        while(counter < self._length):
            rev.add_front(curr_node.get_data())
            curr_node = curr_node.get_next()
            counter += 1
        return rev


    def to_list(self):
        return [item for item in self]


    def count(self, value):
        total_count = 0
        if isinstance(value, self._basic_node):
            value = value.get_data()
        for curr_val in self:
            if curr_val == value:
                total_count += 1
        return total_count


    def copy(self):
        copied_list = self._create_instance()
        if not self.is_empty():
            copied_node = None
            for val in self:
                copied_node = copied_list._insert_value(copied_node, val)
        return copied_list


