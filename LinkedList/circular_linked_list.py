from linked_list import Node, LinkedList



class CircularLinkedList(LinkedList):
    """Basic object for the Circular Linked List"""
    def __init__(self, item=None):
        super().__init__(item)
        self.head.set_next(self.head)


    def __repr__(self):
        """Represents the Circular linked list as a string"""
        first_line, second_line, third_line = [], [], []
        if self.is_empty():
            first_line  += ['┌─']
            second_line += ['│']
            third_line  += ['└─']
            return "{}\n{}\n{}".format(\
            ''.join(first_line), ''.join(second_line), ''.join(third_line))
        else:
            # print just the head
            top_part, middle_part, lower_part = self._print_node(self.head)
            first_line += top_part
            second_line += middle_part
            third_line += lower_part
            # print the remaining nodes if found
            top_part, middle_part, lower_part = \
                self._print_linked_list(self.head.get_next(), self.head)
            first_line += top_part
            second_line += middle_part
            third_line += lower_part
        # backtrace representation
        head_data = str(self.head.get_data())
        left_offset = (len(head_data)+4)//2
        remaining = len("".join(second_line)) - left_offset
        second_line += [' ┐']
        third_line += [' │']
        fourth_line = (' '*left_offset) + '↑' + (' '*(remaining)) + '│'
        fifth_line = (' '*left_offset) + '└' + ('─'*(remaining)) + '┘'
        return "{}\n{}\n{}\n{}\n{}".format(\
            "".join(first_line), "".join(second_line), "".join(third_line),\
            fourth_line, fifth_line)


    def _validate_index(self, idx):
        if type(idx) != int:
            raise TypeError("Indices must be an integer!")
        elif idx <= -1:
            raise IndexError(\
                "Negative indexing isn't supported with this functinoality!!")


    def __getitem__(self, idx):
        """Retrieves the element at the given index."""
        self._validate_index(idx)
        idx = idx % (self.length)
        return super().__getitem__(idx)


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
        if prev_node == None:
            if self.is_empty():
                self.head.set_data(new_node.get_data())
            elif self.length == 1:
                new_node.set_next(self.head.get_next())
                self.head.set_next(new_node)
                self.head = new_node
            else:
                new_node.set_next(self.head.get_next())
                self.head.set_next(new_node)
                #swap data between new_node and self.head
                new_node.data, self.head.data = self.head.data, new_node.data
                new_node = self.head
        else:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        self.length += 1
        return new_node


    def __setitem__(self, idx, item):
        self._validate_index(idx)
        idx = idx % (self.length)
        super().__setitem__(idx, item)
    
    
    def insert(self, idx, item):
        self._validate_index((idx))
        idx = idx % (self.length+1)
        super()._insert(idx, item)
    

    def __delitem__(self, idx):
        """Removes a node at index=idx from the Circular Linked List"""
        self._validate_index((idx))
        idx = idx % (self.length+1)
        super().__delitem__(idx)


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

    rev = l.reverse()
    print(rev)
    rev.remove_end()        # now item2 no answer hey item
    rev.remove_front()      # item2 no answer hey item
    print(rev.is_empty())
    
    rev.clear()
    print(rev.is_empty())
    print(rev)