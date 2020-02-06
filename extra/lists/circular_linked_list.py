# from linked_list import Node, LinkedList
from extra.lists.linked_list import Node, LinkedList




class CircularLinkedList(LinkedList):
    """Basic object for the Circular Linked List"""
    def __name__(self):
        return "CircularLinkedList()"
    

    def __init__(self, item=None):
        super().__init__(item)
        self.head.next = self.head

    
    def _create_instance(self):
        return CircularLinkedList()
    

    ############################## PRINT ##############################
    def __repr__(self):
        """Represents the Circular linked list as a string
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 2 │⟶│ 3 │⟶│ 4 │⟶│ 5 │⟶│ 6 │⟶│ 7 │⟶ ┐
        └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘  │
           ↑                                       │
           └───────────────────────────────────────┘
        """
        if self.is_empty():
            return super()._print_empty_linked_list()
        # start with just the head
        first_line, second_line, third_line = self._print_node(self.head)
        # print the remaining nodes if found
        top_part, middle_part, lower_part = \
            self._print_linked_list(self.head.get_next(), self.head)
        first_line  += top_part
        second_line += middle_part
        third_line  += lower_part
        # backtrace representation
        second_line += [' ┐']
        third_line  += [' │']

        first_line  = "".join(first_line)
        second_line = "".join(second_line)
        third_line  = "".join(third_line)

        head_data = str(self.head.get_data())
        left_offset = (len(head_data)+4)//2
        remaining = (len(second_line) - 2) - left_offset
        
        fourth_line = (' '*left_offset) + '↑' + (' '*(remaining)) + '│'
        fifth_line  = (' '*left_offset) + '└' + ('─'*(remaining)) + '┘'
        return "{}\n{}\n{}\n{}\n{}".format(\
            first_line, second_line, third_line, fourth_line, fifth_line)


    ############################## SEARCH ##############################
    def __contains__(self, value):
        #NOTE: DON'T validate the given value
        # check if value is a Node() object
        if isinstance(value, Node):
            # if value is the same object as self._basic_node
            if isinstance(value, self._basic_node):
                value = value.get_data()
            # if value is a generic Node object
            else:
                return False
        # check the head
        if self.head.get_data() == value:
            return True
        # search the rest of the CircularLinkedList()
        found_node = self._search( value,
                                start_node = self.head.get_next(),
                                stop_node = self.head)
        if found_node == None or found_node.get_data() != value:
            return False
        return True


    def _validate_index(self, idx, accept_negative=False):
        if type(idx) != int:
            raise TypeError("Indices must be an integer!")
        elif idx <= -1 and accept_negative==False:
            raise IndexError(\
                "Negative indexing isn't supported with this functinoality!!")


    def __getitem__(self, idx):
        """Retrieves the element at the given index."""
        if self.is_empty():
            raise IndexError(f"{self.__name__()} is empty!!")
        self._validate_index(idx)
        idx = idx % self.length if self.length != 0 else 0
        return super().__getitem__(idx)


    ############################## INSERT ##############################
    def _insert_node(self, prev_node, new_node):
        assert isinstance(new_node, self._basic_node)
        assert new_node.get_data() is not None
        # start inserting the node
        if self.length == 0:
            new_node.set_next(new_node)
            self.head = new_node
        if prev_node is None:
            new_node.set_next(self.head.get_next())
            self.head.set_next(new_node)
            if self.length == 1:
                self.head = new_node
            else:
                #swap data between new_node and self.head
                new_node.data, self.head.data = self.head.data, new_node.data
                new_node = self.head #to be returned
        else:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        self.length += 1
        return new_node
    
    
    def insert(self, idx, item):
        self._validate_index((idx))
        idx = idx % (self.length+1)
        super()._insert(idx, item)


    ############################### SET ################################
    def __setitem__(self, idx, item):
        if self.is_empty():
            raise IndexError("Circular Linked List is empty!!")
        self._validate_index(idx)
        idx = idx % self.length if self.length != 0 else 0
        super()._replace_node(idx, item)
    

    ############################## REMOVE ##############################
    def _remove_node(self, prev_node, node_to_be_removed):
        assert node_to_be_removed != None, "Can't remove `None` node!!"
        # if node to be removed is the first
        if prev_node == None:
            if self.length == 1:
                self.head.data = None
            else:
                next_to_head = self.head.get_next()
                self.head.set_data(next_to_head.get_data())
                self.head.set_next(next_to_head.get_next())
        else:
            prev_node.set_next(node_to_be_removed.get_next())
        self.length -= 1
    

    def __delitem__(self, idx):
        """Removes a node at index=idx from the Circular Linked List"""
        self._validate_index((idx))
        idx = idx % self.length if self.length != 0 else 0
        super()._remove_idx(idx)


    ############################## MISC ##############################
    def reverse(self):
        """Reverses the whole linked list with complexity of O(n)"""
        rev = CircularLinkedList()
        curr_node = self.head
        while(curr_node.next != self.head):
            rev.add_front(curr_node.get_data())
            curr_node = curr_node.get_next()
        rev.add_front(curr_node.get_data())
        return rev




if __name__ == "__main__":
    l = CircularLinkedList()
    l.insert(100, 'answer')
    l.add_front('item')     # item answer
    l.insert(2, 'item2')    # item answer item2
    l.insert(1, 'hey')      # item hey answer item2
    l.add_front("yes")      # yes item hey answer item2
    l.insert(len(l)-1, "no")# yes item hey answer no item2
    l.add_end("now")        # yes item hey answer no item2 now
    print(l)
    print(l[2])
    print("Length:", len(l))

    rev = l.reverse()       # now item2 no answer hey item yes
    rev.remove_end()        # now item2 no answer hey item
    rev.remove_front()      # item2 no answer hey item
    print(rev)
    print("Length:", len(rev))
    print("item2" in rev)
    print("item" in rev)
    print("apple" in rev)
    print(rev.to_list())
    
    rev.clear()
    rev.add_front('')
    rev[0] = Node(10)
    del rev[1]
    print(rev)
    print(rev.is_empty())
