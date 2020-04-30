# from linked_list import Node, LinkedList
from extra.lists.linked_list import Node, LinkedList




class DoublyNode(Node):
    """Basic object for the Node used for double linked lists"""
    def __name__(self):
        return "extra.DoublyNode()"
    

    def __init__(self, item):
        super().__init__(item)
        self._prev = None


    def __repr__(self):
        """Represents Node object as a string"""
        prv = self._prev.get_data() if self._prev is not None else None
        nxt = self._next.get_data() if self._next is not None else None
        return f"DoublyNode(data: {self.data}, prev: {prv}, next: {nxt})"
    

    def get_prev(self):
        return self._prev
    

    def set_prev(self, prev_node):
        if prev_node is None:
            self._prev = None
        elif not isinstance(prev_node, DoublyNode):
            raise TypeError(
                f"Can't set {type(prev_node)} as a {self.__name__()}!!")
        else:
            self._prev = prev_node
            prev_node._next = self
    

    def set_next(self, next_node):
        if next_node is None:
            self._next = None
        elif not isinstance(next_node, DoublyNode):
            raise TypeError(
                f"Can't set {type(next_node)} as a {self.__name__()}!!")
        else:
            self._next = next_node
            next_node._prev = self




class DoublyLinkedList(LinkedList):
    """Basic object for the double linked list"""
    _basic_node = DoublyNode
   
   
    def __name__(self):
        return "extra.DoublyLinkedList()"

    
    def __init__(self):
        super().__init__()
        self._tail = None
    

    def _create_instance(self):
        return DoublyLinkedList()


    ##############################      PRINT     ##############################
    def _print_node(self, node):
        top_border    = [' ┌']
        middle_border = ['⟷│']
        lower_border  = [' └']
        item = node._represent()
        width = len(item)+2 #2: for a space before & after an item
        top_border += (['─']*width) + ['┐']
        middle_border += [f" {item} │"]
        if node.get_next() is None: middle_border += ['⟷']
        lower_border += (['─']*width) + ['┘']
        return top_border, middle_border, lower_border


    ##############################     SEARCH     ##############################
    def _get_node(self, idx):
        # iterate over the double linked list (forwards)
        if idx <= self._length//2:
            return super()._get_node(idx)
        else:
            # iterate over the double linked list (backwards)
            counter = self._length
            curr_node = self._tail
            while(counter > idx):
                counter -= 1
                curr_node = curr_node.get_prev()
            prev_node = curr_node
            curr_node = prev_node.get_next()
            return prev_node, curr_node


    ##############################     INSERT     ##############################
    def _insert_node(self, prev_node, item):
        # handle different types of `item`
        if isinstance(item, self._basic_node):
            assert item.get_data() is not None, \
                "Can't insert `None` value as a node!!"
            new_node = item
        else:
            assert item is not None, "Can't insert `None` value as a node!!"
            new_node = self._basic_node(item)
        # start inserting the node
        if self._length == 0:
            self._head = self._tail = new_node
        elif self._length == 1:
            if prev_node is None:
                new_node.set_next(self._tail)
                self._head = new_node
            else:
                self._tail = new_node
                self._head.set_next(self._tail)
        else:
            if prev_node is None:
                new_node.set_next(self._head)
                self._head = new_node
            else:
                if prev_node.get_next() is None:
                    self._tail.set_next(new_node)
                    self._tail = new_node
                else:
                    new_node.set_next(prev_node.get_next())
                    prev_node.set_next(new_node)
        self._length += 1
        return new_node
    

    ##############################     REMOVE     ##############################
    def _remove_node(self, prev_node, node_to_be_removed):
        assert node_to_be_removed is not None, "Can't remove `None`!!"

        next_node = node_to_be_removed.get_next()
        # if node to be removed is the first
        if self._length == 1:
            #NOTE: don't use set_data() here
            self._head.data = self._tail.data = None
            self._length -= 1
        elif self._length == 2:
            if prev_node is None:
                next_node.set_prev(None)
                self._head = next_node
            elif next_node is None:
                prev_node.set_next(None)
                self._tail = prev_node
            self._length -= 1
        else:
            if next_node is None:
                prev_node.set_next(next_node)
                self._tail = prev_node
                self._length -= 1
            else:
                super()._remove_node(prev_node, node_to_be_removed)


    ##############################      Join      ##############################
    def join(self, other_dlist):
        if not isinstance(other_dlist, self.__class__):
            raise TypeError("Type Mismatch! Can't join this Doubly Linked List.")
        if other_dlist.is_empty():
            pass # do nothing
        elif self.is_empty(): 
            self._head = other_dlist._head
            self._tail = other_dlist._tail
            self._length += other_dlist._length
        else:
            self._tail.set_next(other_dlist._head)
            self._tail = other_dlist._tail
            self._length += other_dlist._length
    

    ##############################    ROTATION    ##############################
    def rotate_left(self, distance, inplace=True):
        if type(inplace) != bool:
            raise TypeError("`inplace` is a boolean flag (True by default)!!")
        super()._validate_distance(distance)
        rotated = self._rotate(distance, "LEFT")
        if not inplace: return rotated
        self._head = rotated._head
        self._tail = rotated._tail
        
    
    def rotate_right(self, distance, inplace=True):
        if type(inplace) != bool:
            raise TypeError("`inplace` is a boolean flag (True by default)!!")
        super()._validate_distance(distance)
        rotated = self._rotate(distance, "RIGHT")
        if not inplace: return rotated
        self._head = rotated._head
        self._tail = rotated._tail


