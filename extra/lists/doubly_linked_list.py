from linked_list import Node, LinkedList




class DoublyNode(Node):
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
        assert ( isinstance(prev_node, Node) and \
                prev_node.get_data() is not None)\
                or prev_node is None
        self.prev = prev_node
        if prev_node != None: prev_node.next = self 
    

    def set_next(self, next_node):
        super().set_next(next_node)
        if next_node != None: next_node.prev = self



class DoublyLinkedList(LinkedList):
    """Basic object for the double linked list"""
    def __init__(self, item=None):
        if isinstance(item, DoublyNode):
            item.set_next(None)
            self.head = self.tail = item
            self.length = 1 if item.get_data() is not None else 0
        else:
            self.head = self.tail = DoublyNode(item)
            self.length = 1 if item is not None else 0
    

    def _create_instance(self):
        return DoublyLinkedList()


    ############################## PRINT ##############################
    def _print_node(self, node):
        top_border = [' ┌']
        middle = ['⟷│']
        lower_border = [' └']
        item = str(node)
        width = len(item)+2 #2: for a space before & after an item
        top_border += (['─']*width) + ['┐']
        middle += [f" {item} │"]
        if node.get_next() is None: middle += ['⟷']
        lower_border += (['─']*width) + ['┘']
        return top_border, middle, lower_border


    ############################## SEARCH ##############################
    def _get_node(self, idx):
        # iterate over the double linked list (forwards)
        if idx <= self.length//2:
            return super()._get_node(idx)
        else:
            # iterate over the double linked list (backwards)
            counter = self.length
            curr_node = self.tail
            while(counter > idx):
                counter -= 1
                curr_node = curr_node.get_prev()
            return curr_node, curr_node.get_next()


    ############################## INSERT ##############################
    def _insert_node(self, prev_node, item):
        # handle different types of `item`
        if isinstance(item, Node):
            assert item.get_data() != None, \
                "Can't insert `None` value as a node!!"
            new_node = item
        else:
            assert item != None, "Can't insert `None` value as a node!!"
            new_node = DoublyNode(item)
        # start inserting the node
        if self.length == 0:
            self.head = self.tail = new_node
        elif self.length == 1:
            if prev_node == None:
                new_node.set_next(self.tail)
                self.head = new_node
            else:
                self.tail = new_node
                self.head.set_next(self.tail)
        else:
            if prev_node == None:
                new_node.set_next(self.head)
                self.head = new_node
            else:
                if prev_node.get_next() == None:
                    self.tail.set_next(new_node)
                    self.tail = new_node
                else:
                    new_node.set_next(prev_node.get_next())
                    prev_node.set_next(new_node)
        self.length += 1
        return new_node
    

    def _insert_value(self, prev_node, value):
        assert prev_node is None or isinstance(prev_node, Node)
        assert value is not None and not isinstance(value, Node)
        new_node = DoublyNode(value)
        return self._insert_node(prev_node, new_node)


    ############################## REMOVE ##############################
    def _remove_node(self, prev_node, node_to_be_removed):
        assert node_to_be_removed != None, "Can't remove `None`!!"
        next_node = node_to_be_removed.get_next()
        # if node to be removed is the first
        if self.length == 1:
            self.head = self.tail = DoublyNode()
            self.length -= 1
        elif self.length == 2:
            if prev_node == None:
                new_node = DoublyNode(next_node.get_data())
            elif next_node == None:
                new_node = DoublyNode(prev_node.get_data())
            self.head = self.tail = new_node
            self.length -= 1
        else:
            if next_node == None:
                prev_node.set_next(next_node)
                self.tail = prev_node
                self.length -= 1
            else:
                super()._remove_node(prev_node, node_to_be_removed)




if __name__ == "__main__":
    # dl = DoublyLinkedList()
    # # test removing from empty list:
    # dl.remove_front() #Nothing
    # dl.remove_end()   #Nothing
    # dl.remove(10)     #Nothing
    # # del l[0]       #throughs IndexError

    # dl.add_front(10)  #10 
    # dl.add_front(5)   #5 10
    # print(dl)
    # dl.remove(20)     #nothing
    # dl.remove_front() #10
    # print(dl)
    # dl.remove_end()   #[]
    # print(dl)
    # dl.insert(0, 100) #100
    # dl.insert(1, 200) #100 200
    # dl.insert(1, 100) #100 100 200
    # print(dl)
    # dl.remove(100)    #200
    # print(dl)
    # dl.clear()        #[]

    # # test remove() alone
    # dl.add_end(0)     #0
    # dl.remove(0)      #[]
    # print(dl)

    # # addinng
    # dl.add_front(6)   #6
    # dl.add_end(20)    #6 20
    # print(dl)
    # dl.insert(1, 10)   #6 10 20
    # dl.insert(2, 77)   #6 10 77 20
    # dl.insert(4, 43)   #6 10 77 20 43
    # dl.insert(0, 2)    #2 6 10 77 20 43
    # print(43 in dl)    #true
    # print(dl)
    # del dl[len(dl)-1]   #2 6 10 77 20
    # print("LENGTH:", len(dl))
    # print(dl.to_list())#[2, 6, 10, 77, 20]

    # print(dl[0], dl[3], "\n") #2 77

    # rev = dl.reverse() #20 77 10 6 2
    # print(rev)
    # print("REV LENGTH:", len(rev))
    # print(rev[1], rev[2]) #77 10

    # dl.clear()
    # print("Linked List is empty?", dl.is_empty())
    # print("Reversed Linked List is empty?", rev.is_empty())
    # print(dl)

    ll = LinkedList.from_iterable([1,2, 3])
    dl = DoublyLinkedList.from_iterable(ll)
    print(dl)

    print(dl.reverse())