"""
A linked list is a simple linear data structure where objects are linked using
pointers to their associated location. Unlike arrays whose objects are stored at
continuous locations. Each node stores a reference to an object that is an
element of the sequence, as well as a reference to the next node of the linked 
list.

The first node of a linked list is known as the **head** of the linked list. 
By starting at the linked list's head and moving to the latter nodes using each
node's next reference, we can reach the end of the list. This process is
commonly known as *traversing* the linked list. 
 
.. image:: ../../img/lists/linked_list.gif


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
| __gt__()       | Checks if the list is greater than or equal the other. | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __contains__() | Checks the existence of the given item                 | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __getitem__()  | Returns the element at a certain index.                | O(k)        | O(k)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| add_front()    | Adds the given item at the head                        | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| add_end()      | Adds the given item at the tail                        | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| insert()       | Adds the given item at the given index.                | O(k)        | O(k)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __setitem__()  | Replaces the value at the given index with given value.| O(k)        | O(k)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __delitem__()  | Deletes the value at the given index.                  | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| remove_front() | Removes the node at the head.                          | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| remove_end()   | Removes the node at the tail.                          | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| remove()       | Removes the given value if found.                      | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| clear()        | Clears the whole linked list.                          | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| split()        | Splits the list into two at the given index.           | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| extend()       | Extends the linked list using another linked list.     | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| rotate_left()  | Left-rotates the list by the given value.              | O(k%n)      | O(k%n)      |
+----------------+--------------------------------------------------------+-------------+-------------+
| rotate_right() | Right-rotates the list by the given value.             | O(k%n)      | O(k%n)      |
+----------------+--------------------------------------------------------+-------------+-------------+
| reverse()      | Reverses the linked list.                              | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| to_list()      | Converts the linked list to built-in list.             | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| count()        | Counts how many the given value found in the list.     | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| copy()         | Copies the linked list.                                | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+


Class Documentation
===================
Here are all of the public methods that can be used with `LinkedList()` objects:
"""
import warnings, operator
from extra.interface import Extra




class Node(Extra):
    """A node is the basic unit for building linked lists."""
    __name__ = "extra.Node()"


    def __init__(self, item):
        """
        Creates a `Node()` object used mainly with `LinkedList()` objects!!

        Parameters
        ----------
        item: object 
            The value to be saved within the `Node()` instance

        Raises
        ------
        TypeError: If the given item is an `Extra` object.
        ValueError: If the given item is `None`.
        """
        super()._validate_item(item)
        if type(item) == str:
            item = item.replace('\n', '\\n')
        self._data = item
        self._next = None


    def __repr__(self):
        """
        Represents `Node()` object as a string.

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
        nxt = self._next.get_data() if self._next is not None else None
        return f"Node(data: {self._data}, next: {nxt})"


    def get_data(self):
        """
        Returns the node's data
        
        Returns
        -------
        object:
            The data saved inside the `Node()` instance
        """
        return self._data
    

    def set_data(self, data):
        """
        Sets the data within the Node()'s object
        
        Parameters
        ----------
        data: object
            The python object to be saved within the `Node()`.

        Raises
        ------
        TypeError: If the input value is an `Extra` object.
        ValueError: If the input valueis `None`.
        """
        super()._validate_item(data)
        if type(data) == str:
            data = data.replace('\n', '\\n')
        self._data = data
    

    def get_next(self):
        """
        Returns the next `Node()` instance of the current one.

        Returns
        -------
        Node():
            The `Node()` instance that follows the current `Node()` or `None`.
        """
        return self._next
    

    def set_next(self, next_node):
        """
        Sets the next pointer of the current `Node()` to the given node.

        Parameters
        ----------
        next_node: Node()
            The `Node()` that will follow the current `Node()`.

        Raises
        ------
        TypeError: If the given item is an `Extra` object.
        """
        if next_node is None:
            self._next = None
        elif not isinstance(next_node, Node):
            raise TypeError(
                f"Can't set {type(next_node)} as a `{self.__name__}`!!"
            )
        else:
            self._next = next_node


    def _represent(self):
        """
        A helpful function used to represent the node when printing!!
        
        Returns
        -------
        str:
            A string representing the Node is a very simple way.
        
        Example
        -------
        >>> x = Node(10)
        >>> x
        Node(data:10, next:None)
        >>> x._represent()
        10
        >>> type(x._represent())
        <class 'str'>
        """
        return str(self._data)




class LinkedList(Extra):
    """
    A linked list is a simple linear data structure where objects are linked
    using pointers to their associated location. Unlike arrays whose objects are
    stored at continuous locations. Each node stores a reference to an object
    that is an element of the sequence, as well as a reference to the next node
    of the linked list.
    """
    _basic_node = Node
    __name__ = "extra.LinkedList()"
    

    def __init__(self, iterable=None):
        """
        Initializes a `LinkedList()` object instance using an optional iterable
        object in time-complexity of O(n) where **n** is the number of elements
        inside the given `iterable`.

        Parameters
        ----------
        iterable: any iterable object (default: None)
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
               
        Raises
        ------
        TypeError: It can be raised in two cases
            1. In case the given object isn't iterable.
            2. If one of the iterable elements is an `Extra` object.

        ValueError: If one of the iterable elements is `None`.

        Examples
        --------
        >>> ll = LinkedList([10, -5, 7, 9])
        >>> ll
        ┌────┐ ┌────┐ ┌───┐ ┌───┐ 
        │ 10 │⟶│ -5 │⟶│ 7 │⟶│ 9 │⟶
        └────┘ └────┘ └───┘ └───┘ 

        Using an iterable object with `None` as one of its elements will raise
        `ValueError`

        >>> ll = LinkedList([2, None])
        ValueError: Can't use `None` as an element within `extra.LinkedList()`!!
        
        Using a non-iterable object will raise `TypeError`

        >>> ll = LinkedList(2)
        TypeError: The given object isn't iterable!!
        
        Using nested `LinkedList` objects will raise `TypeError` as well

        >>> ll_1 = LinkedList([1])
        >>> ll_2 = LinkedList([1, ll_1])
        TypeError: Can't create `extra.LinkedList()` using `extra.LinkedList()`!!

        Note
        -----
        Since most of the data structures found in this package are iterables, 
        then you can use this classmethod to convert from one data structure to
        `Linked List` just like so:

        >>> dll = DoublyLinkedList([2, 5])
        >>> ll = LinkedList(dll)
        >>> ll
        ┌───┐ ┌───┐ 
        │ 2 │⟶│ 5 │⟶
        └───┘ └───┘ 
        """
        if iterable is None:
            self._head = None
            self._length = 0
        elif not hasattr(iterable, "__iter__"):
            raise TypeError("The given object isn't iterable!!")
        elif isinstance(iterable, self.__class__):
            #in case the given iterable is alread a LinkedList()
            self._head = iterable._head
            self._length = iterable._length
        else:
            self._head = None
            self._length = 0
            prev_node = None
            for item in iterable:
                self._validate_item(item)
                if isinstance(item, Node): #Node here is generic
                    item = item.get_data()
                prev_node = self._insert_value(prev_node, item)


    def _create_instance(self):
        """
        Returns an instance of the class

        Returns
        -------
        LinkedList()
            It returns an empty `LinkedList()` instance.
        """
        return LinkedList()


    ##############################     PRINT      ##############################
    def _print_node(self, node):
        """
        Prints the given node of the LinkedList() instance.

        Parameters
        ----------
        node: `Node()`
            The `Node()` object that we want to print.

        Returns
        -------
        tuple
            It returns a tuple of three strings representing the given node
            when printed.
        
        Raises
        ------
        AssertionError: In case the given object isn't `Node()`

        Example
        -------
        >>> ll = LinkedList()
        >>> ll.add_front(10)
        >>> lines = ["".join(x) for x in ll._print_node(ll._head)]
        >>> "\n".join(lines)
        ┌────┐ 
        │ 10 │⟶
        └────┘
        """
        assert isinstance(node, self._basic_node)

        top_border = ['┌']
        middle = ['│']
        lower_border = ['└']
        item = node._represent()
        width = len(item)+2 #2: for a space before & after an item
        top_border += (['─']*width) + ['┐ ']
        middle += [f" {item} │⟶"]
        lower_border += (['─']*width) + ['┘ ']
        return top_border, middle, lower_border
    

    def _print_empty_linked_list(self):
        """
        Prints the `LinkedList()` instance when it's empty.

        Returns
        -------
        str
            A string representing an empty `LinkedList()` instance

        Raises
        ------
        AssertionError: In case the `LinkedList()` instance isn't empty!!

        Example
        -------
        >>> ll = LinkedList()
        >>> ll
        ┌─
        │
        └─
        """
        assert self._length == 0

        top_border    = ['┌─']
        middle_border = ['│']
        lower_border  = ['└─']
        return "{}\n{}\n{}".format(\
            ''.join(top_border), ''.join(middle_border), ''.join(lower_border))

        
    def _print_linked_list(self, start_node):
        """
        Prints the given node within the `LinkedList()` instance. Each node in
        the linked list is printed in three lines. So, the following is how the
        `Node(1.0)` look like:
        ┌─────┐ 
        │ 1.0 │⟶
        └─────┘


        Parameters
        ----------
        node: a `Node()` object that we want to print

        Returns
        -------
        tuple
            It returns a tuple of three lists representing the three lines of 
            the printed node. For example, the first item in the `tuple` is a 
            list of strings collectively represent the first line, and same goes
            for the second and third item.
        
        Raises
        ------
        AssertionError: In case the given object isn't `Node()`

        Example
        -------
        >>> ll = LinkedList()
        >>> ll.add_front(10)
        >>> lines = ["".join(x) for x in ll._print_node(ll._head)]
        >>> "\n".join(lines)
        ┌────┐ 
        │ 10 │⟶
        └────┘
        """
        assert isinstance(start_node, self._basic_node)

        # NOTE: complexity of + operator is O(1) in lists and O(n) in string
        top_border = []
        middle_border = []
        lower_border = []
        counter = 0
        curr_node = start_node
        while(counter < self._length):
            top_part, middle_part, lower_part = self._print_node(curr_node)
            top_border += top_part
            middle_border += middle_part
            lower_border += lower_part
            # update curr_node
            curr_node = curr_node.get_next()
            counter += 1
        return top_border, middle_border, lower_border

    
    def __repr__(self):
        """
        Represents the linked list as a string.

        Returns
        -------
        str:
            The string-representation of the `LinkedList()` instance.
        
        Example
        -------
        >>> ll = LinkedList([20, 77, 10, 6, 2])
        >>> ll
        ┌────┐ ┌────┐ ┌────┐ ┌───┐ ┌───┐ 
        │ 20 │⟶│ 77 │⟶│ 10 │⟶│ 6 │⟶│ 2 │⟶
        └────┘ └────┘ └────┘ └───┘ └───┘ 
        """
        if self.is_empty():
            return self._print_empty_linked_list()
        top_border, middle, lower_border = self._print_linked_list(self._head)
        return "{}\n{}\n{}".format(\
            ''.join(top_border), ''.join(middle), ''.join(lower_border))


    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the `LinkedList()` in time-complexity of O(1)
        
        Returns
        -------
        int:
            The length of the `LinkedList()` instance. By Length, I mean the
            number of nodes of in the instance.
        
        Examples
        --------
        >>> ll = LinkedList()
        >>> len(ll)
        0
        >>> ll = LinkedList((2, 5, 0))
        >>> len(ll)
        3
        """
        return self._length
    

    def is_empty(self):
        """
        Checks if `LinkedList()` instance is empty or not in time-complexity of
        O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the `LinkedList()` instance is empty or
            not. `True` shows that this instance is empty and `False` shows
            it's not empty.
        
        Example
        --------
        >>> ll = LinkedList()
        >>> ll.is_empty()
        True
        >>> ll.add_front(5)
        >>> ll.is_empty()
        False
        """
        return self._length == 0

    
    ##############################    OPERATOR    ##############################
    def __iter__(self):
        """
        Iterates over the `LinkedList()` instance and returns a generator in 
        time-complexity of O(n) where **n** is the number of elements in the 
        `LinkedList()` instance.

        Returns
        -------
        generator:
            The value of each node in the instance.
        
        Examples
        --------
        >>> ll = LinkedList([1, 2, 3])
        >>> for item in ll:
        ...     print(item)
        1
        2
        3
        """
        counter = 0
        curr_node = self._head
        while(counter < self._length):
            yield curr_node.get_data()
            counter += 1
            curr_node = curr_node.get_next()


    def _compare(self, other, op):
        """
        Compares two intances of `LinkedList()`and returns the index at which 
        two nodes didn't satisfy the given operator. They could be the end of
        both instances or at just some random position in the middle.

        Parameters
        ----------
        other: `LinkedList()`
            The other instance that we want to compare with the current one
        op: operator.function
            An operator function that represents ==, >=, <=, !=, <, > operators
        
        Returns
        -------
        int
            The index at which the given operator wasn't satisfied
        
        bool
            `True` if all elements in both instances are exactly the same.
            `False` other wise
        
        Raises
        ------
        TypeError: In case one element in the first instance doesn't match the
            type of the opposing element in the other instance.
        
        Examples
        --------
        >>> ll_1 = LinkedList([1, 2, 3])
        >>> ll_2 = LinkedList([1, 3, 2])
        >>> ll_1._compare(ll_2, operator.eq)
        1
        >>> ll_1.comprare(ll_1, operator.le)
        2
        >>> ll_1._compare(LinkedList(), operator.eq)
        0
        """
        assert isinstance(other, self.__class__)
        assert op.__name__ in dir(operator)

        # start_comparing
        counter = 0
        pointer1 = self._head
        pointer2 = other._head
        all_equal = True
        while(counter < min(self._length, other._length)):
            try:
                #NOTE: Don't remove the following if-condition
                if pointer1.get_data() == pointer2.get_data():
                    pass
                else:
                    all_equal = False
                    if not op(pointer1.get_data(), pointer2.get_data()):
                        break
            except TypeError:
                raise TypeError(
                    f"Inconsist data-types within the two {self.__name__} " + 
                    "instances!!"
                )
            pointer1 = pointer1.get_next()
            pointer2 = pointer2.get_next()
            counter += 1
        return counter, all_equal


    def __eq__(self, other):
        """
        Checks if two `LinkedList()` instances are equal to each other. And this
        happens if, and only if, the following two conditions are satisfied:
        
        1. The two instances are equal in length (have same number of elements).

        2. Every single element in the first instance is equal, in both \
            **value** and **type**, to the opposing element of the other \
            instance.

        Parameters
        ----------
        other: `LinkedList()`
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if both instances are equal, and `False` otherwise.
        
        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a `LinkedList()` instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.

        Examples
        --------
        >>> ll_1 = LinkedList([1, 2, 3])
        >>> ll_2 = LinkedList([1, 3, 2])
        >>> ll_1 == ll_2
        False
        >>> ll_1 == ll_1
        True
        """
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Can't compare `{self.__name__}` to `{type(other)}`"
            )
        # check length
        if self._length != other._length:
            return False
        idx, _ = self._compare(other, operator.eq)
        return True if idx == self._length == other._length else False
    

    def __ne__(self, other):
        """
        Checks if two `LinkedList()` instances are NOT equal to each other.
        And this happens if, and only if, either one of the following two
        conditions is satisfied:
        
        1. The two instances are NOT equal in length (number of elements).

        2. Just one element in the first instance is NOT equal, in either \
            **value** or **type**, to the opposing element of the other \
            instance.

        Parameters
        ----------
        other: `LinkedList()`
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if both instances are NOT equal, and `False` otherwise.

        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a `LinkedList()` instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.
        
        Examples
        --------
        >>> ll_1 = LinkedList([1, 2, 3])
        >>> ll_2 = LinkedList([1, 3, 2])
        >>> ll_1 != ll_2
        True
        >>> ll_1 != ll_1
        False
        """
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Can't compare `{self.__name__}` to `{type(other)}`"
            )
        if self._length != other._length:
            return True
        idx, _ = self._compare(other, operator.eq)
        return False if idx == self._length == other._length else True
    

    def __lt__(self, other):
        """
        Checks if the first `LinkedList()` instance is less than the other
        instance. And this happens if all elements in the first instance are
        equal with at least one element less than the opposing element of the
        second instance.

        Parameters
        ----------
        `LinkedList()`
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if the first instance is less than the second, and `False`
            otherwise.
        
        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a `LinkedList()` instance.
            2. In case one element in the first instance doesn't match the type of \
                the opposing element in the other instance.

        Examples
        --------

        >>> ll_1 = LinkedList([1, 3, 2])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 < ll_2
        True

        >>> ll_1 = LinkedList([1, 3])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 < ll_2
        True

        >>> ll_1 = LinkedList([1, 5])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 < ll_2
        False

        >>> ll_1 = LinkedList([5, 2, 1])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 < ll_2
        False

        >>> ll_1 = LinkedList([1, 2, 3])
        >>> ll_2 = LinkedList([1, 2, 3])
        >>> ll_1 < ll_2
        False
        """
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Can't compare `{self.__name__}` to `{type(other)}`"
            )
        idx, all_equal = self._compare(other, operator.lt)
        if all_equal:
            return True if self._length < other._length else False
        else:
            return True if idx == self._length else False
    

    def __le__(self, other):
        """
        Checks if the first `LinkedList()` instance is less than or equal to the
        other instance. And this happens if all elements in the first instance
        are equal or less than the opposing elements of the second instance.

        Parameters
        ----------
        `LinkedList()`
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if the first instance is less than or equal to the second
            instance, and `False` otherwise.
        
        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a `LinkedList()` instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.

        Examples
        --------

        >>> ll_1 = LinkedList([1, 3, 2])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 <= ll_2
        True

        >>> ll_1 = LinkedList([1, 3])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 <= ll_2
        True

        >>> ll_1 = LinkedList([1, 5])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 <= ll_2
        False

        >>> ll_1 = LinkedList([5, 2, 1])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 <= ll_2
        False

        >>> ll_1 = LinkedList([1, 2, 3])
        >>> ll_2 = LinkedList([1, 2, 3])
        >>> ll_1 <= ll_2
        True
        """
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Can't compare `{self.__name__}` to `{type(other)}`"
            )
        idx, _ = self._compare(other, operator.le)
        return True if idx == self._length else False
    

    def __gt__(self, other):
        """
        Checks if the first `LinkedList()` instance is greater than the other
        instance. And this happens if all elements in the first instance are
        equal with at least one element greater than the opposing element of the
        second instance.

        Parameters
        ----------
        `LinkedList()`
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if the first instance is greater than the second, and `False`
            otherwise.

        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a `LinkedList()` instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.
        
        Examples
        --------

        >>> ll_1 = LinkedList([1, 3, 5])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 > ll_2
        True

        >>> ll_1 = LinkedList([1, 3, 2, 1])
        >>> ll_2 = LinkedList([1, 3, 2])
        >>> ll_1 > ll_2
        True

        >>> ll_1 = LinkedList([1, 5])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 > ll_2
        False

        >>> ll_1 = LinkedList([5, 2, 1])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 > ll_2
        False

        >>> ll_1 = LinkedList([1, 2, 3])
        >>> ll_2 = LinkedList([1, 2, 3])
        >>> ll_1 > ll_2
        False
        """
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Can't compare `{self.__name__}` to `{type(other)}`"
            )
        return not (self <= other)
    

    def __ge__(self, other):
        """
        Checks if the first `LinkedList()` instance is greater than or equal to
        the other instance. And this happens if all elements in the first
        instance are greater than or equal to the opposing element of the
        second instance.

        Parameters
        ----------
        `LinkedList()`
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if the first instance is greater than or equal to the second,
            and `False` otherwise.
        
        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a `LinkedList()` instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.

        Examples
        --------

        >>> ll_1 = LinkedList([1, 3, 5])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 >= ll_2
        True

        >>> ll_1 = LinkedList([1, 3, 2, 1])
        >>> ll_2 = LinkedList([1, 3, 2])
        >>> ll_1 >= ll_2
        True

        >>> ll_1 = LinkedList([1, 5])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 >= ll_2
        False

        >>> ll_1 = LinkedList([5, 2, 1])
        >>> ll_2 = LinkedList([1, 3, 3])
        >>> ll_1 >= ll_2
        False

        >>> ll_1 = LinkedList([1, 2, 3])
        >>> ll_2 = LinkedList([1, 2, 3])
        >>> ll_1 >= ll_2
        True
        """
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Can't compare `{self.__name__}` to `{type(other)}`"
            )
        return not (self < other)


    ##############################     SEARCH     ##############################
    def _search(self, value, start_node):
        """
        Searches the Linked List for a given value and returns the first node
        containing that value if found. If not found, it returns the last node
        in the Linked List.

        Parameters
        ----------
        value: Object
            The value to be searched for in the `LinkedList()` instance.
        
        start_node: Node()
            A reference to the object object at which we want to start search
            for the given value.
        
        Returns
        -------
        Node():
            Either the node object that contains the given value or the last
            node in the `LinkedList()` instance if the given value wasn't found.
        
        Raises:
        -------
        AssertionError: This happens in two cases
            1. If `value` is an instance of `Node()`.
            2. If the `start_node` isn't an instance of `Node()`.

        Examples
        --------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll._search(2, ll._head)
        Node(data: 2, next: 3)
        >>> ll._search(0, ll._head)
        Node(data: 2, next: None)
        >>> ll._search(1, ll._head._next)
        Node(data: 2, next: None)
        """
        assert not isinstance(value, Node) #Node here is generic
        assert isinstance(start_node, self._basic_node)

        curr_node = start_node
        while(curr_node.get_next() is not None):
            if curr_node.get_data() == value:
                return curr_node
            curr_node = curr_node.get_next()
        return curr_node


    def __contains__(self, value):
        """
        Checks if the given value exists in the `LinkedList()` instance in time-
        complexity of O(n) where **n** is the total number of elements in the
        `LinkedList()` instance.

        Parameters
        ----------
        value: Object
            The value to be searched for in the `LinkedList()` instance.
        
        Returns
        -------
        bool
            `True` if the given value exists in the `LinkedList()` instance, and
            `False` otherwise.

        Examples
        --------
        >>> ll = LinkedList([1, 3, 5])
        >>> 1 in ll
        True
        >>> 0 in ll
        False
        >>> "hello" in ll
        False
        """
        if value is None or self.is_empty():
            return False
        found_node = self._search(value, self._head)
        if found_node.get_data() != value:
            return False
        return True


    def _get_node(self, idx):
        """
        Retrieves the `Node()` at the given index of the `LinkedList()`
        instance.

        Parameters
        ----------
        idx: int
            The index at which the `Node()` object should be returned.
        
        Returns
        -------
        Node():
            The previous node to the node at the given index.
        Node():
            The node at the given index.
        
        Raises
        ------
        AssertionError: If the given index is bigger than the LinkedList length.

        Example
        -------
        >>> ll = LinkedList([1, 2, 3])
        >>> prev_node, node = ll._get_node(2)
        >>> prev_node
        (Node(data: 2, next: 3)
        >>> node
        Node(data: 3, next: None)
        """
        assert 0 <= idx or idx < self._length
        # iterate over the linked list
        counter = 0
        prev_node = None
        curr_node = self._head
        while(counter != idx):  
            counter += 1
            prev_node = curr_node
            curr_node = curr_node.get_next()
        return prev_node, curr_node


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
            2. If the given index is out of the `LinkedList()` boundaries.
            3. If the given index is negative while `accept_negative` flag is \
                `False`.
        
        Examples
        --------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll._validate_index('1')
        TypeError: Given index must be an integer!!
        >>> ll._validate_index(-2)
        IndexError: Negative indexing isn't supported with this functinoality!!
        >>> ll._validate_index(slice(0, 2))
        IndexError: Slice indexing isn't supported with this functinoality!!
        
        And it would return nothing if the given index if valid:

        >>> ll._validate_index(2)
        >>> ll._validate_index(-2, accept_negative=True)
        >>> ll._validate_index(slice(0, 2), accept_slice=True)
        """
        if isinstance(idx, slice):
            if not accept_slice:
                raise IndexError(
                    "Slice indexing isn't supported with this functinoality!!"
                )
        elif type(idx) != int:
            raise TypeError("Given index must be an integer!!")
        elif idx <= -1 and not accept_negative:
            raise IndexError(\
                "Negative indexing isn't supported with this functinoality!!")
        elif idx < -self._length or idx > self._length:
            raise IndexError("Given index is out of the boundaries!!")


    def __getitem__(self, idx):
        """
        Retrieves the element at the given index. The given index could be a 
        zero-based `int` or a `slice` object. This method supports negative
        indexing. This method does that in time-complexity of O(k) where **k**
        is the given index.

        Parameters
        ----------
        idx: int or slice
            The index (multiple indices) to be used to retrieve values from the
            `LinkedList()` instance.
        
        Returns
        -------
        object or `LinkedList()`:
            If the given index is an `int`, then it returns the value at this 
            index. If the given index is a `slice` object, then it returns a 
            `LinkedList()` instance containing the desired values.
        
        Raises
        ------
        TypeError: If the given index isn't `int`.
        IndexError: If the given index is out of the `LinkedList()` boundaries.

        Examples
        --------
        >>> ll = LinkedList([1, 2, 3, 4, 5])
        >>> ll[0]
        1
        >>> ll[-2]
        4
        >>> ll[2:]
        ┌───┐ ┌───┐ ┌───┐ 
        │ 3 │⟶│ 4 │⟶│ 5 │⟶
        └───┘ └───┘ └───┘ 
        >>> ll[0:5:2]
        ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 3 │⟶│ 5 │⟶
        └───┘ └───┘ └───┘ 
        >>> ll[10]
        IndexError: Given index is out of the boundaries!!
        """
        # sanity check over given index
        self._validate_index(idx, accept_negative=True, accept_slice=True)
        if isinstance(idx, slice):
            indices = range(*idx.indices(self._length))
            max_idx = indices[-1] if indices else -1
            indices = set(indices)
            # start getting wanted nodes
            counter = 0
            prev_node = None
            curr_node = self._head
            out_llist = self._create_instance()
            while(counter <= max_idx):
                if counter in indices:
                    prev_node = out_llist._insert_value(prev_node,
                                                        curr_node.get_data())
                curr_node = curr_node.get_next()
                counter += 1
            return out_llist
        else:
            if idx == self._length:
                raise IndexError("Given index is out of the boundaries!!")
            # convert idx to positive if -ve
            if idx <= -1: idx += self._length
            # get the item
            _, node = self._get_node(idx)
            return node.get_data()


    ##############################     INSERT     ##############################
    def _insert_node(self, prev_node, new_node):
        """
        Inserts a `new_node` at a position defined by the given `prev_node`.

        Parameters
        ----------
        prev_node: Node()
            A reference to the node next to which a new node should be inserted.
        new_node: Node()
            A referece to the new node to be inserted.
        
        Returns
        -------
        Node():
            A reference to the new node after being inserted in the
            `LinkedList()`.
            
        Raises
        ------
        AssertionError: This happens in one of the following cases:
            1. The `prev_node` isn't a `Node()` object
            2. The `new_node` isn't a `Node()` object
        
        Example
        -------
        >>> ll = LinkedList([1, 2, 3])
        >>> new_node = Node(10)
        >>> ll._insert_node(ll._head, new_node)
        Node(data: 10, next: 2)
        """
        assert prev_node is None or isinstance(prev_node, self._basic_node)
        assert isinstance(new_node, self._basic_node)
        assert new_node.get_data() is not None

        # start inserting the node
        if self._length == 0:
            new_node.set_next(None)
            self._head = new_node
        elif prev_node is None:
            new_node.set_next(self._head)
            self._head = new_node
        else:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        self._length += 1
        return new_node


    def _insert_value(self, prev_node, value):
        """
        Insertd a value at a position defined by the given `prev_node`.

        Parameters
        ----------
        prev_node: Node()
            A reference to the node next to which a new node should be inserted.
        value: object
            An object to be inserted.
        
        Returns
        -------
        Node():
            A reference to the new node after being inserted in the
            `LinkedList()`.
        
        Raises
        ------
        AssertionError: This happens in one of the following cases:
            1. The `prev_node` isn't a `Node()` object.
            2. The `value` is `None` or an instance of `Node()`.
        
        Example
        -------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll._insert_value(ll._head, 10)
        Node(data: 10, next: 2)
        """
        assert prev_node is None or isinstance(prev_node, self._basic_node)
        assert value is not None and not isinstance(value, self._basic_node)
        
        new_node = self._basic_node(value)
        return self._insert_node(prev_node, new_node)
    

    def _insert(self, idx, item):
        """
        Insertd a value at a position defined by the given index.

        Parameters
        ----------
        idx: int
            An integer pointing to the index at which the given value should be
            inserted.
        item: object
            An object to be inserted.
        
        Returns
        -------
        Node():
            A reference to the new node after being inserted in the
            `LinkedList()`.
        
        Raises
        ------
        AssertionError: If the given index is out of the LinkedList()
            boundaries.
        
        Example
        -------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll._insert(1, 10)
        Node(data: 10, next: 2)
        """
        assert 0 <= idx or idx <= self._length
        prev_node, _ = self._get_node(idx)
        if isinstance(item, Node):  #Keep it generic
            assert item.get_data() is not None
            return self._insert_node(prev_node, item)
        else:
            assert item is not None
            return self._insert_value(prev_node, item)


    def add_front(self, item):
        """
        Adds the given value at the head of the `LinkedList()` instance in
        time-complexity of O(1).

        Parameters
        ----------
        item: object
            The value to be inserted at the `LinkedList()` head.
        
        Raises
        ------
        TypeError: If the given item is an instance of `Extra`.
        ValueError: If the given item is `None`.

        Examples
        --------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll.add_front(10)
        >>> ll
        ┌────┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 10 │⟶│ 1 │⟶│ 2 │⟶│ 3 │⟶
        └────┘ └───┘ └───┘ └───┘ 
        """
        super()._validate_item(item)
        self._insert(0, item)


    def add_end(self, item):
        """
        Adds the given value at the tail of the `LinkedList()` instance in
        time-complexity of O(n).

        Parameters
        ----------
        item: object
            The value to be inserted at the `LinkedList()` tail.
        
        Raises
        ------
        TypeError: If the given item is an instance of `Extra`.
        ValueError: If the given item is `None`.

        Examples
        --------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll.add_end(10)
        >>> ll
        ┌───┐ ┌───┐ ┌───┐ ┌────┐ 
        │ 1 │⟶│ 2 │⟶│ 3 │⟶│ 10 │⟶
        └───┘ └───┘ └───┘ └────┘         
        """
        super()._validate_item(item)
        self._insert(len(self), item)
    
    
    def insert(self, idx, item):
        """
        Insertd a value at a position defined by the given index.

        Parameters
        ----------
        idx: int
            An integer pointing to the index at which the given value should be
            inserted.
        item: object
            An object to be inserted.
        
        Raises
        ------
        IndexError: This happens in one of the following cases: 
            1. If the given index is out of the `LinkedList()` boundaries.
            2. If the given index is less than zero (-ve).
        TypeError: This happens in one of the following cases:
            1. If the given index isn't integer.
            2. If the given item is an instance of `Extra`.
        ValueError: If the given item is `None`.
        
        Example
        -------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll.insert(1, 10)
        >>> ll
        ┌───┐ ┌────┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 10 │⟶│ 2 │⟶│ 3 │⟶
        └───┘ └────┘ └───┘ └───┘ 
        >>> ll.insert(5, 8)
        IndexError: Given index is out of the boundaries!!
        >>> ll.insert(1, None)
        ValueError: Can't use `None` as an element within `extra.LinkedList()`!!
        >>> ll.insert(-1, 100)
        IndexError: Negative indexing isn't supported with this functinoality!!
        """
        self._validate_index(idx)
        super()._validate_item(item)
        self._insert(idx, item)


    def extend(self, other):
        """
        Extends the current `LinkedList()` instance by appending the elements of
        the other `LinkedList()` instance in time-complexity of O(n) where **n**
        is the lengh of the current instance.

        Parameters
        ----------
        other: `LinkedList()`
            The `LinkedList()` instance whose elements will be appended.
                
        Raises
        ------
        TypeError: If the given object isn't a `LinkedList()` instance.

        Example
        -------
        >>> ll_1 = LinkedList([1, 2])
        >>> ll_2 = LinkedList([3, 4, 5])
        >>> ll_1.extend(ll_2)
        >>> ll_1
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 2 │⟶│ 3 │⟶│ 4 │⟶│ 5 │⟶
        └───┘ └───┘ └───┘ └───┘ └───┘ 
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Type Mismatch! " + 
                f"Can't extend `{self.__name__}` with `{type(other)}`!!"
            )
        if other.is_empty():
            pass # do nothing
        elif self.is_empty():
            self._head = other._head
            self._length = other._length
        else:
            last_node, _ = self._get_node(self._length)
            last_node.set_next(other._head)
            self._length += other._length
    
    
    ##############################       SET      ##############################
    def _replace_value(self, idx, new_value):
        """
        Replaces the value of the node at the given index with the `new_value`.

        Parameters
        ----------
        idx: int
            The index at which we want to replace the node.
        new_value: object
            The new value that will replace the old one.
        
        Raises
        ------
        AssertionError: This can be raised in the following cases:
            1. if the given index is out of the boundaries.
            2. If the `new_value` is not `None`.
        """
        assert 0 <= idx or idx <= self._length
        assert new_value is not None

        _, old_node = self._get_node(idx)
        old_node.set_data(new_value)
    

    def __setitem__(self, idx, item):
        """
        Replaces the value at the given index with the given item. It does that
        in time-complexity of O(k) where **k** is the index value.

        Parameters
        ----------
        idx: int
            An integer pointing to the index at which the given value should be
            inserted.
        item: object
            An object to be inserted.
        
        Raises
        ------
        IndexError: If the given index is either negative or out of the
            boundaries.
        ValueError: If the given object is `None`.
        TypeError: This get raised in one of the following cases:
            1. If the given index type is not `int`.
            2. If the given object is an instance of `Extra`.
        
        TODOs
        -----
        1. Handle negative indexing
        2. Handle slice objects

        Examples
        --------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll[0] = 10
        >>> ll[2] = 30
        >>> ll
        ┌────┐ ┌───┐ ┌────┐ 
        │ 10 │⟶│ 2 │⟶│ 30 │⟶
        └────┘ └───┘ └────┘ 
        >>> ll[-1] = 0
        IndexError: Negative indexing isn't supported with this functinoality!!
        >>> ll[3] = 40
        IndexError: Given index is out of the boundaries!!
        """
        self._validate_index(idx)
        if idx == self._length:
            raise IndexError("Given index is out of the boundaries!!")
        super()._validate_item(item)
        self._replace_value(idx, item)
        

    ##############################     REMOVE     ##############################
    def _remove_node(self, prev_node, node_to_be_removed):
        """
        Removes a node from the `LinkedList()` instance.

        Parameters
        ----------
        prev_node: Node()
            A reference to the node next to the node that will be removed.
        node_to_be_removed: Node()
            A referece to the node to be removed.
        
        Raises
        ------
        AssertionError: This happens in one of the following cases:
            1. The `prev_node` isn't a `Node()` object or `None.
            2. The `node_to_be_removed` isn't a `Node()` object
        
        Example
        -------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll
        ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 2 │⟶│ 3 │⟶
        └───┘ └───┘ └───┘ 
        >>> ll._remove_node(ll._head, ll._head._next)
        >>> ll
        ┌───┐ ┌───┐ 
        │ 1 │⟶│ 3 │⟶
        └───┘ └───┘ 
        """
        assert prev_node is None or isinstance(prev_node, self._basic_node)
        assert isinstance(node_to_be_removed, self._basic_node)

        next_node = node_to_be_removed.get_next()
        # if node to be removed is the first
        if prev_node is None:
            if self._length == 1:
                #NOTE: don't use set_data() here
                self._head._data = None
            else:
                self._head.set_next(next_node.get_next())
                self._head.set_data(next_node.get_data())
        else:
            prev_node.set_next(next_node)
        self._length -= 1


    def _remove_idx(self, idx):
        """
        Removes a node from the `LinkedList()` at the given index.

        Parameters
        ----------
        idx: int
            An integer pointing to the index at which the given value should be
            removed.
        
        Raises
        ------
        AssertionError: If The given index is either negative or bigger than or
            equal the length of the `LinkedList()` instance.
        
        Example
        -------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll
        ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 2 │⟶│ 3 │⟶
        └───┘ └───┘ └───┘ 
        >>> ll._remove_idx(1)
        >>> ll
        ┌───┐ ┌───┐ 
        │ 1 │⟶│ 3 │⟶
        └───┘ └───┘ 
        """
        assert 0 <= idx or idx < self._length

        prev_node, node = self._get_node(idx)
        self._remove_node(prev_node, node)


    def __delitem__(self, idx):
        """
        Deletes the value at the given index. It does that in time-complexity
        of O(k) where **k** is the index value.

        Parameters
        ----------
        idx: int
            An integer pointing to the index where the node that should be
            removed.
        
        Raises
        ------
        IndexError: If the given index is either negative or out of the
            boundaries.
        
        TODOs
        -----
        1. Handle negative indexing
        2. Handle slice objects

        Examples
        --------
        >>> ll = LinkedList([1, 2, 3])
        >>> del ll[0]
        >>> ll
        ┌───┐ ┌───┐ 
        │ 2 │⟶│ 3 │⟶
        └───┘ └───┘ 
        >>> del ll[-1]
        IndexError: Negative indexing isn't supported with this functinoality!!
        >>> del ll[3]
        IndexError: Given index is out of the boundaries!!
        """
        self._validate_index(idx)
        if idx == self._length:
            raise IndexError("Given index is out of the boundaries!!")
        self._remove_idx(idx)
    

    def remove_front(self):
        """
        Removes the value at the head of the `LinkedList()` instance in time-
        complexity of O(1).

        Examples
        --------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll.remove_front()
        >>> ll
        ┌───┐ ┌───┐ 
        │ 2 │⟶│ 3 │⟶
        └───┘ └───┘ 
        >>> ll.remove_front()
        >>> ll
        ┌───┐ 
        │ 3 │⟶
        └───┘ 
        """
        if not self.is_empty():
            self.__delitem__(0)


    def remove_end(self):
        """
        Removes the value at the tail of the `LinkedList()` instance in time-
        complexity of O(n) where **n** is the number of elements in the 
        `LinkedList()` instance.

        Examples
        --------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll.remove_end()
        >>> ll
        ┌───┐ ┌───┐ 
        │ 1 │⟶│ 2 │⟶
        └───┘ └───┘ 
        >>> ll.remove_end()
        >>> ll
        ┌───┐ 
        │ 1 │⟶
        └───┘ 
        """
        if not self.is_empty():
            self.__delitem__( self._length-1 )


    def _remove_value(self, value, all):
        """
        Removes node(s) whose value equal to the given value.

        Parameters
        ----------
        value: object
            The value to be removed from the `LinkedList()` instance.
        all: bool
            A flag; if `True`, all occurrences of the given value are remove. If
            `False`, only the first occurrence is removed.
        
        Raises
        ------
        AssertionError: This get raised in one of the following cases:
            1. If The given value is `None` or and instance of `Extra` class.
            2. If `all` flag isn't boolean.
        
        Example
        -------
        >>> ll = LinkedList([1, 2, 3, 2, 2])
        >>> ll._remove_value(2, False)
        >>> ll
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 3 │⟶│ 2 │⟶│ 2 │⟶
        └───┘ └───┘ └───┘ └───┘ 
        >>> ll._remove_value(10, False) #does nothing
        >>> ll._remove_value(2, True)
        >>> ll
        ┌───┐ ┌───┐ 
        │ 1 │⟶│ 3 │⟶
        └───┘ └───┘ 
        """
        # removes all occurrences (when all==True) of `value` if found.
        assert not isinstance(value, self._basic_node) and value is not None
        assert type(all) == bool

        counter = 0
        prev = None
        curr_node = self._head
        FOUND_FIRST = False #True when the first occurrence is found
        total_length = self._length
        while(counter < total_length):
            if all==False and FOUND_FIRST:
                return
            if curr_node.get_data() == value:
                FOUND_FIRST = True
                self._remove_node(prev, curr_node)
                curr_node = prev.get_next() if prev is not None else self._head
            else:
                prev = curr_node
                curr_node = curr_node.get_next()
            counter += 1

    
    def remove(self, value, all=True):
        """
        Removes node(s) whose value equal to the given value.

        Parameters
        ----------
        value: object
            The value to be removed from the `LinkedList()` instance.
        all: bool
            A flag (default: `True`); if `True`, all occurrences of the given
            value are remove. If `False`, only the first occurrence is removed.
        
        Raises
        ------
        ValueError: If The given value is `None`.
        TypeError: This get raised in one of the following cases:
            1. If the type of the `all` flag isn't boolean.
            2. If the given value is an instance of `Extra` class.
        
        Example
        -------
        >>> ll = LinkedList([1, 2, 3, 2, 2])
        >>> ll.remove(2, False)
        >>> ll
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 3 │⟶│ 2 │⟶│ 2 │⟶
        └───┘ └───┘ └───┘ └───┘ 
        >>> ll.remove(10) #does nothing
        >>> ll.remove(2)
        >>> ll
        ┌───┐ ┌───┐ 
        │ 1 │⟶│ 3 │⟶
        └───┘ └───┘ 
        """
        if type(all) != bool:
            raise TypeError("`all` is a boolean flag (True by default)!!")
        super()._validate_item(value)
        self._remove_value(value, all=all)


    def clear(self):
        """
        Removes all nodes within the `LinkedList()` in time-complexity of O(1).

        Example
        -------
        >>> ll = LinkedList([1, 2, 3])
        ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 2 │⟶│ 3 │⟶
        └───┘ └───┘ └───┘ 
        >>> ll.clear()
        >>> ll.is_empty()
        True
        >>> ll
        ┌─
        │
        └─
        """
        self.__init__()
    

    ##############################      SPLIT     ##############################
    def _split(self, idx):
        """
        Splits the `LinkedList()` instance into two instances based on the given
        index in time-complexity of O(n) where **n** is the number of elements
        in the original instance. We can consider `idx` as the start index of
        the second `LinkedList()` after splitting. If `idx=0`, then the first
        returned `LinkedList()` will be empty while the second returned
        `LinkedList()` will be the same length as the original.

        Parameters
        ----------
        idx: int
            A positive integer pointing to the index at which the `LinkedList()`
            instance should be split.
        
        Returns
        -------
        `LinkedList()`: 
            The left `LinkedList()` instance returned after split.
        `LinkedList()`: 
            The right `LinkedList()` instance returned after split
        
        Raises
        ------
        AssertionError: If the index's type is not integer.

        Examples
        --------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll
        ┌───┐ ┌───┐ ┌───┐
        │ 1 │⟶│ 2 │⟶│ 3 │
        └───┘ └───┘ └───┘
        >>> left, right = ll._split(1)
        >>> left
        ┌───┐ 
        │ 1 │⟶
        └───┘ 
        >>> right
        ┌───┐ ┌───┐ 
        │ 2 │⟶│ 3 │⟶
        └───┘ └───┘ 
        """
        assert type(idx) == int

        left_list = self._create_instance()
        right_list = self._create_instance()
        if not self.is_empty():
            counter = 0
            prev_node = None
            curr_node = self._head
            # left list
            while(counter < idx):
                prev_node = left_list._insert_value(prev_node,
                                                    curr_node.get_data())
                curr_node = curr_node.get_next()
                counter += 1
            # right list
            while(counter < self._length):
                prev_node = right_list._insert_value(prev_node,
                                                    curr_node.get_data())
                curr_node = curr_node.get_next()
                counter += 1
        return left_list, right_list
    

    def split(self, idx):
        """
        Splits the `LinkedList()` instance into two instances based on the given
        index in time-complexity of O(n) where **n** is the number of elements
        in the original instance. We can consider `idx` as the start index of
        the second `LinkedList()` after splitting. If `idx=0`, then the first
        returned `LinkedList()` will be empty while the second returned
        `LinkedList()` will be the same length as the original.

        Parameters
        ----------
        idx: int
            A positive integer pointing to the index at which the `LinkedList()`
            instance should be split.
        
        Returns
        -------
        `LinkedList()`: 
            The left `LinkedList()` instance returned after split.
        `LinkedList()`: 
            The right `LinkedList()` instance returned after split
        
        Raises
        ------
        TypeError: If the given index isn't `int`.
        IndexError: If the given index is either negative or out of the
            `LinkedList()` boundaries.

        Examples
        --------
        >>> ll = LinkedList([1, 2, 3])
        >>> ll
        ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 2 │⟶│ 3 │⟶
        └───┘ └───┘ └───┘ 
        >>> left, right = ll.split(1)
        >>> left
        ┌───┐ 
        │ 1 │⟶
        └───┘ 
        >>> right
        ┌───┐ ┌───┐ 
        │ 2 │⟶│ 3 │⟶
        └───┘ └───┘ 
        """
        self._validate_index(idx)
        return self._split(idx)
        

    ##############################    ROTATION    ##############################
    def _validate_distance(self, distance):
        """
        Checks the validity of the given distance value. It raises the
        appropriate error when the distance isn't valid and it returns nothing
        if the distance is valid.

        Parameters
        ----------
        distance: int
            The distance value (mainly used for rotation).
        
        Raises
        ------
        TypeError: If the given distance isn't `int`.
        ValueError: If the given distance is negative.
        
        Examples
        --------
        >>> ll = `LinkedList()`
        >>> ll._validate_distance(1)
        >>> ll._validate_distance('1')
        TypeError: Rotation distance has to be an `int`!!
        >>> ll._validate_distance(-2)
        IndexError: Negative indexing isn't supported with this functinoality!!
        >>> ll._validate_index(slice(0, 2))
        ValueError: Rotation distance has to be >= zero!!
        """
        if type(distance) != int:
            raise TypeError("Rotation distance has to be an `int`!!")
        if distance < 0:
            raise ValueError("Rotation distance has to be >= zero!!")
    
    
    def __calibrate_distance(self, distance, direction):
        """
        Converts invalid distance value into a valid one paying attentionthe
        given rotation direction.

        Parameters
        ----------
        distance: int
            The rotation distance.
        direction: str
            A string representing the rotation directions. It's either "RIGHT"
            or "LEFT".
        
        Returns
        -------
        int: The clibrated distance value.

        Raises
        ------
        AssertionError: It can be raised due to one of the following cases:
            1. The type of given `distance` isn't `int`.
            2. The direction value is not "RIGHT" or "LEFT".
        """
        assert type(distance) == int
        assert direction in {"RIGHT", "LEFT"}

        distance = distance % self._length if self._length > 0 else 0
        if direction == "RIGHT":
            distance = self._length - distance
        return distance


    def _rotate(self, distance, direction):
        """
        Rotates the `LinkedList()` instance to the given `direction` by a
        certain given `distance` and returns the rotated instance. It does all
        of that in time-complexity of O(n) where **n** is the number of elements
        in the `LinkedList()` instance.

        Parameters
        ----------
        distance: int
            The rotation distance.
        direction: str
            A string representing the rotation directions. It's either "RIGHT"
            or "LEFT".
        
        Returns
        -------
        `LinkedList()`:
            The rotated instance.
        
        Examples
        --------
        >>> ll = LinkedList([1, 2, 3, 4])
        >>> ll._rotate(1, "LEFT")
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 2 │⟶│ 3 │⟶│ 4 │⟶│ 1 │⟶
        └───┘ └───┘ └───┘ └───┘ 
        >>> ll._rotate(1, "RIGHT")
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 4 │⟶│ 1 │⟶│ 2 │⟶│ 3 │⟶
        └───┘ └───┘ └───┘ └───┘ 
        >>> # it works fine when the distance is bigger than the instance length
        >>> ll._rotate(10, "LEFT")
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 3 │⟶│ 4 │⟶│ 1 │⟶│ 2 │⟶
        └───┘ └───┘ └───┘ └───┘ 
        >>> ll._rotate(15, "RIGHT")
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 2 │⟶│ 3 │⟶│ 4 │⟶│ 1 │⟶
        └───┘ └───┘ └───┘ └───┘ 
        """
        distance = self.__calibrate_distance(distance, direction)
        # split based on distance
        left_list, right_list = self.split(distance)
        # join them to mimic rotation effect
        right_list.extend(left_list)
        # return rotated
        return right_list


    def rotate_left(self, distance, inplace=True):
        """
        Rotates the `LinkedList()` instance to the left by a certain given
        `distance`. If `inplace=True`, it does the rotation in-place. If not, 
        it returns the rotated instance. The time-compelxity of this method is
        O(n) where **n** is the number of elements in the `LinkedList()`
        instance.

        Parameters
        ----------
        distance: int
            The rotation distance to the left.
        inplace: bool
            A flag to determine if the rotation is going to be in-place or not.
            (default `True`).
        
        Returns
        -------
        `LinkedList()`:
            The rotated instance if `inplace=True`
        
        Examples
        --------
        >>> ll = LinkedList([1, 2, 3, 4])
        >>> ll.rotate_left(1)
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 2 │⟶│ 3 │⟶│ 4 │⟶│ 1 │⟶
        └───┘ └───┘ └───┘ └───┘ 
        >>> # it works fine when the distance is bigger than the instance length
        >>> ll.rotate_left(10)
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 3 │⟶│ 4 │⟶│ 1 │⟶│ 2 │⟶
        └───┘ └───┘ └───┘ └───┘ 
        """
        if type(inplace) != bool:
            raise TypeError("`inplace` is a boolean flag (True by default)!!")
        self._validate_distance(distance)
        rotated = self._rotate(distance, "LEFT")
        if not inplace: return rotated
        self._head = rotated._head
        
    
    def rotate_right(self, distance, inplace=True):
        """
        Rotates the `LinkedList()` instance to the right by a certain given
        `distance`. If `inplace=True`, it does the rotation in-place. If not, 
        it returns the rotated instance. The time-compelxity of this method is
        O(n) where **n** is the number of elements in the `LinkedList()`
        instance.

        Parameters
        ----------
        distance: int
            The rotation distance to the right.
        inplace: bool
            A flag to determine if the rotation is going to be in-place or not.
            (default `True`).
        
        Returns
        -------
        `LinkedList()`:
            The rotated instance if `inplace=True`
        
        Examples
        --------
        >>> ll = LinkedList([1, 2, 3, 4])
        >>> ll.rotate_right(1)
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 4 │⟶│ 1 │⟶│ 2 │⟶│ 3 │⟶
        └───┘ └───┘ └───┘ └───┘ 
        >>> # it works fine when the distance is bigger than the instance length
        >>> ll.rotate_right(15)
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 2 │⟶│ 3 │⟶│ 4 │⟶│ 1 │⟶
        └───┘ └───┘ └───┘ └───┘ 
        """
        self._validate_distance(distance)
        rotated = self._rotate(distance, "RIGHT")
        if not inplace: return rotated
        self._head = rotated._head

    
    ##############################      MISC      ##############################
    def reverse(self):
        """
        Reverses the whole `LinkedList()` instance in time-complexity of O(n)
        where **n** is the number of elements in the `LinkedList()`.

        Returns
        -------
        `LinkedList()`:
            The reversed `LinkedList()` instance.
        
        Example
        -------
        >>> ll = LinkedList([1, 2, 3, 4])
        >>> ll.reverse()
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 4 │⟶│ 3 │⟶│ 2 │⟶│ 1 │⟶
        └───┘ └───┘ └───┘ └───┘ 
        """
        rev = self._create_instance()
        counter = 0
        curr_node = self._head
        while(counter < self._length):
            rev.add_front(curr_node.get_data())
            curr_node = curr_node.get_next()
            counter += 1
        return rev


    def to_list(self):
        """
        Converts the `LinkedList()` instance to a `list` in time-complexity of
        O(n) where **n** is the number of elements in the instance.

        Returns
        -------
        list:
            A `list` object containing the same elements as the `LinkedList()`
            instance.
        
        Example
        -------
        >>> ll = LinkedList()
        >>> ll.add_front(20)
        >>> ll.add_front(10)
        >>> ll.add_end(30)
        >>> ll
        ┌────┐ ┌────┐ ┌────┐ 
        │ 10 │⟶│ 20 │⟶│ 30 │⟶
        └────┘ └────┘ └────┘ 
        >>> ll.to_list()
        [10, 20, 30]
        """
        return [item for item in self]


    def count(self, value):
        """
        Counts the number of occurrence the given value is in our `LinkedList()`
        instance.

        Parameters
        ----------
        value: object
            The object to count its occurrences
        
        Returns
        -------
        int:
            The number of times the given value is found in the `LinkedList()`
            instance. And 0 if it wasn't found.
        
        Example
        -------
        >>> ll = LinkedList([0, 1, 1, 2, 3, 5])
        >>> ll.count(3)
        1
        >>> ll.count(1)
        2
        >>> ll.count("he")
        0
        """
        total_count = 0
        if isinstance(value, self._basic_node):
            value = value.get_data()
        for curr_val in self:
            if curr_val == value:
                total_count += 1
        return total_count


    def copy(self):
        """
        Copies the `LinkedList()` instance in a shallow-manner.

        Returns
        -------
        `LinkedList()`:
            The shallow copy of the original instance.
        
        Example
        ------
        >>> ll = LinkedList()
        >>> ll.add_end(10)
        >>> ll.add_end(20)
        >>> ll.copy()
        ┌────┐ ┌────┐ 
        │ 10 │⟶│ 20 │⟶
        └────┘ └────┘ 
        """
        copied_list = self._create_instance()
        if not self.is_empty():
            copied_node = None
            for val in self:
                copied_node = copied_list._insert_value(copied_node, val)
        return copied_list


