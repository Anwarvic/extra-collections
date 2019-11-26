from linked_list import Node, LinkedList



class CircularLinkedList(LinkedList):
    """Basic object for the Circular Linked List"""
    def __init__(self, item=None):
       super().__init__(item)
       self.head.set_next(self.head)

    def __repr__(self):
        """Represents the Circular linked list as a string"""
        # represent the Linked List
        first_line, second_line, third_line = \
            super()._print_linked_list(stop_node=self.head)
        # check status
        if self.is_empty():
            return "{}\n{}\n{}".format(\
            ''.join(first_line), ''.join(second_line), ''.join(third_line))
        # backtrace representation
        else:
            second_line += [' ┐']
            third_line += [' │']
            left_offset = (len(str(self.head.data))+3)//2
            remaining = len(first_line) - left_offset
            fourth_line = (' '*left_offset) + '↑' + (' '*(remaining)) + '│'
            fifth_line = (' '*left_offset) + '└' + ('─'*(remaining)) + '┘'
            return "{}\n{}\n{}\n{}\n{}".format(\
                "".join(first_line), "".join(second_line), "".join(third_line),\
                fourth_line, fifth_line)
        

    def __getitem__(self, idx):
        """Retrieves the element at the given index."""
        self._validate_index(idx)
        idx = idx % (self.length)
        return super().__getitem__(idx)


    def __setitem__(self, idx, item):
        idx = idx % (self.length)
        super().__setitem__(idx, item)


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
        pointer = self.head
        while(pointer.next != self.head):
            rev.add_front(pointer.data)
            pointer = pointer.next
        rev.add_front(pointer.data)
        return rev




if __name__ == "__main__":
    l = CircularLinkedList()
    # l.insert(100, 'answer')
    # l.add_end('item')     #answer item
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
