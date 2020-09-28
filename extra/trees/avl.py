"""
AVL is a self-balancing binary search tree which is a non-linear data structure
that stores numbers hierarchical with the assertion that any operation, like
insertion, searching, and deletion, will be done in **log(n)** time-complexity
where **n** is the number of elements in the AVL. AVL was named after the
initials of its inventors: Adel’son-Vel’skii and Landis.

.. image:: ../../img/trees/avl.gif

The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **h** is the Splay Tre height which approximatley equals to **log(n)**.

+--------------------------+--------------------------------------------------+------------+---------+
| Method                   | Description                                      | Worst-case | Optimal |
+==========================+==================================================+============+=========+
| __len__()                | Returns the number of nodes.                     | O(1)       | O(1)    |
+--------------------------+--------------------------------------------------+------------+---------+
| is_empty()               | Checks if object is empty.                       | O(1)       | O(1)    |
+--------------------------+--------------------------------------------------+------------+---------+
| __repr__()               | Represents the AVL Tree.                         | O(n)       | O(n)    |
+--------------------------+--------------------------------------------------+------------+---------+
| __iter__()               | Iterates over the AVL Tree.                      | O(n)       | O(n)    |
+--------------------------+--------------------------------------------------+------------+---------+
| __contains__()           | Checks the existence of the given item.          | O(h)       | O(h)    |
+--------------------------+--------------------------------------------------+------------+---------+
| get_height()             | Gets the AVL Tree's height.                      | O(n)       | O(1)    |
+--------------------------+--------------------------------------------------+------------+---------+
| get_depth()              | Gets the AVL Tree's depth.                       | O(n)       | O(1)    |
+--------------------------+--------------------------------------------------+------------+---------+
| get_nodes_per_level()    | Returns a list of all nodes per level.           | O(n)       | O(n)    |
+--------------------------+--------------------------------------------------+------------+---------+
| is_balanced()            | Checks if the AVL Tree is balanced.              | O(n)       | O(1)    |
+--------------------------+--------------------------------------------------+------------+---------+
| is_perfect()             | Checks if the AVL Tree is perfect.               | O(n)       | O(1)    |
+--------------------------+--------------------------------------------------+------------+---------+
| is_strict()              | Checks if the AVL Tree is strict.                | O(n)       | O(1)    |
+--------------------------+--------------------------------------------------+------------+---------+
| count_leaf_nodes()       | Counts all leaf nodes in the tree.               | O(n)       | O(n)    |
+--------------------------+--------------------------------------------------+------------+---------+
| clear()                  | Clears the whole tree instance.                  | O(1)       | O(1)    |
+--------------------------+--------------------------------------------------+------------+---------+
| to_list()                | Converts the bianry tree instance to list.       | O(n)       | O(n)    |
+--------------------------+--------------------------------------------------+------------+---------+
| traverse()               | Traverses the AVL Tree based on given method.    | O(n)       | O(n)    |
+--------------------------+--------------------------------------------------+------------+---------+
| preorder_traverse()      | Traverses the AVL Tree in an pre-order manner.   | O(n)       | O(n)    |
+--------------------------+--------------------------------------------------+------------+---------+
| inorder_traverse()       | Traverses the AVL Tree in an in-order manner.    | O(n)       | O(n)    |
+--------------------------+--------------------------------------------------+------------+---------+
| postorder_traverse()     | Traverses the AVL Tree in an post-order manner.  | O(n)       | O(n)    |
+--------------------------+--------------------------------------------------+------------+---------+
| breadth_first_traverse() | Traverses the AVL Tree level by level.           | O(n)       | O(n)    |
+--------------------------+--------------------------------------------------+------------+---------+
| depth_first_traverse()   | Traverses the AVL Tree in an pre-order manner.   | O(n)       | O(n)    |
+--------------------------+--------------------------------------------------+------------+---------+
| get_min()                | Gets the minimum number in the AVL Tree.         | O(h)       | O(h)    |
+--------------------------+--------------------------------------------------+------------+---------+
| get_max()                | Gets the maximum number in the AVL Tree.         | O(h)       | O(h)    |
+--------------------------+--------------------------------------------------+------------+---------+
| insert()                 | Inserts a certain value to the AVL Tree.         | O(h)       | O(h)    |
+--------------------------+--------------------------------------------------+------------+---------+
| remove()                 | Removes a certain value from the AVL Tree.       | O(h)       | O(h)    |
+--------------------------+--------------------------------------------------+------------+---------+

Class Documentation
===================
Here are all of the public methods that can be used with `AVL()` objects:

"""
from extra.trees.bst import BSTNode, BST



class AVLNode(BSTNode):
    """
    An AVL node is the basic unit for building AVL trees. A AVL node must
    contain a  number. Each AVL node has either zero, one or two children AVL
    nodes. The node that has no children is called a **leaf node**. The only 
    difference between `AVLNode()` and `BSTNode()` is that the former dedicates
    a variable for the `height` which makes balancing `AVL()` objects done in 
    a constant time.
    """
    __name__ = "extra.AVLNode()"
    

    def __init__(self, value):
        """
        Creates a `AVLNode()` object which is the basic unit for building 
        AVL() objects!!

        Parameters
        ----------
        value: int or float
            The value to be saved within the `AVLNode()` instance

        Raises
        ------
        ValueError: If the given item is `None`.
        TypeError: If the given item isn't a number.
        """
        super().__init__(value)
        self._height = 0
    

    def set_left(self, new_node):
        """
        Sets the given `AVLNode()` as a left child for the current `AVLNode()`.

        Parameters
        ----------
        child: AVLNode()
            The `AVLNode()` that will be a left child for the current one.

        Raises
        ------
        TypeError: If the given item is not an `AVLNode()` object.
        """
        super().set_left(new_node)
        self._height = max(self.get_children_heights())
    

    def set_right(self, new_node):
        """
        Sets the given `AVLNode()` as a right child for the current `AVLNode()`.

        Parameters
        ----------
        child: AVLNode()
            The `AVLNode()` that will be a right child for the current one.

        Raises
        ------
        TypeError: If the given item is not an `AVLNode()` object.
        """
        super().set_right(new_node)
        self._height = max(self.get_children_heights())
    

    def get_height(self):
        """
        Returns the height of the `AVLNode()`.

        Returns
        -------
        int:
            The height of the current `AVLNode()`.
        """
        return self._height
    

    def get_left_height(self):
        """
        Returns the height of the left `AVLNode()` child.

        Returns
        -------
        int:
            The height of the left `AVLNode()` child.
        """
        return 1 + self.get_left().get_height() \
            if self.get_left() is not None else 0
        

    def get_right_height(self):
        """
        Returns the height of the right `AVLNode()` child.

        Returns
        -------
        int:
            The height of the right `AVLNode()` child.
        """
        return 1 + self.get_right().get_height() \
            if self.get_right() is not None else 0
    

    def get_children_heights(self):
        """
        Returns a list of two children heights of the current `AVLNode()`
        instance where the first value is the height of the left child and the
        other is the height of the right child.

        Returns
        -------
        list:
            A list of the two children of the `AVLNode()` instance.
        """
        return [self.get_left_height(), self.get_right_height()]
    

    def set_height(self, new_height):
        """
        Sets the height of the current `AVLNode()`.

        Parameters
        ----------
        new_height: int
            The new height that should be assigned to the current `AVLNode()`
        
        Raises
        ------
        TypeError: If the given `height` isn't an integer.
        ValueError: If the given `height` is less than zero.
        """
        if type(new_height) != int:
            raise TypeError("Height has to be an integer number >= 0!!")
        elif new_height < 0:
            raise ValueError("Height has to be an integer number >= 0!!")
        self._height = new_height
    

    def is_balanced(self):
        left_height, right_height = self.get_children_heights()
        return abs(right_height - left_height) <= 1
    

    def __repr__(self):
        """
        Represents `AVLNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `AVLNode()` instance.
        
        Example
        -------
        >>> x = AVLNode(10)
        >>> x
        AVLNode(10)
        """
        return f"AVLNode({self._data})"
    



class AVL(BST):
    """
    AVL is self-balancing (BST), Binary Search Tree  which is a non-linear data
    structure that can be defined recursively using a collection of `AVLNode()`
    instances, where each node contains a numeric value and it has either zero,
    one or two references to the children `BSTNode()` instances. And the value
    holding by the node must be greater than all values being hold by the left
    subtree and smaller that all the values being hold by the right subtree.
    """
    _basic_node = AVLNode
    __name__ = "extra.AVL()"
    

    def __init__(self, iterable=None):
        """
        Initializes an `AVL()` instance using an optional iterable object in
        time-complexity of O(n) where **n** is the number of elements inside
        the given `iterable`.

        Parameters
        ----------
        iterable: iterable (default: None)
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
        
        Raises
        ------
        TypeError: It can be raised in two cases
            1. In case the given object isn't iterable.
            2. If one of the elements in the iterable is an `Extra` object.
            3. If one of the elements in the iterable is NOT a number.

        ValueError: If one of the iterable elements is `None`.

        Examples
        --------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7

        Using an iterable object with `None` as one of its elements will raise
        `ValueError`

        >>> avl = AVL([2, None])
        ValueError: Can't use `None` as an element within `extra.AVL()`!!
        
        Using a non-iterable object will raise `TypeError`

        >>> avl = AVL(2)
        TypeError: The given object isn't iterable!!
        
        Using nested `AVL()` objects will raise `TypeError` as well

        >>> avl_1 = AVL([1])
        >>> avl_2 = AVL([1, avl_1])
        TypeError: Can't create `extra.AVL()` using `extra.AVL()`!!
        """
        super().__init__(iterable)
    

    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the `AVL()` instance in time-complexity of O(1).
        
        Returns
        -------
        int:
            The length of the `AVL()` instance. Length is the number of
            tree nodes in the instance.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> len(avl)
        7
        """
        return super().__len__()
    

    def is_empty(self):
        """
        Checks if the `AVL()` instance is empty or not in constant time-
        complexity.
        
        Returns
        -------
        bool:
            A boolean flag showing if the `AVL()` instance is empty or
            not. `True` shows that this instance is empty and `False` shows it's
            not empty.
        
        Example
        --------
        >>> avl = AVL()
        >>> avl.is_empty()
        True
        >>> avl.insert(10)
        >>> avl.is_empty()
        False
        """
        return super().is_empty()
    

    ##############################       MAX      ##############################
    def get_max(self):
        """
        Gets the maximum value in the `AVL()` isntance. The maximum value
        can be found at the right-most tree node in the `AVL()` instance.

        Returns
        -------
        int or float:
            The maximum numeric value in the `AVL()` instance.
        
        Raises
        ------
        IndexError: In case the `AVL()` instance is empty.

        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.get_max()
        7
        """
        return super().get_max()
    

    ##############################       MIN      ##############################
    def get_min(self):
        """
        Gets the minimum value in the `AVL()` isntance. The minimum value
        can be found at the left-most tree node in the `AVL()` instance.

        Returns
        -------
        int or float:
            The maximum numeric value in the `AVL()` instance.
        
        Raises
        ------
        IndexError: In case the `AVL()` instance is empty.

        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.get_min()
        1
        """
        return super().get_min()


    ##############################     SEARCH     ##############################
    def __contains__(self, find_val):
        """
        Searches the `AVL()` for the given value and returns `True` if the 
        value exists and `False` if not.

        Parameters
        ----------
        find_val: int or float
            The value to be searched for in the `AVL()` instance.
        
        Returns
        -------
        bool:
            Returns `True` if the value exists in the `AVL()` instance and
            `False` if not.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> 5 in avl
        True
        >> 50 in bst
        False
        """
        return super().__contains__(find_val)


    ##############################   INSERTION    ##############################
    def _insert(self, value):
        """
        Inserts a numeric value in the `AVL()` instance according to the rules
        of binary search trees.

        Parameters
        ----------
        value: int or float
            The new numeric value that will be inserted.
        
        Returns
        -------
        AVLNode():
            A reference to the new node after being inserted to the subtree.
        
        Raises
        ------
        AssertionError: If the given `value` is not neither a numeric value nor
        an `AVLNode()`.
        """
        assert type(value) in {int, float} or \
                    isinstance(value, self._basic_node)
        
        if isinstance(value, self._basic_node):
            inserted_node = super()._insert_node(self._root, value)
        else:
            inserted_node = super()._insert_value(self._root, value)
        # update heights & rebalance when needed
        parent = inserted_node.get_parent()
        while(parent is not None):
            grand_parent = parent.get_parent()
            parent.set_height(max(parent.get_children_heights()))
            if not parent.is_balanced():
                parent = self._rebalance(parent)
                self._attach(grand_parent, parent)
            parent = grand_parent
        return inserted_node
    

    def insert(self, value):
        """
        Inserts a numeric value in the AVL()` instance according to the
        rules of binary search trees.

        Parameters
        ----------
        value: int or float
            The new numeric value that will be inserted.
        
        Raises
        ------
        ValueError: If the given `value` is `None`.
        TypeError: If the given `value` is not a numeric value.

        Example
        -------
        >>> avl = AVL()
        >>> avl.insert(10)
        >>> avl
        10
        >>> avl.insert(5)
        >>> avl
        5
         \\
          10
        >>> avl.insert(15)
          10
         /  \\
        5    15
        >>> avl.insert(8)
        >>> avl
          __10
         /    \\
        5      15
         \\
          8
        >>> avl.insert("2")
        TypeError: `extra.AVL()` accepts only numbers!!
        """
        super().insert(value)


    ##############################    REMOVAL     ##############################
    def _remove(self, del_value, start_node):
        """
        Removes the `del_value` from the subtree whose root is the given
        `start_node` object. 

        Parameters
        ----------
        del_value: int or float
            The value to be deleted from the subtree.
        start_node: AVLNode()
            The root of the subtree from which the `del_value` will be removed.
        
        Returns
        -------
        AVLNode():
            A refernce to the last accessed node when removing the value from
            the subtree. This could be either the removed node or its parent.
        
        Raises
        ------
        AssertionError: This can be raised in these cases:
            1. If the given `del_value` isn't a numeric value.
            2. If the given `start_node` isn't a `BSTNode()`.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl._remove(5, avl._root)
        AVLNode(6)
        >>> avl
            __4__
           /     \\
          2       6
         / \\      \\
        1   3       7
        """
        assert type(del_value) in {int, float}
        assert isinstance(start_node, self._basic_node)

        length_before = self._length
        last_accessed_node = super()._remove(del_value, start_node)
        if self._length != length_before:
            parent = last_accessed_node
            while(parent is not None):
                grand_parent = parent.get_parent()
                parent.set_height(max(parent.get_children_heights()))
                if not parent.is_balanced():
                    parent = self._rebalance(parent)
                    self._attach(grand_parent, parent)
                parent = grand_parent
        return last_accessed_node
        

    def remove(self, del_value):
        """
        Removes the `del_value` from the `AVL()` instance. 

        Parameters
        ----------
        del_value: int or float
            The value to be deleted from the subtree.
        
        Raises
        ------
        UserWarning: If the `AVL()` instance is empty of if the value wasn't \
            found in the instance.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.remove(6)
        >>> avl
            __4__
           /     \\
          2       7
         / \\     /
        1   3   5
        >>> avl.remove(50)
        UserWarning: Couldn't find `50` in `extra.AVL()`!!
        """
        super().remove(del_value)


    def clear(self):
        """
        Removes all nodes within the `AVL()` instance in constant time.

        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.clear()
        >>> avl
        / \\
        >>> avl.is_empty()
        True
        """
        super().clear()
    

    ##############################  HEIGHT/DEPTH  ##############################
    def _get_height(self, start_node):
        """
        Gets the height of the subtree defined by the given `start_node`
        parameter. The tree's height is the number of edges between the given
        `start_node` and the furthest leaf node.

        Returns
        -------
        int:
            A positive integer representing the height of the given
            `start_node`.
        
        Raises
        ------
        AssertionError: If the given `start_node` isn't a `TreeNode()`
        
        Example
        -------
        """
        return start_node.get_height()
    

    def get_height(self):
        """
        Gets the height of the `AVL()` instance. The AVL's height
        is the number of edges between the root and the furthest leaf node.

        Returns
        -------
        int:
            A positive integer representing the height of the instance.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.get_height()
        22
        """
        return super().get_height()
    

    def get_depth(self):
        """
        Gets the depth of the `AVL()` instance.

        Returns
        -------
        int:
            A positive integer representing the depth of the instance.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.get_depth()
        0
        """
        return super().get_depth()
    

    ##############################   LEAF NODES   ##############################
    def count_leaf_nodes(self):
        """
        Counts the number of leaf nodes in the `AVL()` instance. Leaf
        nodes are the tree nodes that have no children.

        Returns
        -------
        int:
            A positive integer representing the number of leaf nodes in the 
            `AVL()`.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.count_leaf_nodes()
        4
        """
        return super().count_leaf_nodes()


    ##############################     BALANCE    ##############################
    def _get_unbalanced_node(self, start_node):
        """
        Gets the first imbalanced node in the subtree whose root is the given
        `start_node`.

        Parameters
        ----------
        start_node: AVLNode()
            A reference to the node where searching for imbalance begins.
        
        Returns
        -------
        AVLNode():
            A reference to the first imbalanced node in the given subtree.
        
        Raises
        ------
        AssertionError: If the given node isn't an `AVLNode()`.
        """
        assert isinstance(start_node, self._basic_node)

        child = start_node
        parent = start_node.get_parent()
        grand_parent = start_node.get_grand_parent()
        while(grand_parent is not None and grand_parent.is_balanced()):
            return self._get_unbalanced_node(parent)
        return grand_parent, parent, child
    

    def _rebalance(self, start_node):
        """
        Rebalances the given subtree whose root is the given `start_node`.

        Parameters
        ----------
        start_node: AVLNode()
            A reference to the node where we should start re-balancing.
        
        Returns
        -------
        AVLNode():
            A reference to the same node after balancing.
        
        Raises
        ------
        AssertionError: If the given node isn't an `AVLNode()`.
        """
        assert isinstance(start_node, self._basic_node)

        # get the heavy parent
        grand_parent = start_node
        left_height, right_height = grand_parent.get_children_heights()
        parent = grand_parent.get_left() \
            if left_height > right_height else grand_parent.get_right()
        # get the heavy child
        left_height, right_height = parent.get_children_heights()
        node = parent.get_left() \
            if left_height > right_height else parent.get_right()
        
        # determine the direction
        if parent.is_left_child():
            if node.is_left_child():
                # left-left
                middle = self._rotate_right(grand_parent)
            else:
                # left-right
                middle = self._rotate_left_right(grand_parent)
        else:
            if node.is_left_child():
                # right-left
                middle = self._rotate_right_left(grand_parent)
            else:
                # right-right
                middle = self._rotate_left(grand_parent)
        return middle
    

    def is_balanced(self):
        """
        Checks if the `AVL()` instance is balanced. A AVL is
        balanced if the difference between the depth of any two leaf nodes is
        less than or equal to one.

        Returns
        -------
        bool:
            `True` if the `AVL()` instance is balanced and `False` if it
            is not balanced.
        
        Raises
        ------
        UserWarning: If the `AVL()` is empty.

        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> bst.is_balanced()
        True
        """
        if self.is_empty():
            return super().is_balanced()
        return self._root.is_balanced()


    ##############################    PERFECT     ##############################
    def is_perfect(self):
        """
        Checks if the `AVL()` instance is perfect. A AVL is perfect
        if all its levels are completely filled.

        Returns
        -------
        bool:
            `True` if the `AVL()` instance is perfect and `False` if it is
            not perfect.
        
        Raises
        ------
        UserWarning: If the `AVL()` is empty.

        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.is_perfect()
        True
        """
        return super().is_perfect()


    ##############################     STRICT     ##############################
    def is_strict(self):
        """
        Checks if the `AVL()` instance is strict. A AVL is strict if
        all its non-leaf nodes have two children (left and right).

        Returns
        -------
        bool:
            `True` if the `AVL()` instance is strict and `False` if it is
            not strict.
        
        Raises
        ------
        UserWarning: If the `AVL()` is empty.

        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> bst.is_strict()
        True
        """
        return super().is_strict()
    

    ##############################      ITER      ##############################
    def __iter__(self):
        """
        Iterates over the `AVL()` instance and returns a generator of the 
        `AVLNode()` values in breadth-first manner.

        Returns
        -------
        generator:
            The value of each node in the instance.

        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> for value in avl:
        ...     print(value, end=',')
        4,2,6,1,3,5,7
        """
        return super().__iter__()


    def to_list(self):
        """
        Converts the `AVL()` instance to a `list` where values will be
        inserted in breadth-first manner.

        Returns
        -------
        list:
            A `list` object containing the same elements as the `AVL()`
            instance.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.to_list()
        [4, 2, 6, 1, 3, 5, 7]
        """
        return super().to_list()


    ##############################      NODES     ##############################
    def get_nodes_per_level(self):
        """
        Retrieves all tree nodes within the `AVL()` instance so that all
        tree nodes in a certain level will be concatenated into a separate list.

        Returns
        -------
        list:
            A nested list where the first inner-list has all the tree nodes in 
            the first level, the second inner-list has all the tree nodes in the 
            second level, ... so on.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.get_nodes_per_level()
        [[4], [2, 6], [1, 3, 5, 7]]
        """
        return super().get_nodes_per_level()


    ##############################   Pre-Order    ##############################
    def preorder_traverse(self):
        """
        Traverses the `AVL()` instance in pre-order manner. Which means
        that the **parent** is visited first. Then, the **left subtree** (if
        found), then the **right subtree** (if found).
        
        Note
        -----
        It's the same as `depth_first_traverse()` method.

        Returns
        --------
        list:
            A list of all values of the pre-order visited nodes.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.preorder_traverse()
        [4, 2, 1, 3, 6, 5, 7]
        """
        return super().preorder_traverse()


    def depth_first_traverse(self):
        """
        Traverses the `AVL()` instance in depth-first manner. Which means
        that the **parent** is visited first. Then, the **left subtree** (if
        found), then the **right subtree** (if found). 
        
        Note
        -----
        It's the same as `preorder_traverse()` method.

        Returns
        --------
        list:
            A list of all values of the pre-order visited nodes.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.depth_first_traverse()
        [4, 2, 1, 3, 6, 5, 7]
        """
        return super().depth_first_traverse()


    ##############################   Post-Order   ##############################
    def postorder_traverse(self):
        """
        Traverses the `AVL()` instance in post-order manner. Which means
        that the **left subtree** (if found) is visited first. Then, the **right
        subtree** (if found) then the **parent**.
        
        Returns
        --------
        list:
            A list of all values of the pre-order visited nodes.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.postorder_traverse()
        [1, 3, 2, 5, 7, 6, 4]
        """
        return super().postorder_traverse() 


    ##############################    In-Order    ##############################
    def inorder_traverse(self):
        """
        Traverses the `AVL()` instance in in-order manner. Which means that the
        **left subtree** (if found) is visited first. Then, the **parent** then
        the **right subtree** (if found).
        
        Returns
        --------
        list:
            A list of all values of the in-order visited nodes.
        
        Example
        -------
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.inorder_traverse()
        [1, 2, 3, 4, 5, 6, 7]
        """
        return super().inorder_traverse()


    #############################  BREADTH-FIRST ##############################
    def breadth_first_traverse(self):
        """
        Traverses the `AVL()` instance in breadth-first manner. Which means that
        the tree nodes will be visited level by level.
        
        Returns
        --------
        list:
            A list of all values of the pre-order visited nodes.
        
        Example
        -------
        >>> avl = AVL([[2, 5, 4, 6, 3])
        >>> avl
          3__
         /   \\
        2     5
             / \\
            4   6
        >>> avl.breadth_first_traverse()
        [4, 2, 6, 1, 3, 5, 7]
        """
        return super().breadth_first_traverse()


    ##############################    TRAVERSE    ##############################
    def traverse(self, method='inorder'):
        """
        Traversal is the process to visit all nodes of a AVL starting from the
        root as we cannot randomly access any node in a binary tree. There are
        four ways which we use to traverse a AVL:

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
        >>> avl = AVL([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7
        >>> avl.traverse("preorder")
        [4, 2, 1, 3, 6, 5, 7]
        >>> avl.traverse("inorder")
        [1, 2, 3, 4, 5, 6, 7]
        >>> avl.traverse("postorder")
        [1, 3, 2, 5, 7, 6, 4]
        >>> avl.traverse("breadth-first")
        [4, 2, 6, 1, 3, 5, 7]
        >>> avl.traverse("extra")
        ValueError: Given traverse method has to be one of these:
        {'breadth-first', 'postorder', 'inorder', 'depth-first', 'preorder'}
        """
        return super().traverse(method)


