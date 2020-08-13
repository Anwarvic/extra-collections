"""
AVL is a self-balancing binary search tree which is a non-linear data structure
that stores numbers hierarchical with the assertion that any operation, like
insertion, searching, and deletion, will be done in **log(n)** time-complexity
where **n** is the number of elements in the AVL. AVL was named after the
initials of its inventors: Adel’son-Vel’skii and Landis.
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
        >>> AVLNode(10)
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
    

    def __init__(self):
        """
        Creates an empty `AVL()` object!!
        
        Example
        -------
        >>> avl = AVL()
        >>> type(avl)
        <class 'extra.trees.avl.AVL'>
        """
        super().__init__()
    

    @classmethod
    def from_iterable(cls, iterable):
        """
        A class method which creates an `AVL()` instance using an iterable
        in time-complexity of O(n) where **n** is the number of elements inside
        the given `iterable`.

        Parameters
        ----------
        iterable: iterable
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
        
        Returns
        -------
        AVL()
            It returns a `AVL()` instance with input values being inserted
            in the same order.
        
        Raises
        ------
        TypeError: It can be raised in two cases
            1. In case the given object isn't iterable.
            2. If one of the elements in the iterable is an `Extra` object.
            3. If one of the elements in the iterable is NOT a number.

        ValueError: If one of the iterable elements is `None`.

        Examples
        --------
        >>> avl = AVL.from_iterable([1, 2, 3, 4, 5, 6, 7])
        >>> avl
            __4__
           /     \\
          2       6
         / \\    / \\
        1   3   5   7

        Using an iterable object with `None` as one of its elements will raise
        `ValueError`

        >>> avl = AVL.from_iterable([2, None])
        ValueError: Can't use `None` as an element within `extra.AVL()`!!
        
        Using a non-iterable object will raise `TypeError`

        >>> avl = AVL.from_iterable(2)
        TypeError: The given object isn't iterable!!
        
        Using nested `AVL()` objects will raise `TypeError` as well

        >>> avl_1 = AVL.from_iterable([1])
        >>> avl_2 = AVL.from_iterable([1, avl_1])
        TypeError: Can't create `extra.AVL()` using `extra.AVL()`!!
        """
        return super().from_iterable(iterable)


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
        >>> avl = AVL.from_iterable([1, 2, 3, 4, 5, 6, 7])
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
        >>> avl = AVL.from_iterable([1, 2, 3, 4, 5, 6, 7])
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
        >>> avl = AVL.from_iterable([1, 2, 3, 4, 5, 6, 7])
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
        >>> avl = AVL.from_iterable([1, 2, 3, 4, 5, 6, 7])
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
        >>> avl = AVL.from_iterable([1, 2, 3, 4, 5, 6, 7])
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
        >>> avl = AVL.from_iterable([1, 2, 3, 4, 5, 6, 7])
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
        >>> avl = AVL.from_iterable([1, 2, 3, 4, 5, 6, 7])
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
        >>> avl = AVL.from_iterable([1, 2, 3, 4, 5, 6, 7])
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
        >>> avl = AVL.from_iterable([1, 2, 3, 4, 5, 6, 7])
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
        Gets the node that is unbalanced in the subtree whose root is the given
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
    

    