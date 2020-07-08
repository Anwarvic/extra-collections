"""
Splay Tree is a binary search tree which is a non-linear data structure that
stores numbers hierarchical. With the exception of the top element, each element
in the binary serach tree has a parent element and each node has two children
elements at most. We typically call the top element of the binary search tree,
"the root". The root is drawn as the highest element, with the other elements
being connected below (just the opposite of an actual tree).

The only difference between "Splay Trees" and "BSTs" is that any operation done
to the the former, like insertion, deletion, or even a search, should be
followed by a move-to-root operation called "splaying" that changes the
structure of the tree. 

To understand the splaying operation even more, let's look at the the following
SplayTree which is a BST in a first place.

.. code-block:: text

      3__
     /   \\
    2     5
         / \\
        4   6

Now, let's insert `4.5` to this SplayTree; now the Splay Tree will look like the
following:

.. code-block:: text

        __4.5
       /     \\
      3       5
     / \\       \\
    2   4       6

As we can see, the newly-inserted node has been moved to the root which makes it
faster to be accessed for later usage. This happens with all searching,
insertion and deletion.


The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **h** is the Splay Tre height which approximatley equals to **log(n)**.

+--------------------------+----------------------------------------------------+------------+---------+
| Method                   | Description                                        | Worst-case | Optimal |
+==========================+====================================================+============+=========+
| __len__()                | Returns the number of nodes.                       | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_empty()               | Checks if object is empty.                         | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __repr__()               | Represents the Splay Tree.                         | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __iter__()               | Iterates over the Splay Tree.                      | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __contains__()           | Checks the existence of the given item.            | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_height()             | Gets the Splay Tree's height.                      | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_depth()              | Gets the Splay Tree's depth.                       | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_nodes()              | Returns a list of all nodes per level.             | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_balanced()            | Checks if the Splay Tree is balanced.              | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_perfect()             | Checks if the Splay Tree is perfect.               | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_strict()              | Checks if the Splay Tree is strict.                | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| count_leaf_nodes()       | Counts all leaf nodes in the tree.                 | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| clear()                  | Clears the whole tree instance.                    | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| to_list()                | Converts the bianry tree instance to list.         | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| traverse()               | Traverses the Splay Tree based on given method.    | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| preorder_traverse()      | Traverses the Splay Tree in an pre-order manner.   | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| inorder_traverse()       | Traverses the Splay Tree in an in-order manner.    | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| postorder_traverse()     | Traverses the Splay Tree in an post-order manner.  | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| breadth_first_traverse() | Traverses the Splay Tree level by level.           | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| depth_first_traverse()   | Traverses the Splay Tree in an pre-order manner.   | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_min()                | Gets the minimum number in the Splay Tree.         | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_max()                | Gets the maximum number in the Splay Tree.         | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| insert()                 | Inserts a certain value to the Splay Tree.         | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| remove()                 | Removes a certain value from the Splay Tree.       | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+

Class Documentation
===================
Here are all of the public methods that can be used with `SplayTree()` objects:
"""
import warnings
from extra.trees.bst import BST




class SplayTree(BST):
    """
    A Splay Tree is a non-linear data structure that can be defined recursively
    using a collection of `BSTNode()` instances, where each node contains a 
    numeric value and it has either zero, one or two references to the children
    `BSTNode()` instances. Any node that has been accessed is moved to the root
    directly to make it faster to be accessed again. This operation is called
    "splaying". Hence the name of this data structure.
    """
    __name__ = "extra.SplayTree()"
    

    def __init__(self):
        """
        Creates an empty `SplayTree()` object!!
        
        Example
        -------
        >>> stree = SplayTree()
        >>> type(stree)
        <class 'extra.trees.splay_tree.SplayTree'>
        """
        super().__init__()
        self._length = 0


    @classmethod
    def from_iterable(cls, iterable):
        """
        A class method which creates a `SplayTree()` instance using an iterable
        in time-complexity of O(n) where **n** is the number of elements inside
        the given `iterable`.

        Parameters
        ----------
        iterable: iterable
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
        
        Returns
        -------
        SplayTree()
            It returns a `SplayTree()` instance with input values being inserted
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
        >>> stree = SplayTree.from_iterable([[2, 5, 4, 6, 3])
        >>> stree
          3__
         /   \\
        2     5
             / \\
            4   6

        Using an iterable object with `None` as one of its elements will raise
        `ValueError`

        >>> stree = SplayTree.from_iterable([2, None])
        ValueError: Can't use `None` as an element within `extra.SplayTree()`!!
        
        Using a non-iterable object will raise `TypeError`

        >>> stree = SplayTree.from_iterable(2)
        TypeError: The given object isn't iterable!!
        
        Using nested `SplayTree()` objects will raise `TypeError` as well

        >>> stree_1 = SplayTree.from_iterable([1])
        >>> stree_2 = SplayTree.from_iterable([1, stree_1])
        TypeError: Can't create `extra.SplayTree()` using `extra.SplayTree()`!!
        """
        return super().from_iterable(iterable)


    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the `SplayTree()` instance in time-complexity of O(1).
        
        Returns
        -------
        int:
            The length of the `SplayTree()` instance. Length is the number of
            tree nodes in the instance.
        
        Example
        -------
        >>> stree = SplayTree.from_iterable([[2, 5, 4, 6, 3])
        >>> stree
          3__
         /   \\
        2     5
             / \\
            4   6
        >>> len(stree)
        5
        """
        return super().__len__()
    

    def is_empty(self):
        """
        Checks if the `SplayTree()` instance is empty or not in constant time-
        complexity.
        
        Returns
        -------
        bool:
            A boolean flag showing if the `SplayTree()` instance is empty or
            not. `True` shows that this instance is empty and `False` shows it's
            not empty.
        
        Example
        --------
        >>> stree = SplayTree()
        >>> stree.is_empty()
        True
        >>> stree.insert(10)
        >>> stree.is_empty()
        False
        """
        return super().is_empty()
    

    ##############################       MAX      ##############################
    def get_max(self):
        """
        Gets the maximum value in the `SplayTree()` isntance. The maximum value
        can be found at the right-most tree node in the `SplayTree()` instance.

        Returns
        -------
        int or float:
            The maximum numeric value in the `SplayTree()` instance.
        
        Raises
        ------
        IndexError: In case the `SplayTree()` instance is empty.

        Example
        -------
        >>> stree = SplayTree.from_iterable([[2, 5, 4, 6, 3])
        >>> stree
          3__
         /   \\
        2     5
             / \\
            4   6
        >>> stree.get_max()
        6
        """
        return super().get_max()
    

    ##############################       MIN      ##############################
    def get_min(self):
        """
        Gets the minimum value in the `SplayTree()` isntance. The minimum value
        can be found at the left-most tree node in the `SplayTree()` instance.

        Returns
        -------
        int or float:
            The maximum numeric value in the `SplayTree()` instance.
        
        Raises
        ------
        IndexError: In case the `SplayTree()` instance is empty.

        Example
        -------
        >>> stree = SplayTree.from_iterable([[2, 5, 4, 6, 3])
        >>> stree
          3__
         /   \\
        2     5
             / \\
            4   6
        >>> stree.get_min()
        2
        """
        return super().get_min()


    ##############################    SPLAYING    ##############################
    def __zig_zig(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zig-zig operation")
        child = start_node
        parent = child.get_parent()
        grand_parent = child.get_grand_parent()
        # start zig-zig
        child.set_parent( grand_parent.get_parent() )
        grand_parent.set_left(parent.get_right())
        parent.set_right(grand_parent)
        parent.set_left(child.get_right())
        child.set_right(parent)
        #child is now the grand-parent
        return child
    

    def __zag_zag(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zag-zag operation")
        child = start_node
        parent = child.get_parent()
        grand_parent = child.get_grand_parent()
        # start zag-zag
        child.set_parent( grand_parent.get_parent() )
        grand_parent.set_right(parent.get_left())
        parent.set_left(grand_parent)
        parent.set_right(child.get_left())
        child.set_left(parent)
        #child is now the grand-parent
        return child


    def __zig_zag(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zig-zag operation")
        child = start_node
        parent = child.get_parent()
        grand_parent = child.get_grand_parent()
        # start zig-zag
        child.set_parent( grand_parent.get_parent() )
        grand_parent.set_left(child.get_right())
        parent.set_right(child.get_left())
        child.set_right(grand_parent)
        child.set_left(parent)
        return child


    def __zag_zig(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zag-zig operation")
        child = start_node
        parent = child.get_parent()
        grand_parent = child.get_grand_parent()
        # start zag-zig
        child.set_parent( grand_parent.get_parent() )
        grand_parent.set_right(child.get_left())
        parent.set_left(child.get_right())
        child.set_left(grand_parent)
        child.set_right(parent)
        return child


    def __zig(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zig operation")
        child = start_node
        parent = child.get_parent()
        child.set_parent( parent.get_parent() )
        parent.set_left(child.get_right())
        child.set_right(parent)
        return child
    

    def __zag(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zag operation")
        child = start_node
        parent = child.get_parent()
        child.set_parent( parent.get_parent() )
        parent.set_right(child.get_left())
        child.set_left(parent)
        return child


    def __splaying(self, start_node):
        assert isinstance(start_node, self._basic_node)
        child = start_node
        parent = child.get_parent()
        if parent is None:
            return start_node
        grand_parent = child.get_grand_parent()
        # get the operation type
        if grand_parent is None:
            if child.is_left_child():
                root = self.__zig(child)
            else:
                root = self.__zag(child)
        else:
            # left -> left
            if parent.is_left_child() and child.is_left_child():
                grand_parent = self.__zig_zig(child)
            # left -> right
            elif parent.is_left_child() and not child.is_left_child():
                grand_parent = self.__zig_zag(child)
            # right -> left
            elif not parent.is_left_child() and child.is_left_child():
                grand_parent = self.__zag_zig(child)
            # right -> right
            else:
                grand_parent = self.__zag_zag(child)
            if grand_parent.get_parent() is not None:
                root = self.__splaying(grand_parent)
            else:
                root = grand_parent
        return root
    
    
    def _splay(self, start_node):
        """
        Splays the given subtree whose root is the given `start_node` object.
        Splaying means "moving the node to the root". And this operation is done
        after searching, insertion and deletion.

        Parameters
        ----------
        start_node: BSTNode()
            A reference to the root of the subtree.
        """
        self._root = self.__splaying(start_node)


    ##############################     SEARCH     ##############################
    def __contains__(self, find_val):
        """
        Searches the `SplayTree()` for the given value and returns `True` if the 
        value exists and `False` if not.

        Parameters
        ----------
        find_val: int or float
            The value to be searched for in the `SplayTree()` instance.
        
        Returns
        -------
        bool:
            Returns `True` if the value exists in the `SplayTree()` instance and
            `False` if not.
        
        Example
        -------
        >>> stree = SplayTree.from_iterable([[2, 5, 4, 6, 3])
        >>> stree
          3__
         /   \\
        2     5
             / \\
            4   6
        >>> 5 in stree
        True
        >>> stree
            __5
           /   \\
          3     6
         / \\
        2   4
        >> 50 in bst
        False
        >>> stree
                6
               /
            __5
           /
          3
         / \\
        2   4

        Note
        ----
        As you can see from the previous example, the `SplayTree()` instance
        changes its structure each time we search for a certain value. If the
        value if found, the found node will be moved to the root. If the value
        isn't found, the last accessed node will be moved to the root. And
        that's what happended when searching for `50`, the last accessed value 
        which is the greatest value (`6`) in the splay tree is moved to the
        root.
        """
        super()._validate_item(find_val)
        node = super()._search(find_val, self._root)
        self._splay(node)
        return node.get_data() == find_val


    ##############################   INSERTION    ##############################
    def insert(self, value):
        """
        Inserts a numeric value in the SplayTree()` instance according to the
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
        >>> stree = SplayTree()
        >>> stree.insert(10)
        >>> stree
        10
        >>> stree.insert(5)
        >>> stree
        5
         \\
          10
        >>> stree.insert(15)
            _15
           /
          10
         /
        5
        >>> stree.insert(8)
        >>> stree
          8___
         /    \\
        5     _15
             /
            10
        >>> stree.insert("2")
        TypeError: `extra.SplayTree()` accepts only numbers!!
        """
        super()._validate_item(value)
        if self.is_empty():
            self._root = super()._basic_node(value)
            self._length += 1
        else:
            new_node = super()._insert(value)
            self._splay(new_node)


    ##############################    REMOVAL     ##############################
    def remove(self, del_value):
        """
        Removes the `del_value` from the `SplayTree()` instance. 

        Parameters
        ----------
        del_value: int or float
            The value to be deleted from the subtree.
        
        Raises
        ------
        UserWarning: If the `SplayTree()` instance is empty of if the value wasn't \
            found in the instance.
        
        Example
        -------
        >>> stree = SplayTree.from_iterable([[2, 5, 4, 6, 3])
        >>> stree
          3__
         /   \\
        2     5
             / \\
            4   6
        >>> stree.remove(5)
        >>> stree
            __6
           /
          3
         / \\
        2   4
        >>> stree.remove(50)
        UserWarning: Couldn't find `50` in `extra.SplayTree()`!!
        """
        if self.is_empty():
            warnings.warn(f"`{self.__name__}` is empty!!", UserWarning)
            return
        elif type(del_value) not in {int, float}:
            warnings.warn(f"Couldn't find `{del_value}` in `{self.__name__}`!!",
                UserWarning
            )
            return 
        # check if splay tree has only one item and it's the one to be deleted
        elif self._root.is_leaf() and del_value == self._root.get_data():
            self._root = None
            self._length -= 1
        else:
            node = super()._remove(del_value, self._root)
            self._splay(node)


    ##############################  HEIGHT/DEPTH  ##############################
    def get_height(self):
        """
        Gets the height of the `SplayTree()` instance. The SplayTree's height
        is the number of edges between the root and the furthest leaf node.

        Returns
        -------
        int:
            A positive integer representing the height of the instance.
        
        Example
        -------
        >>> stree = SplayTree.from_iterable([[2, 5, 4, 6, 3])
        >>> stree
          3__
         /   \\
        2     5
             / \\
            4   6
        >>> stree.get_height()
        2
        """
        return super().get_height()
    

    

