"""
A treap is a binary tree that stores a collection of nodes. Each node in the
treap contains two main values:

- **data**: The numeric value inserted to the treap.
- **priority**: A numeric value that indicates how important this node is. 
    The bigger this numeric value is, the higher its priority in the treap
    becomes.

Each node in the treap must satisfy two additional properties:

1. **BST Property**: It is a relational property defined in terms of the numeric
value stored at the node. So, for every node, the numeric value stored at the
is greater than all the numeric values found in the left subtree and less than
those found in the node's right subtree. In other words, we can consider the 
treap as a BST (Binary Search Tree) with respect to the values insterted.

2. **Max Heap Property**: It is a relational property defined in terms of the 
priority of the node. So, for every node, other than the root, the priority of
the node is less than or equal to the value stored at the node's parent. As a
consequence of this property, the priority encountered on a path from the root
to a leaf node are in nonincreasing order. Also, the maximum priority is always
stored at the root of the treap.

As we can see, we can consider the treap as both "Tree" and "Heap". Hence, the
name: "Treap".

Note
----
The priority values are always hidden. If you want to see the priorty for each
node in the `Treap()`, you can set the static variable `SHOW_PRIORITY` to
`True` just like so:

>>> Treap.SHOW_PRIORITY = True


[image]




"""
import random
import warnings
from extra.trees.bst import BSTNode, BST




class TreapNode(BSTNode):
    """
    A treap node is the basic unit for building Treap instances. A treap node
    must contain a number. Each treap node has either zero, one or two children
    treap nodes. The node that has no children is called a **leaf node**.
    """
    __name__ = "extra.TreapNode()"
    

    def __init__(self, data, priority=None):
        """
        Creates a `TreapNode()` object which is the basic unit for building 
        `Treap()` objects!!

        Parameters
        ----------
        data: int or float
            The value to be saved within the `TreapNode()` instance
        priority: int or float (default: None)
            A numeric value indicating the priority of the `TreapNode()`.
        
        Raises
        ------
        ValueError: If the given data is `None`.
        TypeError: It can be raised in the following two cases:
            1. If the given data isn't a number.
            2. If the given priority isn't a number.
        """
        if priority is not None and type(priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
        super().__init__(data)
        self._priority = \
            random.randint(0, 100) if priority is None else priority


    def get_priority(self):
        """
        Returns the priority of the current `TreapNode()` instance.

        Returns
        -------
        int or float:
            The priority of the current `TreapNode()`.
        """
        return self._priority


    def set_priority(self, new_priority):
        """
        Sets the given priority as the priority of the current `TreapNode()`.

        Parameters
        ----------
        new_priority: int or float
            The new priority of the current `TreapNode()`.

        Raises
        ------
        TypeError: If the given priority is not a number.
        """
        if type(new_priority) in {int, float}: 
            raise TypeError("Given priority has to be a number!!")
        self._priority = new_priority


    def __repr__(self):
        """
        Represents `TreapNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `TreapNode()` instance.
        
        Example
        -------
        >>> x = TreapNode(10, priority=0)
        >>> x
        >>> TreapNode(data: 10, priority: 0)
        """
        return f"TreapNode(data: {self._data}, Priority: {self._priority})"


    def _represent(self):
        """
        A helpful function used to represent the node when printing!!
        
        Returns
        -------
        str:
            A string representing the `TreapNode()` is a very simple way.
        
        Example
        -------
        >>> x = TreapNode(10, priority=2)
        >>> x
        TreapNode(data:10, priority:2)
        >>> x._represent()
        10
        >>> type(x._represent())
        <class 'str'>

        And if we set the `SHOW_PRIORITY` static variable to `True`, it will 
        look like this:
        
        >>> Treap.SHOW_PRIORITY = True
        >>> x._represent()
        10|P:2
        """
        if Treap.SHOW_PRIORITY:
            return f"{self._data}|P:{self._priority}"
        else:
            return f"{self._data}"




class Treap(BST):
    """
    A Treap is a binary tree that stores a collection of nodes. Each node in the
    treap contains two main values: "data" and "priority" and must satisfy two
    additional properties: 
    
    1. node's data must follow the rules of binary search tree.
    2. node's priority must follow the rules of max heap where the node with the
    heighest priority must always be at the root without breaking the rules of
    BST.
    """
    SHOW_PRIORITY = False
    _basic_node = TreapNode
    __name__ = "extra.Treap()"
    

    def __init__(self, seed=None):
        """
        Creates an empty `Treap()` object!!

        Parameters
        ----------
        seed: int or float (default: None)
            A seed to generate consistent random numbers.
        
        Example
        -------
        >>> treap = Treap()
        >>> type(treap)
        <class 'extra.trees.treap.Treap'>
        """
        random.seed(seed)
        super().__init__()

    
    @classmethod
    def from_iterable(cls, iterable, seed=None):
        """
        A class method which creates a `Treap()` instance using an iterable
        in time-complexity of O(n) where **n** is the number of elements inside
        the given `iterable`.

        Parameters
        ----------
        iterable: iterable
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
        seed: int or float (default: None)
            A seed to generate consistent random numbers.
        
        Returns
        -------
        Treap()
            It returns a `Treap()` instance with input values being inserted.
        
        Raises
        ------
        TypeError: It can be raised in three cases
            1. In case the given object isn't iterable.
            2. If one of the elements in the iterable is an `Extra` object.
            3. If one of the elements in the iterable is NOT a number.

        ValueError: If one of the iterable elements is `None`.

        Examples
        --------
        >>> treap = Treap.from_iterable([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0

        Without setting the seed, each time we run the code, we will get a
        different structure.

        >>> treap = Treap.from_iterable([0, 2, 1, 4, 9, 7, 3])
        >>> treap
            ____4
           /     \\
          1__     7
         /   \\    \\
        0     3     9
             /
            2
        >>> treap = Treap.from_iterable([0, 2, 1, 4, 9, 7, 3])
        >>> treap
              ____7
             /     \\
            2__     9
           /   \\
          1     4
         /     /
        0     3


        Using an iterable object with `None` as one of its elements will raise
        `ValueError`

        >>> Treap.from_iterable([2, None])
        ValueError: Can't use `None` as an element within `extra.Treap()`!!
        
        Using a non-iterable object will raise `TypeError`

        >>> Treap.from_iterable(2)
        TypeError: The given object isn't iterable!!
        
        Using nested `Treap()` objects will raise `TypeError` as well

        >>> treap_1 = Treap.from_iterable([1])
        >>> treap_2 = Treap.from_iterable([1, treap_1])
        TypeError: Can't create `extra.Treap()` using `extra.Treap()`!!
        """
        if not hasattr(iterable, "__iter__"):
            raise TypeError("The given object isn't iterable!!")
        if len(iterable) == 0:
            raise ValueError("The given iterable is empty!!")
        treap = cls(seed)
        for item in iterable:
            treap.insert(item)
        return treap


    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the `Treap()` instance in time-complexity of O(1).
        
        Returns
        -------
        int:
            The length of the `Treap()` instance. Length is the number of tree 
            nodes in the instance.
        
        Example
        -------
        >>> treap = Treap.from_iterable([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> len(treap)
        7
        """
        return self._length


    def is_empty(self):
        """
        Checks if the `Treap()` instance is empty or not in time-complexity of
        O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the `Treap()` instance is empty or not.
            `True` shows that this instance is empty and `False` shows it's
            not empty.
        
        Example
        --------
        >>> treap = Treap()
        >>> treap.is_empty()
        True
        >>> treap.insert(10)
        >>> treap.is_empty()
        False
        """
        return super().is_empty()
    
    
    ##############################     MAX/MIN    ##############################
    def get_max(self):
        """
        Gets the maximum value in the `Treap()` isntance. The maximum value can be
        found at the right-most tree node in the `Treap()` instance.

        Returns
        -------
        int or float:
            The maximum numeric value in the `Treap()` instance.
        
        Raises
        ------
        IndexError: In case the `Treap()` instance is empty.

        Example
        -------
        >>> treap = Treap.from_iterable([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.get_max()
        9
        """
        if self.is_empty():
            raise IndexError(\
                f"Can't get the maximum value of an empty `{self.__name__}`")
        max_node = self._get_max_node(self._root)
        return max_node.get_data()


    def get_min(self):
        """
        Gets the minimum value in the `Treap()` isntance. The minimum value can be
        found at the left-most tree node in the `Treap()` instance.

        Returns
        -------
        int or float:
            The minimum numeric value in the `Treap()` instance.
        
        Raises
        ------
        IndexError: In case the `Treap()` instance is empty.

        Example
        -------
        >>> treap = Treap.from_iterable([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.get_min()
        0
        """
        if self.is_empty():
            raise IndexError(\
                f"Can't get the minimum value of an empty `{self.__name__}`")
        min_node = self._get_min_node(self._root)
        return min_node.get_data()


    ##############################      SEARCH    ##############################
    def __contains__(self, find_val):
        """
        Searches the `Treap()` for the given value and returns `True` if the 
        value exists and `False` if not.

        Parameters
        ----------
        find_val: int or float
            The value to be searched for in the `Treap()` instance.
        
        Returns
        -------
        bool:
            Returns `True` if the value exists in the `Treap()` instance and
            `False` if not.
        
        Example
        -------
        >>> treap = Treap.from_iterable([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> 3 in treap
        True
        >> 50 in treap
        False
        """
        if self.is_empty() or type(find_val) not in {int, float}:
            return False
        found_node = self._search(find_val, self._root)
        return found_node.get_data() == find_val


    ##############################     INSERT     ##############################
    def __validate_priority(self, new_priority):
        """
        Makes sure the priority is a valid value. 
        
        Parameters
        ----------
        new_priority: int or flaot
            The priority's new value.
        
        Raises
        -------
        TypeError: If the given new priority is not a numeric value.
        """
        if new_priority is not None and type(new_priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
    

    def insert(self, value, priority=None):
        """
        Inserts a numeric value in the `Treap()` instance according to the rules
        of binary search trees and max heap.

        Parameters
        ----------
        value: int or float
            The new numeric value that will be inserted.
        priority: int or float (default: None)
            The priority of the newly inserted node.
        
        Raises
        ------
        ValueError: If the given `value` is `None`.
        TypeError: If either the given `value` or the given `priority` is not a
        numeric value.

        Example
        -------
        >>> treap = Treap()
        >>> treap.insert(10)
        >>> treap.insert(5)
        >>> treap.insert(15)
        >>> treap
          ___15
         /
        5
         \\
          10

        If we ran the same code again, we probably will get a different
        structure because the priority of the nodes are assigned randomly which
        changes the `Treap()` structure. Let's, now, set the priority of the 
        inserted node:

        >>> treap.insert(10, priority=10)
        >>> treap.insert(5, priority=2)
        >>> treap.insert(15, priority=7)
        >>> treap
          10
         /  \\
        5    15
        >>> Treap.SHOW_PRIORITY = True
            __10|P:10__
           /           \\
        5|P:2         15|P:7
        >>> treap.insert("2")
        TypeError: `extra.Treap()` accepts only numbers!!
        """
        # validate inserted value
        super()._validate_item(value)
        self.__validate_priority(priority)
        if self.is_empty():
            self._root = self._basic_node(value, priority)
            self._length += 1
        else:
            # perform standard BST-insert
            new_node = super()._insert_node(self._root,
                                self._basic_node(value, priority))
            # using rotations when necessary
            parent = new_node.get_parent()
            while(parent is not None):
                grandparent = parent.get_parent()
                if parent.get_priority() > new_node.get_priority():
                    break
                else:
                    if new_node.is_left_child():
                        parent = super()._rotate_right(parent)
                    else:
                        parent = super()._rotate_left(parent)
                    super()._attach(grandparent, parent)
                    new_node = parent
                    parent = grandparent


    ##############################     REMOVE     ##############################
    def remove(self, del_value):
        """
        Removes the `del_value` from the `Treap()` instance. 

        Parameters
        ----------
        del_value: int or float
            The value to be deleted from the `Treap()`.
        
        Raises
        ------
        UserWarning: If the `Treap()` instance is empty of if the value wasn't \
            found in the instance.
        
        Example
        -------
        >>> treap = Treap.from_iterable([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.remove(9)
        >>> treap.remove(0)
        >>> treap
            __4
           /   \\
          2     7
         / \\
        1   3
        >>> treap.remove(50)
        UserWarning: Couldn't find `50` in `extra.Treap()`!!
        """
        if self.is_empty():
            warnings.warn(f"`{self.__name__}` is empty!!", UserWarning)
            return
        elif type(del_value) not in {int, float}:
            warnings.warn(
                f"Couldn't find `{del_value}` in `{self.__name__}`!!",
                UserWarning
            )
            return
        # check if it's the only value
        elif self._root.is_leaf() and del_value == self._root.get_data():
            self._root = None
            self._length -= 1
        else:
            # search for the del_value node
            removed_node = super()._search(del_value, self._root)
            # couldn't find the node
            if removed_node.get_data() != del_value:
                return
            # rotate till removed_node is leaf
            parent = removed_node.get_parent()
            while(not removed_node.is_leaf()):
                # get children's priority
                left_child = removed_node.get_left()
                right_child = removed_node.get_right()
                left_priority = left_child.get_priority() if left_child  else -1
                right_priority=right_child.get_priority() if right_child else -1
                # perform rotation
                if left_priority > right_priority:
                    removed_node = super()._rotate_right(removed_node)
                    super()._attach(parent, removed_node)
                    parent = removed_node
                    removed_node = parent.get_right()
                else:
                    removed_node = super()._rotate_left(removed_node)
                    super()._attach(parent, removed_node)
                    parent = removed_node
                    removed_node = parent.get_left()
            # perform the removal
            if removed_node.is_left_child():
                parent.set_left(None)
            else:
                parent.set_right(None)
            # decrement treap length
            self._length -= 1


    ##############################  HEIGHT/DEPTH  ##############################
    def get_height(self):
        """
        Gets the height of the `Treap()` instance. The Treap's height is the
        number of edges between the root and the furthest leaf node.

        Returns
        -------
        int:
            A positive integer representing the height of the instance.
        
        Example
        -------
        >>> treap = Treap.from_iterable([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.get_height()
        3
        """
        return super().get_height()
    

    def get_depth(self):
        """
        Gets the depth of the `Treap()` instance.

        Returns
        -------
        int:
            A positive integer representing the depth of the instance.
        
        Example
        -------
        >>> treap = Treap.from_iterable([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.get_depth()
        0
        """
        return super().get_depth()
    

    