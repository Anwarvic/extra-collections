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


The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **h** is the height of the BST which approximatley equals to **log(n)** \
    when the tree is balanced.

+--------------------------+----------------------------------------------------+------------+---------+
| Method                   | Description                                        | Worst-case | Optimal |
+==========================+====================================================+============+=========+
| __len__()                | Returns the number of nodes in the treap.          | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_empty()               | Checks if the treap is empty.                      | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __repr__()               | Represents the treap as a string.                  | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __iter__()               | Iterates over the treap.                           | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __contains__()           | Checks the existence of a given item in the treap. | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_height()             | Gets the treap's height.                           | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_depth()              | Gets the treap's depth.                            | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_nodes_per_level()    | Returns a list of all nodes per level.             | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_balanced()            | Checks if the treap is balanced.                   | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_perfect()             | Checks if the treap is perfect.                    | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_strict()              | Checks if the treap is strict.                     | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| count_leaf_nodes()       | Counts all leaf nodes in the treap.                | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| clear()                  | Clears the whole treap.                            | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| to_list()                | Converts the treap instance to list.               | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| traverse()               | Traverses the treap based on given method.         | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| preorder_traverse()      | Traverses the treap in an pre-order manner.        | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| inorder_traverse()       | Traverses the treap in an in-order manner.         | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| postorder_traverse()     | Traverses the treap in an post-order manner.       | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| breadth_first_traverse() | Traverses the treap level by level.                | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| depth_first_traverse()   | Traverses the treap in an pre-order manner.        | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_min()                | Gets the minimum number in the treap.              | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_max()                | Gets the maximum number in the treap.              | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| insert()                 | Inserts a certain value to the treap.              | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| remove()                 | Removes a certain value from the treap.            | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+



Class Documentation
===================
Here are all of the public methods that can be used with `Treap()` objects:

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
        if type(new_priority) not in {int, float}: 
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
        TreapNode(data: 10, priority: 0)
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
    2. node's priority must follow the rules of max heap where the node with \
        the heighest priority must always be at the root without breaking the \
            rules ofBST.
    """
    SHOW_PRIORITY = False
    _basic_node = TreapNode
    __name__ = "extra.Treap()"
    

    def __init__(self, iterable=None, seed=None):
        """
        Initializes a `Treap()` instance using an optional iterable object in
        time-complexity of O(n) where **n** is the number of elements inside
        the given `iterable`.

        Parameters
        ----------
        iterable: iterable (default: None)
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
        seed: int or float (default: None)
            A seed to generate consistent random numbers.
        
        Raises
        ------
        TypeError: It can be raised in three cases
            1. In case the given object isn't iterable.
            2. If one of the elements in the iterable is an `Extra` object.
            3. If one of the elements in the iterable is NOT a number.
        ValueError: If one of the iterable elements is `None`.

        Examples
        --------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
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

        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3])
        >>> treap
            ____4
           /     \\
          1__     7
         /   \\    \\
        0     3     9
             /
            2
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3])
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

        >>> Treap([2, None])
        ValueError: Can't use `None` as an element within `extra.Treap()`!!
        
        Using a non-iterable object will raise `TypeError`

        >>> Treap(2)
        TypeError: The given object isn't iterable!!
        
        Using nested `Treap()` objects will raise `TypeError` as well

        >>> treap_1 = Treap([1])
        >>> treap_2 = Treap([1, treap_1])
        TypeError: Can't create `extra.Treap()` using `extra.Treap()`!!
        """
        random.seed(seed)
        super().__init__(iterable)


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
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
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
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
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
        return super().get_max()


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
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
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
        return super().get_min()


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
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
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
        return super().__contains__(find_val)


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
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
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
                warnings.warn(
                    f"Couldn't find `{del_value}` in `{self.__name__}`",
                    UserWarning
                )
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
    

    def clear(self):
        """
        Removes all nodes within the `Treap()` instance in constant time.

        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.clear()
        >>> treap
        / \\
        >>> treap.is_empty()
        True
        """
        super().clear()


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
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
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
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
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
    

    ##############################   LEAF NODES   ##############################
    def count_leaf_nodes(self):
        """
        Counts the number of leaf nodes in the `Treap()` instance. Leaf nodes
        are the tree nodes that have no children.

        Returns
        -------
        int:
            A positive integer representing the number of leaf nodes in the 
            `Treap()`.
        
        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.count_leaf_nodes()
        3
        """
        return super().count_leaf_nodes()


    ##############################    BALANCED    ##############################
    def is_balanced(self):
        """
        Checks if the `Treap()` instance is balanced. A Treap is balanced if the
        difference between the depth of any two leaf nodes is less than or equal
        to one.

        Returns
        -------
        bool:
            `True` if the `Treap()` instance is balanced and `False` if it is
            not balanced.
        
        Raises
        ------
        UserWarning: If the `Treap()` is empty.

        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.is_balanced()
        True

        Notice that, by changing the seed, you can change the balance of the
        `Treap()`:

        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=2)
        >>> treap
                __7
               /   \\
              3     9
             / \\
            2   4
           /
          1
         /
        0
        >>> treap.is_balanced()
        False
        """
        return super().is_balanced()


    ##############################    PERFECT     ##############################
    def is_perfect(self):
        """
        Checks if the `Treap()` instance is perfect. A Treap is perfect if all
        its levels are completely filled.

        Returns
        -------
        bool:
            `True` if the `Treap()` instance is perfect and `False` if it is not
            perfect.
        
        Raises
        ------
        UserWarning: If the `Treap()` is empty.

        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.is_perfect()
        False
        """
        return super().is_perfect()


    ##############################     STRICT     ##############################
    def is_strict(self):
        """
        Checks if the `Treap()` instance is strict. A Treap is strict if all its
        non-leaf nodes have two children (left and right).

        Returns
        -------
        bool:
            `True` if the `Treap()` instance is strict and `False` if it is not
            strict.
        
        Raises
        ------
        UserWarning: If the `Treap()` is empty.

        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.is_strict()
        False
        """
        return super().is_strict()
    

    ##############################      ITER      ##############################
    def __iter__(self):
        """
        Iterates over the `Treap()` instance and returns a generator of the 
        `BSTNode()` values in breadth-first manner.

        Returns
        -------
        generator:
            The value of each node in the instance.

        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> for value in treap:
        ...     print(value, end=',')
        4,2,9,1,3,7,0,
        """
        return super().__iter__()


    def to_list(self):
        """
        Converts the `Treap()` instance to a `list` where values will be inserted
        in breadth-first manner.

        Returns
        -------
        list:
            A `list` object containing the same elements as the `Treap()`
            instance.
        
        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.to_list()
        [4, 2, 9, 1, 3, 7, 0]
        """
        return super().to_list()


    ##############################      NODES     ##############################
    def get_nodes_per_level(self):
        """
        Retrieves all tree nodes within the `Treap()` instance so that all
        tree nodes in a certain level will be concatenated into a separate list.

        Returns
        -------
        list:
            A nested list where the first inner-list has all the tree nodes in 
            the first level, the second inner-list has all the tree nodes in the 
            second level, ... so on.
        
        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.get_nodes_per_level()
        [[4], [2, 9], [1, 3, 7], [0]]
        """
        return super().get_nodes_per_level()


    ##############################   Pre-Order    ##############################
    def preorder_traverse(self):
        """
        Traverses the `Treap()` instance in pre-order manner. Which means that the
        **parent** is visited first. Then, the **left subtree** (if found), then
        the **right subtree** (if found).
        
        Note
        -----
        It's the same as `depth_first_traverse()` method.

        Returns
        --------
        list:
            A list of all values of the pre-order visited nodes.
        
        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.preorder_traverse()
        [4, 2, 1, 0, 3, 9, 7]
        """
        return super().preorder_traverse()


    def depth_first_traverse(self):
        """
        Traverses the `Treap()` instance in depth-first manner. Which means that
        the **parent** is visited first. Then, the **left subtree** (if found),
        then the **right subtree** (if found). 
        
        Note
        -----
        It's the same as `preorder_traverse()` method.

        Returns
        --------
        list:
            A list of all values of the pre-order visited nodes.
        
        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.depth_first_traverse()
        [4, 2, 1, 0, 3, 9, 7]
        """
        return super().depth_first_traverse()


    ##############################   Post-Order   ##############################
    def postorder_traverse(self):
        """
        Traverses the `Treap()` instance in post-order manner. Which means that
        the **left subtree** (if found) is visited first. Then, the **right
        subtree** (if found) then the **parent**.
        
        Returns
        --------
        list:
            A list of all values of the pre-order visited nodes.
        
        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.postorder_traverse()
        [0, 1, 3, 2, 7, 9, 4]
        """
        return super().postorder_traverse()


    ##############################    In-Order    ##############################
    def inorder_traverse(self):
        """
        Traverses the `Treap()` instance in in-order manner. Which means that the
        **left subtree** (if found) is visited first. Then, the **parent** then
        the **right subtree** (if found).
        
        Returns
        --------
        list:
            A list of all values of the in-order visited nodes.
        
        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.inrder_traverse()
        [0, 1, 2, 3, 4, 7, 9]
        """
        return super().inorder_traverse()


    ##############################  BREADTH-FIRST ##############################
    def breadth_first_traverse(self):
        """
        Traverses the `Treap()` instance in breadth-first manner. Which means that
        the tree nodes will be visited level by level.
        
        Returns
        --------
        list:
            A list of all values of the pre-order visited nodes.
        
        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.breadth_first_traverse()
        [4, 2, 9, 1, 3, 7, 0]
        """
        return super().breadth_first_traverse()


    ##############################    TRAVERSE    ##############################
    def traverse(self, method='inorder'):
        """
        Traversal is the process to visit all nodes of a Treap starting from the
        root as we cannot randomly access any node in a binary tree. There are
        four ways which we use to traverse a Treap:

        1. preorder - depth-first
        2. inorder
        3. posteorder
        4. breadth-first

        Parameters
        ----------
        method: str (default="inorder")
            A lower-cased string describing the type of traversal that will be
            used. It could be one of these values: ["inorder", "postorder",
            "preorder", "depth-first", "breadth-first"]
        
        Returns
        --------
        list:
            A list of all values of the visited nodes according to the specified
            traversal method.
        
        Raises
        ------
        ValueError: If the given method isn't known.
        TypeError: If the given method isn't a string.

        Example
        -------
        >>> treap = Treap([0, 2, 1, 4, 9, 7, 3], seed=123)
        >>> treap
              __4__
             /     \\
            2       9
           / \\    /
          1   3   7
         /
        0
        >>> treap.traverse("preorder")
        [4, 2, 1, 0, 3, 9, 7]
        >>> treap.traverse("inorder")
        [0, 1, 2, 3, 4, 7, 9]
        >>> treap.traverse("postorder")
        [0, 1, 3, 2, 7, 9, 4]
        >>> treap.traverse("breadth-first")
        [4, 2, 9, 1, 3, 7, 0]
        >>> treap.traverse("extra")
        ValueError: Given traverse method has to be one of these:
        {'breadth-first', 'postorder', 'inorder', 'depth-first', 'preorder'}
        """
        return super().traverse(method)


