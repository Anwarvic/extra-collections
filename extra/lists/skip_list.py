"""
A skip list is an awesome linear data structures which consists of a series of
**Linked List** objects, each linked list stores a subset of items sorted by
increasing values plus one setntinel value denoted by -∞ which is smaller than
every possible value that can be inserted. The really interesting part about
skip list is that it supports searching for values in time-complexity of
O(log(n)) which is considered faster than most linear data structures.

The following is a simple skip list containing the first seven number from the 
Fibbonacci series which are: [0, 1, 1, 2, 3, 5, 8]

┌────┐ ┌───┐                         ┌───┐ 
| -∞ │⟶| 0 │⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶| 8 │⟶
├────┤ ├───┤ ┌───┐                   ├───┤ 
| -∞ │⟶| 0 │⟶| 1 │⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶| 8 │⟶
├────┤ ├───┤ ├───┤ ┌───┐ ┌───┐ ┌───┐ ├───┤ 
| -∞ │⟶| 0 │⟶| 1 │⟶| 2 │⟶| 3 │⟶| 5 │⟶| 8 │⟶
└────┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ 

In the above skip list, you can see the following properties:

- The skip list consists of multiple levels or Linked List objects. The number \
    of levels is called "**height**". So, the height of this skip list is `3`.
- The first number in the skip list is our -∞ setntinel value.
- All values are numbers and they are sorted in ascending-manner.
- There are no repeated values.
- There are some numbers that are stored once and there are some numbers that \
    are stored multiple time.

Intuitively, the lists are set up so that the lower linked lists contain more
items of the higher ones. Inserting an item in more than one linked list is 
chosen randomly with probability 1/2. That is, like, we "**flip a coin**"
for each item in the skip list. Thus, we expect the lowest linked list, at
`height=0` to have **n** items. And the linked list at `height=2` to have about
**n/2** items, and the one above it to have about **n/4** items. In other words,
we expect the height of the skip list to be about **log(n)**.

Note
----
The -∞ setntinel value is put in the SkipList() as a convention. So, it doesn't
count as an element in the SkipList(). In other words, the zeroths element in 
the above skip list is `0` not `-∞`.

"""
import random
from extra.interface import Extra
from extra.lists.linked_list import Node, LinkedList




#helper functions
random.seed(1)
def flip_coin():
    """
    A helper function to mimic the action of flipping a coin. The result is
    totally random,

    Returns
    -------
    str:
        Either "head" or "tail".
    
    Example
    -------
    >>> flip_coin()
    'tail'
    >>> flip_coin()
    'head'
    >>> flip_coin()
    'head'
    """
    return random.choice(['head','tail'])


def search_sorted(prev_node, start_node, value):
    """
    A helper function to search the SkipList() instance starting from a certain
    node and searching for a certain value.

    Parameters
    ----------
    prev_node: SkipNode()
        A reference to the node that is previous to the `start_node`.
    start_node: SkipNode()
        A reference to the node at which the searching starts.
    value: int or float
        The number for which we started searching.
    
    Returns
    -------
    SkipNode()
        A reference to the node previus to the node containing the value if the
        value was found. If the value wasn't found, then this will be either 
        `None` or the second last node in the skiplist.
    SkipNode()
        A reference to the node containg the value if the value was found. If 
        the value wasn't found, then this will be the last node in the skiplist.
    """
    # search a sorted linked list and return the last accessed node.
    curr_node = start_node
    next_node = curr_node.get_next()
    while(next_node is not None and next_node.get_data() <= value):
        prev_node = curr_node
        curr_node = next_node
        next_node = curr_node.get_next()
    return prev_node, curr_node




class SkipNode(Node):
    """Basic object for the Node used for skip lists"""
    __name__ = "extra.SkipNode()"
    

    def __init__(self, item):
        """
        Creates a `SkipNode()` object used mainly with SkipList() objects!!

        Parameters
        ----------
        item: object 
            The value to be saved within the `SkipNode()` instance

        Raises
        ------
        ValueError: If the given item is `None`.
        TypeError: If the given item isn't a number.
        """
        super()._validate_item(item)
        if type(item) not in {int, float}:
            raise TypeError(f"`{self.__name__}` contains numbers only!!")
        super().__init__(item)
        self._down = None
    

    def __repr__(self):
        """
        Represents `SkipNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `SkipNode()` instance.
        
        Example
        -------
        >>> x = SkipNode(10)
        >>> x
        >>> SkipNode(data: 10, next:None)
        """
        if self._data == float("-inf"):
            data = "-∞"
        elif self._data == float("inf"):
            data = "∞"
        else:
            data = self._data
        nxt = self._next.get_data() if self._next is not None else None
        return f"SkipNode(data: {data}, next: {nxt})"


    def get_down(self):
        """
        Returns the down `SkipNode()` instance of the current one.

        Returns
        -------
        Node():
            The `SkipNode()` instance that is below the current `SkipNode()`
            or `None` if there weren't any.
        """
        return self._down
    

    def set_down(self, other_node):
        """
        Sets the down pointer of the current `SkipNode()` to the given node.

        Parameters
        ----------
        other_node: SkipNode()
            The `SkipNode()` that will follow the current `SkipNode()`.

        Raises
        ------
        TypeError: If the given item is not an `SkipNode()` object.
        """
        if not isinstance(other_node, SkipNode):
            raise TypeError(f"Given object has to be `{self.__name__}`!!")
        self._down = other_node


    def _represent(self):
        """
        A helpful function used to represent the SkipNode() when printing!!
        
        Returns
        -------
        str:
            A string representing the SkipNode() is a very simple way.
        
        Example
        -------
        >>> x = SkipNode(10)
        >>> x
        SkipNode(data:10, next:None)
        >>> x._represent()
        10
        >>> type(x._represent())
        <class 'str'>
        """
        if self._data == float("-inf"):
            return "-∞"
        elif self._data == float("inf"):
            return "∞"
        return super()._represent()




class SkipList(Extra):
    """Basic object for the skip list"""
    _basic_node = SkipNode
    __name__ = "extra.SkipList()"
    
    
    def __init__(self):
        """
        Creates a SkipList() object!!
        
        Example
        -------
        >>> ll = SkipList()
        >>> type(ll)
        <class 'extra.lists.skip_list.SkipList'>
        """
        #`level_lists` is an array of LinkedList() objects
        ll = LinkedList()
        ll._insert_node(ll._head, self._basic_node(float("-inf")))
        self._level_lists = [ll]
        self._num_levels = 1
    

    @classmethod
    def from_iterable(cls, iterable):
        """
        A class method which creates a SkipList() instance using an iterable
        in time-complexity of O(n) where **n** is the number of elements inside
        the given `iterable`.

        Parameters
        ----------
        iterable: any iterable object.
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
        
        Returns
        -------
        SkipList()
            It returns a SkipList() instance with the same values in the same
            order.
        
        Raises
        ------
        TypeError: It can be raised in two cases
            1. In case the given object isn't iterable.
            2. If one of the elements in the iterable is an `Extra` object.
            3. If one of the elements in the iterable isnot a number.

        ValueError: If one of the iterable elements is `None`.

        Examples
        --------
        >>> sl = SkipList.from_iterable([10, -5, 7, 9])
        >>> sl
        ┌────┐                    ┌────┐ 
        | -∞ │⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶| 10 │⟶
        ├────┤ ┌────┐             ├────┤ 
        | -∞ │⟶| -5 │⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶| 10 │⟶
        ├────┤ ├────┤ ┌───┐ ┌───┐ ├────┤ 
        | -∞ │⟶| -5 │⟶| 7 │⟶| 9 │⟶| 10 │⟶
        └────┘ └────┘ └───┘ └───┘ └────┘ 

        Using an iterable object with `None` as one of its elements will raise
        `ValueError`

        >>> sl = SkipList.from_iterable([2, None])
        ValueError: Can't use `None` as an element within `extra.SkipList()`!!
        
        Using a non-iterable object will raise `TypeError`

        >>> sl = SkipList.from_iterable(2)
        TypeError: The given object isn't iterable!!
        
        Using nested `SkipList` objects will raise `TypeError` as well

        >>> sl_1 = SkipList.from_iterable([1])
        >>> sl_2 = SkipList.from_iterable([1, sl_1])
        TypeError: Can't create `extra.SkipList()` using `extra.SkipList()`!!

        Note
        -----
        Inserting values into different levels in the skip list is completely
        random. So, running the previous example will return different values
        each time you run it. So, in order to obtain the same result as before
        you need to set `random.seed(1)` before running any of the previous 
        example.
        """
        if not hasattr(iterable, "__iter__"):
            raise TypeError("The given object isn't iterable!!")
        elif isinstance(iterable, cls):
            return iterable
        else:
            skiplist = cls()  #cls._create_instance(cls)
            for item in iterable:
                skiplist.insert(item)
            return skiplist
        

    ##############################     PRINT      ##############################
    def __print_node(self, node, zeroth_node, lower_node):
        """
        Prints the given node of the SkipList() instance.

        Parameters
        ----------
        node: SkipNode()
            The SkipNode() to be printed.
        zeroth_node: SkipNode()
            The SkipNode() of the lowest LinkedList (zeorth level) attached to
            the given `node`.
        lower_node: SkipNode()
            The SkipNode() which is directly below the `node`.

        Returns
        -------
        tuple
            It returns a tuple of two lists representing the given middle-part
            and lower-part of the node when printed knowing that each node will
            be printed in three lines in total.
        
        Raises
        ------
        AssertionError: This can be raised in the following cases:
            1. The `node` is not neither `None` nor an instance of SkipNode()
            2. The `zeroth_node` is not neither `None` nor an instance of \
                SkipNode()
            3. The `lower_node` is not neither `None` nor an instance of \
                SkipNode()
        """
        assert node is None or isinstance(node, self._basic_node)
        assert zeroth_node is None or isinstance(zeroth_node, self._basic_node)
        assert lower_node is None or isinstance(lower_node, self._basic_node)
        middle = []
        bottom_border = []
        item = zeroth_node._represent()
        width = len(item)+2 #2: for a space before & after an item
        if node is not None and zeroth_node.get_data() == node.get_data():
            bottom_border += ['└'] if lower_node is None else ['├']
            bottom_border += (['─']*width)
            bottom_border += ['┘ '] if lower_node is None else ['┤ ']
            middle += [f"| {item} │⟶"]
        else:
            middle += [f"⟶{'⟶'*width}⟶⟶"]
            if lower_node is not None and \
                        lower_node.get_data() == zeroth_node.get_data():
                bottom_border += ['┌'] + (['─']*width) + ['┐ ']
            else:
                bottom_border += [' '] + ([' ']*width) + ['  ']
        return middle, bottom_border


    def __print_level(self, level):
        """
        Prints each level in the SkipList() instance.
        
        Parameters
        ----------
        level: int
            A positive zero-indexed integer representing the level rank. The
            lowest level of the SkipList() is zero.
        
        Returns
        -------
        str: 
            A string representing a whole level in the SkipList() knowing that 
            each level should be printed in three lines. This method returns the
            lower & middle line.
        
        Raises
        ------
        AssertionError: In the following cases:
            1. If the type of the given level isn't a level.
            2. If the level index is bigger than the SkipList() height.
        """
        assert type(level) == int
        assert level < self._num_levels

        zeroth_list = self._level_lists[0]
        curr_list = self._level_lists[level]
        # the following two lists will represent the output of this function
        bottom_border = []
        middle = []
        # iterate over two lists in parallel
        zeroth_node = zeroth_list._head
        curr_node = curr_list._head
        lower_node = self._level_lists[level-1]._head if level > 0 else None
        while(zeroth_node is not None):
            middle_part, bottom_part = \
                self.__print_node(curr_node, zeroth_node, lower_node)
            middle += middle_part
            bottom_border += bottom_part
            if curr_node is not None and \
                        zeroth_node.get_data() == curr_node.get_data():
                curr_node = curr_node.get_next()
            if lower_node is not None and \
                        zeroth_node.get_data() == lower_node.get_data():
                lower_node = lower_node.get_next()
            zeroth_node = zeroth_node.get_next()
        return "{}\n{}".format(''.join(middle), ''.join(bottom_border))


    def __print_top_border(self):
        """
        Prints out the top border of the Skip List.

        Returns:
        str:
            A one-line string representing the top-border of the SkipList()
        """
        lower_list = self._level_lists[0]
        top_list = self._level_lists[self._num_levels-1]
        # the following two lists will represent the output of this function
        top_border = []
        # iterate over two lists in parallel
        lower_node = lower_list._head
        curr_node = top_list._head
        while(lower_node != None):
            item = lower_node._represent()
            width = len(item)+2 #2: for a space before & after an item
            if curr_node is not None and \
                        lower_node.get_data() == curr_node.get_data():
                top_border += ['┌'] + (['─']*width) + ['┐ ']
                curr_node = curr_node.get_next()
            else:
                top_border += [' '] + ([' ']*width) + ['  ']
            lower_node = lower_node.get_next()
        return "{}".format(''.join(top_border))


    def __repr__(self):
        """
        Represents the linked list as a string. The time-complexity of this
        method is O(n*h) where **n** is the number of nodes in the SkipList()
        and **h** is the height of the SkipList().
        
        Returns
        -------
        str:
            The string-representation of the `SkipList()` instance.

        Example
        -------
        >>> random.seed(1)
        >>> sl = SkipList.from_iterable([20, 77, 10, 6, 2])
        >>> sl
        ┌────┐                    ┌────┐        
        | -∞ │⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶| 20 │⟶⟶⟶⟶⟶⟶⟶⟶
        ├────┤                    ├────┤ ┌────┐ 
        | -∞ │⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶| 20 │⟶| 77 │⟶
        ├────┤ ┌───┐ ┌───┐ ┌────┐ ├────┤ ├────┤ 
        | -∞ │⟶| 2 │⟶| 6 │⟶| 10 │⟶| 20 │⟶| 77 │⟶
        └────┘ └───┘ └───┘ └────┘ └────┘ └────┘ 
        """
        output = [self.__print_top_border()]
        output += [self.__print_level(level) \
                    for level in range(self._num_levels-1, -1, -1)]
        return "\n".join(output)
    

    ##############################     LENGTH     ##############################    
    def __len__(self):
        """
        Gets the length of the SkipList() in time-complexity of O(1).
        
        Returns
        -------
        int:
            The length of the SkipList() instance. By Length, I mean the
            number of nodes of in the instance.
        
        Examples
        --------
        >>> sl = SkipList()
        >>> len(sl)
        0
        >>> sl = SkipList.from_iterable((2, 5, 0))
        >>> len(sl)
        3
        """
        n = len(self._level_lists[0])
        return  n-1 if n > 0 else 0
    

    def is_empty(self):
        """
        Checks if SkipList() instance is empty or not in time-complexity of
        O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the SkipList() instance is empty or
            not. `True` shows that this instance is empty and `False` shows
            it's not empty.
        
        Example
        --------
        >>> ll = SkipList()
        >>> ll.is_empty()
        True
        >>> ll.insert(5)
        >>> ll.is_empty()
        False
        """
        return len(self) == 0


    ##############################     HEIGHT     ##############################
    def get_height(self):
        """
        Gets the height of the SkipNode() instance. SkipNode() height is the 
        number of levels where each level is a LinkedList() object.

        Returns
        -------
        int:
            A positive integer representing the height of the instance.
        
        Example
        -------
        >>> random.seed(1)
        >>> sl = SkipList.from_iterable([20, 77, 10, 6, 2])
        >>> sl.get_height()
        3
        """
        return self._num_levels


    ##############################    ITERATOR    ##############################
    def __iter__(self):
        """
        Iterates over the SkipList() instance and returns a generator in 
        time-complexity of O(n) where **n** is the number of elements in the 
        SkipList() instance.

        Returns
        -------
        generator:
            The value of each node in the instance.
        
        Examples
        --------
        >>> sl = SkipList.from_iterable([3, 1, 2])
        >>> for item in sl:
        ...     print(item)
        1
        2
        3
        """
        for item in self._level_lists[0][1:]:
            yield item

    
    ##############################     SEARCH     ##############################
    def _validate_item(self, item):
        """
        Checks the validity of the given item. It raises the appropriate error
        when the item isn't valid and it returns nothing if the item is valid.

        Parameters
        ----------
        item: object
        
        Raises
        ------
        ValueError: If the given item is `None`.
        TypeError: If the given item is not a number.
        """
        super()._validate_item(item)
        if type(item) not in {int, float}:
            raise TypeError(f"`{self.__name__}` supports only numbers!!")
        

    def _validate_index(self, idx, accept_negative=False, accept_slice=False):
        """
        Checks the validity of the given index. It raises the appropriate error
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
            2. If the given index is out of the SkipList() boundaries.
            3. If the given index is negative while `accept_negative` flag is \
                `False`.
        
        Examples
        --------
        >>> sl = SkipList.from_iterable([1, 2, 3])
        >>> sl._validate_index('1')
        TypeError: Given index must be an integer!!
        >>> sl._validate_index(-2)
        IndexError: Negative indexing isn't supported with this functinoality!!
        >>> sl._validate_index(slice(0, 2))
        IndexError: Slice indexing isn't supported with this functinoality!!
        
        And it would return nothing if the given index if valid:

        >>> sl._validate_index(2)
        >>> sl._validate_index(-2, accept_negative=True)
        >>> sl._validate_index(slice(0, 2), accept_slice=True)
        """
        if isinstance(idx, slice):
            if not accept_slice:
                raise IndexError(
                    "Slice indexing isn't supported with this functinoality!!"
                )
        if type(idx) != int:
            raise TypeError("Given index must be an integer!")
        elif idx <= -1 and accept_negative==False:
            raise IndexError(\
                "Negative indexing isn't supported with this functinoality!!")
        elif idx < - len(self) or idx >= len(self):
            raise IndexError("Can't find any element at the given index!!")


    def _search(self, value):
        """
        Searches the SkipList() for a given value and returns the first node
        containing that value if found and some other necessary info. If not
        found, it returns the node whose value is less that the given value and
        yet bigger than other values.

        Parameters
        ----------
        value: int or float
            The value to be searched for in the SkipList() instance.
        
        Returns
        -------
        SkipNode():
            If the value is found, this object represents the previous node to
            the found node. If the value isn't found, this object represents
            the previous node to the last accessed node.
        SkipNode():
            If the value is found, this object is the found node. If the value
            is not found, this object is the last accessed node.
        list:
            A list of all accessed SkipNode() objects sorted in descending
            manner.
        
        Raises:
        -------
        AssertionError: If the given value isn't a number

        Examples
        --------
        >>> sl = SkipList.from_iterable([10, -2, 3])
        >>> sl
        ┌────┐              ┌────┐ 
        | -∞ │⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶| 10 │⟶
        ├────┤ ┌────┐       ├────┤ 
        | -∞ │⟶| -2 │⟶⟶⟶⟶⟶⟶⟶| 10 │⟶
        ├────┤ ├────┤ ┌───┐ ├────┤ 
        | -∞ │⟶| -2 │⟶| 3 │⟶| 10 │⟶
        └────┘ └────┘ └───┘ └────┘ 
        >>> prev_node, node, last_accessed_nodes = sl._search(3)
        >>> prev_node
        SkipNode(data: -2, next: 3)
        >>> node
        Node(data: 2, next: None)
        >>> last_accessed_nodes
        [SkipNode(data: -2, next: 10), SkipNode(data: -∞, next: 10)]
        """
        # returns the last accessed node when searching a certain value.
        assert type(value) in {int, float}

        last_accessed_nodes = []
        top_list = self._level_lists[self._num_levels-1]
        prev_node = None
        start_node = top_list._head
        while(start_node.get_down() != None):
            prev_node, found_node = search_sorted(prev_node, start_node, value)
            if found_node.get_data() == value:
                return prev_node, found_node, last_accessed_nodes
            last_accessed_nodes.append(found_node)
            start_node = found_node.get_down()
            if prev_node is not None: prev_node = prev_node.get_down() 
        prev_node, found_node = search_sorted(prev_node, start_node, value)
        assert len(last_accessed_nodes) == self._num_levels-1
        return prev_node, found_node, last_accessed_nodes[::-1]


    def __contains__(self, value):
        """
        Checks if the given value exists in the SkipList() instance in time-
        complexity of O(log(n)) where **n** is the total number of elements in
        the SkipList() instance.

        Parameters
        ----------
        value: Object
            The value to be searched for in the SkipList() instance.
        
        Returns
        -------
        bool
            `True` if the given value exists in the SkipList() instance, and
            `False` otherwise.

        Raises
        ------
        ValueError: If the given item is `None`.
        
        Examples
        --------
        >>> sl = SkipList.from_iterable([1, 3, 5])
        >>> 1 in sl
        True
        >>> 0 in sl
        False
        >>> "hello" in sl
        False
        """
        if type(value) not in {int, float}:
            return False
        self._validate_item(value)
        _, found_node, _ = self._search(value)
        return found_node.get_data() == value
    

    def __getitem__(self, idx):
        """
        Retrieves the element at the given index in time-complexity of O(k)
        where **k** is the given index. The given index is a zero-based `int`.
        This method doesn't support negative indexing and doesn't support
        `slice` objects either. 

        Parameters
        ----------
        idx: int
            The index (multiple indices) to be used to retrieve values from the
            LinkedList() instance.
        
        Returns
        -------
        int or float:
            The value at this index inside the SkipList() instance.
        
        Raises
        ------
        TypeError: If the given index isn't `int`.
        IndexError: This happens in one of the following cases: 
            1. If the given index is negative.
            2. if the given index is a `slice` object.
            3. If the given index is out of the SkipList() boundaries.

        Examples
        --------
        >>> sl = SkipList.from_iterable([4, 3, 1, 5, 2])
        >>> sl[0]
        1
        >>> sl[4]
        5
        >>> sl[10]
        IndexError: Can't find any element at the given index!!
        >>> sl[-2]
        IndexError: Negative indexing isn't supported with this functinoality!!
        >>> sl[2:]
        IndexError: Slice indexing isn't supported with this functinoality!!

        Note
        ----
        The -∞ setntinel value is put in the SkipList() as a convention. So, it
        doesn't count as an element in the SkipList(). In other words, the
        zeroths element in the above skip list is `0` not `-∞`.
        """
        self._validate_index(idx)
        #NOTE: idx+1 to skip -∞
        node = self._level_lists[0].__getitem__(idx+1)
        return node


    ##############################     INSERT     ##############################
    def _add_extra_level(self):
        """
        Creates a new level at the top of the SkipList(), a new level is a new
        LinkedList() instance attached to the SkipList().

        Returns
        -------
        LinkedList():
            The newly-created LinkedList() instance after being attached to the
            other LinkedList() object in the lower level.
        """
        top_list = self._level_lists[self._num_levels-1]
        new_llist = LinkedList()
        new_llist._insert_node(new_llist._head, self._basic_node(float("-inf")))
        # connect the head of the new linked list to the lower linked list
        new_llist._head.set_down(top_list._head)
        # add new linked list to the SkipList
        self._level_lists.append(new_llist)
        self._num_levels += 1
        return new_llist
    
    
    def _promote(self, upper_prev_node, curr_node, curr_level):
        """
        Promotes a node to the higher level. Promoting is done by copying the
        node from (x)th level to the (x+1)th level.

        Parameters
        ----------
        upper_prev_node: SkipNode()
            The tail of the LinkedList() object in the above level.
        curr_node: SkipNode()
            The node to be promoted.
        curr_level: int
            The current level rank (level of the node before promoting).
        
        Returns
        -------
        SkipNode():
            The SkipNode() object after being promoted in the higher level.
        """
        assert isinstance(upper_prev_node, self._basic_node)
        assert isinstance(curr_node, self._basic_node)
        assert curr_level < self._num_levels

        # create new node with the same data as curr_data
        upper_node = self._basic_node(curr_node.get_data())
        # connect the upper list to the new node
        upper_node = self._level_lists[curr_level+1]._insert_node(
                                                    upper_prev_node, upper_node)
        # connect the current list with the upper one
        upper_node.set_down(curr_node)
        return upper_node


    def insert(self, value):
        """
        Insertd a value to the SkipList() instance in time-complexity of
        O(log(n)) where **n** is the number of elements in the SkipList().

        Parameters
        ----------
        value: int or float
            The number to be inserted in the SkipList() instance.
        
        Raises
        ------
        TypeError: If the given `value` isn't a number.

        Example
        -------
        >>> random.seed(1)
        >>> sl = SkipList.from_iterable([2, 1, 3])
        >>> sl.insert(10)
        >>> sl
        ┌────┐                   ┌───┐       ┌────┐ 
        | -∞ │⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶| 4 │⟶⟶⟶⟶⟶⟶⟶| 10 │⟶
        ├────┤             ┌───┐ ├───┤       ├────┤ 
        | -∞ │⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶| 3 │⟶| 4 │⟶⟶⟶⟶⟶⟶⟶| 10 │⟶
        ├────┤ ┌───┐ ┌───┐ ├───┤ ├───┤ ┌───┐ ├────┤ 
        | -∞ │⟶| 1 │⟶| 2 │⟶| 3 │⟶| 4 │⟶| 5 │⟶| 10 │⟶
        └────┘ └───┘ └───┘ └───┘ └───┘ └───┘ └────┘ 
        >>> ll.insert("10")
        TypeError: `extra.SkipList()` supports only numbers!!

        Note
        -----
        Inserting values into different levels in the skip list is completely
        random. So, running the previous example will return different values
        each time you run it. So, in order to obtain the same result as before
        you need to set `random.seed(1)` before running any of the previous 
        example.
        """
        self._validate_item(value)
        # search for that value
        _, found_node, last_accessed_nodes = self._search(value)
        # `value` already exists in our SkipList
        if found_node.get_data() == value:
            return
        # create new_node with the new value
        new_node = self._basic_node(value)
        # insert new_node to the 0th linkedlist
        curr_node = self._level_lists[0]._insert_node(found_node, new_node) 
        
        # promote the new_node if flipping the coin results `Head`
        curr_level = 0
        while flip_coin() == "head":
            if curr_level >= self._num_levels-1:
                top_list = self._add_extra_level()
                upper_prev_node = top_list._head
            else:
                upper_prev_node = last_accessed_nodes[curr_level]
            # promote new_node
            curr_node = self._promote(upper_prev_node, curr_node, curr_level)
            curr_level += 1

    
    ##############################     REMOVE     ##############################
    def _remove_level(self, level):
        """
        Removes a level from the SkipList() instance. We need to do so when 
        deleting a value from the SkipList() instance which results in a a
        whole level being empty, so we will need to get rid of this level.

        Parameters
        ----------
        level: int
            The level rank which we want to remove.
        
        Raises
        ------
        AssertionError: This can happen in two cases:
            1. If the type of the given `level` isn't `int`.
            2. If the level is less than 1 and greater than the total number \
                of levels.
        """
        assert type(level) == int and 1 <= level < self._num_levels
        
        del self._level_lists[level]
        self._num_levels -= 1
    

    def remove(self, value):
        """
        Removes node whose value equal to the given value.

        Parameters
        ----------
        value: int or float
            The value to be removed from the SkipList() instance.
               
        Example
        -------
        >>> random.seed(1)
        >>> sl = SkipList.from_iterable([4, 3, 1, 5])
        >>> sl
        ┌────┐             ┌───┐       
        | -∞ │⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶⟶| 4 │⟶⟶⟶⟶⟶⟶⟶
        ├────┤       ┌───┐ ├───┤       
        | -∞ │⟶⟶⟶⟶⟶⟶⟶| 3 │⟶| 4 │⟶⟶⟶⟶⟶⟶⟶
        ├────┤ ┌───┐ ├───┤ ├───┤ ┌───┐ 
        | -∞ │⟶| 1 │⟶| 3 │⟶| 4 │⟶| 5 │⟶
        └────┘ └───┘ └───┘ └───┘ └───┘ 
        >>> sl.remove(10) #does nothing
        >>> sl.remove(4)
        >>> sl
        ┌────┐       ┌───┐       
        | -∞ │⟶⟶⟶⟶⟶⟶⟶| 3 │⟶⟶⟶⟶⟶⟶⟶
        ├────┤ ┌───┐ ├───┤ ┌───┐ 
        | -∞ │⟶| 1 │⟶| 3 │⟶| 5 │⟶
        └────┘ └───┘ └───┘ └───┘ 

        Note
        ----
        In the previuos example, the top level was deleted when we removed `4` 
        since it was empty after removal.
        """
        if type(value) not in {int, float}:
            return
        # search for that value
        prev_node, found_node, last_accessed_nodes = self._search(value)
        #NOTE: len(last_accessed_nodes) can be used to get the level where
        #  this value was found
        if found_node.get_data() == value:
            level = self._num_levels - 1 - len(last_accessed_nodes)
            while(level >= 0):
                curr_level_list = self._level_lists[level]
                curr_level_list._remove_node(prev_node, found_node)
                # check if curr_level_list is empty()
                if level != 0 and len(curr_level_list) == 1:
                    self._remove_level(level)
                level -= 1
                found_node = found_node.get_down()
                # update value of prev_node
                if prev_node is not None and found_node is not None:
                    prev_node = prev_node.get_down()
                    next_node = prev_node.get_next()
                    while(next_node.get_data() != found_node.get_data()):
                        prev_node = next_node
                        next_node = prev_node.get_next()


    def __delitem__(self, idx):
        self._validate_index(idx)
        #NOTE: idx+1 to skip -∞
        _, node = self._level_lists[0]._get_node(idx+1)
        self.remove(node.get_data())
    

    def clear(self):
        self.__init__()
    

    ##############################      MISC      ##############################
    def to_list(self):
        return [item for item in self]


