"""
A treap is a binary tree that stores a collection of nodes. Each node in the
treap contains two main values:

- **data**: The numeric value inserted to the treap.
- **priority**: A numeric value that indicates how important this node is. \
    The bigger this numeric value is, the higher its priority in the treap \
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
        if seed is not None: random.seed(seed)
        super().__init__()

    
    @classmethod
    def from_iterable(cls, iterable, seed=None):
        if seed is not None: random.seed(seed)
        if not hasattr(iterable, "__iter__"):
            raise TypeError("The given object isn't iterable!!")
        if len(iterable) == 0:
            raise ValueError("The given iterable is empty!!")
        treap = cls()
        for item in iterable:
            treap.insert(item)
        return treap


    ##############################     INSERT     ##############################
    def __validate_priority(self, new_priority):
        if new_priority is not None and type(new_priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
    

    def insert(self, value, priority=None):
        # validate inserted value
        super()._validate_item(value)
        self.__validate_priority(priority)
        if self.is_empty():
            self._root = self._basic_node(value)
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


