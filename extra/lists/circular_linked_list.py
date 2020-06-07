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
    

    @classmethod
    def from_iterable(cls, iterable):
        """
        A class method which creates a CircularLinkedList() instance using an
        iterable in time-complexity of O(n) where **n** is the number of
        elements inside the given `iterable`.

        Parameters
        ----------
        iterable: iterable object.
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
        
        Returns
        -------
        CircularLinkedList()
            It returns a CircularLinkedList() instance with the same values in
            the same order.
        
        Raises
        ------
        TypeError: It can be raised in two cases
            1. In case the given object isn't iterable.
            2. If one of the iterable elements is an `Extra` object.

        ValueError: If one of the iterable elements is `None`.

        Examples
        --------
        >>> cll = CircularLinkedList.from_iterable([10, -5, 7, 9])
        >>> cll
        ┌────┐ ┌────┐ ┌───┐ ┌───┐ 
        │ 10 │⟶│ -5 │⟶│ 7 │⟶│ 9 │⟶ ┐
        └────┘ └────┘ └───┘ └───┘  │
           ↑                       │
           └───────────────────────┘

        Using an iterable object with `None` as one of its elements will raise
        `ValueError`

        >>> cll = CircularLinkedList.from_iterable([2, None])
        ValueError: Can't use `None` as an element within `extra.CircularLinkedList()`!!
        
        Using a non-iterable object will raise `TypeError`

        >>> cll = CircularLinkedList.from_iterable(2)
        TypeError: The given object isn't iterable!!
        
        Using nested `CircularLinkedList` objects will raise `TypeError` as well

        >>> cll_1 = CircularLinkedList.from_iterable([1])
        >>> cll_2 = CircularLinkedList.from_iterable([1, cll_1])
        TypeError: Can't create `extra.CircularLinkedList()` using `extra.CircularLinkedList()`!!

        Note
        -----
        Since most of the data structures found in this package are iterables, 
        then you can use this classmethod to convert from one data structure to
        `CircularLinkedList` just like so:

        >>> ll = LinkedList.from_iterable([2, 5])
        >>> cll = CircularLinkedList.from_iterable(ll)
        >>> cll
        ┌───┐ ┌───┐ 
        │ 2 │⟶│ 5 │⟶ ┐
        └───┘ └───┘  │
          ↑          │
          └──────────┘
        """
        return super().from_iterable(iterable)
    

    ##############################      PRINT     ##############################
    def __repr__(self):
        """Represents the Circular linked list as a string
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 2 │⟶│ 3 │⟶│ 4 │⟶│ 5 │⟶│ 6 │⟶│ 7 │⟶ ┐
        └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘  │
          ↑                                        │
          └────────────────────────────────────────┘
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


    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the CircularLinkedList() in time-complexity of O(1)
        
        Returns
        -------
        int:
            The length of the CircularLinkedList() instance. By Length, I mean
            the number of nodes of in the instance.
        
        Examples
        --------
        >>> cll = CircularLinkedList()
        >>> len(cll)
        0
        >>> cll = CircularLinkedList.from_iterable((2, 5, 0))
        >>> len(cll)
        3
        """
        return self._length
    

    def is_empty(self):
        """
        Checks if CircularLinkedList() instance is empty or not in time-
        complexity of O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the CircularLinkedList() instance is empty
            or not. `True` shows that this instance is empty and `False` shows
            it's not empty.
        
        Example
        --------
        >>> cll = CircularLinkedList()
        >>> cll.is_empty()
        True
        >>> cll.add_front(5)
        >>> cll.is_empty()
        False
        """
        return self._length == 0

    
    ##############################    OPERATOR    ##############################
    def __iter__(self):
        """
        Iterates over the CircularLinkedList() instance and returns a generator
        in time-complexity of O(n) where **n** is the number of elements in the 
        CircularLinkedList() instance.

        Returns
        -------
        generator:
            The value of each node in the instance.
        
        Examples
        --------
        >>> cll = CircularLinkedList.from_iterable([1, 2, 3])
        >>> for item in cll:
        ...     print(item)
        1
        2
        3
        """
        return super().__iter__()
    

    def __eq__(self, other):
        """
        Checks if two CircularLinkedList() instances are equal to each other.
        And this happens if, and only if, the following two conditions are met:
        
        1. The two instances are equal in length (have same number of elements).

        2. Every single element in the first instance is equal, in both \
            **value** and **type**, to the opposing element of the other \
            instance.

        Parameters
        ----------
        other: CircularLinkedList()
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if both instances are equal, and `False` otherwise.
        
        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a CircularLinkedList() instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.

        Examples
        --------
        >>> cll_1 = CircularLinkedList.from_iterable([1, 2, 3])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 2])
        >>> cll_1 == cll_2
        False
        >>> cll_1 == cll_1
        True
        """
        return super().__eq__(other)


    def __ne__(self, other):
        """
        Checks if two CircularLinkedList() instances are NOT equal to each other.
        And this happens if, and only if, either one of the following two
        conditions is satisfied:
        
        1. The two instances are NOT equal in length (number of elements).

        2. Just one element in the first instance is NOT equal, in either \
            **value** or **type**, to the opposing element of the other \
            instance.

        Parameters
        ----------
        other: CircularLinkedList()
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if both instances are NOT equal, and `False` otherwise.

        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a LinkedList() instance.
            2. In case one element in the first instance doesn't match the \
                type of  the opposing element in the other instance.
        
        Examples
        --------
        >>> cll_1 = CircularLinkedList.from_iterable([1, 2, 3])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 2])
        >>> cll_1 != cll_2
        True
        >>> cll_1 != cll_1
        False
        """
        return super().__ne__(other)
    

    def __lt__(self, other):
        """
        Checks if the first CircularLinkedList() instance is less than the other
        instance. And this happens if all elements in the first instance are
        equal with at least one element less than the opposing element of the
        second instance.

        Parameters
        ----------
        CircularLinkedList()
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if the first instance is less than the second, and `False`
            otherwise.
        
        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a CircularLinkedList() instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.

        Examples
        --------

        >>> cll_1 = CircularLinkedList.from_iterable([1, 3, 2])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 < cll_2
        True

        >>> cll_1 = CircularLinkedList.from_iterable([1, 3])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 < cll_2
        True

        >>> cll_1 = CircularLinkedList.from_iterable([1, 5])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 < cll_2
        False

        >>> cll_1 = CircularLinkedList.from_iterable([5, 2, 1])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 < cll_2
        False

        >>> cll_1 = CircularLinkedList.from_iterable([1, 2, 3])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 2, 3])
        >>> cll_1 < cll_2
        False
        """
        return super().__lt__(other)


    def __le__(self, other):
        """
        Checks if the first CircularLinkedList() instance is less than or equal to
        the other instance. And this happens if all elements in the first
        instance are equal or less than the opposing elements of the second
        instance.

        Parameters
        ----------
        CircularLinkedList()
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if the first instance is less than or equal to the second
            instance, and `False` otherwise.
        
        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a LinkedList() instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.

        Examples
        --------

        >>> cll_1 = CircularLinkedList.from_iterable([1, 3, 2])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 <= cll_2
        True

        >>> cll_1 = CircularLinkedList.from_iterable([1, 3])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 <= cll_2
        True

        >>> cll_1 = CircularLinkedList.from_iterable([1, 5])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 <= cll_2
        False

        >>> cll_1 = CircularLinkedList.from_iterable([5, 2, 1])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 <= cll_2
        False

        >>> cll_1 = CircularLinkedList.from_iterable([1, 2, 3])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 2, 3])
        >>> cll_1 <= cll_2
        True
        """
        return super().__le__(other)
    
    
    def __gt__(self, other):
        """
        Checks if the first CircularLinkedList() instance is greater than the
        other instance. And this happens if all elements in the first instance
        are equal with at least one element greater than the opposing element of
        the second instance.

        Parameters
        ----------
        CircularLinkedList()
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if the first instance is greater than the second, and `False`
            otherwise.

        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a LinkedList() instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.
        
        Examples
        --------

        >>> cll_1 = CircularLinkedList.from_iterable([1, 3, 5])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 > cll_2
        True

        >>> cll_1 = CircularLinkedList.from_iterable([1, 3, 2, 1])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 2])
        >>> cll_1 > cll_2
        True

        >>> cll_1 = CircularLinkedList.from_iterable([1, 5])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 > cll_2
        False

        >>> cll_1 = CircularLinkedList.from_iterable([5, 2, 1])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 > cll_2
        False

        >>> cll_1 = CircularLinkedList.from_iterable([1, 2, 3])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 2, 3])
        >>> cll_1 > cll_2
        False
        """
        return super().__gt__(other)
    

    def __ge__(self, other):
        """
        Checks if the first CircularLinkedList() instance is greater than or equal
        to the other instance. And this happens if all elements in the first
        instance are greater than or equal to the opposing element of the
        second instance.

        Parameters
        ----------
        CircularLinkedList()
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if the first instance is greater than or equal to the second,
            and `False` otherwise.
        
        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a LinkedList() instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.

        Examples
        --------

        >>> cll_1 = CircularLinkedList.from_iterable([1, 3, 5])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 >= cll_2
        True

        >>> cll_1 = CircularLinkedList.from_iterable([1, 3, 2, 1])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 2])
        >>> cll_1 >= cll_2
        True

        >>> cll_1 = CircularLinkedList.from_iterable([1, 5])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 >= cll_2
        False

        >>> cll_1 = CircularLinkedList.from_iterable([5, 2, 1])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 3, 3])
        >>> cll_1 >= cll_2
        False

        >>> cll_1 = CircularLinkedList.from_iterable([1, 2, 3])
        >>> cll_2 = CircularLinkedList.from_iterable([1, 2, 3])
        >>> cll_1 >= cll_2
        True
        """
        return super().__ge__(other)


    ##############################     SEARCH     ##############################
    def _validate_index(self, idx, accept_negative=False, accept_slice=False):
        """
        Checks the validity of the given index.It raises the appropriate error
        when the index isn't valid and it returns nothing if the index is valid.

        Parameters
        ----------
        idx: int
            The index value.
        accept_negative: bool
            A flag to enable accepting negative indices, default `False`.
        accept_slice: bool
            A flag to enable accepting `slice` objects, default `False`.
        
        Raises
        ------
        TypeError: If the given index isn't `int`.
        IndexError: This happens in one of the following cases: 
            1. if the given index is a `slice` object while `accept_slice` \
                flag is `False`.
            2. If the given index is out of the CircularLinkedList() boundaries.
        
        Examples
        --------
        >>> cll = CircularLinkedList.from_iterable([1, 2, 3])
        >>> cll._validate_index('1')
        TypeError: Given index must be an integer!!
        >>> cll._validate_index(-2)
        IndexError: Negative indexing isn't supported with this functinoality!!
        >>> cll._validate_index(slice(0, 2))
        IndexError: Slice indexing isn't supported with this functinoality!!
        
        And it would return nothing if the given index if valid:

        >>> cll._validate_index(2)
        >>> cll._validate_index(-2, accept_negative=True)
        >>> cll._validate_index(slice(0, 2), accept_slice=True)
        """
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
            super()._remove_idx(idx)


    ############################## MISC ##############################
    def split(self, idx):
        self._validate_index(idx)
        idx = idx % self._length if self._length != 0 else 0
        return super()._split(idx)
    
