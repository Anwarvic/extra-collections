from linked_list import Node, LinkedList



class DoubleNode(Node):
    """Basic object for the Node used for double linked lists"""
    def __init__(self, item=None):
        self.data = item
        self.prev = None
        self.next = None


    def __repr__(self):
        """Represents Node object as a string"""
        data = self.data
        nxt = self.next.data if self.next else None
        prv = self.prev.data if self.prev else None
        return "Node: (data: {}, prev: {}, next: {})".format(data, prv, nxt)
    

    def get_prev(self):
        return self.prev
    

    def set_prev(self, prev_node):
        if not isinstance(prev_node, Node) and prev_node != None:
            raise TypeError("Linked List elements have to be of type `Node`")
        if prev_node != None: prev_node.next = self 
        self.prev = prev_node
    

    def set_next(self, next_node):
        if not isinstance(next_node, Node) and next_node != None:
            raise TypeError("Linked List elements have to be of type `Node`")
        if next_node != None: next_node.prev = self
        self.next = next_node



class DoubleLinkedList(LinkedList):
    """Basic object for the double linked list"""
    def __init__(self, item=None):
        if isinstance(item, Node):
            self.head = item
            self.length = 1 if item.get_data() != None else 0
        else:
            self.head = self.tail = DoubleNode(item)
            self.length = 1 if item != None else 0


    def __create_instance(self):
        return DoubleLinkedList()

    def __repr__(self):
        """Represents the double linked list as a string"""
        # NOTE: complexity of + operator is O(1) in lists and O(n) in string
        top_border = ["─┬"]
        middle = [" ↔"]
        down_border = ["─┴"]
        if not self.is_empty():
            curr_node = self.head
            while(curr_node != None):
                item = str(curr_node)
                width = len(str(item))+2 #2: for a space before & after an item
                top_border += (['─']*width) + ['┬']
                middle += [f" {item} ↔"]
                down_border += (['─']*width) + ['┴']
                curr_node = curr_node.get_next()
        top_border += ['─']
        middle += [' ']
        down_border += ['─']
        return "{}\n{}\n{}".format(\
            ''.join(top_border), ''.join(middle), ''.join(down_border))


    def _insert_node(self, prev_node, item):
        # handle different types of `item`
        if isinstance(item, Node):
            assert item.get_data() != None, \
                "Can't insert `None` value as a node!!"
            new_node = item
        else:
            assert item != None, "Can't insert `None` value as a node!!"
            new_node = DoubleNode(item)
        
        # start inserting the node
        if prev_node == None:
            if self.length == 0:
                self.head = self.tail = new_node
            elif self.length == 1:
                new_node.set_next(self.tail)
                self.head = new_node
            else:
                new_node.set_next(self.head.get_next())
                self.head = new_node
        else:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        self.length += 1
        return new_node


    def add_end(self, item):
        """Adds node at the tail of the double linked list with O(1) complexity.
        """
        self._insert_node(self.tail, item)


    def insert(self, idx, item):
        """Inserts a certain item at a given index into the double linked list.
        """
        self._validate_index(idx)
        # when idx is smaller than half the linked list length
        if idx <= self.length//2:
            super().insert(idx, item)
        # when idx is bigger than half the linked list length
        else:
            # iterate over the double linked list (backwards)
            counter = self.length
            curr_node = self.tail
            while(counter != idx):
                counter -= 1
                curr_node = curr_node.get_prev()
            self._insert_node(curr_node, item)


    def _remove_node(self, prev_node, node_to_be_removed):
        assert node_to_be_removed != None, "Can't remove `None`!!"
        next_node = node_to_be_removed.get_next()
        # if node to be removed is the first
        if self.length == 1:
            self.head = self.tail = DoubleNode()
            self.length -= 1
        elif self.length == 2:
            if prev_node == None:
                new_node = DoubleNode(next_node.get_data())
            elif next_node == None:
                new_node = DoubleNode(prev_node.get_data())
            self.head = self.tail = new_node
            self.length -= 1
        else:
            super()._remove_node(prev_node, node_to_be_removed)


    def remove_end(self):
        """Removes the double linked list tail with complexity of O(1)"""
        if not self.is_empty():
            self._remove_node(self.tail.get_prev(), self.tail)


    def __delitem__(self, idx):
        """Removes a node at index=idx from the double linked list"""
        self._validate_index(idx)
        if idx == self.length:
            raise IndexError("Can't find any element at the given index!!")
        # when idx is smaller than half the linked list length
        if idx < self.length//2:
            super().__delitem__(idx)
        # when idx is bigger than half the linked list length
        else:
            # iterate over the double linked list (forwards)
            counter = self.length-1
            curr_node = self.tail
            while(counter != idx):
                counter -= 1
                curr_node = curr_node.get_prev()
            self._remove_node(curr_node.get_prev(), curr_node)






if __name__ == "__main__":
    l = DoubleLinkedList()
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
    print(43 in l)
    print(l)
    del l[len(l)-1]
    print(l)
    print("LENGTH:", len(l))
    print(l.to_list())

    print(l[0], l[3], "\n")

    rev = l.reverse()#43 20 77 10 2
    print(rev)
    print("REV LENGTH:", len(rev))
    print(rev[1], rev[2])

    l.clear()
    print("Linked List is empty?", l.is_empty())
    print("Reversed Linked List is empty?", rev.is_empty())
    print(l)
