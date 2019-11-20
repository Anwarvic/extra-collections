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
            self.head = DoubleNode(item)
            self.length = 1 if item != None else 0

    
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
        if idx < self.length//2:
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


    def _remove_node(self, prev_node, node):
        assert node != None, "Can't remove `None`!!"
        next_node = node.get_next()
        # if node to be removed is the first
        if self.length == 1:
            self.head = self.tail = DoubleNode()
        elif self.length == 2:
            if prev_node == None:
                self.head = next_node
                self.tail.set_prev(self.head)
            elif next_node == None:
                self.tail = prev_node
                self.head.set_next(self.tail)
        else:
            super()._remove_node(prev_node, node)


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

    
    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        self.head = self.tail = Node()
        self.length = 0


    def reverse(self):
        """Reverses the whole double linked list with complexity of O(n)"""
        rev = DoubleLinkedList()
        if self.length == 0:
            return DoubleLinkedList()
        # iterate over original double linked list in (forward)
        pointer = self.head
        while(pointer != None):
            rev.add_front(pointer.data)
            pointer = pointer.next
        return rev




if __name__ == "__main__":
    l = DoubleLinkedList()
    l.add_front(6)   #6
    l.add_end(20)    #6 20
    l.insert(1, 10)  #6 10 20
    l.insert(-2, 999)#6 10 999 20
    l.insert_multiple(2, [1, 2, 3, 4])  #6 10 1 2 3 4 999 20
    l.insert(-9, -555)#-555 6 10 1 2 3 4 999 20
    print(l)
    print("LENGTH:", len(l))

    l.remove(-9)     #6 10 1 2 3 4 999 20
    l.remove(-2)     #6 10 1 2 3 4 20
    l.remove_front() #10 1 2 3 4 20
    l.remove_end()   #10 1 2 3 4
    l.remove(0)      #1 2 3 4
    print(l)
    print("LENGTH:", len(l))
    
    print(l[0], l[3], "\n")

    rev = l.reverse()#4 3 2 1
    print(rev)
    print("REV LENGTH:", len(rev))
    print(rev[1], rev[2])

    # iterate over l backwards
    print("===== Backward Iteration =====")
    pointer = l.tail
    while(pointer != None):
        print(pointer)
        pointer = pointer.prev
    # iterate over l forward
    print("===== Forward Iteration =====")
    pointer = l.head
    while(pointer != None):
        print(pointer)
        pointer = pointer.next

    l.clear()
    print("Linked List is empty?", l.is_empty())
    print("Reversed Linked List is empty?", rev.is_empty())

    ### additional testing