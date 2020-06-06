"""
A circular linked list is a simple linear data structure where objects are
linked using pointers to their associated location. Unlike arrays whose objects
are stored at continuous locations. Each node stores a reference to an object
that is an element of the sequence, as well as a reference to the next node of
the circular linked list.

The first node of a circular linked list is known as the **head** of the linked
list. And the last node is known as the **tail**. The **tail** of a circular
linked list always points to the **head**. 
 
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
| __getitem__()  | Returns the element at a certain index.                | O(k)        | O(k)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| add_front()    | Adds the given item at the head                        | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| add_end()      | Adds the given item at the tail                        | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| insert()       | Adds the given item at the given index                 | O(k)        | O(k)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __setitem__()  | Replaces the value at the given index with given value | O(k)        | O(k)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __delitem__()  | Deletes the value at the given index                   | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| remove_front() | Removes the node at the head                           | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| remove_end()   | Removes the node at the tail                           | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| remove()       | Removes the given value if found                       | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| clear()        | Clears the whole linked list                           | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| split()        | Splits the list into two at the given index            | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| extend()       | Extends the linked list using another linked list.     | O(n)        | O(n)        |
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
Here are all of the public methods that can be used with `Linked List()`
objects:
"""
from extra.lists.linked_list import LinkedList




class CircularLinkedList(LinkedList):
    """Basic object for the Circular Linked List"""
    __name__ = "extra.CircularLinkedList()"


    def __init__(self):
        """
        Creates a CircularLinkedList() object!!
        
        Example
        -------
        >>> ll = CircularLinkedList()
        >>> type(ll)
        <class 'extra.lists.circular_linked_list.CircularLinkedList'>
        """
        super().__init__()


    def _create_instance(self):
        """
        Returns an instance of the class

        Returns
        -------
        CircularLinkedList()
            It returns an empty CircularLinkedList() instance.
        """
        return CircularLinkedList()
    

    ##############################      PRINT     ##############################
    def __repr__(self):
        """Represents the Circular linked list as a string
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 2 │⟶│ 3 │⟶│ 4 │⟶│ 5 │⟶│ 6 │⟶│ 7 │⟶ ┐
        └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘  │
           ↑                                       │
           └───────────────────────────────────────┘
        """
        if super().is_empty():
            return super()._print_empty_linked_list()
        first_line, second_line, third_line = \
                super()._print_linked_list(self._head)
        # backtrace representation
        second_line += [' ┐']
        third_line  += [' │']

        first_line  = "".join(first_line)
        second_line = "".join(second_line)
        third_line  = "".join(third_line)

        head_data = str(self._head.get_data())
        left_offset = (len(head_data)+4)//2
        remaining = (len(second_line) - 2) - left_offset
        
        fourth_line = (' '*left_offset) + '↑' + (' '*(remaining)) + '│'
        fifth_line  = (' '*left_offset) + '└' + ('─'*(remaining)) + '┘'
        return "{}\n{}\n{}\n{}\n{}".format(\
            first_line, second_line, third_line, fourth_line, fifth_line)


    ##############################     SEARCH     ##############################
    def _validate_index(self, idx, accept_negative=False, accept_slice=False):
        if isinstance(idx, slice):
            if not accept_slice:
                raise IndexError(\
                    "Slice indexing isn't supported with this functinoality!!")
        elif type(idx) != int:
            raise TypeError("Indices must be an integer!")
        elif idx <= -1 and not accept_negative:
            raise IndexError(\
                "Negative indexing isn't supported with this functinoality!!")


    def __getitem__(self, idx):
        """Retrieves the element at the given index."""
        self._validate_index(idx)
        if self.is_empty():
            raise IndexError(f"{self.__module__} is empty!!")
        idx = idx % self._length if self._length != 0 else 0
        return super().__getitem__(idx)


    ##############################     INSERT     ##############################
    def _insert_node(self, prev_node, new_node):
        assert isinstance(new_node, self._basic_node)
        assert new_node.get_data() is not None

        # start inserting the node
        if self._length == 0:
            new_node.set_next(new_node)
            self._head = new_node
        elif prev_node is None:
            new_node.set_next(self._head.get_next())
            self._head.set_next(new_node)
            #swap data between new_node and self._head
            new_node._data, self._head._data = self._head._data, new_node._data
            new_node = self._head #to be returned
        else:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        self._length += 1
        return new_node
    
    
    def insert(self, idx, item):
        self._validate_index((idx))
        self._validate_item(item)
        idx = idx % (self._length+1)
        super()._insert(idx, item)


    ##############################       SET      ##############################
    def __setitem__(self, idx, item):
        self._validate_index(idx)
        idx = idx % self._length if self._length != 0 else 0
        super()._replace_node(idx, item)
    

    ##############################     REMOVE     ##############################
    def _remove_node(self, prev_node, node_to_be_removed):
        assert prev_node is None or isinstance(prev_node, self._basic_node)
        assert isinstance(node_to_be_removed, self._basic_node)

        # if node to be removed is the first
        if prev_node is None:
            if self._length == 1:
                self._head._data = None #NOTE: don't use set_data() here
            else:
                next_to_head = self._head.get_next()
                self._head.set_data(next_to_head.get_data())
                self._head.set_next(next_to_head.get_next())
        else:
            prev_node.set_next(node_to_be_removed.get_next())
        self._length -= 1
    

    def __delitem__(self, idx):
        """Removes a node at index=idx from the Circular Linked List"""
        self._validate_index(idx)
        if not self.is_empty():
            idx = idx % self._length if self._length != 0 else 0
            node = super()._remove_idx(idx)
            return node


    ############################## MISC ##############################
    def split(self, idx):
        self._validate_index(idx)
        idx = idx % self._length if self._length != 0 else 0
        return super()._split(idx)
    
