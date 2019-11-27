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
            first_line += ['┌─']
            second_line += ['│']
            third_line += ['└─']
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
                new_node.data, self.head.data = self.head.data, new_node.data
                new_node = self.head
        else:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        self.length += 1
        return new_node


    def __setitem__(self, idx, item):
        idx = idx % (self.length)
        super().__setitem__(idx, item)
    
    
    def insert(self, idx, item):
        idx = idx % (self.length) if self.length > 0 else 0
        super().insert(idx, item)



    def add_end(self, item):
        raise NotImplementedError(\
            "Can't insert at the end of a Circular Linked List!!")


    def remove_end(self):
        """Removes the circular linked list tail with complexity of O(n)"""
        raise NotImplementedError(\
            "Can't remove from the end of a Circular Linked List!!")


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
    l.add_front('item')     #answer item
    # l.insert(2, 'item2')  #answer item item2
    # l.insert(-1, 'item3') #answer item item3 item2
    # l.insert(-20, 'item4') #item item2 item3
    print(l)
    # l.add_front(100)
    # l.add_front(700)
    # l.add_end(90)
    # l.add_front("B")
    # print(l)
    # print(l[-10])

    # l.insert(10, 'item')
    # print(l)

    # rev = l.reverse()
    # rev.remove_end()
    # print(rev)
    # print(rev[-1])
    # print(rev.is_empty())
    
    # rev.remove_front()
    # print(rev.is_empty())
