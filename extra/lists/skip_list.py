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


    def _validate_item(self, item):
        super()._validate_item(item)
        if type(item) not in {int, float}:
            raise TypeError(f"`{self.__name__}` supports only numbers!!")
        

    def _validate_index(self, idx, accept_negative=False):
        if isinstance(idx, slice):
            raise NotImplementedError("Slices isn't supported yet!!")
        if type(idx) != int:
            raise TypeError("Given index must be an integer!")
        elif idx <= -1 and accept_negative==False:
            raise IndexError(\
                "Negative indexing isn't supported with this functinoality!!")
        elif idx < - len(self) or idx >= len(self):
            raise IndexError("Can't find any element at the given index!!")


    @classmethod
    def from_iterable(cls, iterable):
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
        This private method is responsible for representing each node in the 
        Skip List. To do its job, it needs to use two other nodes:
        - zeroth_node: node of the 0th level of the Skip List where all nodes
            are represented.
        - lower_node: node of the lower level.
        """
        middle = []
        bottom_border = []
        item = zeroth_node._represent()
        width = len(item)+2 #2: for a space before & after an item
        if node != None and zeroth_node.get_data() == node.get_data():
            bottom_border += ['└'] if lower_node == None else ['├']
            bottom_border += (['─']*width)
            bottom_border += ['┘ '] if lower_node == None else ['┤ ']
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
        This private method is responsible for representing each level in the 
        Skip List.
        NOTE: I know this isn't the best way to do it, but that's what popped up
        first into my mind.
        """
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
        This method is only responsible for just one thing, to print out the 
        top border of the Skip List.
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
        The complexity of this method is O(n*l) where:
            - n: is the number of nodes in the first list
            - l: is the number of levels
        Skip List is gonna look like this:
        ┌────┐                     ┌───┐
        │ -∞ │⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷│ 2 │⟷
        ├────┤        ┌────┐       ├───┤
        │ -∞ │⟷⟷⟷⟷⟷⟷⟷⟷│ 10 │⟷⟷⟷⟷⟷⟷⟷│ 2 │⟷
        ├────┤ ┌────┐ ├────┤ ┌───┐ ├───┤
        │ -∞ │⟷│ 77 │⟷│ 10 │⟷│ 6 │⟷│ 2 │⟷
        └────┘ └────┘ └────┘ └───┘ └───┘
        """
        output = [self.__print_top_border()]
        output += [self.__print_level(level) \
                    for level in range(self._num_levels-1, -1, -1)]
        return "\n".join(output)
    

    ##############################     LENGTH     ##############################    
    def __len__(self):
        return len(self._level_lists[0]) - 1
    

    def is_empty(self):
        return len(self) == 0

    ##############################     HEIGHT     ##############################
    def get_height(self):
        return self._num_levels

    ##############################    ITERATOR    ##############################
    def __iter__(self):
        for item in self._level_lists[0][1:]:
            yield item

    
    ##############################     SEARCH     ##############################
    def _search(self, value):
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


    def search(self, value):
        """Search Skip List is one in O(log(n)) time"""
        if type(value) not in {int, float}:
            return False
        self._validate_item(value)
        _, found_node, _ = self._search(value)
        return found_node.get_data() == value


    def __contains__(self, value):
        return self.search(value)
    

    def __getitem__(self, idx):
        self._validate_index(idx)
        #NOTE: idx+1 to skip -∞
        node = self._level_lists[0].__getitem__(idx+1)
        return node.get_data()


    ##############################     INSERT     ##############################
    def _add_extra_level(self):
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
        Inserts a value to our Skip List. Insertion is done in O(log(n)) time
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
        assert type(level) == int and 1 <= level < self._num_levels
        del self._level_lists[level]
        self._num_levels -= 1
    

    def remove(self, value):
        """removal is done in O(log(n))"""
        if type(value) not in {int, float}:
            return
        self._validate_item(value)
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


