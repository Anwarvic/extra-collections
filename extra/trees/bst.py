"""
A binary search tree, or BST for short, is a non-linear data structure that
stores numbers hierarchical. With the exception of the top element, each element
in the binary serach tree has a parent element and each node has two children
elements at most. We typically call the top element of the binary search tree,
"the root". The root is drawn as the highest element, with the other elements
being connected below (just the opposite of an actual tree).

.. image:: ../../img/trees/bst.gif

In other words, we can consider the binary search tree as a binary tree that 
stores numbers where the value stored in a certain node is greater than all the 
numbers found in the node's left subtree and less than those found in the node's
right subtree.

So, the following is a simple BST:

.. code-block:: text

          __8___
         /      \\
      __5       _15
     /   \\    /
    2     7   10
     \\
      3


In the previous binary search tree, we can say the following:

- `8` has no parent.
- `8` is the parent of both `5` and `15`. `5` is the left child of `8` and \
    `15` is the right child. 
- `8` is the grandparnet of `2`, `7` and `10`.
- `15` is the uncle of `2` and `7`. While `5` is the uncle of just `10`.
- `15` is the sibling of `5` and vice versa. And `2` is the sibling of `7` and \
    vice versa.

Now, let's try to use the previous BST to explain a few terms:

- **Tree Node**: Each entry in the BSTis called a tree node. So, `8`, `5`, \
    `15`, ... `3` are all tree nodes. So, the number of nodes in the previous \
    BST is 7.
- **Root**: The root is the first tree node in the BST and it's the only \
    tree node that has no *parent*. So, `8` is the root of the previuos tree.
- **Leaf Node**: The leaf node is a tree node that has no children. So, both \
    `3`, `7`, and `10` are leaf nodes. So, the number of leaf nodes in the \
    previous tree is 3.
- **Height**: The tree height is the number of edges between the root and the \
    furthest leaf node. In this case, the tree height is just 3 as there are \
    three edges between `8` and `3`.
- **Depth**: The depth of a tree node is the number of edges between this tree \
    node and the root. So, the depth of the tree's root is always 0.
- **Balanced Tree**: A BST is said to be balanced if the difference between \
    the depth of any two leaf nodes is less than or equal one. So, this BST \
    is balanced
- **Perfect Tree**: A BST is said to be perfect if all its levels are \
    completely filled. So, the pervious BST is NOT perfect.
- **Strict Tree**: A BST is said to be strict if all its non-leaf nodes has \
    left and right children. So, the pervious BST is NOT strict.
- **Traversal**: Traversal is the process to visit all nodes of a BST starting \
    from the root as we cannot randomly access any node in a BST. There are \
    four ways which we use to traverse a BST:

    - **Pre-order Traversal**: It's also known as "Depth-first Traversal" \
        where the **parent** is visited first. Then, the **left subtree** \
        (if found), then the **right subtree** (if found). So, the pre-order \
        traversal of the previous BST will be: \

            8 ⟶ 5 ⟶ 2 ⟶ 3 ⟶ 7 ⟶ 15 ⟶ 10
        
    - **In-order Traversal**: The **left subtree** (if found) is visited first\
        . Then, the **parent** then the **right subtree** (if found). So, the \
        in-order traversal of the previous BST will be: \

            2 ⟶ 3 ⟶ 5 ⟶ 7 ⟶ 8 ⟶ 10 ⟶ 15
        
    - **Post-order Traversal**: The **left subtree** (if found) is visited \
        first. Then, the **right subtree** (if found) then the **parent**. So, \
        the post-order traversal of the previous BST will be: \

            3 ⟶ 2 ⟶ 7 ⟶ 5 ⟶ 10 ⟶ 15 ⟶ 8
        
    - **Breadth-order Traversal**: It's also known as "Level-order Traversal" \
        where all nodes is visited by the order of the level they are in. So, \
        tree nodes in the first level are visited before all tree nodes in the \
        second level and so on. So, the breadth-first traversal of the \
        previuos BST will be: \

            8 ⟶ 5 ⟶ 15 ⟶ 2 ⟶ 7 ⟶ 10 ⟶ 3

.. image:: ../../img/trees/bst.gif

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
| __len__()                | Returns the number of nodes.                       | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_empty()               | Checks if object is empty.                         | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __repr__()               | Represents the BST.                                | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __iter__()               | Iterates over the BST.                             | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __contains__()           | Checks the existence of the given item.            | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_height()             | Gets the BST's height.                             | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_depth()              | Gets the BST's depth.                              | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_nodes_per_level()    | Returns a list of all nodes per level.             | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_balanced()            | Checks if the BST is balanced.                     | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_perfect()             | Checks if the BST is perfect.                      | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_strict()              | Checks if the BST is strict.                       | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| count_leaf_nodes()       | Counts all leaf nodes in the tree.                 | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| clear()                  | Clears the whole tree instance.                    | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| to_list()                | Converts the bianry tree instance to list.         | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| traverse()               | Traverses the BST based on given method.           | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| preorder_traverse()      | Traverses the BST in an pre-order manner.          | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| inorder_traverse()       | Traverses the BST in an in-order manner.           | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| postorder_traverse()     | Traverses the BST in an post-order manner.         | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| breadth_first_traverse() | Traverses the BST level by level.                  | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| depth_first_traverse()   | Traverses the BST in an pre-order manner.          | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_min()                | Gets the minimum number in the BST.                | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_max()                | Gets the maximum number in the BST.                | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| insert()                 | Inserts a certain value to the BST.                | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| remove()                 | Removes a certain value from the BST.              | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+



Class Documentation
===================
Here are all of the public methods that can be used with `BST()` objects:

"""
import warnings
from extra.trees.binary_tree import BinaryTreeNode, BinaryTree




class BSTNode(BinaryTreeNode):
    """
    A BST node is the basic unit for building BSTs. A BST node must contain a 
    number. Each BST node has either zero, one or two children BST nodes.
    The node that has no children is called a **leaf node**.
    """
    __name__ = "extra.BSTNode()"
    

    def __init__(self, value):
        """
        Creates a `BSTNode()` object which is the basic unit for building 
        `BST()` objects!!

        Parameters
        ----------
        value: int or float
            The value to be saved within the `BSTNode()` instance

        Raises
        ------
        ValueError: If the given item is `None`.
        TypeError: If the given item isn't a number.
        """
        if type(value) not in {int, float}:
            raise TypeError(f"`{self.__name__}` contains only numbers!!")
        super().__init__(value)
        self._parent = None


    def get_parent(self):
        """
        Returns the parent of the current `BSTNode()` instance.

        Returns
        -------
        BSTNode() or None:
            A reference to the parent of the current `BSTNode()` which could be
            a `BSTNode() object or `None` in case the current `BSTNode()` is the
            root of the `BST()`.
        """
        return self._parent


    def get_grand_parent(self):
        """
        Returns the grand-parent of the current `BSTNode()` instance.

        Returns
        -------
        BSTNode() or None:
            The grand-parent of the current `BSTNode()` which could be a
            `BSTNode() object or `None` in case the current `BSTNode()` is the
            root of the `BST()` or the root's children.
        """
        return self._parent.get_parent() if self._parent is not None else None


    def get_uncle(self):
        """
        Returns the uncle of the current `BSTNode()` instance. The uncle is the
        sibling of the parent.

        Returns
        -------
        BSTNode() or None:
            The uncle of the current `BSTNode()` which could be a `BSTNode() 
            object or `None` in case the current `BSTNode()` has no uncle.
        """
        parent = self._parent
        if parent is None:
            return None
        grand_parent = parent.get_parent()
        if grand_parent is None:
            return None
        return grand_parent.get_right() \
            if parent.is_left_child() else grand_parent.get_left()


    def get_sibling(self):
        """
        Returns the sibling of the current `BSTNode()` instance.

        Returns
        -------
        BSTNode() or None:
            The sibling of the current `BSTNode()` which could be a `BSTNode() 
            object or `None` in case the current `BSTNode()` doesn't have a 
            sibling.
        """
        # return the brother if found
        parent = self._parent
        if parent is None:
            return None
        return parent.get_right() if self.is_left_child() else parent.get_left()


    def set_left(self, new_node):
        """
        Sets the given `BSTNode()` as a left child for the current `BSTNode()`.

        Parameters
        ----------
        child: BSTNode()
            The `BSTNode()` that will be a left child for the current one.

        Raises
        ------
        TypeError: If the given item is not an `BSTNode()` object.
        """
        if not (new_node is None or isinstance(new_node, BSTNode)):
            raise TypeError(f"Can't set {type(new_node)} as a left child!!")
        self._left = new_node
        if new_node is not None:
            self._left._parent = self


    def set_right(self, new_node):
        """
        Sets the given `BSTNode()` as a right child for the current `BSTNode()`.

        Parameters
        ----------
        child: BSTNode()
            The `BSTNode()` that will be a right child for the current one.

        Raises
        ------
        TypeError: If the given item is not an `BSTNode()` object.
        """
        if not (new_node is None or isinstance(new_node, BSTNode)):
            raise TypeError(f"Can't set {type(new_node)} as a right child!!")
        self._right = new_node
        if new_node is not None:
            self._right._parent = self


    def set_parent(self, new_node):
        """
        Sets the given `BSTNode()` as a parent for the current `BSTNode()`.

        Parameters
        ----------
        child: BSTNode()
            The `BSTNode()` that will be a parent for the current one.

        Raises
        ------
        TypeError: If the given item is neither a `BSTNode()` object nor `None`.
        """
        if not (new_node is None or isinstance(new_node, BSTNode)):
            raise TypeError(f"Can't set {type(new_node)} as a child's parent!!")
        self._parent = new_node


    def is_left_child(self):
        """
        Check if the current `BSTNode()` is a left child.

        Returns
        -------
        bool:
            `True` if the current `BSTNode()` is a left-child. And `False` if
            it's not.
        """
        return self._parent.get_data() > self.get_data()


    def __repr__(self):
        """
        Represents `BSTNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `BSTNode()` instance.
        
        Example
        -------
        >>> x = BSTNode(10)
        >>> x
        BSTNode(10)
        """
        return f"BSTNode({self._data})"




class BST(BinaryTree):
    """
    A BST is a non-linear data structure that can be defined recursively
    using a collection of `BSTNode()` instances, where each node contains a 
    numeric value and it has either zero, one or two references to the children
    `BSTNode()` instances. And the value holding by the node must be greater
    than all values being hold by the left subtree and smaller that all the
    values being hold by the right subtree.
    """
    _basic_node = BSTNode
    __name__ = "extra.BST()"


    def __init__(self, iterable=None):
        """      
        Initializes a `BST()` instance using an optiona iterable object in time-
        complexity of O(n) where **n** is the number of elements inside the
        given `iterable`.

        Parameters
        ----------
        iterable: iterable (default: None)
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
        
        Raises
        ------
        TypeError: It can be raised in three cases
            1. In case the given object isn't iterable.
            2. If one of the elements in the iterable is an `Extra` object.
            3. If one of the elements in the iterable is NOT a number.
        ValueError: If one of the iterable elements is `None`.

        Examples
        --------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3

        Using an iterable object with `None` as one of its elements will raise
        `ValueError`

        >>> BST([2, None])
        ValueError: Can't use `None` as an element within `extra.BST()`!!
        
        Using a non-iterable object will raise `TypeError`

        >>> BST(2)
        TypeError: The given object isn't iterable!!
        
        Using nested `BST()` objects will raise `TypeError` as well

        >>> bst_1 = BST([1])
        >>> bst_2 = BST([1, bst_1])
        TypeError: Can't create `extra.BST()` using `extra.BST()`!!
        """
        super().__init__()
        self._length = 0

        if iterable is None:
            return
        elif not hasattr(iterable, "__iter__"):
            raise TypeError("The given object isn't iterable!!")
        else:
            for item in iterable:
                self.insert(item)


    def _validate_item(self, item):
        """
        Makes sure the input variable type can be processed. The main use for 
        this method is to make sure we can't create nested objects from the 
        package.
        
        Parameters
        ----------
        item: object
            The input object of any type.
        
        Raises
        -------
        ValueError: If `item` is `None`
        TypeError: If `item` is not a numeric value.
        """
        super()._validate_item(item)
        if type(item) not in {int, float}:
            raise TypeError(f"`{self.__name__}` accepts only numbers!!")
    

    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the `BST()` instance in time-complexity of O(1).
        
        Returns
        -------
        int:
            The length of the `BST()` instance. Length is the number of tree 
            nodes in the instance.
        
        Example
        -------
        >>> bst = BST.from_itearble([2, 1, 3])
        >>> bst
            __2__
           /     \\
          1       3
        >>> len(bst)
        3
        """
        return self._length


    def is_empty(self):
        """
        Checks if the `BST()` instance is empty or not in time-complexity of
        O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the `BST()` instance is empty or not.
            `True` shows that this instance is empty and `False` shows it's
            not empty.
        
        Example
        --------
        >>> bst = BST()
        >>> bst.is_empty()
        True
        >>> bst.insert(10)
        >>> bst.is_empty()
        False
        """
        return super().is_empty()
    
    
    ##############################       MAX      ##############################
    def _get_max_node(self, start_node):
        """
        Gets the `BSTNode()` that holds the maximum numeric value in the given
        binary search subtree whose root is the given `start_node`. The maximum
        value can be found at the right-most tree node in the right subtree.

        Parameters
        ----------
        start_node: BSTNode()
            The root of the subtree from which we want to get the maximum value.
        
        Returns
        -------
        BSTNode():
            The `BSTNode()` that holds the maximum numeric value in the subtree.
        
        Raises
        ------
        AssertionError: If the given `start_node` isn't an instance of \
            `BSTNode()`
        """
        assert isinstance(start_node, self._basic_node)

        # get the right-most node
        if start_node.get_right() == None:
            return start_node
        else:
            return self._get_max_node(start_node.get_right())


    def get_max(self):
        """
        Gets the maximum value in the `BST()` isntance. The maximum value can be
        found at the right-most tree node in the `BST()` instance.

        Returns
        -------
        int or float:
            The maximum numeric value in the `BST()` instance.
        
        Raises
        ------
        IndexError: In case the `BST()` instance is empty.

        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.get_max()
        15
        """
        if self.is_empty():
            raise IndexError(\
                f"Can't get the maximum value of an empty `{self.__name__}`")
        max_node = self._get_max_node(self._root)
        return max_node.get_data()


    ##############################       MIN      ##############################
    def _get_min_node(self, start_node):
        """
        Gets the `BSTNode()` that holds the minimum numeric value in the given
        binary search subtree whose root is the given `start_node`. The minimum
        value can be found at the left-most tree node in the left subtree.

        Parameters
        ----------
        start_node: BSTNode()
            The root of the subtree from which we want to get the minimum value.
        
        Returns
        -------
        BSTNode():
            The `BSTNode()` that holds the minimum numeric value in the subtree.
        
        Raises
        ------
        AssertionError: If the given `start_node` isn't an instance of \
            `BSTNode()`
        """

        assert isinstance(start_node, self._basic_node)

        # get the left-most node
        if start_node.get_left() == None:
            return start_node
        else:
            return self._get_min_node(start_node.get_left())


    def get_min(self):
        """
        Gets the minimum value in the `BST()` isntance. The minimum value can be
        found at the left-most tree node in the `BST()` instance.

        Returns
        -------
        int or float:
            The minimum numeric value in the `BST()` instance.
        
        Raises
        ------
        IndexError: In case the `BST()` instance is empty.

        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.get_min()
        2
        """
        if self.is_empty():
            raise IndexError(\
                f"Can't get the minimum value of an empty `{self.__name__}`")
        min_node = self._get_min_node(self._root)
        return min_node.get_data()


    ##############################      SEARCH    ##############################
    def _search(self, find_val, start_node):
        """
        Searches the `BST()` for a given value (`find_val`) starting from the
        subtree whose root is the given `start_node` and returns the node
        containing that value if found. If not found, it returns the last 
        accessed node.

        Parameters
        ----------
        find_val: int or float
            The value to be searched for in the `BST()` instance.
        start_node: BSTNode()
            The root of the subtree where the search will begin.
        
        Returns
        -------
        BSTNode():
            If the value is found, this object represents the found node. If the
            value isn't found, this object will be the last accessed node.

        Raises
        ------
        AssertionError: This can be raised in one of the following cases:
            1. If `find_val` is NOT a numeric value.
            2. If the given `start_node` isn't an instance of `BSTNode()`.

        Examples
        --------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst._search(5, bst._root)
        BSTNode(5)
        >>> bst._search(5, bst._root._right)
        BSTNode(10)
        """
        assert isinstance(start_node, self._basic_node)
        assert type(find_val) in {float, int}

        if find_val == start_node.get_data():
            return start_node
        elif find_val < start_node.get_data():
            if start_node.get_left():
                return self._search(find_val, start_node.get_left())
            else:
                return start_node
        else:
            if start_node.get_right():
                return self._search(find_val, start_node.get_right())
            else:
                return start_node


    def __contains__(self, find_val):
        """
        Searches the `BST()` for the given value and returns `True` if the 
        value exists and `False` if not.

        Parameters
        ----------
        find_val: int or float
            The value to be searched for in the `BST()` instance.
        
        Returns
        -------
        bool:
            Returns `True` if the value exists in the `BST()` instance and
            `False` if not.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> 5 in bst
        True
        >> 50 in bst
        False
        """
        if self.is_empty() or type(find_val) not in {int, float}:
            return False
        found_node = self._search(find_val, self._root)
        return found_node.get_data() == find_val


    ##############################     INSERT     ##############################
    def _insert_node(self, start_node, inserted_node):
        """
        Inserts a `BSTNode()` in the subtree whose root is `start_node`
        according to the rules of binary search trees.

        Parameters
        ----------
        start_node: BSTNode()
            The root of the subtree where the new node will be inserted.
        inserted_node: BSTNode()
            The new node that will be inserted
        
        Returns
        -------
        BSTNode():
            A reference to the new node after being inserted to the subtree.
        
        Raises
        ------
        AssertionError: This will be raised in the following cases:
            1. If `start_node` isn't an instance of `BSTNode()`.
            2. If the `inserted_node` is not either `None` nor an instance of \
                `BSTNode()`.

        """
        assert isinstance(start_node, self._basic_node)
        assert inserted_node is None or \
            isinstance(inserted_node, self._basic_node)
        
        value = inserted_node.get_data()
        if value == start_node.get_data():
            warnings.warn(f"`{value}` already exists in `{self.__name__}`",
                UserWarning
            )
            return start_node
        elif value < start_node.get_data():
            if start_node.get_left():
                return self._insert_node(start_node.get_left(), inserted_node)
            else:
                start_node.set_left( inserted_node )
                self._length += 1
                return inserted_node
        else:
            if start_node.get_right():
                return self._insert_node(start_node.get_right(), inserted_node)
            else:
                start_node.set_right( inserted_node )
                self._length += 1
                return inserted_node


    def _insert_value(self, start_node, value):
        """
        Inserts a numeric value in the subtree whose root is `start_node`
        according to the rules of binary search trees.

        Parameters
        ----------
        start_node: BSTNode()
            The root of the subtree where the new node will be inserted.
        value: int or float
            The new numeric value that will be inserted.
        
        Returns
        -------
        BSTNode():
            A reference to the new node after being inserted to the subtree.
        
        Raises
        ------
        AssertionError: This will be raised in the following cases:
            1. If `start_node` isn't an instance of `BSTNode()`.
            2. If the given `value` is not a numeric value.

        """
        assert isinstance(start_node, self._basic_node)
        assert type(value) in {float, int}

        inserted_node = self._basic_node(value)
        return self._insert_node(start_node, inserted_node)


    def _insert(self, value):
        """
        Inserts a numeric value in the `BST()` instance according to the rules
        of binary search trees.

        Parameters
        ----------
        value: int or float
            The new numeric value that will be inserted.
        
        Returns
        -------
        BSTNode():
            A reference to the new node after being inserted to the subtree.
        
        Raises
        ------
        AssertionError: If the given `value` is not a numeric value.
        """
        assert type(value) in {int, float} or \
                    isinstance(value, self._basic_node)
        
        if isinstance(value, self._basic_node):
            return self._insert_node(self._root, value)
        else:
            return self._insert_value(self._root, value)


    def insert(self, value):
        """
        Inserts a numeric value in the `BST()` instance according to the rules
        of binary search trees.

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
        >>> bst = BST()
        >>> bst.insert(10)
        >>> bst.insert(5)
        >>> bst.insert(15)
        >>> bst
          10
         /  \\
        5    15
        >>> bst.insert("2")
        TypeError: `extra.BST()` accepts only numbers!!
        """
        self._validate_item(value)
        if self.is_empty():
            self._root = self._basic_node(value)
            self._length += 1
        else:
            self._insert(value)


    ##############################     REMOVE     ##############################
    def _find_replacement(self, node):
        """
        Find a replacement to the numeric value of the given `node` as 
        preparation step before removing `node`. This replacement will be
        either the in-order predecessor or the in-order successor.

        Parameters
        ----------
        node: BSTNode()
            The node that will be replaced.
        
        Returns
        -------
        BSTNode():
            The node that will replace the given `node`.
        
        Raises
        ------
        AssertionError: If the given `node` isn't a `BSTNode()` object.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst._find_replacement(bst._root)
        BSTNode(10)
        >>> bst._find_replacement(bst._root._left)
        BSTNode(7)
        """
        assert isinstance(node, self._basic_node)

        if node.get_right():
            # in-order successor
            replacement_node = self._get_min_node(node.get_right())
        elif node.get_left():
            # in-order predecessor
            replacement_node = self._get_max_node(node.get_left())
        else:
            # start_node is leaf
            replacement_node = None
        return replacement_node
    

    def _transplant(self, node, replacement):
        """
        Exchanges the given `node` with the given `replacement`.

        Parameters
        ----------
        node: BSTNode()
            A reference to the node that will be replaced.
        replacement: BSTNode()
            A reference to the replacement node which will replace the `node`.
        
        Raises
        ------
        AssertionError: This can be raised due to one of the following cases:
            1. The given `node` isn't a `BSTNode()`.
            2. The given `replacement` node is neither `BSTNode()` nor `None`.
        """
        assert isinstance(node, self._basic_node)
        assert replacement is None or isinstance(replacement, self._basic_node)

        # replace 'node' with 'replacement'
        if replacement is None:
            parent = node.get_parent()
            if parent.get_left() == node:
                parent.set_left(replacement)
            else:
                parent.set_right(replacement)
        else:
            if replacement.is_leaf():
                new_replacement = None
            elif replacement.get_left():
                new_replacement = replacement.get_left()
            else:
                new_replacement = replacement.get_right()
            # swap data
            self._basic_node.swap(node, replacement)
            self._transplant(replacement, new_replacement)


    def _remove(self, del_value, start_node):
        """
        Removes the `del_value` from the subtree whose root is the given
        `start_node` object. 

        Parameters
        ----------
        del_value: int or float
            The value to be deleted from the subtree.
        start_node: BSTNode()
            The root of the subtree from which the `del_value` will be removed.
        
        Returns
        -------
        BSTNode():
            A refernce to the last accessed node when removing the value from
            the subtree. This could be either the removed node or its parent.
        
        Raises
        ------
        AssertionError: This can be raised in these cases:
            1. If the given `del_value` isn't a numeric value.
            2. If the given `start_node` isn't a `BSTNode()`.
        UserWarning: If the given `del_value` wasn't found in the `BST()`.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst._remove(5, bst._root)
        BSTNode(7)
        >>> bst
              8___
             /    \\
          __7     _15
         /       /
        2       10
         \\
          3
        """
        assert type(del_value) in {int, float}
        assert isinstance(start_node, self._basic_node)

        # search for the del_value node
        removed_node = self._search(del_value, self._root)
        # couldn't find the node
        if removed_node.get_data() != del_value:
            warnings.warn(f"Couldn't find `{del_value}` in `{self.__name__}`",
                UserWarning
            )
            last_accessed_node = removed_node
            return last_accessed_node
        # find replacement
        replacement = self._find_replacement(removed_node)
        # get last accessed node after replacement
        if replacement is None:
            parent = removed_node.get_parent()
        else:
            parent = replacement.get_parent()
        # replace 'del_node' with 'replacement'
        self._transplant(removed_node, replacement)
        # decrease bst length
        self._length -= 1
        # return last accessed node when removing
        last_accessed_node = parent
        return last_accessed_node


    def remove(self, del_value):
        """
        Removes the `del_value` from the `BST()` instance. 

        Parameters
        ----------
        del_value: int or float
            The value to be deleted from the subtree.
        
        Raises
        ------
        UserWarning: If the `BST()` instance is empty of if the value wasn't \
            found in the instance.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.remove(5)
        >>> bst
              8___
             /    \\
          __7     _15
         /       /
        2       10
         \\
          3
        >>> bst.remove(50)
        UserWarning: Couldn't find `50` in `extra.BST()`!!
        """
        if self.is_empty():
            warnings.warn(f"`{self.__name__}` is empty!!", UserWarning)
            return
        elif type(del_value) not in {int, float}:
            warnings.warn(f"Couldn't find `{del_value}` in `{self.__name__}`!!",
                UserWarning
            )
            return 
        # check if bst has only one item and it's the one to be deleted
        elif self._root.is_leaf() and del_value == self._root.get_data():
            self._root = None
            self._length -= 1
        else:
            self._remove(del_value, self._root)
    

    def clear(self):
        """
        Removes all nodes within the `BST()` instance in constant time.

        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.clear()
        >>> bst
        / \\
        >>> bst.is_empty()
        True
        """
        super().clear()


    ##############################     ROTATE     ##############################
    def _rotate_left(self, start_node):
        """
        Rotates the given subtree whose root is `start_node` to the left side.

        Parameters
        ----------
        start_node: BSTNode()
            A reference to the root of the subtree that will be rotated
        
        Returns
        -------
        BSTNode():
            A reference to the new root fo the subtree after rotation.
        
        Raises
        ------
        AssertionError: If the given `start_node` is not `BSTNode()`.

        Example
        -------
        >>> bst = BST([1, 2, 3])
        >>> bst
        1
         \\
          2
           \\
            3
        >>> bst._root = bst._rotate_left(bst._root)
        >>> bst
          2
         / \\
        1   3
        """
        assert isinstance(start_node, self._basic_node)

        # print("Rotating Left")
        middle = start_node.get_right()
        middle.set_parent( start_node.get_parent() )
        start_node.set_right(middle.get_left())
        middle.set_left(start_node)
        return middle


    def _rotate_right(self, start_node):
        """
        Rotates the given subtree whose root is `start_node` to the right side.

        Parameters
        ----------
        start_node: BSTNode()
            A reference to the root of the subtree that will be rotated
        
        Returns
        -------
        BSTNode():
            A reference to the new root fo the subtree after rotation.
        
        Raises
        ------
        AssertionError: If the given `start_node` is not `BSTNode()`.

        Example
        -------
        >>> bst = BST([3, 2, 1])
        >>> bst
            3
           /
          2
         /
        1
        >>> bst._root = bst._rotate_right(bst._root)
        >>> bst
          2
         / \\
        1   3
        """
        assert isinstance(start_node, self._basic_node)

        # print("Rotating Right")
        middle = start_node.get_left()
        middle.set_parent( start_node.get_parent() )
        start_node.set_left(middle.get_right())
        middle.set_right(start_node)
        return middle
    

    def _rotate_left_right(self, start_node):
        """
        Double-rotates the given subtree whose root is `start_node` to the left
        side first, then to the right side.

        Parameters
        ----------
        start_node: BSTNode()
            A reference to the root of the subtree that will be rotated
        
        Returns
        -------
        BSTNode():
            A reference to the new root fo the subtree after rotation.
        
        Raises
        ------
        AssertionError: If the given `start_node` is not `BSTNode()`.

        Example
        -------
        >>> bst = BST([3, 1, 2])
        >>> bst
          __3
         /
        1
         \\
          2
        >>> bst._root = bst._rotate_left_right(bst._root)
        >>> bst
          2
         / \\
        1   3
        """
        assert isinstance(start_node, self._basic_node)

        # print("Rotating Left-Right")
        middle = start_node.get_left().get_right()
        middle.set_parent( start_node.get_parent() )
        start_node.get_left().set_right(middle.get_left())
        middle.set_left(start_node.get_left())
        start_node.set_left(middle.get_right())
        middle.set_right(start_node)
        return middle


    def _rotate_right_left(self, start_node):
        """
        Double-rotates the given subtree whose root is `start_node` to the right
        side first, then to the left side.

        Parameters
        ----------
        start_node: BSTNode()
            A reference to the root of the subtree that will be rotated
        
        Returns
        -------
        BSTNode():
            A reference to the new root fo the subtree after rotation.
        
        Raises
        ------
        AssertionError: If the given `start_node` is not `BSTNode()`.

        Example
        -------
        >>> bst = BST([1, 3, 2])
        >>> bst
        1__
           \\
            3
           /
          2
        >>> bst._root = bst._rotate_left_right(bst._root)
        >>> bst
          2
         / \\
        1   3
        """
        assert isinstance(start_node, self._basic_node)

        # print("Rotating Right-Left")
        middle = start_node.get_right().get_left()
        middle.set_parent( start_node.get_parent() )
        start_node.get_right().set_left(middle.get_right())
        middle.set_right(start_node.get_right())
        start_node.set_right(middle.get_left())
        middle.set_left(start_node)
        return middle


    def _attach(self, parent, child):
        """
        A simple method to connect between two nodes where the first is the
        parent and the other is the child.

        Parameters
        ----------
        parent: BSTNode()
            A reference to the node that will be the parent.
        child: BSTNode()
            A reference to the node that will be the child.
        
        Raises
        ------
        AssertionError: In the following cases:
            1. If the `parent` is neither `BSTNode()` not `None`.
            2. If the given `child` is NOT a `BSTNode()`.
        """
        assert parent is None or isinstance(parent, self._basic_node)
        assert isinstance(child, self._basic_node)

        if parent is None:
            self._root = child
        else:
            if parent.get_data() > child.get_data():
                parent.set_left(child) 
            else:
                parent.set_right(child)


    ##############################  HEIGHT/DEPTH  ##############################
    def get_height(self):
        """
        Gets the height of the `BST()` instance. The BST's height is the number
        of edges between the root and the furthest leaf node.

        Returns
        -------
        int:
            A positive integer representing the height of the instance.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.get_height()
        3
        """
        return super().get_height()
    

    def get_depth(self):
        """
        Gets the depth of the `BST()` instance.

        Returns
        -------
        int:
            A positive integer representing the depth of the instance.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.get_depth()
        0
        """
        return super().get_depth()
    

    ##############################   LEAF NODES   ##############################
    def count_leaf_nodes(self):
        """
        Counts the number of leaf nodes in the `BST()` instance. Leaf nodes are
        the tree nodes that have no children.

        Returns
        -------
        int:
            A positive integer representing the number of leaf nodes in the 
            `BST()`.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.count_leaf_nodes()
        3
        """
        return super().count_leaf_nodes()


    ##############################    BALANCED    ##############################
    def is_balanced(self):
        """
        Checks if the `BST()` instance is balanced. A BST is balanced if the
        difference between the depth of any two leaf nodes is less than or equal
        to one.

        Returns
        -------
        bool:
            `True` if the `BST()` instance is balanced and `False` if it is not
            balanced.
        
        Raises
        ------
        UserWarning: If the `BST()` is empty.

        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.is_balanced()
        True
        """
        return super().is_balanced()


    ##############################    PERFECT     ##############################
    def is_perfect(self):
        """
        Checks if the `BST()` instance is perfect. A BST is perfect if all its
        levels are completely filled.

        Returns
        -------
        bool:
            `True` if the `BST()` instance is perfect and `False` if it is not
            perfect.
        
        Raises
        ------
        UserWarning: If the `BST()` is empty.

        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.is_perfect()
        False
        >>> bst = BST([8, 5, 2, 7, 15, 10, 20])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /   \\
        2     7   10    20
        >>> bst.is_perfect()
        True
        """
        return super().is_perfect()


    ##############################     STRICT     ##############################
    def is_strict(self):
        """
        Checks if the `BST()` instance is strict. A BST is strict if all its
        non-leaf nodes have two children (left and right).

        Returns
        -------
        bool:
            `True` if the `BST()` instance is strict and `False` if it is not
            strict.
        
        Raises
        ------
        UserWarning: If the `BST()` is empty.

        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.is_strict()
        False
        """
        return super().is_strict()
    

    ##############################      ITER      ##############################
    def __iter__(self):
        """
        Iterates over the `BST()` instance and returns a generator of the 
        `BSTNode()` values in breadth-first manner.

        Returns
        -------
        generator:
            The value of each node in the instance.

        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> for value in bst:
        ...     print(value, end=',')
        8,5,15,2,7,10,3,
        """
        return super().__iter__()


    def to_list(self):
        """
        Converts the `BST()` instance to a `list` where values will be inserted
        in breadth-first manner.

        Returns
        -------
        list:
            A `list` object containing the same elements as the `BST()`
            instance.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.to_list()
        [8, 5, 15, 2, 7, 10, 3]
        """
        return super().to_list()


    ##############################      NODES     ##############################
    def get_nodes_per_level(self):
        """
        Retrieves all tree nodes within the `BST()` instance so that all
        tree nodes in a certain level will be concatenated into a separate list.

        Returns
        -------
        list:
            A nested list where the first inner-list has all the tree nodes in 
            the first level, the second inner-list has all the tree nodes in the 
            second level, ... so on.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.get_nodes_per_level()
        [[8], [5, 15], [2, 7, 10], [3]]
        """
        return super().get_nodes_per_level()


    ##############################   Pre-Order    ##############################
    def preorder_traverse(self):
        """
        Traverses the `BST()` instance in pre-order manner. Which means that the
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
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.preorder_traverse()
        [8, 5, 2, 3, 7, 15, 10]
        """
        return super().preorder_traverse()


    def depth_first_traverse(self):
        """
        Traverses the `BST()` instance in depth-first manner. Which means that
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
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.depth_first_traverse()
        [8, 5, 2, 3, 7, 15, 10]
        """
        return super().depth_first_traverse()


    ##############################   Post-Order   ##############################
    def postorder_traverse(self):
        """
        Traverses the `BST()` instance in post-order manner. Which means that
        the **left subtree** (if found) is visited first. Then, the **right
        subtree** (if found) then the **parent**.
        
        Returns
        --------
        list:
            A list of all values of the pre-order visited nodes.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.postorder_traverse()
        [3, 2, 7, 5, 10, 15, 8]
        """
        return super().postorder_traverse()


    ##############################    In-Order    ##############################
    def inorder_traverse(self):
        """
        Traverses the `BST()` instance in in-order manner. Which means that the
        **left subtree** (if found) is visited first. Then, the **parent** then
        the **right subtree** (if found).
        
        Returns
        --------
        list:
            A list of all values of the in-order visited nodes.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.inrder_traverse()
        [2, 3, 5, 7, 8, 10, 15]
        """
        return super().inorder_traverse()


    ##############################  BREADTH-FIRST ##############################
    def breadth_first_traverse(self):
        """
        Traverses the `BST()` instance in breadth-first manner. Which means that
        the tree nodes will be visited level by level.
        
        Returns
        --------
        list:
            A list of all values of the pre-order visited nodes.
        
        Example
        -------
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.breadth_first_traverse()
        [8, 5, 15, 2, 7, 10, 3]
        """
        return super().breadth_first_traverse()


    ##############################    TRAVERSE    ##############################
    def traverse(self, method='inorder'):
        """
        Traversal is the process to visit all nodes of a BST starting from the
        root as we cannot randomly access any node in a binary tree. There are
        four ways which we use to traverse a BST:

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
        >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
        >>> bst
              __8___
             /      \\
          __5       _15
         /   \\    /
        2     7   10
         \\
          3
        >>> bst.traverse("preorder")
        [8, 5, 2, 3, 7, 15, 10]
        >>> bst.traverse("inorder")
        [2, 3, 5, 7, 8, 10, 15]
        >>> bst.traverse("postorder")
        [3, 2, 7, 5, 10, 15, 8]
        >>> bst.traverse("breadth-first")
        [8, 5, 15, 2, 7, 10, 3]
        >>> bst.traverse("extra")
        ValueError: Given traverse method has to be one of these:
        {'breadth-first', 'postorder', 'inorder', 'depth-first', 'preorder'}
        """
        return super().traverse(method)


