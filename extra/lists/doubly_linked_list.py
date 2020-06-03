"""
A doubly linked list is a simple linear data structure where objects are linked
using pointers to their associated location. Unlike arrays whose objects are
stored at continuous locations. Each node stores two references: the first is a
reference to the next element of the sequence. And the second is a reference to
the previous element of the sequence.

The first node of a doubly linked list is known as the **head** of the doubly
linked list. By starting at the doubly linked list's head and moving to the
latter nodes using each node's next reference, we can reach the end of the list.
This process is commonly known as *traversing* the doubly linked list. 
 
[image]

The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **m** is the number of elements in the *other* container.
- **k** is the value of a parameter.

+----------------+--------------------------------------------------------+-------------+-------------+
| Method         | Description                                            | Worst-case  | Optimal     |
+================+========================================================+=============+=============+
| __len__()      | Returns the number of nodes                            | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| is_empty()     | Checks if object is empty                              | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __repr__()     | Represents the object                                  | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __iters__()    | Iterates over the object                               | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __eq__()       | Checks if two linked lists are equal                   | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __ne__()       | Checks if two linked lists are not equal               | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __lt__()       | Checks if the linked list is less than the other       | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __le__()       | Checks if the list is less than or equal the other     | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __gt__()       | Checks if the linked list is greater than the other    | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __gt__()       | Checks if the list is greater than or equal the other  | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __contains__() | Checks the existence of the given item                 | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __getitem__()  | Returns the element at a certain index.                |O(min(k,n/2))|O(min(k,n/2))|
+----------------+--------------------------------------------------------+-------------+-------------+
| add_front()    | Adds the given item at the head                        | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| add_end()      | Adds the given item at the tail                        | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| insert()       | Adds the given item at the given index                 |O(min(k,n/2))|O(min(k,n/2))|
+----------------+--------------------------------------------------------+-------------+-------------+
| __setitem__()  | Replaces the value at the given index with given value |O(min(k,n/2))|O(min(k,n/2))|
+----------------+--------------------------------------------------------+-------------+-------------+
| __delitem__()  | Deletes the value at the given index                   |O(min(k,n/2))|O(min(k,n/2))|
+----------------+--------------------------------------------------------+-------------+-------------+
| remove_front() | Removes the node at the head                           | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| remove_end()   | Removes the node at the tail                           | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| remove()       | Removes the given value if found                       | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| clear()        | Clears the whole linked list                           | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| split()        | Splits the list into two at the given index            |O(min(k,n/2))|O(min(k,n/2))|
+----------------+--------------------------------------------------------+-------------+-------------+
| extend()       | Extends the linked list using another linked list.     | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| rotate_left()  | Left-rotates the list by the given value               | O(k)        | O(k)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| rotate_right() | Right-rotates the list by the given value              | O(k)        | O(k)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| reverse()      | Reverses the linked list                               | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| to_list()      | Converts the linked list to built-in list              | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| count()        | Counts how many the given value found in the list      | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| copy()         | Copies the linked list                                 | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+


Class Documentation
===================
Here are all of the public methods that can be used with `Doubly Linked List()`
objects:
"""
from extra.lists.linked_list import Node, LinkedList




class DoublyNode(Node):
    """Basic object for the Node used for doubly linked lists"""
    def __init__(self, item):
        """
        Creates a `DoublyNode()` object used mainly with `DoublyLinkedList()`
        objects!!

        Parameters
        ----------
        item: object 
            The value to be saved within the `DoublyNode()` instance.

        Raises
        ------
        TypeError: If the given item is an `Extra` object.
        ValueError: If the given item is `None`.
        """
        super().__init__(item)
        self._prev = None


    def __repr__(self):
        """
        Represents `DoublyNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `Node()` instance.
        
        Example
        -------
        >>> x = Node(10)
        >>> x
        >>> Node(data: 10, next:None)
        """
        prv = self._prev.get_data() if self._prev is not None else None
        nxt = self._next.get_data() if self._next is not None else None
        return f"DoublyNode(data: {self.data}, prev: {prv}, next: {nxt})"
    

    def get_prev(self):
        """
        Returns the prev `DoublyNode()` instance of the current one.

        Returns
        -------
        Node():
            The `Node()` instance that follows the current `DoublyNode()` or
            `None`.
        """
        return self._prev
    

    def set_prev(self, prev_node):
        """
        Sets the prev pointer of the current `DoublyNode()` to the given node.

        Parameters
        ----------
        next_node: DoublyNode()
            The `DoublyNode()` instance that will follow the current one.

        Raises
        ------
        TypeError: If the given item is an `Extra` object.
        """
        if prev_node is None:
            self._prev = None
        elif not isinstance(prev_node, DoublyNode):
            raise TypeError(
                f"Can't set {type(prev_node)} as a {self.__module__}!!")
        else:
            self._prev = prev_node
            prev_node._next = self
    

    def set_next(self, next_node):
        """
        Sets the next pointer of the current `DoublyNode()` to the given node.

        Parameters
        ----------
        next_node: DoublyNode()
            The `DoublyNode()` that will follow the current one.

        Raises
        ------
        TypeError: If the given item is an `Extra` object.
        """
        if next_node is None:
            self._next = None
        elif not isinstance(next_node, DoublyNode):
            raise TypeError(
                f"Can't set {type(next_node)} as a {self.__module__}!!")
        else:
            self._next = next_node
            next_node._prev = self




class DoublyLinkedList(LinkedList):
    """Basic object for the double linked list"""
    _basic_node = DoublyNode
   
   
    def __init__(self):
        """
        Creates a `DoublyLinkedList()` object!!
        
        Example
        -------
        >>> ll = DoublyLinkedList()
        >>> type(ll)
        <class 'extra.lists.doubly_linked_list.DoublyLinkedList'>
        """
        super().__init__()
        self._tail = None
    

    def _create_instance(self):
        """
        Returns an instance of the class

        Returns
        -------
        DoublyLinkedList()
            It returns an empty DoublyLinkedList() instance.
        """
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


